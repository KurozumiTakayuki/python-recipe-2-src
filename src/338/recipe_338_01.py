from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("file:///C:/・・・・/05.sample.html")

# IDで要素を指定
element = driver.find_element(By.CLASS_NAME, "my-class")

# 指定要素のテキストを出力
print("テキスト", element.text)

# 指定要素のdata属性を出力
print("data属性", element.get_attribute("data"))

# 指定要素全体を含むHTMLを出力
print("outerHTML", element.get_attribute("outerHTML"))

# 指定要素の内部のHTMLを出力
print("innerHTML", element.get_attribute("innerHTML"))

# ブラウザを閉じる
driver.quit()
