import streamlit as st
import plotly.express as px
from backend import get_data
from datetime import datetime, timezone

# Page configuration
st.set_page_config(
    page_title="Weather Forecast",
    page_icon="🌤️",
    layout = "wide"
)

# Main page header
st.title("🌤️ Weather Forecast")
st.caption("Explore upcoming weather conditions and temperature trends.")

st.divider()

# Sidebar controls
with st.sidebar:
    st.header("⚙️ Settings")

    place = st.text_input("Enter a city", placeholder="e.g. Toronto")

    days = st.slider(
        "Forecast Days",
        min_value=1,
        max_value=5,
        help="Select the number of forecast days"
    )

    option = st.selectbox(
        "Select data to view",
        ("Temperature", "Sky")
    )

# Main forecast section
st.subheader(f"{option} Forecast")

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
            st.metric("🌅 Sunrise", sunrise, border=True)

        with col2:
            st.metric("🌇 Sunset", sunset, border=True)


        if option == "Temperature":
            temperatures = [item["main"]["temp"] for item in filtered_data]
            dates = [item["dt_txt"] for item in filtered_data]

            # Create an improved temperature chart
            figure = px.line(
                x=dates,
                y=temperatures,
                labels={
                    "x": "Date and Time",
                    "y": "Temperature (°C)"
                },
                markers=True,
                template="plotly_dark"
            )

            figure.update_traces(
                line=dict(color="#7ABFFF", width=3),
                marker=dict(size=7, color="#7ABFFF")
            )

            figure.update_layout(
                height=400,
                hovermode="x unified",
                margin=dict(l=20, r=20, t=30, b=20)
            )

            with st.container(border=True):
                st.plotly_chart(figure, use_container_width=True)

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

            formatted_dates = [
                datetime.strptime(date, "%Y-%m-%d %H:%M:%S").strftime("%a, %b %d • %I %p")
                for date in dates
            ]

            captions = [
                f"{condition} | {date}"
                for condition, date in zip(sky_conditions, formatted_dates)
            ]

            # Display weather images in rows of four
            for i in range(0, len(image_paths), 4):
                cols = st.columns(4)

                for col, image_path, caption in zip(
                    cols,
                    image_paths[i:i+4],
                    captions[i:i+4]
                ):
                    with col:
                        with st.container(border=True):
                            st.image(image_path, use_container_width=True)
                            st.caption(caption)

    except KeyError:
        st.write("That place does not exist.")


