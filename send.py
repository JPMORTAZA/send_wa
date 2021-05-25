from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

#gerador de números
primeiro_num = 5551990000000 #numero de inicio
ultimo_num = 5551990000050 #numero fim 
link = "https://wa.me/"
mensagem ='''
    Olá, tudo bem? 
    Estou testando uma ferramenta de automatização, não precisa me responder.
    Valeu
''' #cada linha é um enter ou seja envia uma mensagem
arquivo = open("numeros.txt", "w")
for linha in range(primeiro_num, ultimo_num):
    arquivo.write(f"{link}{linha}\n")
arquivo.close()
driver = webdriver.Chrome()

with open("numeros.txt","r") as arquivo:
    for linha in arquivo.readlines():
        driver.get(linha)
        time.sleep(2)
        driver.find_element_by_xpath('//*[@id="action-button"]').click()
        time.sleep(2)
        driver.find_element_by_xpath('//*[@id="fallback_block"]/div/div/a').click()
        time.sleep(3)
        driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]').send_keys(mensagem)
        driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]').send_keys(Keys.ENTER)
        time.sleep(1)
