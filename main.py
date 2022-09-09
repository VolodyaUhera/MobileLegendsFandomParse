"""
requests
B4s python
На вхід url сторінка на вихід список url з героями
"""
import requests
from bs4 import BeautifulSoup
import os
import csv
import pandas as pd


def main():
    domain = "https://mobile-legends.fandom.com"
    url = 'https://mobile-legends.fandom.com/wiki/List_of_heroes'

    output_folder = "output"
    os.makedirs(output_folder, exist_ok=True)

    res = requests.get(url)

    soup = BeautifulSoup(res.text, "lxml")

    all_links = soup.select("tr > td > b > a[href]")

    with open(os.path.join(output_folder, 'test.csv'), 'w') as f:
        f.write("title, href\n")
        for link in all_links:
            f.write(f"{link.get('title')},{domain + link.get('href')}\n")


if __name__ == '__main__':
    main()
