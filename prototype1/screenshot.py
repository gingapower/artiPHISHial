from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from PIL import Image
import os

def take_screenshot(url, output_file):
    try:
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

        cwd = os.getcwd()

        # Define the relative path to the file
        relative_path = "screenhot.png"

        # Combine the current working directory and the relative path
        file_path = os.path.join(cwd, relative_path)

        # Use the file path in your code
        url = f"file://{file_path}"

        # Open the image file using PIL
        image = Image.open(file_path)

        # Display the image using the default image viewer
        image.show()

    except Exception as e:
        print(f"An error occurred while taking a screenshot: {e}")