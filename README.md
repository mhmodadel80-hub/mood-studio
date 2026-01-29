# mood-studio

Local, free, practical-unlimited pipeline to:
1) Generate a long English YouTube voiceover script using a local LLM (Ollama + Llama 3.1).
2) Convert the script to a single WAV voiceover using Piper TTS (offline).

## Requirements
- Python 3.10+
- Ollama installed and running
- Piper binary + a US English voice (ONNX + JSON)

## Quick start
1) Copy config:
```bash
cp config.example.json config.json
```
2) Edit `config.json` (topic, model, piper paths).
3) Install deps:
```bash
pip install -r requirements.txt
```
4) Run:
```bash
python run_pipeline.py
```

Outputs:
- `out/script.txt`
- `out/final.wav`
