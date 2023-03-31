from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def take_screenshot(url, output_file):
    # Set up Chrome options
    chrome_options = Options()
    chrome_options.add_argument('--headless') # Run Chrome in headless mode (no GUI)
    chrome_options.add_argument('--disable-gpu') # Disable GPU acceleration (not needed for screenshots)
    
    # Initialize Chrome driver
    driver = webdriver.Chrome(options=chrome_options)
    
    # Navigate to the URL and wait for page to load
    driver.get(url)
    driver.implicitly_wait(10) # Wait for up to 10 seconds for page to load
    
    # Take screenshot and save to file
    driver.save_screenshot(output_file)
    
    # Clean up
    driver.quit()
#url ='https://dashboard.clearbit.com/login'
#output = 'screenshot.png'
#take_screenshot(url, output)