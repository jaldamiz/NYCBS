from streamlit import st
import pandas as pd
import pyspark
from pyspark.sql import SparkSession

def create_dashboard(spark_session):
    # Load the dataset
    df = load_data()

    # Display the dashboard title
    st.title("NYCBS Streamlit App")

    # Show a sample of the data
    st.subheader("Sample Data")
    st.write(df.limit(10).toPandas())

    # Create a chart
    st.subheader("Data Visualization")
    st.bar_chart(df.groupBy("column_name").count().toPandas())

def load_data(spark_session):
    # Load the CSV file into a Spark DataFrame
    df = spark_session.read.csv("data/sample_dataset.csv", header=True, inferSchema=True)
    return df

def main():
    spark_session = SparkSession.builder \
        .appName("Streamlit Spark App") \
        .getOrCreate()
    
    create_dashboard(spark_session)

if __name__ == "__main__":
    main()