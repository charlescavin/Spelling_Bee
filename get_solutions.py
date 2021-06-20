import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
from webdrivermanager import GeckoDriverManager

# driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
gdd = GeckoDriverManager()
gdd.download_and_install()

driver = webdriver.Firefox()
driver.get("https://www.nytimes.com/puzzles/spelling-bee")

results = []

content = driver.page_source
soup = BeautifulSoup(content, features="lxml")

# Loop over all elements returned by the `findAll` call. It has the filter `attrs` given
# to it in order to limit the data returned to those elements with a given class only.
for element in soup.findAll(attrs={"class": "pz-game-field"}):
    print("element:", element)
