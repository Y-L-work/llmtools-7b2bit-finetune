from llmtools.engine.lora.config import FinetuneConfig

TUNE_CONFIG = FinetuneConfig(
    dataset="data/alpaca.json",
    lora_out_dir="output/llama-7b-quantized-lora",
    mbatch_size=1,
    batch_size=2,
    epochs=3,
    lr=2e-4,
    cutoff_len=256,
    lora_r=8,
    lora_alpha=16,
    lora_dropout=0.05,
    val_set_size=0.2,
    warmup_steps=50,
    save_steps=50,
    save_total_limit=3,
    logging_steps=10,
)
