from selenium.webdriver.common.by import By

def test(driver,Zestawy):

    RedirectToProfil = driver.find_element(By.XPATH, "//nav//div[2]//a[3]")
    RedirectToProfil.click()
    Zestawy_TEST = []
    for x in range(len(Zestawy)):
        ZestawName = driver.find_element(By.XPATH,"//tbody//tr[1]//td[1]")
        text = ZestawName.text
        Zestawy_TEST.append(text)

    UsunBtn = driver.find_element(By.XPATH, "//tbody//tr[1]//td[3]//button")
    UsunBtn.click()

    rows = driver.find_elements(By.XPATH, "//tbody//tr")
    return len(rows)




