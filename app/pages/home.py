import streamlit as st
from spark.data_processing import load_data, process_data
from spark.spark_session import create_spark_session
import matplotlib.pyplot as plt
import seaborn as sns
import pydeck as pdk

def main():
    st.title("NYCBS Streamlit App")
    st.subheader("Home Page")

    # Spark session
    spark = create_spark_session()

    data = load_data(spark)
    data = process_data(data)

    #create a siderbar for filtering data
    st.sidebar.subheader("Filter Data") 

    # Filter data based on trip duration
    min_duration = st.sidebar.slider("Min Duration", 0, 100, 0)

    # Filter data based on trip duration
    data_filtered_duration = data.filter(data.trip_duration > min_duration)
    data = data_filtered_duration

    # Filter data based on the bike type
    data_filtered_bike_type = st.sidebar.selectbox("Bike Type", ["classic_bike", "electric_bike"])
    data = data.filter(data.rideable_type == data_filtered_bike_type)

    # Filter data based on distance bucket
    data_filtered_distance_bucket = st.sidebar.selectbox("Distance Bucket", ["0-1 km", "2-4 km", "4-9 km", "10+ km"])
    data = data.filter(data.distance_bucket == data_filtered_distance_bucket)

    st.write("Data: ", data.toPandas())

    # Perform the groupBy operation and convert the result to a Pandas DataFrame.
    bucket_distribution = data.groupBy("distance_bucket").count().toPandas()
    st.bar_chart(bucket_distribution.set_index("distance_bucket"))

    # Perform the groupBy operation and convert the result to a Pandas DataFrame.
    daily_rentals_pd = data.groupBy("rental_date").count().toPandas()
    # Display the time series line chart in Streamlit.
    st.line_chart(daily_rentals_pd.set_index("rental_date"))

    # Group by the extracted date and count the number of rentals per day.
    daily_rentals = data.groupBy("rental_date").count().orderBy("rental_date").toPandas()


    # Group by station and count the bike rentals per station.
    station_counts = data.groupBy("start_station_id", "start_lat", "start_lng").count()
    station_counts_pd = station_counts.toPandas()


    # Define the initial view centered on NYC.
    view_state = pdk.ViewState(
        latitude=40.7128, 
        longitude=-74.0060, 
        zoom=11, 
        pitch=50
    )

    # Rename columns to match the expected keys in the map.
    station_counts_pd = station_counts_pd.rename(columns={
        "start_lat": "lat",
        "start_lng": "lon",
        "count": "rentals"
    })


    # Create a PyDeck ScatterplotLayer.
    layer = pdk.Layer(
        "ScatterplotLayer",
        data=station_counts_pd,
        get_position='[lon, lat]',
        get_radius="rentals",  # Adjust this scaling factor as needed
        get_fill_color=[255, 0, 0, 160],
        pickable=True
    )

    # Build the deck with the layer and the view state.
    deck = pdk.Deck(
        layers=[layer],
        initial_view_state=view_state,
        tooltip={"text": "Bike Rentals: {rentals}"}
    )

    # Streamlit app layout.
    st.title("NYC Bike Rentals per Station")
    st.pydeck_chart(deck)

if __name__ == "__main__":
    main()