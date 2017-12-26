from requests import Session
from bases.data import data


class APIMethods:

    def __init__(self):
        self.client = Session()
        self.client.verify = False
        self.client.headers.update({'Content-Type': 'application/json'})

    @staticmethod
    def _kupatana_url():
        _url = ''
        return _url
