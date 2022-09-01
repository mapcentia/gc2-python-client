import requests
import logging


class Gc2:
    def __init__(
            self,
            url="https://swarm.gc2.io/",
            api_version="v3",
            user=None,
            pw=None,
    ):
        self.api_version = api_version
        self.base_url = url
        self.headers = {"content-type": "application/json; charset=utf-8"}
        self.user = None
        self.__password = None
        self.__auth = None
        if user and pw:
            self.set_authentication(user, pw)
        self.__set_url()

    def __set_url(self):
        self.url = f"{self.base_url}/api/{self.api_version}"

    def __check_auth(self):
        url = f"{self.url}/oauth/token"
        resp = requests.post(url, '{"grant_type": "password","username": "mydb","password": "hawk2000","database": "mydb","client_id": "xxxxxxxxxx","client_secret": "xxxxxxxxxx"}')
        if resp.status_code != 200:
            raise Exception(
                "Wrong user or password. Please check your inputs."
            )
        elif resp.status_code == 400:
            raise Exception(f"Error {resp.status_code}: {resp.text}")
        else:
            logging.info(f"{self.user} is logged in.")

    def set_authentication(self, user, pw):
        """
        Set the user and password for the actinia instance and checks if the
        logging is working via the locations endpoint.
        :param user: String with username
        :param pw: String with user password
        :raises: exception if the user cannot log in
        """
        self.user = user
        self.__password = pw
        self.__auth = (user, pw)
        try:
            self.__check_auth()
        except Exception as e:
            self.user = None
            self.__password = None
            self.__auth = None
            raise e
