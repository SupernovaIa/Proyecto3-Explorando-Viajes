import pandas as pd
import serpapi

import os

key_2 = os.getenv('token2')


def clean_flights_df(df):
    """
    Cleans and structures flight data by extracting and organizing relevant information, including emissions, flight details, and airport information.

    Parameters:
    - df (pd.DataFrame): The raw flight data DataFrame containing flight and emissions information.

    Returns:
    - (pd.DataFrame): A cleaned DataFrame containing organized columns for departure and arrival information, flight details, emissions, and price.
    """

    # Getting emissions info
    df_emissions = df["carbon_emissions"].apply(pd.Series)
    df_emissions.columns = ['Actual emisions', 'Typical emissions', 'Difference emissions (%)']

    # Extracting flights info
    df_flights = pd.DataFrame(df["flights"].apply(pd.Series)[0].to_list())

    # Selecting only relevant columns
    df_info = df_flights[['airplane', 'airline', 'legroom']]
    df_info.columns = ['Airplane', 'Airline', 'Legroom (cm)']

    # Getting departure info
    df_departure = pd.DataFrame(df_flights['departure_airport'].to_list())
    df_departure.columns = ['Departure Airport', 'Departure ID', 'Departure time']

    # Getting arrival info
    df_arrival = pd.DataFrame(df_flights['arrival_airport'].to_list())
    df_arrival.columns = ['Arrival Airport', 'Arrival ID', 'Arrival time']

    # Putting everything together
    df_clean = pd.concat([df_departure, df_arrival, df_info, df_emissions], axis=1)

    # Adding the price
    df_clean['Price'] = df['price']
    return df_clean


def get_flight_info(origin, destiny, date):  
    """
    Fetches flight information for a specified route and date, processes the results, and returns a cleaned DataFrame with relevant flight details.

    Parameters:
    - origin (str): The IATA code of the departure airport.
    - destiny (str): The IATA code of the destination airport.
    - date (str): The outbound flight date in 'YYYY-MM-DD' format.

    Returns:
    - (pd.DataFrame): A cleaned DataFrame containing flight details, including emissions, price, and other relevant information.
    """
    params = {
    "api_key": key_2,
    "engine": "google_flights",
    "hl": "es",
    "gl": "es",
    "departure_id": origin,
    "arrival_id": destiny,
    "outbound_date": date,
    "currency": "EUR",
    "adults": "1", # One passenger
    "stops": "1", # Non stops
    "type": "2", # One way
    "travel_class": "1", # Economy class
    "emissions": "1" # Low emissions
    }

    try:
        search = serpapi.search(params)
        flights = search.data['other_flights']
        df = pd.DataFrame(flights)
        clean_df = clean_flights_df(df)

        return clean_df
    
    except:
        print(f"No flighs from {origin} to {destiny} on {date}")
