# llmtools-7b2bit-finetune

🚀 **llmtools-7b2bit-finetune** 是一個使用 **LLMTools** 在 **RTX 3050 Ti (4GB VRAM)** 上 **微調 LLaMA-7B (2-bit 量化)** 的專案。

## 📌 專案概述
本專案的目標是透過 **LLMTools** 進行 **2-bit LoRA 微調**，以便在 **資源受限的 GPU (如 RTX 3050 Ti)** 上高效訓練大語言模型 (**LLaMA-7B**)。這樣的微調方式能夠顯著降低 VRAM 需求，使 **低階顯卡也能參與 LLM 微調**。

## 🔧 技術棧
- **LLMTools** - 用於 LLM 低比特量化與微調
- **PyTorch 2.1.1（CUDA 12.1）** - 深度學習框架
- **Hugging Face Transformers** - 模型下載與管理
- **Docker** - 容器化執行環境
- **Alpaca Dataset** - 微調時使用的標準數據集

## 📁 專案目錄結構
```
llmtools_7b2bit_finetune/
│── src/
│   ├── train.py             # 主要微調腳本
│   ├── download_model.py    # 下載 2-bit 量化模型
│   ├── preprocess_data.py   # 數據預處理
│   ├── config.py            # 設定微調參數
│── data/
│   ├── alpaca.json          # 訓練數據
│── output/                  # 保存微調後的模型
│── requirements.txt         # 依賴安裝
│── run.sh                   # 快速運行腳本
│── README.md                # 本文件
│── Dockerfile               # Docker 環境定義
│── docker-compose.yml       # Docker Compose 設定
```

## 🔨 安裝與環境設定
### 1️⃣ 建立並啟動 Python 環境
```bash
conda create -n llmtools_env python=3.10 -y
conda activate llmtools_env
```

### 2️⃣ 安裝依賴
```bash
pip install -r requirements.txt
```

### 3️⃣ 下載 LLaMA-7B 2-bit 量化模型
```bash
python src/download_model.py
```
> **注意**：預設存放位置為 `D:/huggingface_models/Llama_1_7b_E8P_2Bit/`

## 🚀 運行微調
### 方式 1：直接執行 Python 腳本
```bash
python src/train.py
```

### 方式 2：使用 Docker 運行
```bash
docker-compose up --build
```

## 📌 目前專案進度
✅ **環境與依賴安裝**
✅ **下載 LLaMA-7B 2-bit 量化模型**
✅ **數據預處理 (Alpaca Dataset)**
✅ **基本微調腳本 (`train.py`) 建立**
⏳ **測試 2-bit 微調過程**
⏳ **模型訓練與效果驗證**
⏳ **微調後模型的推理測試**

**📌 計畫中的改進方向：**
- **嘗試不同的 LoRA 超參數調整**
- **探索最佳 2-bit 量化策略以降低 VRAM 使用量**
- **增加 TensorRT 加速推理**

---

> **作者**: @coffeetea
> **GitHub Repo**: [即將建立]

