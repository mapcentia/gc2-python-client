import requests
import json


class Schema:
    def __init__(
            self,
            gc2
    ):
        self.__gc2 = gc2
        self.__url = f"{gc2.url}/schema"
        self.data = None

    def get(self):
        resp = requests.get(f"{self.__url}", headers=self.__gc2.headers)
        if resp.status_code != 200:
            raise Exception(f"Error {resp.status_code}: {resp.text}")
        else:
            self.data = json.loads(resp.text)["data"]
            return
