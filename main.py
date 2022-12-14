from selenium import webdriver
import time


chrome = webdriver.Chrome(executable_path='./chromedriver')
chrome.get('https://www.google.com')
time.sleep(2)
chrome.get('https://www.zapimoveis.com.br/')

print("abrir")

