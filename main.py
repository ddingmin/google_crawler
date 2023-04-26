from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import urllib.request
import os
driver = webdriver.Chrome(service= Service(ChromeDriverManager().install()))


def read_keywords():
    f = open("keywords.txt", 'r', encoding='UTF8')
    keywords = []
    while 1:
        keyword = f.readline().strip()
        if not keyword: break
        keywords.append(keyword)
    return keywords


def crawl_google(keywords):
    for keyword in keywords:
        idx = 1
        url = f"https://www.google.co.kr/search?q={keyword}&tbm=isch"
        img_selector = "img.Q4LuWd"
        driver.get(url)
        images = driver.find_elements(By.CSS_SELECTOR, img_selector)

        # 키워드에 맞는 폴더 생성
        if not os.path.exists(keyword):
            os.makedirs(keyword)
    
        # 이미지 저장
        for image in images:
            image_src = image.get_attribute('src')
            if not image_src: continue
            urllib.request.urlretrieve(image_src, f'{keyword}/{idx}.png')
            idx += 1

crawl_google(read_keywords())