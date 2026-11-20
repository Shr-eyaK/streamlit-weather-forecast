# Weather Forecast Web App

## Overview

This interactive web application allows users to check weather forecasts for up to 5 days in cities around the world. It provides temperature information and sky conditions through an easy-to-use interface with interactive visualizations.

## Features

- **City Selection**: Enter the name of any city to retrieve its weather forecast.
- **Forecast Days**: Use the slider to select the number of forecast days, up to 5 days.
- **Data Options**: Choose whether to view temperature trends or sky conditions.
- **Temperature Visualization**: Explore forecasted temperature trends through interactive Plotly graphs.
- **Sky Conditions**: View visual representations of forecasted weather conditions.
- **Interactive Interface**: Easily customize forecast options and explore weather information.

## How It Works

1. Start the web application using the command `streamlit run main.py`.
2. Enter the name of the city for which you want to check the weather.
3. Use the slider to select the number of forecast days (up to 5).
4. Select whether you want to view temperature or sky conditions.
5. Click on "Run" to retrieve the forecast.
6. The application displays an interactive temperature graph or images representing sky conditions for the selected days.

## Technologies Used

- **Python**: Application logic and data processing.
- **Streamlit**: Interactive web application interface.
- **Plotly**: Interactive data visualization.
- **Requests**: HTTP requests to retrieve weather data.
- **OpenWeatherMap API**: Weather forecast data provider.

## Prerequisites

Before running the application, make sure you have the following:

- Python 3.10 or later.
- An API key from [OpenWeatherMap](https://openweathermap.org/api).
- The required Python libraries listed in `requirements.txt`.

## Installation and Setup

1. Clone the repository:

   `git clone YOUR_GITHUB_REPOSITORY_URL`

2. Navigate to the project directory:

   `cd streamlit-weather-forecast`

3. Create and activate a virtual environment:

   `py -m venv .venv`

   `.venv\Scripts\Activate.ps1`

4. Install the required dependencies:

   `pip install -r requirements.txt`

5. Configure your OpenWeatherMap API key by creating a `.streamlit` folder and a `secrets.toml` file inside it.

6. Add your API key to `secrets.toml` using the following configuration:

   ```toml
   [openweathermap]
   api_key = "YOUR_API_KEY"
   ```

7. Start the application:

   `streamlit run main.py`

8. Open the local URL provided by Streamlit in your browser.

## Configuration

- Store your OpenWeatherMap API key securely using Streamlit secrets.
- Do not upload your `secrets.toml` file or expose your API key in a public repository.
- Dependencies can be installed using `requirements.txt`.

## Notes

- The application retrieves weather forecast data dynamically through the OpenWeatherMap API.
- Forecast availability may depend on the selected city and API service.
- The application can be customized with additional features and visualizations.

## Project Background

This project was completed as part of a university project and further prepared for public deployment as a portfolio project.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.