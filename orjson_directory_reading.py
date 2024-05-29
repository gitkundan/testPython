import asyncio
import aiofiles
import orjson
from pathlib import Path

async def read_file_and_parse(bin_file):
    async with aiofiles.open(bin_file, mode='rb') as f:
        bin_data = await f.read()
        
        try:
            json_data = orjson.loads(bin_data)
            if isinstance(json_data, list):
                return json_data
            else:
                print(f"File {bin_file} does not contain a list of dictionaries. Skipping.")
                return None
        except orjson.JSONDecodeError as e:
            print(f"Error decoding JSON from file {bin_file}: {e}")
            return None

async def main():
    data_dir = Path('C:/data')
    bin_files = data_dir.glob('*.bin')

    final = []

    tasks = [read_file_and_parse(bin_file) for bin_file in bin_files]
    results = await asyncio.gather(*tasks)

    for result in results:
        if result is not None:
            final.extend(result)

    print(f"Total dictionaries collected: {len(final)}")

asyncio.run(main())
