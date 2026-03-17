from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

def test_google():
    # Start browser
    driver = webdriver.Chrome()

    # Open Google
    driver.get("https://www.google.com")

    time.sleep(2)

    # Find search box
    search_box = driver.find_element(By.NAME, "q")

    # Type NVIDIA
    search_box.send_keys("NVIDIA")

    time.sleep(1)

    # Press Enter
    search_box.send_keys(Keys.RETURN)

    time.sleep(3)

    # Close browser
    driver.quit()

if __name__ == "__main__":
    test_google()