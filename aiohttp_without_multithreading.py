# works without multithreading
import aiohttp
import asyncio

async def get_starred_repos(language, session):
    url = f"https://api.github.com/search/repositories?q=stars:>100+language:{language}&sort=stars&order=desc"
    headers = {
        "Authorization": f"token your PAT",
        "Accept": "application/vnd.github.v3+json"
    }
    async with session.get(url, headers=headers) as response:
        if response.status == 200:
            data = await response.json()
            # Limiting to top 10 results
            return [item['full_name'] for item in data['items'][:10]]
        else:
            print(f"Failed to retrieve data. Status code: {response.status}")
            return []

languages = ["Python", "JavaScript", "Java"]
proxy_config = {
    "http": "http://your_proxy_host:port",
    "https": "http://your_proxy_host:port",
}

async def main():
    # async with aiohttp.ClientSession(proxies=proxy_config) as session:
    async with aiohttp.ClientSession() as session:
        tasks = []
        for lang in languages:
            tasks.append(get_starred_repos(lang, session))
        results = await asyncio.gather(*tasks)
        for i, lang in enumerate(languages):
            print(f"\nTop 10 starred repositories in {lang}:")
            for repo in results[i]:
                print(repo)

if __name__ == "__main__":
    asyncio.run(main())
