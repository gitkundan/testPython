Post to an endpoint, read the response, store the response, process the response in another file
------------------------------------------------------------------------------------------

Approach 1 : 
import aiohttp
import aiofiles
import orjson
import tempfile
import os
import asyncio
from tqdm.asyncio import tqdm

class GetHosts:
    def __init__(self, url, asset, file_path):
        self.url = url
        self.payload = {"asset": asset}
        self.file_path = file_path

    async def fetch_and_store(self):
        async with aiohttp.ClientSession() as session:
            async with session.post(self.url, json=self.payload) as response:
                if response.status == 200:
                    async with aiofiles.open(self.file_path, 'ab') as f:
                        while True:
                            chunk = await response.content.read(1024)
                            if not chunk:
                                break
                            await f.write(chunk)
                else:
                    raise Exception(f"Failed to fetch data for asset {self.payload['asset']}: {response.status}")

class ReadFile:
    def __init__(self, file_path):
        self.file_path = file_path

    async def read_and_parse(self):
        async with aiofiles.open(self.file_path, 'rb') as f:
            content = await f.read()
            parsed_content = orjson.loads(content)
            print(f"Length of content: {len(parsed_content)}")

async def process_assets(url, assets):
    with tempfile.TemporaryDirectory() as temp_dir:
        combined_file_path = os.path.join(temp_dir, "combined_assets.bin")
        
        for asset in tqdm(assets, desc="Processing assets"):
            get_hosts = GetHosts(url, asset, combined_file_path)
            await get_hosts.fetch_and_store()

        read_file = ReadFile(combined_file_path)
        await read_file.read_and_parse()
        # The temporary files will be automatically cleaned up when the context manager exits.

# Example usage
async def main():
    url = "http://example.com/api/endpoint"  # Replace with your actual URL
    assets = {"wh-1", "wh-2"}  # Mockup list of assets

    await process_assets(url, assets)

# To run the main function
asyncio.run(main())

-----------------------------------------------------------------------------------------------
Approach 2: 
import aiohttp
import aiofiles
import orjson
import os
import tempfile
from tqdm import tqdm

class GetHosts:
    def __init__(self, url, assets):
        self.url = url
        self.assets = assets

    async def post_payload(self, asset):
        async with aiohttp.ClientSession() as session:
            async with session.post(self.url, data=asset) as resp:
                data = await resp.read()
                return data

    async def store_responses(self):
        temp_dir = tempfile.TemporaryDirectory()
        file_path = os.path.join(temp_dir.name, 'response.bin')
        for asset in tqdm(self.assets, desc="Processing assets"):
            data = await self.post_payload(asset)
            async with aiofiles.open(file_path, 'ab') as f:
                await f.write(data)
        return file_path

class ReadFile:
    def __init__(self, file_path):
        self.file_path = file_path

    async def read_file(self):
        async with aiofiles.open(self.file_path, 'rb') as f:
            data = await f.read()
            return data

    async def parse_and_print_length(self):
        data = await self.read_file()
        parsed_data = orjson.loads(data)
        print(f'Length of content in the file: {len(parsed_data)}')

# Usage
async def main():
    assets = {"wh-1", "wh-2"}
    get_hosts = GetHosts("http://api-endpoint.com", assets)
    file_path = await get_hosts.store_responses()

    read_file = ReadFile(file_path)
    await read_file.parse_and_print_length()

# Run the main function
import asyncio
asyncio.run(main())
