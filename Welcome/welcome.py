from selenium import webdriver

browser = webdriver.Chrome()
browser.get("https://www.youtube.com/")
browser.quit()