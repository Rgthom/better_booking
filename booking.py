# 

from selenium import webdriver
import time

# Initialize the WebDriver (assuming Chrome)
driver = webdriver.Chrome()

# Navigate to the page
driver.get("https://bookings.better.org.uk/location/charlton-lido/swim-doctor/2024-02-05/by-time/class/45867687")

# Optionally, wait a few seconds to ensure the page has fully loaded
# Adjust the sleep time based on your network speed and the page's complexity
time.sleep(5)  # Waits for 5 seconds

# Retrieve the full HTML content of the page
html_content = driver.page_source

# Close the WebDriver
driver.quit()

# Print the HTML content
print(html_content)

# Save the HTML content to a text file
with open("/Users/rickthompson/projects/swim_lessons/page_source.txt", "w", encoding="utf-8") as file:
    file.write(html_content)
