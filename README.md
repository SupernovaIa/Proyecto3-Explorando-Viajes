# 🌍 Smart Travel Agency: Destination and Experience Analysis

## 📜 Project Description

![thepower education_15750_Sign_about_Barcelona_and_Budapest_bo_211d3b8d-22c6-4894-b653-a2f6e1dd63bb_2](https://github.com/user-attachments/assets/08fd14b5-b61a-4e1c-af3a-5914b0c397d7)

This project focuses on using advanced technologies to provide an exceptional **travel experience** to our clients. We focus on lonely people that need a great experience on Christmas.

We combine data on transportation, accommodation, and local activities to help our clients plan their perfect vacation based on information about tourist destinations. We use a combination of **APIs** and **Web Scraping** techniques to obtain real-time information from various providers.

The main goal is to help our clients enjoy their vacation to the fullest, offering **personalized recommendations based on data**. We have selected **Budapest** and **Barcelona** for testing, where a detailed study of available flights from **Madrid**, accommodations, and activities is conducted.

### Key areas of analysis:

**Flights, Accommodation, and Activities**: Collect information about flight frequency, schedules, accommodation prices, and available activities to optimize travel recommendations and provide the best possible experience to clients.

**Use of APIs and Web Scraping**: Various tools were used for this project. We employed the **Google Flights API** through **SerpApi** to obtain detailed and accurate information about available flights. Additionally, scraping techniques were performed on sites like **Booking.com** and **Civitatis.com** to collect information about accommodations and local activities, overcoming possible limitations in API availability.

**Exploratory Data Analysis (EDA)**: Use exploratory analysis to understand which destinations and options best suit the needs of our clients.

## 💻 Project Structure

```
Proyecto3-Explorando-Viajes
├── data/                                 # Folder containing datasets
│   ├── activities_barcelona.csv          # Activities in Barcelona
│   ├── activities_budapest.csv           # Activities in Budapest
│   ├── all_flights.csv                   # General flights information
│   ├── departure_flights.csv             # Departure flights details
│   ├── hotels_barcelona.csv              # Hotels data for Barcelona
│   ├── hotels_budapest.csv               # Hotels data for Budapest
│   ├── return_flights.csv                # Return flights details
├── notebook/                             # Jupyter Notebooks for different project phases
│   ├── booking.ipynb                     # Notebook for Booking.com data collection
│   ├── civitatis.ipynb                   # Notebook for Civitatis.com data collection
│   ├── flights.ipynb                     # Notebook for flights data collection
├── src/                                  # Source code for project functions
│   ├── support_booking.py                # Python helper functions for Booking scraping
│   ├── support_civitatis.py              # Python helper functions for Civitatis scraping
│   ├── support_flights.py                # Python helper functions for flight data
├── .env                                  # Environment variables
├── .gitignore                            # Git ignore file
├── README.md                             # Project description
├── requirements.txt                      # Project requirements
```

## 🔧 Installation and Requirements

This project was developed using **Python 3.12**. To set up the project environment, follow these steps:

### Additional Requirements
- **[SerpApi](https://serpapi.com/)**: To efficiently access the Google Flights API and obtain flight data.

### 1. Clone the repository:
```bash
   git clone https://github.com/SupernovaIa/Proyecto3-Explorando-Viajes
```

### 2. Navigate to the project directory:
```bash
   cd Proyecto3-Explorando-Viajes
```

### 3. Install the required libraries:
The following libraries are required for this project:

- **[Selenium](https://www.selenium.dev/)** (v4.21.0)
- **[Beautiful Soup](https://beautiful-soup-4.readthedocs.io/en/latest/#installing-beautiful-soup)** (v4.12.3)
- **[Pandas](https://pandas.pydata.org/docs/getting_started/install.html)** (v2.2.2)
- **[Numpy](https://numpy.org/install/)** (v1.26.4)
- **[Matplotlib](https://matplotlib.org/)** (v3.9.2)
- **[Seaborn](https://seaborn.pydata.org/)** (v0.13.2)

To install these libraries, run the following command:
```bash
   pip install -r requirements.txt
```

### 4. Run the Jupyter Notebooks:
Once the environment is set up, you can run the Jupyter Notebooks one by one to analyze data on flights, accommodations, and activities.

## 📊 Results and Conclusions

The data analysis provided the following insights:

- **Flights**: Overall, flights from Madrid to Budapest tend to be more expensive and generate higher emissions compared to those to Barcelona. However, this is mainly due to the significantly longer distance of the journey. For trips to Budapest, we have several airlines to choose from, and we have selected the one offering the lowest prices and emissions.
- **Accommodation**: Price trends for accommodations in Budapest and Barcelona are quite similar. There doesn't appear to be a clear correlation between ratings and price. In Budapest, lower-rated accommodations are often located in central areas, suggesting that some travelers may prioritize location over quality.
- **Local Activities**: Both cities offer a wide range of activities. The price and rating distribution is similar in both cases, with no significant correlation between price and ratings for local activities.

## 🔄 Next Steps:
Some further analysis we can perform in the next steps:
- **Flights**: Conduct a broader analysis that includes categories beyond low emissions or budget options. Normalize the data based on flight distance or duration for a more accurate comparison.
- **Accommodation**: Expand the selection of hotels and include additional filters, categories, and information such as accommodation type, room size, and whether breakfast is included.
- **Local Activities**: Add more activity categories to allow for a deeper and more detailed analysis. Also, study the available time slots for the activities to enhance the evaluation.
- **Destinations**: Expand the analysis to include more cities.


## 🤝 Contributions

Contributions to this project are welcome! Follow these steps to contribute:

1. Fork the repository.
2. Create a new branch for your changes.
3. Submit a pull request when ready.

If you have suggestions or improvements, feel free to open an issue.

## ✍️ Authors
- **Javier Carreira** - Lead Developer - GitHub

Special thanks to the Hack(io) team for the opportunity to work on this project.