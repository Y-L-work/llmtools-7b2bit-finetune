FROM nvidia/cuda:12.1.0-devel-ubuntu20.04

# 設置基礎環境
ENV DEBIAN_FRONTEND=noninteractive
RUN apt update && apt install -y \
    python3.9 python3.9-venv python3.9-dev \
    curl git wget unzip \
    && rm -rf /var/lib/apt/lists/*

# 安裝 pip & virtualenv
RUN curl -sS https://bootstrap.pypa.io/get-pip.py | python3.9
RUN pip install --upgrade pip

# 設置工作目錄
WORKDIR /app

# 複製專案
COPY . .

# 安裝 Python 依賴
RUN pip install -r requirements.txt

# 設定 CUDA
ENV CUDA_VISIBLE_DEVICES=0

# 啟動微調腳本
CMD ["bash", "run.sh"]
