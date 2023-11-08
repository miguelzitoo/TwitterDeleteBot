from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import pyautogui
import time

usuario = input('Qual seu user: ')
senha = input('Qual sua senha: ')
quantidade_post = int(input('Quantidade de post que você quer apagar? '))
driver = webdriver.Chrome(ChromeDriverManager().install())

driver.get(f'https://twitter.com/{usuario}')
time.sleep(5)
# usuario/avançar
driver.find_element(By.XPATH, '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[5]/label').click()
pyautogui.write(usuario)
driver.find_element(By.XPATH, '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[6]/div').click()
time.sleep(3)
# inserir senha 
driver.find_element(By.XPATH, '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div').click()
pyautogui.write(senha)
time.sleep(1)
driver.find_element(By.XPATH, '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div[1]/div/div/div').click()
time.sleep(5)
# tela cheia 
driver.set_window_size(1920, 1080)
time.sleep(2)
i = 0 

for i in range(quantidade_post):
    bolinha = driver.find_element(By.CLASS_NAME, 'r-1jkjb')
    bolinha.click()
    time.sleep(3)
    exc = driver.find_element(By.XPATH, '//*[@id="layers"]/div[2]/div/div/div/div[2]/div/div[3]/div/div/div/div[1]/div[2]/div/span')
    excluir = exc.text
    if excluir == "Excluir" or "Delete":
        exc.click()
        time.sleep(1)
        x = driver.find_element(By.XPATH,'//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div[2]/div[1]/div/span')
        dele = x.text
        if dele == "Excluir" or "Delete":
            x.click()
        else:
            next
    else:
        rt = driver.find_element(By.CLASS_NAME, 'r-xoduu5')
        rt.click()
        next
    time.sleep(3)
    i += 1

exit()