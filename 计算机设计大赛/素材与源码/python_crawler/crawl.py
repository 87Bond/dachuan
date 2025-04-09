import os
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import uuid
import time
import json
# 设置 Selenium WebDriver
options = webdriver.ChromeOptions()
options.add_argument('--headless')  # 无头模式，不打开浏览器界面
# options.add_argument('--disable-gpu')  # 禁用 GPU
# options.add_argument('--no-sandbox')  # 不使用沙盒模式

# 自动下载并设置 chromedriver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)


# def scroll_page(driver, scroll_pause_time=5, max_scrolls=15):
#     """模拟滚动页面"""
#     last_height = driver.execute_script("return document.body.scrollHeight")  # 获取当前页面的高度
#     for _ in range(max_scrolls):  # 控制滚动的次数
#         driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")  # 滚动到底部
#         time.sleep(scroll_pause_time)  # 等待页面加载
#         new_height = driver.execute_script("return document.body.scrollHeight")  # 获取新的页面高度
#         if new_height == last_height:  # 如果页面高度没有变化，说明已加载完所有内容
#             break
#         last_height = new_height


def get_photos(url,js):
    # 创建文件夹保存图片
    os.makedirs('culture', exist_ok=True)

    # 加载页面
    driver.get(url)

    # # 滚动页面并加载更多内容
    # scroll_page(driver)

    # 获取页面中所有的 img 标签
    img_tags = driver.find_elements(By.TAG_NAME, 'img')

    for img in img_tags:
        time.sleep(0.5)
        try:
            # 获取 img 标签的宽度和高度
            width = img.get_attribute('width')
            height = img.get_attribute('height')

            # 如果没有宽度或高度，跳过此图片
            if width is None or height is None:
                continue

            # 如果图片宽度或高度小于40，跳过
            if int(width) < 40 or int(height) < 40:
                continue

            if int(width) > 1024 or int(height) > 1024:
                continue
            # 获取图片的 URL
            img_url = img.get_attribute('src')
            if not img_url:
                continue  # 如果没有图片链接，跳过

            # 获取图片的文件名，并添加 UUID
            code=uuid.uuid4().hex
            img_name = os.path.join('culture', code + '.' + 'jpg')

            # 下载图片
            img_response = requests.get(img_url, stream=True)
            img_response.raise_for_status()  # 如果请求失败，抛出异常
            
            # 保存图片
            with open(img_name, 'wb') as f:
                f.write(img_response.content)
                print(f"下载成功: {img_name}")
                js['data_lists'].append({'caption':img.get_attribute('alt'),'name':code})
                

        except requests.exceptions.RequestException as e:
            print(f"下载图片 {img_url} 时发生错误: {e}")


if __name__ == '__main__':
    # 输入需要爬取的 URL
    file=open('images.json','r')
    js=json.load(file)
    file.close()
    urls = [
        "https://digicol.dpm.org.cn/?page=1&category=5,15,10,21,14,6,4,3,23,7,20"
    ]
    for url in urls:
        get_photos(url,js)
    file=open('images.json','w')
    file.write(json.dumps(js,ensure_ascii=False,indent=4))
    file.close()
    # 关闭浏览器
    driver.quit()
