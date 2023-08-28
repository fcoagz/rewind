from tqdm import tqdm
import requests
import os

def get(url: str, title: str) -> None:
    response = requests.get(url, stream = True)

    if not response.status_code == requests.codes.ok:
        raise response.raise_for_status()

    print(f"[DEBUG] - WE HAVE ACCESSED THE PAGE {title}")

    total_size = int(response.headers.get('content-length', 0))
    folder_path = 'rewind_video'

    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
    
    ext = '.mp4'
    next_file_name = f'{title}{ext}'

    progress_bar = tqdm(total = total_size, unit='iB', unit_scale=True, desc=f'[REWIND] - DOWNLOAD VIDEO {title}')
    with open(os.path.join(folder_path, next_file_name), "wb") as f:
        for i in response.iter_content(chunk_size=1024):
            progress_bar.update(len(i))
            f.write(i)
    progress_bar.close()
    
    print(f"[INFORMATION] - DOWNLOAD IS COMPLETED")