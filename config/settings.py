import os
from dotenv import load_dotenv


load_dotenv()


NVIDIA_API_KEY = os.getenv("NVIDIA_API_KEY")
NVIDIA_MODEL = os.getenv("NVIDIA_MODEL", "meta/llama-3.1-8b-instruct")
NVIDIA_BASE_URL = os.getenv("NVIDIA_BASE_URL", "https://integrate.api.nvidia.com/v1")


def validate_settings() -> None:
    """
    Valida se as configurações essenciais estão disponíveis.
    """
    if not NVIDIA_API_KEY:
        raise ValueError(
            "A variável NVIDIA_API_KEY não foi encontrada. "
            "Crie um arquivo .env com sua chave da NVIDIA."
        )