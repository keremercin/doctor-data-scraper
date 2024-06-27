from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
import pandas as pd

def scrape_doctor_data(url, output_file):
    # Initialize WebDriver with ChromeDriverManager
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)

    # Open the web page
    driver.get(url)

    # Allow the user to interact with the page for 20 seconds
    print("You have 20 seconds to interact with the page.")
    time.sleep(20)

    # Notify that the script will continue
    print("Manual interactions complete, resuming script...")

    # List to store the data
    data = []

    # Find and extract the required elements
    cards = driver.find_elements(By.CSS_SELECTOR, '.Card_card__BOrl4')
    for card in cards:
        try:
            # Doctor's name
            doctor_name = card.find_element(By.CSS_SELECTOR, '.DoctorCard_header__name--text__KqOEk').text
        except:
            doctor_name = 'Information Not Available'

        try:
            # Address information
            address_parts = card.find_elements(By.CSS_SELECTOR, '.CardAddress_card-address__content__+MaVd div')
            address = ' '.join([part.text for part in address_parts])
        except:
            address = 'Information Not Available'

        # Add data to the list
        data.append(['Dynamic Value 1', 'Dynamic Value 2', doctor_name, address])

    # Close the WebDriver
    driver.quit()

    # Convert the data to a DataFrame and save to Excel
    df = pd.DataFrame(data, columns=['Column 1', 'Column 2', 'Doctor Name', 'Address'])
    df.to_excel(output_file, index=False)

    print(f"Data scraping complete. Data saved to {output_file}.")

if __name__ == "__main__":
    url = 'https://www.medifind.com/specialty/otolaryngology'  # URL of the website to scrape
    output_file = 'output.xlsx'  # Path to save the Excel file

    scrape_doctor_data(url, output_file)
