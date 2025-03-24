from selenium.webdriver.common.by import By

def test(driver,Zestawy,name):

    wybierzBTN = driver.find_element(By.XPATH, f"//button[@value='{name}']")
    wybierzBTN.click()

    WpisywanieReczneBtn = driver.find_element(By.ID, "Mode_wpisywanie")
    WpisywanieReczneBtn.click()

    OdpInput = driver.find_element(By.ID, "Odpowiedz")
    DalejBtn = driver.find_element(By.ID, "Dalej")

    zestaw = Zestawy[name]

    for question in zestaw:
        OdpInput.send_keys(zestaw[question])
        DalejBtn.click()

    ZestawyLink = driver.find_element(By.XPATH, "//div[@id='EndGame']//div[3]//a")
    ZestawyLink.click()