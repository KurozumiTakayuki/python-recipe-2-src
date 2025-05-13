from selenium import webdriver

driver = webdriver.Chrome()

# https://gihyo.jp/に遷移
driver.get("https://gihyo.jp/")

# ページのタイトルを取得して出力
print(driver.title)

# ブラウザを閉じる
driver.quit()
