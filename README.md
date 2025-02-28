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
   mkdir -p raw_data
   curl -L -o raw_data/202501-citibike-tripdata.zip https://s3.amazonaws.com/tripdata/202501-citibike-tripdata.zip

5. **Install Java JDK**
   https://www.oracle.com/java/technologies/downloads/

6. **Install maven**
   https://maven.apache.org/download.cgi

7. **Run spark-iceberg-helper maven project**
   cd spark-iceberg-helper
   mvn clean package -U 

8. **Run nycvs.ipnbc**

8. **Run the Streamlit app:**
   '''bash
   streamlit run app/pages/home.py
   '''

## Usage

- Navigate to the main page of the app to view the data visualizations and interact with the dashboard components.
- The app utilizes a sample dataset located in the `data` directory for demonstration purposes.

## Contributing

Feel free to submit issues or pull requests for improvements and enhancements.