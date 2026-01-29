import subprocess
from pathlib import Path


def tts_with_piper(text: str, piper_exe: str, voice_model: str, voice_config: str, output_wav: str):
    Path(output_wav).parent.mkdir(parents=True, exist_ok=True)

    cmd = [
        piper_exe,
        "--model", voice_model,
        "--config", voice_config,
        "--output_file", output_wav,
    ]

    p = subprocess.Popen(cmd, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    out, err = p.communicate(input=text)
    if p.returncode != 0:
        raise RuntimeError(f"Piper failed: {err}")

    return out
