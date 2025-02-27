from pyspark.sql import SparkSession

def create_spark_session(app_name="NYCBS Streamlit App"):
    spark = SparkSession.builder \
        .appName(app_name) \
        .config("spark.driver.extraJavaOptions", "") \
        .getOrCreate()
    return spark

def get_spark_context():
    spark = create_spark_session()
    return spark.sparkContext