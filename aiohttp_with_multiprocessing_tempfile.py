import aiohttp
import asyncio
import tempfile
from multiprocessing import Pool

async def get_starred_repos(language, session):
    url = f"https://api.github.com/search/repositories?q=stars:>100+language:{language}&sort=stars&order=desc"
    headers = {
        "Authorization": f"token PATM",
        "Accept": "application/vnd.github.v3+json"
    }
    async with session.get(url, headers=headers) as response:
        if response.status == 200:
            with tempfile.NamedTemporaryFile(mode='w+b', delete=False) as temp_file:
                async for chunk in response.content.iter_chunked(1024):
                    temp_file.write(chunk)
                temp_file.flush()
                return temp_file.name
        else:
            print(f"Failed to retrieve data. Status code: {response.status}")
            return None

async def fetch_language_repos(language):
    async with aiohttp.ClientSession() as session:
        temp_file_path = await get_starred_repos(language, session)
        if temp_file_path:
            with open(temp_file_path, 'rb') as temp_file:
                data = temp_file.read()
                # Process the data as needed
                repos = [item['full_name'] for item in data['items'][:10]]
                return repos

def process_language(language):
    return asyncio.run(fetch_language_repos(language))

async def main():
    languages = ["Python", "JavaScript", "Java"]
    with Pool() as pool:
        results = pool.map(process_language, languages)

    for i, lang in enumerate(languages):
        print(f"\nTop 10 starred repositories in {lang}:")
        for repo in results[i]:
            print(repo)

if __name__ == "__main__":
    asyncio.run(main())
