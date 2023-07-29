import typing
import os
from dotenv import load_dotenv
from filestack import Client


load_dotenv()
API_KEY: typing.Final = os.getenv("API_KEY")


class FileSharer:

    def __init__(self, filepath, api_key=API_KEY):
        self.filepath = filepath
        self.api_key = api_key

    def share(self):
        client = Client(self.api_key)
        file_link = client.upload(filepath=self.filepath)
        return file_link.url
