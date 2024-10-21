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

- **Flight Availability**: Certain limitations were found in the frequency of flights to some selected destinations, especially during certain times of the year. This is crucial for travel planning.
- **Accommodation Prices and Services**: The collected data shows that accommodation availability and prices vary significantly between high and low seasons. Some destinations have a clear oversupply during specific months, which can be leveraged to offer discounts.
- **Local Activities**: The most popular activities include gastronomic tourism and adventure sports. Additionally, sustainability and eco-conscious experiences are particularly attractive to certain segments of clients, such as solo travelers seeking sustainable alternatives.
- **Temporal Patterns**: Seasonal trends were identified for flights and accommodations, with peaks during holiday months and summer.

## 🔄 Next Steps:
- **In-Depth Destination Analysis**: Conduct a detailed analysis of destinations with greater price and availability variability, as well as improve personalization of recommendations for different types of clients.
- **Experience Improvement**: Implement a predictive model to recommend the best time to book flights and accommodation based on collected data.
- **Sustainability**: Explore more options for sustainable activities to meet the needs of eco-conscious clients.

## 🤝 Contributions

Contributions to this project are welcome! Follow these steps to contribute:

1. Fork the repository.
2. Create a new branch for your changes.
3. Submit a pull request when ready.

If you have suggestions or improvements, feel free to open an issue.

## ✍️ Authors
- **Javier Carreira** - Lead Developer - GitHub

Special thanks to the Hack(io) team for the opportunity to work on this project.