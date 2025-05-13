from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("file:///C:/・・・・/337.sample.html")

# IDで要素を指定
element_by_id = driver.find_element(By.ID, "my-id")

# クラス名で要素を指定
element_by_class = driver.find_element(By.CLASS_NAME, "my-class")

# タグ名で要素を指定
element_by_tag = driver.find_element(By.TAG_NAME, "a")

# CSSセレクタで要素を指定
element_by_css = driver.find_element(By.CSS_SELECTOR, "div.my-class > p")

# XPathで要素を指定
element_by_xpath = driver.find_element(By.XPATH, "//div[@class='my-class']")

print(element_by_id.text, element_by_class.text, element_by_tag.text, element_by_css.text, element_by_xpath.text)

# ブラウザを閉じる
driver.quit()
