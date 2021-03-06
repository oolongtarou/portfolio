import requests
from bs4 import BeautifulSoup
import urllib
from pathlib import Path
import uuid
import time


# 関数の定義
def image_scraping(output_folder, url):
    Path(output_folder).mkdir(exist_ok=True)


    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    images = soup.find_all("img")

    for image in images:
        long_image_url = urllib.parse.urljoin(url, image["src"])
        image_data = requests.get(long_image_url)
        
        time.sleep(2)
        
        with open(str(output_folder)+str(uuid.uuid4())+str(".png"),"wb") as file:
            file.write(image_data.content)
        

# 関数の実行
# image_scraping('出力先フォルダ', '画像を取得したいサイトのURL')
image_scraping()