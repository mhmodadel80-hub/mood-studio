import requests


def generate_script(topic: str, target_words: int, style: str, model: str, url: str, temperature: float = 0.7) -> str:
    prompt = f"""
You are a professional YouTube documentary scriptwriter.
Write ONE continuous English voiceover script about: {topic}

Constraints:
- Target length: ~{target_words} words (as close as possible).
- Style: {style}
- Output ONLY the final script (no outline, no headings, no notes).
- Keep it cohesive and consistent in tone.
""".strip()

    payload = {
        "model": model,
        "prompt": prompt,
        "stream": False,
        "options": {"temperature": temperature}
    }

    r = requests.post(f"{url.rstrip('/')}/api/generate", json=payload, timeout=1200)
    r.raise_for_status()
    return r.json()["response"]
