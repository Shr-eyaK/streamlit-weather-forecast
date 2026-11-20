import streamlit as st
import plotly.express as px
from backend import get_data
from datetime import datetime, timezone

# frontend - add title, text input, slider, select box, and sub header
st.title("Weather Forecast for the Next Days")
place = st.text_input("Place: ")
days = st.slider("Forecast Days", min_value=1, max_value=5,
                 help="Select the number of forecast days")
option = st.selectbox("Select data to view",
                      ("Temperature", "Sky"))
st.subheader(f"{option} for the next {days} days in {place}")

if place:
    # Get the temperature/sky data
    try:
        filtered_data, city_data = get_data(place, days)
        
        #Show sunrise/sunset times
        timezone_offset = city_data["timezone"]

        def convert_time(timestamp, timezone_offset):
            local_time = datetime.fromtimestamp(
                timestamp + timezone_offset, timezone.utc
            )
            return local_time.strftime("%I:%M %p")

        sunrise = convert_time(city_data["sunrise"], timezone_offset)
        sunset = convert_time(city_data["sunset"], timezone_offset)

    
        # Display sunrise and sunset
        col1, col2 = st.columns(2)

        with col1:
            st.metric("🌅 Sunrise", sunrise)

        with col2:
            st.metric("🌇 Sunset", sunset)


        if option == "Temperature":
            temperatures = [dict["main"]["temp"] for dict in filtered_data]
            dates = [dict["dt_txt"] for dict in filtered_data]
            # Create a temperature plot
            figure = px.line(x=dates, y=temperatures, labels={"x": "Dates", "y": "Temperature (C)"})
            st.plotly_chart(figure)

        if option == "Sky":
            images = {
                "Clear": "images/clear.png",
                "Clouds": "images/cloud.png",
                "Rain": "images/rain.png",
                "Snow": "images/snow.png"
            }
            sky_conditions = [item["weather"][0]["main"] for item in filtered_data]
           
            dates = [dict["dt_txt"] for dict in filtered_data]

            image_paths = [
                images.get(condition, "images/cloud.png")
                for condition in sky_conditions
            ]

            captions = [
                f"{condition} - {date}"
                for condition, date in zip(sky_conditions, dates)
            ]

            st.image(image_paths, width=115, caption=captions)

    except KeyError:
        st.write("That place does not exist.")


