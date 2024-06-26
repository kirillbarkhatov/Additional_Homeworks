import logging
import json
import requests

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

fh = logging.FileHandler("logs.log", mode= "a")
formatter = logging.Formatter("%(message)s")
fh.setFormatter(formatter)
logger.addHandler(fh)


def get_photos(album: int, limit: int = 100):
    logger.info("INFO:root:Starting app...")
    url = "https://jsonplaceholder.typicode.com/photos"
    response = requests.get(url)
    data_response = list(filter(lambda x: x["albumId"] == album, response.json()))
    print(json.dumps(data_response, indent=4))
    logger.info(f"INFO:root:Downloading album {album} images...")
    count_photos = min(limit, len(data_response))
    print(count_photos)
    for i in range(count_photos):
        path_file = f"photos/{album}-{i+1}.jpg"
        url_photo = data_response[i]["thumbnailUrl"]
        photo = requests.get(url_photo)
        logger.info(f"INFO:root:Saving image {i + 1} to {path_file}")
        with open(path_file, "wb") as file:
            file.write(photo.content)

    logger.info(f"INFO:root:Finished downloading images. Total images downloaded: {count_photos}")



get_photos(2, 5)
