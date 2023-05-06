from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from PIL import Image
import os
import platform
from termcolor import colored

def take_screenshot(url, output_file):
    try:
        # Set up Chrome options
        chrome_options = Options()
        chrome_options.add_argument('--headless') # Run Chrome in headless mode (no GUI)
        chrome_options.add_argument('--disable-gpu') # Disable GPU acceleration (not needed for screenshots)
        # Suppress console log messages
        if platform.system() == 'Windows':
            chrome_options.add_argument('log-level=3')
        else:
            chrome_options.add_argument('--log-level=3')
            chrome_options.add_argument('--disable-logging')
            chrome_options.add_argument('--no-sandbox')
        
        # Initialize Chrome driver
        driver = webdriver.Chrome(options=chrome_options)
        
        # Navigate to the URL and wait for page to load
        driver.get(url)
        driver.implicitly_wait(10) # Wait for up to 10 seconds for page to load

        # Accept cookies
        try:
            cookie = {'name': 'cookie_name', 'value': 'cookie_value'}
            driver.add_cookie(cookie)

            # Refresh the page to apply the new cookie
            driver.refresh()
        except:
            print("no cookies")

        # Get the full height of the webpage
        height = driver.execute_script("return Math.max( document.body.scrollHeight, document.body.offsetHeight, document.documentElement.clientHeight, document.documentElement.scrollHeight, document.documentElement.offsetHeight )")
        
        # Set the window size to match the full height of the webpage
        driver.set_window_size(1920, height)

        # Take screenshot and save to file
        driver.save_screenshot(output_file)
        
        # Clean up
        driver.quit()
        print(colored("Screenshot taken","green"))
      
    except Exception as e:
        print(f"An error occurred while taking a screenshot: {e}")
