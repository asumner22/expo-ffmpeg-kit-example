import unittest
from appium import webdriver
from appium.options.ios import XCUITestOptions
from appium.webdriver.common.appiumby import AppiumBy
from config import ios_capabilities
import time

class TestAppium(unittest.TestCase):
    def setUp(self) -> None:
        # Initialize the driver
        self.driver = webdriver.Remote('http://localhost:4723', options=ios_capabilities)

    def test_enable_dictation(self):
        # Wait for the settings to load
        time.sleep(2)

        el2 = self.driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Start a local development server with:")
        element_value = el2.get_attribute('value')
        expected_value = "Start a local development server with:"
        self.assertEqual(element_value, expected_value)

        time.sleep(2)


    def tearDown(self) -> None:
        # Quit the driver
        if self.driver:
            self.driver.quit()

if __name__ == '__main__':
    unittest.main()
