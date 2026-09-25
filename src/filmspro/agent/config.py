import os
from dotenv import load_dotenv

# carregar o arquivos .env
load_dotenv()

class Config:
    # Gerenciador de Configurações centralizado.

    GROQ_API_KEY=os.getenv("GROQ_API_KEY")
    OMDB_API_KEY=os.getenv("OMDB_API_KEY")

    @classmethod
    def validade(cls):

        if not cls.GROQ_API_KEY:
            raise ValueError("GROQ_API_KEY não está definida no arquivo .env")
        if not cls.OMDB_API_KEY:
            raise ValueError("OMDB_API_KEY não está definida no arquivo .env")
