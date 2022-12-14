from selenium import webdriver
import time
from selenium.webdriver.common.by import By

url = 'https://www.zapimoveis.com.br/aluguel/apartamentos/sp+sao-paulo+zona-sul+vl-mariana/?pagina='

preco = '//*[@id="app"]/section/div[1]/div[3]/div[2]/div[1]/div[@@]/div/div[1]/div[2]/div[1]/div/p/strong'
p =     '//*[@id="app"]/section/div[1]/div[3]/div[2]/div[1]/div[2]/div/div[1]/div[2]/div[1]/div/p/strong'
chrome = webdriver.Chrome(executable_path='./chromedriver')
#chrome.get('https://www.google.com')
#time.sleep(2)
#chrome.get('https://www.zapimoveis.com.br/')


for i in range(10):
    chrome.get(url + str(i + 1))
    time.sleep(1)

    for i in range(20):

        try:
            price = chrome.find_element(By.XPATH, preco.replace('@@', str(i + 1))).text
            print(price)

        except:
          print('uma propaganda foi encontrada')




print("abrir")

