# 📈 Real-Time Crypto Price Tracker using Kafka, Spark & Matplotlib

This project is a real-time data pipeline that tracks and visualizes **Bitcoin (BTC)** prices live.

It uses:
- 📨 Kafka for real-time data streaming
- ⚡ PySpark for processing incoming data streams
- 📁 CSV for local storage
- 📊 Matplotlib for live visualization

---

## 🧠 Project Motivation

In modern data systems, the ability to **stream, process, and visualize data in real-time** is critical.  
This project simulates a financial analytics system that fetches live BTC prices, streams them using Kafka, and visualizes them live.

Perfect for:
- Practicing real-time pipelines
- Understanding Kafka + Spark integration
- Building data engineering skills

---

## 🛠️ Tech Stack Used

| Component         | Technology                     |
|------------------|--------------------------------|
| Data Source       | [CoinGecko API](https://www.coingecko.com) |
| Messaging Queue   | Apache Kafka (localhost)       |
| Stream Processing | PySpark (Structured Streaming) |
| Storage           | CSV (local filesystem)         |
| Visualization     | Matplotlib (live refresh)      |

---

## 📦 Project Structure

```
real-time-crypto-kafka-project/
├── producer/
│   └── crypto_producer.py
├── consumer/
│   └── spark_crypto_processor.py
├── visualization/
│   ├── visualize.py
│   └── visualize_live.py
├── data/
│   └── processed_crypto/        # Output CSVs from Spark
├── requirements.txt
└── README.md
```

---

## 🚀 How to Run the Project

### ✅ Step 1: Start Kafka & Zookeeper (on localhost)

Make sure you have Kafka & Zookeeper running locally. You can use these:

```bash
zookeeper-server-start.bat config/zookeeper.properties
kafka-server-start.bat config/server.properties
```

### ✅ Step 2: Install Python Requirements

```bash
pip install -r requirements.txt
```

### ✅ Step 3: Run the Kafka Producer

```bash
python producer/crypto_producer.py
```

This fetches live BTC price and sends to Kafka topic `crypto_prices`.

### ✅ Step 4: Run the Spark Streaming Consumer

```bash
spark-submit consumer/spark_crypto_processor.py
```

It reads from Kafka, processes the data, and writes to `data/processed_crypto/`.

### ✅ Step 5: Live Visualization (Matplotlib)

```bash
python visualization/visualize_live.py
```

This plots the real-time BTC price from the CSV output.

---

## 🧪 Sample Message (JSON)

```json
{
  "symbol": "BTC",
  "price_usd": 29457.23,
  "timestamp": "2025-08-08T16:10:00Z"
}
```

---

## 📊 Sample Output (Screenshot)

> *Insert chart image here if available*

---

## 📈 Future Improvements

- Add support for Ethereum (ETH) and other coins
- Write data into PostgreSQL or data lake
- Build Streamlit dashboard for live web UI
- Use Docker for complete orchestration

---

## 👨‍💻 Author

Made with ❤️ by [Your Name]  
GitHub: https://github.com/yourusername