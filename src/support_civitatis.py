from bs4 import BeautifulSoup

import pandas as pd
from time import sleep
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


def open_url(city, date):
    """
    Opens a browser window, navigates to a series of pages for a specified city and date, and retrieves the HTML content of the pages.

    Parameters:
    - city (str): The name of the city to include in the URL.
    - date (str): The date to include in the URL query string.

    Returns:
    - list: A list of BeautifulSoup objects containing the parsed HTML content of each page.
    """

    # Open browser window
    driver = webdriver.Chrome()

    list_of_soups = []

    # Loop for maximum 10 pages
    for i in range(1, 11):
        # Get the proper url
        url = f"https://www.civitatis.com/es/{city}/?page={i}&fromDate={date}&toDate={date}"
        driver.get(url)
        driver.maximize_window()

        try:
            # Wait for the filter to appear for proper page loading
            WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, 'a-filter--applied')))

        except:
            print(f"Hubo un error esperando la página")

        # Get html source and cook the soup
        page_source = driver.page_source
        soup = BeautifulSoup(page_source, 'html.parser')

        # Print the url in case we want to use it later for testing
        print(url)

        # Check if the last page is equal to the previous one
        if len(list_of_soups) > 0:
            if soup.find('div', {'class': 'o-search-list__item'}) == list_of_soups[-1].find('div', {'class': 'o-search-list__item'}):
                print('Exit')
                break

        list_of_soups.append(soup)
    
    # Cerrar navegador
    driver.close()

    return list_of_soups


def soup_to_df(pages):
    """
    Parses a list of BeautifulSoup objects and extracts information into a pandas DataFrame.

    Parameters:
    - pages (list): A list of BeautifulSoup objects representing parsed HTML pages.

    Returns:
    - DataFrame: A pandas DataFrame containing the extracted data with columns for 'Name', 'Score', 'Price (€)', 'Description', 'Times', and 'Link'.
    """
    # Get the item list for every page
    soups = [page.findAll('div', {'class': 'o-search-list__item'}) for page in pages]

    # Empty list to store data
    data = []

    # Defining a dictionary with the funcions that capture the information
    keys = {'Name': lambda x: x.find('h2', {"class": "comfort-card__title"}).text,
            'Score': lambda x: x.find('span', {"class": "m-rating--text"}).text, 
            'Price (€)': lambda x: x.find('span', {"class": "comfort-card__price__text"}).text,
            'Description': lambda x: x.find('div', {"class": "comfort-card__text l-list-card__text"}).text,
            'Times': lambda x: x.find('div', class_='m-availability_times').findAll('span', {'class': '_time _show-on-large'}),
            'Link': lambda x: x.find("a", {'class': 'ga-trackEvent-element _activity-link'}).get('href')
            }

    # Iterate over pages
    for items in soups:
        # Iterate over items
        for item in items:
            # Build an empty dictionary
            dc = {}
            # Fill the dictionary
            for key in keys:

                try:
                    dc[key] = keys[key](item)

                except:
                    dc[key] = None

            data.append(dc)
            
    return pd.DataFrame(data)


def format_times(y):
    """
    Formats a list of time elements by extracting their text content.

    Parameters:
    - y (list or None): A list of BeautifulSoup elements representing times or None.

    Returns:
    - list or None: A list of strings representing the times if y is not None, otherwise None.
    """
    if y != None:
        return list(map(lambda x: x.text, y))
    

def clean_df(df):
    """
    Cleans and formats the columns of a pandas DataFrame by stripping unnecessary characters, converting data types, and formatting links and times.

    Parameters:
    - df (DataFrame): A pandas DataFrame containing columns 'Name', 'Score', 'Price (€)', 'Description', 'Link', and 'Times'.

    Returns:
    - DataFrame: A cleaned pandas DataFrame with formatted and standardized columns.
    """
    df['Name'] = df['Name'].str.strip('\t')
    df['Score'] = df['Score'].str.rstrip('/ 10 ').str.rstrip('\t').str.replace(',', '.').astype(float)
    df['Price (€)'] = df['Price (€)'].str.replace('¡Gratis!', '0').str.replace('€','').str.replace(',','.').astype(float)
    df['Description'] = df['Description'].str.strip('\t')
    df['Link'] = df['Link'].apply(lambda x: 'https://www.civitatis.com' + x if type(x) == str else x)
    df['Times'] = df['Times'].apply(format_times)

    return df