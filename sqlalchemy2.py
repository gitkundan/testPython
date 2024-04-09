"""
[
  {
    "physical_server_id": 1
  },
  {
    "physical_server_id": 2,
    "virtual_platform": {
      "vp_id": 100
    }
  },
  {
    "physical_server_id": 3,
    "virtual_platform": {
      "vp_id": 200,
      "cluster": {
        "cluster_id": 900
      }
    }
  },
  {
    "physical_server_id": 4,
    "virtual_platform": {
      "vp_id": 300,
      "cluster": {
        "cluster_id": 900
      }
    }
  }
]
"""

import json
from sqlalchemy import create_engine, Column, Integer, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker

_file=r'C:\Users\John\Downloads\testPython\server_data.json'
with open(_file) as f:
    json_data=json.load(f)

# Define your database connection
engine = create_engine('sqlite:///cluster.sqlite')

#######################

Base = declarative_base()


class PhysicalServer(Base):
    __tablename__ = 'physical_servers'

    id = Column(Integer, primary_key=True)
    virtual_platform_id = Column(Integer, ForeignKey('virtual_platforms.id'))

    # virtual_platform = relationship("VirtualPlatform", back_populates="physical_servers")

class VirtualPlatform(Base):
    __tablename__ = 'virtual_platforms'

    id = Column(Integer, primary_key=True)
    cluster_id = Column(Integer, ForeignKey('clusters.id'))

    # physical_servers = relationship("PhysicalServer", back_populates="virtual_platform")
    # cluster = relationship("Cluster", back_populates="virtual_platforms")

class Cluster(Base):
    __tablename__ = 'clusters'

    id = Column(Integer, primary_key=True)
    cluster_id=Column(Integer)

    # virtual_platforms = relationship("VirtualPlatform", back_populates="cluster")

#DDL
Base.metadata.create_all(engine)




#INSERT

# Create the engine and session
Session = sessionmaker(bind=engine)
session = Session()

# Parse the JSON data and ingest into the database
for server_data in json_data:
    # Create or get the cluster
    cluster_data = server_data.get("virtual_platform", {}).get("cluster", {})
    cluster_id = cluster_data.get("cluster_id")
    cluster = session.query(Cluster).filter_by(id=cluster_id).first()
    if not cluster:
        for key, value in cluster_data.items():
            if hasattr(cluster, key):
                setattr(cluster, key, value)
        session.add(cluster)
        session.commit()

    # Create or get the virtual platform
    vp_data = server_data.get("virtual_platform", {})
    vp_id = vp_data.get("vp_id")
    virtual_platform = session.query(VirtualPlatform).filter_by(id=vp_id).first()
    if not virtual_platform:
        virtual_platform = VirtualPlatform(cluster_id=cluster.id)
        session.add(virtual_platform)
        session.commit()

    # Create the physical server
    physical_server_id = server_data.get("physical_server_id")
    physical_server = PhysicalServer(virtual_platform_id=virtual_platform.id)
    session.add(physical_server)

# Commit the changes
session.commit()

