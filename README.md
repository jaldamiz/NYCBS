# Streamlit Spark App

This project is a Streamlit application that leverages Apache Spark for data processing and visualization. It provides an interactive dashboard to explore a sample dataset.

## Project Structure

```
NYCBS
├── app
│   ├── pages
│   │   └── home.py          # Main page of the Streamlit app
│   └── components
│       └── dashboard.py     # Dashboard components for visualizations
├── spark
│   ├── spark_session.py     # Initializes Spark session
│   └── data_processing.py    # Functions for data processing
├── data
│   └── sample_dataset.csv    # Sample dataset for demonstration
├── requirements.txt          # Required libraries
└── README.md                 # Project documentation
```

```
NYCBS                           #DBT Project
|-- macros
|
|-- models                       # dbt models
|   |-- mart                     # star schema models
|   |-- staging                  # staging & intermediate models 
|   |-- sources.yml              # source tables from the landing source
|
|-- seeds                        # csv files for loading
|
|-- snapshots                    # SCD models
|
|--dbt_project.yml               #configuration file for the dbt project
```

## Setup Instructions

1. **Clone the repository:**
   '''bash
   git clone https://github.com/jaldamiz/NYCBS.git
   cd streamlit-spark-app
   '''

2. **Create a virtual environment (optional but recommended):**
   '''bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows use `.venv\Scripts\activate`
   '''

3. **Install the required libraries:**
   '''bash
   pip install -r requirements.txt
   '''

4. **Download NYCBS Januray 2025 file**
   '''bash
   mkdir -p raw_data
   curl -L -o raw_data/202501-citibike-tripdata.zip https://s3.amazonaws.com/tripdata/202501-citibike-tripdata.zip   # On Windows use 'curl.exe -L -o raw_data/202501-citibike-tripdata.zip https://s3.amazonaws.com/tripdata/202501-citibike-tripdata.zip'
   '''

5. **Install Java JDK**
   https://www.oracle.com/java/technologies/javase/jdk11-archive-downloads.html

6. **Install spark**
   https://spark.apache.org/downloads.html
   # for windows winutils https://github.com/steveloughran/winutils
   Welcome to
      ____              __
     / __/__  ___ _____/ /__
    _\ \/ _ \/ _ `/ __/  '_/
   /___/ .__/\_,_/_/ /_/\_\   version 3.5.5
      /_/

Using Scala version 2.12.18, Java HotSpot(TM) 64-Bit Server VM, 11.0.25
Branch HEAD
Compiled by user ubuntu on 2025-02-23T20:30:46Z
Revision 7c29c664cdc9321205a98a14858aaf8daaa19db2
Url https://github.com/apache/spark
Type --help for more information.

7. **Install maven (optional)**
   https://maven.apache.org/download.cgi

8. **Run spark-iceberg-helper maven project(optional)**
   '''bash
   cd spark-iceberg-helper
   mvn clean package -U
   '''

9. **Run nycvs.ipnbc**

10. **Run the Streamlit app:**
   '''bash
   streamlit run app/pages/home.py
   '''

## Usage

- Navigate to the main page of the app to view the data visualizations and interact with the dashboard components.
- The app utilizes a sample dataset located in the `data` directory for demonstration purposes.

## Contributing

Feel free to submit issues or pull requests for improvements and enhancements.