import requests
import logging
import json


class Sql:

    def __init__(
            self,
            gc2
    ):
        self.__gc2 = gc2
        self.__url = f"{gc2.url}/sql"
        self.data_list = None
        self.data_dict = None
        self.affected_rows = None
        self.geojson = None
        self.columns = None

    def select(self, sql=None):
        req = {
            "q": sql,
            "srs": 4326,
            "format": "geojson",
            "geoformat": "wkt",
            "allstr": None,
            "lifetime": 0,
            "base64": None
        }
        resp = requests.post(self.__url, headers=self.__gc2.headers, data=json.dumps(req))
        if resp.status_code != 200:
            raise Exception(f"Error {resp.status_code}: {resp.text}")
        else:
            self.geojson = resp.text
            res = json.loads(resp.text)
            row = []
            table_list = []
            table_dict = []
            # Columns
            for p in res["forGrid"]:
                if p["type"] != "geometry":
                    row.append(p["header"])
            self.columns = row
            # Add rows
            for p in res["features"]:
                _list = []
                _dict = {}
                for v in p["properties"]:
                    value = p["properties"][v];
                    _list.append(value)
                    _dict[v] = p["properties"][v]
                table_list.append(_list)
                table_dict.append(_dict)
            self.data_list = table_list
            self.data_dict = table_dict
            return

    def transaction(self, sql=None):
        req = {
            "q": sql,
            "base64": None
        }
        resp = requests.post(self.__url, headers=self.__gc2.headers, data=json.dumps(req))
        if resp.status_code != 200:
            raise Exception(f"Error {resp.status_code}: {resp.text}")
        else:
            self.geojson = resp.text
            res = json.loads(resp.text)
            self.affected_rows = res['affected_rows']
            return
