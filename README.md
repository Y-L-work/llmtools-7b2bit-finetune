<h1 align="center"> llmtools-7b2bit-finetune: 低 VRAM 微調 LLaMA-7B</h1>

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=gradient&height=200&section=header&text=llmtools-7b2bit-finetune&fontSize=50&animation=fadeIn" alt="llmtools-7b2bit-finetune Banner"/>
</p>

<p align="center">
<a href="https://github.com/Y-L-work/llmtools-7b2bit-finetune/stargazers">
  <img src="https://img.shields.io/github/stars/Y-L-work/llmtools-7b2bit-finetune?style=social" alt="Stars">
</a>
<a href="https://github.com/Y-L-work/llmtools-7b2bit-finetune/network/members">
  <img src="https://img.shields.io/github/forks/Y-L-work/llmtools-7b2bit-finetune?style=social" alt="Forks">
</a>
<a href="https://github.com/Y-L-work/llmtools-7b2bit-finetune/issues">
  <img src="https://img.shields.io/github/issues/Y-L-work/llmtools-7b2bit-finetune" alt="Issues">
</a>
<a href="https://github.com/Y-L-work/llmtools-7b2bit-finetune/blob/main/LICENSE">
  <img src="https://img.shields.io/github/license/Y-L-work/llmtools-7b2bit-finetune" alt="License">
</a>
</p>

---

## 📖 專案簡介

 **llmtools-7b2bit-finetune** 是一個使用 **LLMTools** 在 **RTX 3050 Ti (4GB VRAM)** 上 **微調 LLaMA-7B (2-bit 量化)** 的專案。本專案的目標是透過 **2-bit LoRA 微調**，使 **低階顯卡也能有效地進行 LLM 微調**，顯著降低 VRAM 需求。

---

##  功能特色

- 🔹 **2-bit LoRA 微調** — 讓低 VRAM 設備能夠高效微調大型語言模型
- 🔹 **LLMTools 量化技術** — 提供高效能、低記憶體消耗的微調方式
- 🔹 **基於 PyTorch 2.1.1 + CUDA 12.1** — 兼容最新的 GPU 加速技術
- 🔹 **Hugging Face 下載與管理** — 支援熱門 LLaMA-7B 模型
- 🔹 **Docker 容器化部署** — 確保環境一致性

---

## 🛠️ 技術架構

**主要技術與工具**

| 類別 | 🛠️ 工具 & 技術 |
|--------|----------------------|
| 🧠 **LLM 微調** | ![LLMTools](https://img.shields.io/badge/LLMTools-2bit-blue?style=for-the-badge&logo=ai) ![LoRA](https://img.shields.io/badge/LoRA-Optimization-orange?style=for-the-badge) |
| 🔥 **深度學習** | ![PyTorch](https://img.shields.io/badge/PyTorch-2.1.1-red?style=for-the-badge&logo=pytorch) ![CUDA](https://img.shields.io/badge/CUDA-12.1-green?style=for-the-badge) |
| 📚 **模型下載** | ![HuggingFace](https://img.shields.io/badge/HuggingFace-FFD700?style=for-the-badge&logo=huggingface&logoColor=black) |
| 🚢 **容器化部署** | ![Docker](https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white) |
| 📝 **數據集** | ![Alpaca](https://img.shields.io/badge/Alpaca-Dataset-lightblue?style=for-the-badge) |

---

## 📂 專案目錄

```plaintext
llmtools-7b2bit-finetune/
├── src/
│   ├── train.py             # 主要微調腳本
│   ├── download_model.py    # 下載 2-bit 量化模型
│   ├── preprocess_data.py   # 數據預處理
│   ├── config.py            # 設定微調參數
├── data/
│   ├── alpaca.json          # 訓練數據
├── output/                  # 保存微調後的模型
├── requirements.txt         # 依賴安裝
├── run.sh                   # 快速運行腳本
├── Dockerfile               # Docker 環境定義
├── docker-compose.yml       # Docker Compose 設定
└── README.md                # 本文件
```

---

##  快速開始

### 1️⃣ 安裝環境
```bash
conda create -n llmtools_env python=3.10 -y
conda activate llmtools_env
pip install -r requirements.txt
```

### 2️⃣ 下載 LLaMA-7B 2-bit 量化模型
```bash
python src/download_model.py
```
> **注意**：預設存放位置為 `D:/huggingface_models/Llama_1_7b_E8P_2Bit/`

### 3️⃣ 運行微調

✅ **方式 1：直接執行 Python 腳本**
```bash
python src/train.py
```

✅ **方式 2：使用 Docker 運行**
```bash
docker-compose up --build
```

---

##  目前專案進度

✅ **環境與依賴安裝**  
✅ **下載 LLaMA-7B 2-bit 量化模型**  
✅ **數據預處理 (Alpaca Dataset)**  
✅ **基本微調腳本 (`train.py`) 建立**  
⏳ **測試 2-bit 微調過程**  
⏳ **模型訓練與效果驗證**  
⏳ **微調後模型的推理測試**  

**計畫中的改進方向：**
- 🔹 **調整 LoRA 超參數，優化微調效果**
- 🔹 **探索最佳 2-bit 量化策略以降低 VRAM 使用量**
- 🔹 **增加 TensorRT 加速推理，提升執行效能**

---

## 📊 GitHub 活動

![GitHub Activity](https://github-readme-activity-graph.vercel.app/graph?username=Y-L-work&theme=react-dark)

---

<p align="center">
  **如果你喜歡這個專案，請記得給個 ⭐ 支持！**
</p>
