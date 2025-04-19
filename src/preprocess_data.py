from datasets import load_dataset
import os

# 設定數據存放路徑
DATA_PATH = "data/alpaca.json"

# 下載 Alpaca 訓練數據
dataset = load_dataset("tatsu-lab/alpaca")
dataset["train"].to_json(DATA_PATH, orient="records")

print(f"訓練數據已下載並存入 {DATA_PATH}")
