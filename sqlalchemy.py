# https://github.com/zzzeek/python_web_conf_2023/blob/main/slides/05_orm.py
# author tutorial : SQLAlchemy 2.0 - Let's Talk Tutorial.

import sqlalchemy
import json
from dataclasses import dataclass
from typing import List

#mockup json data
github_data = {
    "users": [
        {
            "username": "user1",
            "repositories": [
                {
                    "repo_name": "repo1",
                    "languages": ["Python", "JavaScript", "HTML"]
                },
                {
                    "repo_name": "repo2",
                    "languages": ["Java", "C#"]
                }
            ]
        },
        {
            "username": "user2",
            "repositories": [
                {
                    "repo_name": "repo3",
                    "languages": ["Python", "Ruby"]
                },
                {
                    "repo_name": "repo4",
                    "languages": ["JavaScript", "CSS"]
                }
            ]
        }
    ]
}


#serialize data into dataclass - (1)
@dataclass
class Repository:
    repo_name: str
    languages: List[str]

@dataclass
class User:
    username: str
    repositories: List[Repository]

@dataclass
class GitHubData:
    users: List[User]

#serialize data into dataclass - (2)
def serialize_github_data(data):
    users = []
    for user_data in data['users']:
        repositories = []
        for repo_data in user_data['repositories']:
            repo = Repository(repo_data['repo_name'], repo_data['languages'])
            repositories.append(repo)
        user = User(user_data['username'], repositories)
        users.append(user)
    return GitHubData(users)


github_data_instance = serialize_github_data(github_data)
print(github_data_instance)


#persist data into sqlite using sqlalchemy
To persist the Python dataclasses into an SQLite database called `hr.db` using SQLAlchemy 2.0, you'll need to follow these steps:

1. **Define the SQLAlchemy Models**: First, you need to define SQLAlchemy models that correspond to your dataclasses. These models will be used to create the database tables.

2. **Create the Database and Tables**: Next, you'll create the SQLite database and the tables based on your models.

3. **Insert Data**: Finally, you'll insert the data from your dataclasses into the database.

Here's how you can do it:

### Step 1: Define the SQLAlchemy Models

```python
from sqlalchemy import create_engine, Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import declarative_base, Mapped
from sqlalchemy.sql import func
from typing import Optional
from datetime import datetime

Base = declarative_base()

class Repository(Base):
    __tablename__ = 'repositories'
    id = Column(Integer, primary_key=True)
    repo_name = Column(String)
    languages = Column(String) # For simplicity, we'll store languages as a comma-separated string
    user_id = Column(Integer, ForeignKey('users.id'))

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, init=False)
    username = Column(String)
    repositories = relationship("Repository", back_populates="user")

Repository.user = relationship("User", back_populates="repositories")
```

### Step 2: Create the Database and Tables

```python
engine = create_engine('sqlite:///hr.db')
Base.metadata.create_all(engine)
```

### Step 3: Insert Data

Before inserting data, you need to serialize your dataclasses into instances of the SQLAlchemy models. This involves converting the `languages` list into a comma-separated string for the `Repository` model.

```python
from sqlalchemy.orm import Session

def insert_data(github_data_instance):
    session = Session(engine)

    for user in github_data_instance.users:
        db_user = User(username=user.username)
        session.add(db_user)
        for repo in user.repositories:
            db_repo = Repository(repo_name=repo.repo_name, languages=', '.join(repo.languages), user_id=db_user.id)
            session.add(db_repo)

    session.commit()
    session.close()

# Assuming github_data_instance is the instance of GitHubData you created earlier
insert_data(github_data_instance)
```

This function, `insert_data`, iterates over the `GitHubData` instance, creating `User` and `Repository` instances for each user and repository. It then adds these instances to the session and commits the transaction to the database.

