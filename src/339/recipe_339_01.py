from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("file:///C:/・・・・/339.sample.html")

# 入力欄の要素を取得
input_element = driver.find_element(By.ID, "myinput")

# テキストを入力
input_element.send_keys("検索キーワード")

# 確認用に待機
time.sleep(3)

# 検索ボタンを取得
button_element = driver.find_element(By.ID, "mybutton")

# 確認用に待機
time.sleep(3)

# 検索ボタンを押下
button_element.click()

# 確認用に待機
time.sleep(5)

# ブラウザを閉じる
driver.quit()
