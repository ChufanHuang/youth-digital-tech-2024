from typing import Dict

DOMAIN_TO_EMOJI = {
    "education": "📚",
    "skills": "🧠",
    "safety": "🛡️",
    "health": "🩺",
    "mental_health": "🧘",
    "social": "🤝",
    "work": "💼",
    "tech": "💻",
    "environment": "🌿",
    "housing": "🏠",
    "civic": "🏛️",
}

def encode_row(indicators: Dict[str, int]) -> str:
    """Return a concatenated emoji string for all domains with value == 1."""
    return "".join(DOMAIN_TO_EMOJI[k] for k, v in indicators.items() if v == 1)
