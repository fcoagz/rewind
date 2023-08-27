from rewind import rewind
import yaml

class YouTube(object):
    def __init__(self, url: str) -> None:
        self.url = url
    
    # @property
    # def file_name(self):
    #     import os

    #     folder_path = 'rewind_video'
    #     return r"{}\{1}".format(folder_path, os.listdir(folder_path)[-1])

    @property
    def title(self):
        import requests
        from bs4 import BeautifulSoup

        with open('rewind/config.predetermined.yaml', 'r') as f:
            data = yaml.load(f, Loader=yaml.FullLoader)

            response = requests.get(data["rewind"]["web"] + self.url)
            soup = BeautifulSoup(response.content, "html.parser")

            return soup.title.text
    
    def download(self):
        from urllib.parse import urlparse, parse_qs

        with open('rewind/config.predetermined.yaml', 'r') as f:
            data = yaml.load(f, Loader=yaml.FullLoader)
            parsed_url = urlparse(self.url)
            return rewind.get(data["rewind"]["host"] + parse_qs(parsed_url.query)['v'][0], self.title)


            