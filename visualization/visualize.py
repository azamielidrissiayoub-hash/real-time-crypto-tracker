# visualization/visualize_live.py

import pandas as pd
import matplotlib.pyplot as plt
import os
import time

DATA_DIR = "../consumer/data/processed_crypto"

plt.ion()  # Interactive mode ON

fig, ax = plt.subplots(figsize=(10, 5))

while True:
    try:
        all_files = [
            os.path.join(DATA_DIR, f)
            for f in os.listdir(DATA_DIR)
            if f.endswith(".csv")
        ]
        df = pd.concat(
            (pd.read_csv(f, header=None, names=["symbol", "price_usd", "timestamp"]) for f in all_files)
        )
        df["timestamp"] = pd.to_datetime(df["timestamp"])
        df = df.sort_values("timestamp")

        ax.clear()
        ax.plot(df["timestamp"], df["price_usd"], marker='o', linestyle='-', color='blue')
        ax.set_title("📈 BTC Price - Live Refresh")
        ax.set_xlabel("Timestamp")
        ax.set_ylabel("Price (USD)")
        ax.grid(True)
        plt.xticks(rotation=45)
        plt.tight_layout()

        plt.pause(1)  # Faster: refresh every 1 second
    except Exception as e:
        print("⛔", e)
        time.sleep(1)
