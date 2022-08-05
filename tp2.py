import time
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains


def test_produit_indisponible():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://www.carrefour.fr/")
    wait = WebDriverWait(driver, 10)
    close_cookies_button = wait.until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "#onetrust-accept-btn-handler")))
    close_cookies_button.click()
    hamb_button = driver.find_element(By.CSS_SELECTOR, "span[class=mainbar__nav-toggle-icon]")
    hamb_button.click()

    # hover to epicerie salee
    epicerie_salee = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".nav-item__menu-link [alt='Epicerie salée']")))
    action = ActionChains(driver)
    action.move_to_element(epicerie_salee)
    action.perform()

    # hover to feculent
    feculent = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#data-menu-level-1_R12 > li:nth-child(7)")))
    action.move_to_element(feculent)
    action.perform()

    # clic on pate
    pates = driver.find_element(By.CSS_SELECTOR, "#data-menu-level-2_R12F05 > li:nth-child(3)")
    pates.click()

    # Call function to open product
    # openProducts(driver, 4)
    #openProducts2(driver, 3)

    # Clic on buy button
    buy_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#data-produit-acheter")))
    buy_button.click()

    # Clic on Drive pick up
    pick_up = wait.until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, ".push-services--pickers li:nth-child(1)")))
    pick_up.click()

    # print zip code inside text box
    zip_code = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "[data-cs-mask=true]")))
    zip_code.send_keys("75001")
    time.sleep(1)
    zip_code.send_keys(Keys.ENTER)

    # select first store available
    first_store = wait.until(EC.element_to_be_clickable(
        (By.CSS_SELECTOR, ".drive-service-list__list > li:nth-child(1) button")))
    first_store.click()

    # Control : product is not available
    add_info = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".missing-products")))
    assert "indisponible" in add_info.text
    print("Test is PASSED !!!!")

    # window_in = add_info.get_attribute('class')
    # print(window_in)
    # assert window_in=='missing'

    driver.quit()