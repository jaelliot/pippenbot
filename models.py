# models.py

MODELS = {
    "LLaMA3 8b": {
        "model_id": "llama3-8b-8192",
        "context_window": 8192
    },
    "LLaMA3 70b": {
        "model_id": "llama3-70b-8192",
        "context_window": 8192
    },
    "Mixtral 8x7b": {
        "model_id": "mixtral-8x7b-32768",
        "context_window": 32768
    },
    "Gemma 7b": {
        "model_id": "gemma-7b-it",
        "context_window": 8192
    },
    "Gemma2 9b": {
        "model_id": "gemma2-9b-it",
        "context_window": 8192
    },
    "LLaMA3 405b": {
        "model_id": "llama-3.1-405b-reasoning",
        "context_window": 131072
    },
    "LLaMA3 70b (Preview)": {
        "model_id": "llama-3.1-70b-versatile",
        "context_window": 131072
    },
    "LLaMA3 8b (Preview)": {
        "model_id": "llama-3.1-8b-instant",
        "context_window": 131072
    },
    "LLaMA3 Groq 70b Tool Use (Preview)": {
        "model_id": "llama3-groq-70b-8192-tool-use-preview",
        "context_window": 8192
    },
    "LLaMA3 Groq 8b Tool Use (Preview)": {
        "model_id": "llama3-groq-8b-8192-tool-use-preview",
        "context_window": 8192
    }
}
