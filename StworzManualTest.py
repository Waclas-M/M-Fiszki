import time
from time import sleep

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


def test(driver,Zestawy,name):
    driver.get("http://mfiszki.pl")


    RedirectToStworz = driver.find_element(By.XPATH, "//nav//div[2]//a[1]")
    RedirectToStworz.click()

    StworzManual = driver.find_element(By.XPATH, "//section[@id='chooseSect']/div/a")
    StworzManual.click()


    question = driver.find_element(By.ID, "question_wpis")
    answer = driver.find_element(By.ID, "answer_wpis")
    add_btn = driver.find_element(By.ID, "btn_dla_wpisu")

    zestaw = Zestawy[name]

    for question_L in zestaw.keys():
        question.send_keys(question_L)
        answer.send_keys(zestaw[question_L])
        add_btn.click()
    time.sleep(1.5)
    save_tab = driver.find_element(By.ID, "Zapis_danych_wpisanych")
    save_tab.click()

    title = driver.find_element(By.ID, "id_title")
    title.send_keys(name)

    save_zestwaw = driver.find_element(By.ID, "make_button")
    save_zestwaw.click()
