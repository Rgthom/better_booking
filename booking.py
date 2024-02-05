from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time


options = Options()
options.headless = True  
options.add_argument("--window-size=1920,1080")  


driver = webdriver.Chrome(options=options)


driver.get("https://bookings.better.org.uk/location/charlton-lido/swim-doctor/2024-02-05/by-time/class/45867687")


time.sleep(5)  


html_content = driver.page_source

# Close the WebDriver
driver.quit()


with open("page_source.txt", "w", encoding="utf-8") as file:
    file.write(html_content)
