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
        self.data = None
        self.geojson = None
        self.columns = None

    def run(self, sql=None):
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
            table = []
            row = []
            # Columns
            for p in res["forGrid"]:
                row.append(p["header"])
            self.columns = row
            # Add rows
            for p in res["features"]:
                row = []
                for v in p["properties"]:
                    row.append(p["properties"][v])
                row.append(json.dumps(p["geometry"]))
                table.append(row)
            self.data = table
            return
