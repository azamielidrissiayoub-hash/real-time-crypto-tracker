# producer/crypto_producer.py

from confluent_kafka import Producer
import requests
import json
import time
from datetime import datetime

TOPIC = "crypto_prices"
BROKER = "localhost:9092"

# Kafka producer setup
producer = Producer({'bootstrap.servers': BROKER})

def fetch_crypto_price(symbol="bitcoin"):
    url = f"https://api.coingecko.com/api/v3/simple/price?ids={symbol}&vs_currencies=usd"
    response = requests.get(url)
    price = response.json()[symbol]["usd"]
    return price

def delivery_report(err, msg):
    if err is not None:
        print(f"❌ Message delivery failed: {err}")
    else:
        print(f"✅ Message delivered to {msg.topic()} [{msg.partition()}]")

while True:
    try:
        price = fetch_crypto_price()
        now = datetime.utcnow().isoformat()
        message = {
            "symbol": "BTC",
            "price_usd": price,
            "timestamp": now
        }
        producer.produce(TOPIC, key="btc", value=json.dumps(message), callback=delivery_report)
        producer.poll(1)
        time.sleep(5)  # Fetch every 5 seconds
    except Exception as e:
        print("⚠️ Error:", e)
