from pytube import request
import yaml

class content:
    def __init__(self, url: str) -> None:
        self.url = url

    @property
    def get(self):
        with open('rewind/config.predetermined.yaml', 'r') as f:
            data = yaml.load(f, Loader=yaml.FullLoader)

            response = request.get(data["rewind"]["web"] + self.url)
            return response