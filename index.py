

from bs4 import BeautifulSoup
# import requests
# import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options

# options = Options()
# options.set_preference("browser.download.folderList", 2)
# options.set_preference("browser.download.manager.showWhenStarting", False)
# options.set_preference("browser.download.dir", "/data")
# options.set_preference("browser.helperApps.neverAsk.saveToDisk",
#                        "application/octet-stream,application/pdf")
# options.set_preference("pdfjs.disabled", True)
# options.set_preference("plugin.scan.plid.all", False)
# options.set_preference("plugin.scan.Acrobat", "99.0")


driver = webdriver.Firefox()
# driver.implicitly_wait(3)
weblink = "https://nbtindia.gov.in/NBT_FreeBook4.aspx"
driver.get(weblink)

addr = driver.find_elements_by_link_text('Click Here Download Here')

ids = driver.execute_script(
    "return [...document.querySelectorAll('.Linkgrid')].map(e => e.getAttribute('id'));")
# print(ids)

index = 0
# for each_href in addr:
while(index < len(addr)):

    # print(addr[x].get_attribute['href'])
    # driver.execute_script("window.open('https://nbtindia.gov.in/NBT_FreeBook4.aspx')")

    # driver.current_url = 'https://nbtindia.gov.in/NBT_FreeBook4.aspx'
    # time.sleep(10)
    # webdriver(driver, 20).until(EC.number_of_windows_to_be(2))

    # driver.execute_script("window.open(https://nbtindia.gov.in/NBT_FreeBook4.aspx)")
    wait = WebDriverWait(driver, 1)

    # wait.until(ec.presence_of_element_located((By.ID, "Repeater1_ctl00_lnkedit")))
    driver.implicitly_wait(1)

    # print(len(addr))
    # print(index)
    # driver.switch_to.window(driver.window_handles[index])
    # id = addr[index].get_attribute('id')
    bttnelement = driver.find_element_by_id(ids[index])
    bttni = bttnelement.click()


    webelement = wait.until(ec.presence_of_element_located((By.ID, "btn_sub")))
    downloadButton = driver.find_element_by_id("btn_sub")
    downloadButton.click()
    submitButtonAppear = wait.until(
        ec.presence_of_element_located((By.ID, "Button2")))

    name = driver.find_element_by_name("txt_name")
    name.send_keys("Hello")

    email = driver.find_element_by_name("txt_emailid")
    email.send_keys("dofap49628@mailboxt.com")

    submitButton = driver.find_element_by_id("Button2")
    submitButton.click()

    pdfAppear = wait.until(
        ec.presence_of_element_located((By.ID, "pdfviewread")))
    emebedElement = driver.find_element_by_tag_name('embed')
    pdfLink = emebedElement.get_attribute('src')
    cleanPdfUrl = pdfLink.split("#")[0]

    with open('data.txt', 'a') as file:
        file.write(cleanPdfUrl + "\n")

    # driver.get(pdfLink)
    # print(pdfLink)

    # print(webelement.get_attribute("id"))
    driver.get(weblink)
    index += 1
