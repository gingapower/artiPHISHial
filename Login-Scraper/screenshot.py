from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from PIL import Image

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

        # Specify the file path to your image file
        file_path = "C:\\Users\\fabia\\Desktop\\Projects\\artiPHISHial\\artiPHISHial\\Login-Scraper\\screenhot.png"

        # Open the image file using PIL
        image = Image.open(file_path)

        # Display the image using the default image viewer
        image.show()

    except Exception as e:
        print(f"An error occurred while taking a screenshot: {e}")