import os
from llmtools.llms.autollm import AutoLLMForCausalLM

# 設定 Hugging Face 模型存放路徑
MODEL_PATH = "D:/huggingface_models/Llama_1_7b_E8P_2Bit"
MODEL_NAME = "relaxml/Llama-1-7b-E8P-2Bit"

# 確保目標目錄存在
os.makedirs(MODEL_PATH, exist_ok=True)

print(f"下載 {MODEL_NAME} 到 {MODEL_PATH} ...")
llm, quip_config = AutoLLMForCausalLM.from_pretrained(
    MODEL_NAME,
    load_in_quip=True,
    device_map="auto",
    cache_dir=MODEL_PATH  # 確保下載的模型存入 D 槽
)
print(f"模型下載完成，存放於 {MODEL_PATH}！")
