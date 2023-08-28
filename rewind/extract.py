from urllib.parse import urlparse
from urllib import error
import yaml
import requests
from bs4 import BeautifulSoup

from typing import Any

def video_id(url: str) -> Any:
    video_url = urlparse(url)

    if video_url.netloc == "youtu.be":
            id = video_url.path.split('/')
            return id[1::][0]
    elif video_url.netloc == "www.youtube.com":
        id = video_url.query.split('=')
        return id[1::][0]
    else:
        raise error.URLError("The address does not match the platform")
    
def title_video(url: str):
    with open('rewind/config.predetermined.yaml', 'r') as f:
        data = yaml.load(f, Loader=yaml.FullLoader)

        response = requests.get(data["rewind"]["web"] + url)
        soup = BeautifulSoup(response.content, "html.parser")

        return soup.title.text
    
def publish_date(url: str):
    """
    code not created by me. created by the pytube community
    """
    from datetime import datetime
    from rewind.request import content
    from pytube import extract
    from pytube.exceptions import RegexMatchError

    watch_html = content(url).get

    try:
        result = extract.regex_search(
            r"(?<=itemprop=\"datePublished\" content=\")\d{4}-\d{2}-\d{2}",
            watch_html, group=0
        )
    except RegexMatchError:
        return None
    return datetime.strptime(result, '%Y-%m-%d')
