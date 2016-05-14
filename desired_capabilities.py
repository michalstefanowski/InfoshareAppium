from appium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

def switch_auto_correction_in_settings():
    """
    Switch auto correction in device settings for different test scenario
    """
    desired_capabilities = {}
    desired_capabilities['platformName'] = 'iOS'
    desired_capabilities['platformVersion'] = '9.2'
    desired_capabilities['deviceName'] = 'iPhone 6 9.2'
    desired_capabilities['app'] = "settings"
    desired_capabilities['noReset'] = True
    driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_capabilities)

    # Switch auto correction
    driver.find_element(By.ID, "General").click()
    driver.find_element(By.ID, "Keyboard").click()
    driver.find_element(By.XPATH, "//UIAApplication[1]/UIAWindow[1]/UIATableView[1]/UIATableCell[4]/UIASwitch[1]").click()
    sleep(3)
    driver.quit()