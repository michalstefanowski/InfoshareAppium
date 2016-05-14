import unittest
from appium import webdriver
from foodtracker_locators import *
from selenium.webdriver.common.by import By
from desired_capabilities import switch_auto_correction_in_settings

# App path: "/Users/<USER_NAME>/Library/Developer/CoreSimulator/Devices/<DEVICE_UDID>/data/Containers/Bundle/Application/<APPLICATION_ID>/<APP_NAME>.app"
APP = None


class FoodTrackerTest(unittest.TestCase):

    def setUp(self):

        # Switch auto correction
        # switch_auto_correction_in_settings()

        desired_capabilities = {
            'platformName': 'iOS',
            'platformVersion': '9.2',
            'deviceName': 'iPhone 6 9.2',
            'app': APP,
            'noReset': True
        }
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_capabilities)

    def tearDown(self):
        self.driver.quit()

    def test_add_new_photo_with_max_rate(self):

        print("\nStart FoodTracker app test...\n1. Check list size")
        meal_list = len(self.driver.find_elements(By.XPATH, MEALS_LIST))
        print("\n\tMeals before add: {0}\n".format(meal_list))

        print("2. Click Add button, add photo from camera roll")
        self.driver.find_element(By.ID, ADD_BUTTON).click()
        self.driver.find_element(By.ID, DEFAULT_PHOTO).click()
        self.driver.find_element(By.XPATH, CAMERA_ROLL_CELL).click()
        photo_list = self.driver.find_elements(By.XPATH, CAMERA_ROLL_COLLECTION)
        photo_list[-1].click()

        print("3. Enter meal name")
        meal_name = "Dobre piwko"
        name_textfield = self.driver.find_element(By.XPATH, NAME_TEXTFIELD)
        name_textfield.click()
        name_textfield.send_keys(meal_name)
        self.driver.find_element(By.ID, DONE_BUTTON).click()

        print("4. Add maximum rate")
        self.driver.find_element(By.XPATH, EMPTY_STARS.format("5")).click()
        self.driver.find_element(By.ID, SAVE_BUTTON).click()

        print("5. Check list size after addition")
        meals_after_add_list = len(self.driver.find_elements(By.XPATH, MEALS_LIST))
        self.assertEqual(meals_after_add_list, meal_list + 1, "Meal list size is not correct")
        print("\n\tMeals after add: {0}\n".format(meals_after_add_list))

        print("6. Check last added meal name")
        last_added_name = self.driver.find_element(By.XPATH, MEAL_NAME.format(meals_after_add_list))
        self.assertEqual(last_added_name.text, meal_name, "Meal name is not correct")
        print("\n\tLast added meal name: {0}\n".format(last_added_name.text))

        print("7. Switch to edit mode")
        self.driver.find_element(By.ID, EDIT_BUTTON).click()

        print("8. Select last added meal")
        self.driver.find_element(By.XPATH, DELETE_BUTTON.format(str(meals_after_add_list))).click()

        print("9. Click delete and confirm")
        self.driver.find_element(By.ID, "Delete").click()
        self.driver.find_element(By.ID, "Done").click()

        print("10. Check list size after deletion")
        meals_after_remove_list = len(self.driver.find_elements(By.XPATH, MEALS_LIST))
        self.assertEqual(meals_after_remove_list, meal_list, "Wrong list size.")
        print("\n\tMeals after remove: {0}\n".format(meals_after_remove_list))