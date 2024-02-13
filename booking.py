from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time

# Set up Chrome options
chrome_options = Options()
chrome_options.add_argument("--headless")

# Initialize the WebDriver with the headless option
driver = webdriver.Chrome(options=chrome_options)

# Navigate to the page
driver.get("https://bookings.better.org.uk/location/charlton-lido/swim-doctor/2024-02-12/by-time")

# Optionally, wait a few seconds to ensure the page has fully loaded
# Adjust the sleep time based on your network speed and the page's complexity
time.sleep(10)  # Waits for 10 seconds

# Retrieve the full HTML content of the page
html_content = driver.page_source

# Print the redirected URL
print(driver.current_url)

# Find all the <a> elements on the page
links = driver.find_elements(By.TAG_NAME, "a")

# Print the href of each <a> element
for link in links:
    print(link.get_attribute("href"))

# Close the WebDriver
driver.quit()

# Save the HTML content to a text file