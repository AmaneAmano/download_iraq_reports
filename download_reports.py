import requests
from bs4 import BeautifulSoup
import os
import time

url = "https://www.asahi.com/articles/ASL4J669JL4JUEHF016.html"

response = requests.get(url)
html = response.text

soup = BeautifulSoup(html, "html.parser")
#beautifulsoupオブジェクトを生成
#HTMLパーサーについて警告が出る場合は、第二引数にパーサーを指定する


def save_pdf(filename, pdf):
    with open(filename, "wb") as f:
        f.write(pdf)


def create_filepath(url):
    return "./iraq_report/" + url.split("/")[-1]


def download_pdf(pdf_url):
    res = requests.get(pdf_url)
    return res.content


td = soup.find_all("td", class_="link")
path = "./iraq_report"

if not os.path.isdir(path):
    os.mkdir(path)

for link in td:
    report_url = link.a.get('href')
    pdf = download_pdf(report_url)
    filename = create_filepath(report_url)
    save_pdf(filename, pdf)
    print("Downloaded: " + filename)
    time.sleep(1)


