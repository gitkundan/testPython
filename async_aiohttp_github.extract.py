import requests
from pprint import pprint
import aiohttp
import time
import json

start_time = time.time()


# pat = r"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"

# BASE_URL = r"https://api.github.com"

# users_list = ["cevoaustralia", "numfocus", "pandas-dev"]

# header = {"Authorization": f"Bearer {pat}"}
# header.update({"Accept": "application/vnd.github+json"})

# session = requests.Session()
# repos = session.get(f"{BASE_URL}/users/gitkundan/repos")
# pprint(repos.json())


# session.close

# print("--- %s seconds ---" % (time.time() - start_time))


# def get_users():
#     return users_list

import aiohttp
import asyncio
import json

class GitHubSession:
    BASE_URL = r"https://api.github.com"
    def __init__(self) -> None:
        self.pat = r"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"
        self.header = {"Authorization": f"Bearer {self.pat}"}
        self.header.update( {"Accept": "application/vnd.github+json"})

    async def fetch(self,session,url):
        """generic method to get response from any endpoint"""
        async with session.get(url) as response:
            return await response.json()
    
    async def get_users(self,session,id):
        url_user=f"https://api.github.com/users?since={id}"
        return await self.fetch(session,url_user)
        
    async def get_repos(self, session, user):
        url_repo = user['repos_url']
        return await self.fetch(session,url_repo)

    async def main(self):
        async with aiohttp.ClientSession(headers=self.header) as session:
            _users = [self.get_users(session,i) for i in range(1)]
            users = await asyncio.gather(*_users)
            _repos=[self.get_repos(session,user)for user in users for user in user]
            repos=await asyncio.gather(* _repos)
            return (users,repos)

if __name__ == "__main__":
    obj = GitHubSession()
    loop = asyncio.get_event_loop()
    users,repos=loop.run_until_complete(obj.main())
    with open('output.json','w') as f:
        json.dump(repos,f)
