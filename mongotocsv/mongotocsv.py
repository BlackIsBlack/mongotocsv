import pandas as pd
from pymongo import MongoClient


class MongoExport:
    db = None

    def __init__(self, host: str, username: str, password: str, port: int = 27017):
        if username and password:
            mongo_uri = (
                f"mongodb://{username}:{password}@{host}:{port}/?authMechanism=DEFAULT"
            )
            self.db = MongoClient(mongo_uri)
        else:
            self.db = MongoClient(host, port)

    def create_csv(self, database, collection, query={}, filename="file", no_id=True):
        """Read from Mongo and Store into DataFrame"""

        # Make a query to the specific DB and Collection
        cursor = self.db[database][collection].find(query)

        # Expand the cursor and construct the DataFrame
        df = pd.DataFrame(list(cursor))

        # Delete the _id
        if no_id and "_id" in df:
            del df["_id"]

        return df.to_csv(f"{filename.replace('.csv','')}.csv", index=False)