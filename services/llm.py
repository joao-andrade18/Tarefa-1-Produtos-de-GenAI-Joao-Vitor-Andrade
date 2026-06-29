from openai import OpenAI

from config.settings import NVIDIA_API_KEY, NVIDIA_BASE_URL, NVIDIA_MODEL, validate_settings
from utils.prompts import SYSTEM_PROMPT


def get_client() -> OpenAI:
    """
    Cria o cliente compatível com OpenAI apontando para a API da NVIDIA.
    """
    validate_settings()

    return OpenAI(
        api_key=NVIDIA_API_KEY,
        base_url=NVIDIA_BASE_URL,
    )


def gerar_resposta(mensagens: list[dict]) -> str:
    """
    Envia as mensagens para o modelo da NVIDIA e retorna a resposta.
    """
    client = get_client()

    messages = [
        {"role": "system", "content": SYSTEM_PROMPT},
        *mensagens,
    ]

    response = client.chat.completions.create(
        model=NVIDIA_MODEL,
        messages=messages,
        temperature=0.7,
        max_tokens=1024,
    )

    return response.choices[0].message.content