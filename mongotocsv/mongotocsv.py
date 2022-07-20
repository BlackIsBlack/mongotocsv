import pandas as pd
from pymongo import MongoClient


class MongoExport:
    """
    Create a CSV from a MongoDB collection
    """

    db = None

    def __init__(self, host: str, username: str, password: str, port: int = 27017):
        # Connect to MongoDB
        # If the database requires authentication
        if username and password:
            mongo_uri = (
                f"mongodb://{username}:{password}@{host}:{port}/?authMechanism=DEFAULT"
            )
            self.db = MongoClient(mongo_uri)
        # If no authentication is needed
        else:
            self.db = MongoClient(host, port)

    def create_csv(self, database, collection, query={}, filename="file", no_id=True):
        """Read from Mongo and create a CSV

        Args:
            database (str): The name of the database
            collection (str): The name of the collection
            query (dict, optional): The query to filter the collection. Defaults to {}. example: {'_id': {'$gt': 1}}
            filename (str, optional): The name of the file to be created. Defaults to "file".
            no_id (bool, optional): Whether to include the _id field in the CSV. Defaults to True.

        Returns:
            str: The name of the file created
        """
        # Make a query to the specific DB and Collection
        cursor = self.db[database][collection].find(query)

        # Expand the cursor and construct the DataFrame
        df = pd.DataFrame(list(cursor))

        # Delete the _id
        if no_id and "_id" in df:
            del df["_id"]

        # Write the DataFrame to a CSV
        return df.to_csv(f"{filename.replace('.csv','')}.csv", index=False)

    def create_xlsx(self, database, collection, query={}, filename="file", no_id=True):
        """Read from Mongo and create a XLSX

        Args:
            database (str): The name of the database
            collection (str): The name of the collection
            query (dict, optional): The query to filter the collection. Defaults to {}. example: {'_id': {'$gt': 1}}
            filename (str, optional): The name of the file to be created. Defaults to "file".
            no_id (bool, optional): Whether to include the _id field in the CSV. Defaults to True.

        Returns:
            str: The name of the file created
        """
        # Make a query to the specific DB and Collection
        cursor = self.db[database][collection].find(query)

        # Expand the cursor and construct the DataFrame
        df = pd.DataFrame(list(cursor))

        # Delete the _id
        if no_id and "_id" in df:
            del df["_id"]

        # Write the DataFrame to a CSV
        return df.to_excel(f"{filename.replace('.xlsx','')}.xlsx", index=False)

    def create_json(self, database, collection, query={}, filename="file", no_id=True):
        """Read from Mongo and create a JSON

        Args:
            database (str): The name of the database
            collection (str): The name of the collection
            query (dict, optional): The query to filter the collection. Defaults to {}. example: {'_id': {'$gt': 1}}
            filename (str, optional): The name of the file to be created. Defaults to "file".
            no_id (bool, optional): Whether to include the _id field in the CSV. Defaults to True.

        Returns:
            str: The name of the file created
        """
        # Make a query to the specific DB and Collection
        cursor = self.db[database][collection].find(query)

        # Expand the cursor and construct the DataFrame
        df = pd.DataFrame(list(cursor))

        # Delete the _id
        if no_id and "_id" in df:
            del df["_id"]

        # Write the DataFrame to a CSV
        return df.to_json(f"{filename.replace('.json','')}.json", orient="records", index=False)