# Here's what has changed in the code:

# The fetch_language_repos function is introduced, which takes a language as input and returns the top starred repositories for that language using the get_starred_repos function.
# The process_language function is a wrapper around fetch_language_repos that runs the asynchronous function using asyncio.run.
# In the main function, a multiprocessing.Pool is created using the with statement, which ensures that the pool is properly closed after the tasks are completed.
# The pool.map method is used to apply the process_language function to each language in the languages list. This effectively distributes the work across multiple processes, taking advantage of multiple cores.
# The results from pool.map are stored in the results list, which contains the top starred repositories for each language.
# The results are printed to the console, similar to the original code.
# By using the multiprocessing module, the code now runs each language's repository fetching task in a separate process, utilizing multiple cores if available on the system. This can significantly improve performance, especially when dealing with I/O-bound tasks like making HTTP requests.

# Note that the multiprocessing module has some limitations when working with asynchronous code, as it creates separate processes rather than threads. In this example, we're using asyncio.run within the process_language function to run the asynchronous code in each process.

# Additionally, be aware that the GitHub API has rate limits, and making too many requests in a short period of time may result in rate limiting errors. You may need to handle rate limiting or use an authenticated API request to increase the rate limit, depending on your use case.

import aiohttp
import asyncio
from multiprocessing import Pool

async def get_starred_repos(language, session):
    url = f"https://api.github.com/search/repositories?q=stars:>100+language:{language}&sort=stars&order=desc"
    headers = {
        "Authorization": f"token PAT",
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

async def fetch_language_repos(language):
    async with aiohttp.ClientSession() as session:
        repos = await get_starred_repos(language, session)
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
