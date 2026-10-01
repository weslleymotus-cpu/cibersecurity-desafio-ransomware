from pathlib import Path
from cryptography.fernet import Fernet

# Pasta exclusiva para o laboratório
PASTA_LABORATORIO = Path("laboratorio")

# Arquivo que armazenará a chave do laboratório
ARQUIVO_CHAVE = PASTA_LABORATORIO / "chave.key"


def criar_chave():
    """Cria uma chave de criptografia para o laboratório."""
    PASTA_LABORATORIO.mkdir(exist_ok=True)

    if not ARQUIVO_CHAVE.exists():
        chave = Fernet.generate_key()
        ARQUIVO_CHAVE.write_bytes(chave)
        print("Chave criada com sucesso.")


def criptografar_arquivos():
    """Criptografa somente arquivos TXT da pasta de laboratório."""
    chave = ARQUIVO_CHAVE.read_bytes()
    fernet = Fernet(chave)

    arquivos = list(PASTA_LABORATORIO.glob("*.txt"))

    if not arquivos:
        print("Nenhum arquivo de teste encontrado.")
        return

    for arquivo in arquivos:
        dados = arquivo.read_bytes()
        dados_criptografados = fernet.encrypt(dados)

        arquivo.write_bytes(dados_criptografados)

        print(f"Arquivo criptografado: {arquivo.name}")


def main():
    print("=== LABORATÓRIO EDUCACIONAL ===")

    criar_chave()
    criptografar_arquivos()

    print("Demonstração concluída.")


if __name__ == "__main__":
    main()
