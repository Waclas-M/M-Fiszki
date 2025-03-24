from selenium.webdriver.common.by import By

def test(driver,Zestawy,name):

    EdytujBtn = driver.find_element(By.XPATH, "//tbody//tr[2]//td[4]//button")
    EdytujBtn.click()

    UsunOnAllRekords = driver.find_elements(By.XPATH, "//tbody//tr//td//button")
    print(UsunOnAllRekords)
    for button in UsunOnAllRekords:
        button.click()


    question = driver.find_element(By.ID, "question_wpis")
    answer = driver.find_element(By.ID, "answer_wpis")
    add_btn = driver.find_element(By.ID, "btn_dla_wpisu")

    zestaw = Zestawy[name]

    for question_L in zestaw.keys():
        question.send_keys(question_L)
        answer.send_keys(zestaw[question_L])
        add_btn.click()

    save_tab = driver.find_element(By.ID, "Zapis_danych_wpisanych")
    save_tab.click()

