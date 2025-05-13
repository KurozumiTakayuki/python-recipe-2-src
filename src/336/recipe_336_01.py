from selenium import webdriver

driver = webdriver.Chrome()

# https://gihyo.jp/に遷移
driver.get("https://gihyo.jp/")

# ページのタイトルを取得して出力
print(driver.title, driver.current_url, driver.get_window_size())

# ブラウザを閉じる
driver.quit()
