import os
import pyaes

def decrypt_file(encrypted_file_name, decrypted_file_name, key):
    """
    Descriptografa um arquivo criptografado com AES CTR.
    
    :param encrypted_file_name: Nome do arquivo criptografado.
    :param decrypted_file_name: Nome do arquivo a ser criado com o conteúdo descriptografado.
    :param key: Chave de descriptografia (deve ser em bytes).
    """
    try:
        # Ler o arquivo criptografado
        with open(encrypted_file_name, "rb") as encrypted_file:
            file_data = encrypted_file.read()
        
        # Descriptografar os dados
        aes = pyaes.AESModeOfOperationCTR(key)
        decrypted_data = aes.decrypt(file_data)
        
        # Remover o arquivo criptografado
        os.remove(encrypted_file_name)
        
        # Criar o arquivo descriptografado
        with open(decrypted_file_name, "wb") as decrypted_file:
            decrypted_file.write(decrypted_data)
        
        print(f"Arquivo '{encrypted_file_name}' foi descriptografado com sucesso para '{decrypted_file_name}'.")
    
    except FileNotFoundError:
        print(f"Erro: O arquivo '{encrypted_file_name}' não foi encontrado.")
    except Exception as e:
        print(f"Erro ao processar o arquivo: {e}")

# Parâmetros de entrada
encrypted_file = "teste.txt.ransomwaretroll"
decrypted_file = "teste.txt"
encryption_key = b"testeransomwares"

# Chamada da função
decrypt_file(encrypted_file, decrypted_file, encryption_key)

