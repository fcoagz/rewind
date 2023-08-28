from rewind import rewind
from rewind import extract
from pytube import YouTube as YT
import yaml

folder_path = 'rewind_video'

class YouTube(object):
    def __init__(self, url: str) -> None:
        """
        Clase que representa un objeto de video de YouTube.

        Args:
            url (str): URL del video de YouTube.
        """
        self.url = url

        self.video_id = extract.video_id(url)
        self.watch_video = f"https://youtube.com/watch?v={self.video_id}"

        self.title = extract.title_video(url) if not extract.title_video(url) == "Wayback Machine" else YT(url).title
        self.publish_date = extract.publish_date(url)

    def download(self):
        """
        Descarga el video utilizando la última resolución disponible.
        """
        from requests.exceptions import HTTPError
        try:
            from urllib.parse import urlparse

            with open('rewind/config.predetermined.yaml', 'r') as f:
                data = yaml.load(f, Loader=yaml.FullLoader)
                parsed_url = urlparse(self.url)
                rewind.get(data["rewind"]["host"] + self.video_id, self.title)
        except HTTPError:
            yt_obj = YT(self.url)
            resolutions = [stream.resolution for stream in yt_obj.streams.filter(type="video")]
            dl = yt_obj.streams.filter(res=max(resolutions)).first()
            print(f"[REWIND] - DOWNLOAD VIDEO {self.title}. MB: {dl.filesize_mb}")

            dl.download(folder_path)
            
            print(f"[INFORMATION] - DOWNLOAD IS COMPLETED")