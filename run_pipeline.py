import json
from pathlib import Path

from generate_script import generate_script
from tts_piper import tts_with_piper


def main():
    cfg = json.loads(Path("config.json").read_text(encoding="utf-8"))

    topic = cfg["project"]["topic"]
    target_words = int(cfg["project"]["target_words"])
    style = cfg["project"]["style"]

    script = ""
    if cfg["ollama"]["enabled"]:
        script = generate_script(
            topic=topic,
            target_words=target_words,
            style=style,
            model=cfg["ollama"]["model"],
            url=cfg["ollama"]["url"],
            temperature=float(cfg["ollama"].get("temperature", 0.7)),
        )

    Path("out").mkdir(exist_ok=True)
    Path("out/script.txt").write_text(script, encoding="utf-8")

    if cfg["piper"]["enabled"]:
        tts_with_piper(
            text=script,
            piper_exe=cfg["piper"]["piper_exe"],
            voice_model=cfg["piper"]["voice_model_path"],
            voice_config=cfg["piper"]["voice_config_path"],
            output_wav=cfg["piper"]["output_wav"],
        )

    print("Done: out/script.txt + out/final.wav")


if __name__ == "__main__":
    main()
