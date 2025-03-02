import transformers
from llmtools.engine.hf.trainer import Trainer
from llmtools.engine.lora.peft import quant_peft
from transformers import AutoTokenizer
from llmtools.data import TrainSAD
from src.config import TUNE_CONFIG

# 設定 Hugging Face 模型存放路徑
MODEL_PATH = "D:/huggingface_models/Llama_1_7b_E8P_2Bit"
MODEL_NAME = "relaxml/Llama-1-7b-E8P-2Bit"

# 載入 2-bit 量化模型
from llmtools.llms.autollm import AutoLLMForCausalLM
llm, quip_config = AutoLLMForCausalLM.from_pretrained(
    MODEL_PATH,
    load_in_quip=True,
    device_map="auto"
)
tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME, device_map="auto")

# 設定 LoRA
lora_config = quant_peft.LoraConfig(
    task_type="CAUSAL_LM",
    r=TUNE_CONFIG.lora_r,
    lora_alpha=TUNE_CONFIG.lora_alpha,
    lora_dropout=TUNE_CONFIG.lora_dropout,
    bias="none",
    target_modules=["qkv_proj"],
)

model = quant_peft.get_peft_model(llm, lora_config)

# 載入數據
data = TrainSAD(TUNE_CONFIG.dataset, TUNE_CONFIG.val_set_size, tokenizer, TUNE_CONFIG.cutoff_len)
data.prepare_data()

# 設定訓練參數
training_arguments = transformers.TrainingArguments(
    per_device_train_batch_size=TUNE_CONFIG.mbatch_size,
    gradient_accumulation_steps=2,
    warmup_steps=TUNE_CONFIG.warmup_steps,
    num_train_epochs=TUNE_CONFIG.epochs,
    learning_rate=TUNE_CONFIG.lr,
    fp16=True,
    logging_steps=TUNE_CONFIG.logging_steps,
    save_strategy="steps",
    save_steps=TUNE_CONFIG.save_steps,
    output_dir=TUNE_CONFIG.lora_out_dir,
    save_total_limit=TUNE_CONFIG.save_total_limit,
)

trainer = Trainer(
    model=model,
    train_dataset=data.train_data,
    eval_dataset=data.val_data,
    args=training_arguments,
    data_collator=transformers.DataCollatorForLanguageModeling(tokenizer, mlm=False),
)

trainer.train()

# 保存模型
model.save_pretrained(TUNE_CONFIG.lora_out_dir)
