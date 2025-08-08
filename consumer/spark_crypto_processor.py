# consumer/spark_crypto_processor.py

from pyspark.sql import SparkSession
from pyspark.sql.functions import from_json, col
from pyspark.sql.types import StructType, StringType, DoubleType

# Create Spark Session
spark = SparkSession.builder \
    .appName("CryptoKafkaConsumer") \
    .master("local[*]") \
    .getOrCreate()

# Define Kafka and topic
KAFKA_BOOTSTRAP = "localhost:9092"
KAFKA_TOPIC = "crypto_prices"

# Schema for the Kafka message
schema = StructType() \
    .add("symbol", StringType()) \
    .add("price_usd", DoubleType()) \
    .add("timestamp", StringType())

# Read from Kafka
df_kafka_raw = spark.readStream \
    .format("kafka") \
    .option("kafka.bootstrap.servers", KAFKA_BOOTSTRAP) \
    .option("subscribe", KAFKA_TOPIC) \
    .option("startingOffsets", "latest") \
    .load()

# Convert value (bytes) to string
df_kafka_str = df_kafka_raw.selectExpr("CAST(value AS STRING)")

# Parse JSON
df_crypto = df_kafka_str.select(from_json(col("value"), schema).alias("data")).select("data.*")

# Write stream to CSV (append mode)
query = df_crypto.writeStream \
    .outputMode("append") \
    .format("csv") \
    .option("path", "data/processed_crypto") \
    .option("checkpointLocation", "data/checkpoint_crypto") \
    .start()

query.awaitTermination()
