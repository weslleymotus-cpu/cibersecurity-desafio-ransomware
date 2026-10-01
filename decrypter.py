from pathlib import Path
from cryptography.fernet import Fernet

# Pasta exclusiva para os arquivos de teste
PASTA_LABORATORIO = Path("laboratorio")

# Chave utilizada na criptografia
ARQUIVO_CHAVE = PASTA_LABORATORIO / "chave.key"


def descriptografar_arquivos():
    """Descriptografa somente os arquivos TXT do laboratório."""
    
    if not ARQUIVO_CHAVE.exists():
        print("Chave não encontrada.")
        return

    chave = ARQUIVO_CHAVE.read_bytes()
    fernet = Fernet(chave)

    arquivos = list(PASTA_LABORATORIO.glob("*.txt"))

    if not arquivos:
        print("Nenhum arquivo de teste encontrado.")
        return

    for arquivo in arquivos:
        try:
            dados = arquivo.read_bytes()
            dados_descriptografados = fernet.decrypt(dados)

            arquivo.write_bytes(dados_descriptografados)

            print(f"Arquivo recuperado: {arquivo.name}")

        except Exception:
            print(f"Não foi possível descriptografar: {arquivo.name}")


def main():
    print("=== LABORATÓRIO EDUCACIONAL ===")

    descriptografar_arquivos()

    print("Demonstração de recuperação concluída.")


if __name__ == "__main__":
    main()
