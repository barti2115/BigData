from pyspark.sql import SparkSession


class MySparkApp:
    def __init__(self):
        self.spark = SparkSession.builder.appName("MySparkApp").getOrCreate()

    def read_file(self, filename):
        df = self.spark.read.text(filename)
        return df

    def modify_data(self, df):
        # Convert all letters to upper case
        modified_df = df.withColumn("value", df.value.upper())
        return modified_df

    def save_data(self, df, output_filename):
        # Write modified data to a new file
        df.write.text(output_filename)
