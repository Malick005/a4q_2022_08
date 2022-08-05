import time
from lib2to3.pgen2 import driver

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.action_chains import ActionChains

def test_open_chrome():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https:/www.amazon.fr")
    barre_recherche = driver.find_element(By.XPATH, "//input[@id='twotabsearchtextbox']")
    barre_recherche.send_keys("playstation 5" + Keys.ENTER)
    driver.quit()


def test_tp_Xpath():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://www.carrefour.fr/")
    barre_recherche = driver.find_element(By.XPATH, "//div[@class='banner-actions-container']/button[text()='Tout accepter']")
    # popup_cookies.click()
    time.sleep(2)
    barre_recherche = driver.find_element(By.XPATH, "//input[@aria-label='rechercher parmi le contenue du site']")
    barre_recherche.send_keys("1664")
    #click cookie
    driver.quit()

def test_css_correction():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://www.carrefour.fr/")
    time.sleep(2)
    close_cookies = driver.find_element(By.CSS_SELECTOR, ".banner-actions-container > button")
    close_cookies.click()
    search_bar = driver.find_element(By.CSS_SELECTOR, "input[required]")
    # possibilite utilisation [required]
    search_bar.send_keys("1664")
    search_button = driver.find_element(By.CSS_SELECTOR, "button[type=submit]")
    # possibilite utilisation [type=submit]
    search_button.click()
    first_result = driver.find_element(By.CSS_SELECTOR, ".product-grid-item:nth-child(1) .main-vertical--image")
    first_result.click()
    time.sleep(1)
    buy_button = driver.find_element(By.CSS_SELECTOR, ".pdp-button-container")
    # possibilite utilisation [aria-label='ACHETER'] : mais attention au changement de langue
    buy_button.click()
    time.sleep(2)
    retrait_en_magazin = driver.find_element(By.CSS_SELECTOR, "div.push-services--pickers > ul > li:nth-child(1) div.ds-body-text")
    delivery24 = driver.find_element(By.CSS_SELECTOR, "div.push-services--pickers > ul > li:nth-child(2) div.ds-body-text")
    delivery1 = driver.find_element(By.CSS_SELECTOR, "div.push-services--pickers > ul > li:nth-child(3) div.ds-body-text")
    assert retrait_en_magazin.text == 'Drive\nRetrait gratuit en magasin'
    assert delivery24.text == ' Livraison\nvotre plein de course en 24h'
    assert delivery1.text == 'Livraison\nvotre plein de course en 1h'
    driver.quit()



def test_css_correction_with_wait():
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get("https://www.carrefour.fr/")

        wait = WebDriverWait(driver, 10)
        close_cookies_button = wait.until(
            expected_conditions.element_to_be_clickable((By.CSS_SELECTOR, "#onetrust-accept-btn-handler")))
        close_cookies_button.click()
        search_bar = driver.find_element(By.CSS_SELECTOR, "input[required]")
        # possibilite utilisation [required]
        search_bar.send_keys("1664")
        search_button = driver.find_element(By.CSS_SELECTOR, "button[type=submit]")
        # possibilite utilisation [type=submit]
        search_button.click()
        first_result = driver.find_element(By.CSS_SELECTOR, ".product-grid-item:nth-child(1) .main-vertical--image")
        first_result.click()

        buy_button = wait.until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR, ".pdp-button-container")))
        # possibilite utilisation [aria-label='ACHETER'] : mais attention au changement de langue
        buy_button.click()

        retrait_en_magasin = wait.until(
            expected_conditions.element_to_be_clickable(
                (By.CSS_SELECTOR, ".push-services--pickers li:nth-child(1) label")))
        delivery24 = driver.find_element(By.CSS_SELECTOR, ".push-services--pickers li:nth-child(2) label")
        delivery1 = driver.find_element(By.CSS_SELECTOR, ".push-services--pickers li:nth-child(3) label")

        assert retrait_en_magasin.text == 'Drive\nRetrait gratuit en magasin'
        assert "Drive" in retrait_en_magasin.text
        assert delivery24.text == 'Livraison\nVotre plein de course en 24h'
        assert delivery1.text == 'Livraison 1h\nVos courses d’appoint en 1h'
        driver.quit()

