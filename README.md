# Decrypter e Encrypter
!!!ESSE REPOSITORIO TEM FINS EDUCATIVOS APENAS!!!



Este projeto foi feito em função ao bootcamp santander ciberseguranca 2024 consiste em dois scripts Python para criptografar e descriptografar arquivos dentro de diretórios específicos do usuário em uma máquina Windows. O processo de criptografia e descriptografia é realizado utilizando o algoritmo AES em modo CTR, da biblioteca `pyaes`.

## Tabela de Conteúdos

- [Visão Geral](#visão-geral)
- [Decrypter](#decrypter)
- [Encrypter](#encrypter)
- [Uso](#uso)

## Visão Geral

O projeto oferece funcionalidades para:

- **Descriptografar (`decrypter`)**: Descriptografa arquivos com a extensão `.dioware` nos diretórios `Documentos`, `Imagens`, `Vídeos` e `Downloads` do usuário, utilizando uma chave AES fornecida pelo usuário.
- **Criptografar (`encrypter`)**: Criptografa todos os arquivos nos diretórios especificados e adiciona a extensão `.dioware` aos arquivos, utilizando uma chave AES gerada aleatoriamente.

Ambos os scripts removem os arquivos originais após a criptografia ou descriptografia e salvam os arquivos resultantes com os nomes apropriados.

## Decrypter

O script `decrypter` é responsável por descriptografar arquivos que foram criptografados com a extensão `.dioware`. Ele solicita que o usuário insira uma chave de descriptografia. O script funciona da seguinte forma:

1. Lê o arquivo criptografado.
2. Descriptografa o conteúdo usando AES em modo CTR.
3. Remove o arquivo criptografado original.
4. Salva o arquivo descriptografado com o nome original (removendo a extensão `.dioware`).

### Função Descriptografar Arquivo

A função `decrypt_file` recebe o caminho do arquivo e a chave de descriptografia, realizando o processo de leitura, descriptografia, remoção do arquivo original e criação do novo arquivo descriptografado.

### Função Descriptografar Arquivos do Usuário

A função `decrypt_user_files` percorre os diretórios `Documents`, `Pictures`, `Videos` e `Downloads` do usuário e descriptografa todos os arquivos `.dioware` encontrados, utilizando a chave fornecida.

## Encrypter

O script `encrypter` é responsável por criptografar arquivos em diretórios específicos. Ele utiliza uma chave AES gerada aleatoriamente e adiciona a extensão `.dioware` aos arquivos criptografados. O script funciona da seguinte forma:

1. Lê o arquivo original.
2. Criptografa o conteúdo usando AES em modo CTR.
3. Adiciona a extensão `.dioware` ao nome do arquivo criptografado.
4. Remove o arquivo original.

### Função Gerar IV Aleatório (Chave)

A função `generate_random_iv` gera uma chave aleatória de 16 bytes, que é utilizada para criptografar os arquivos. Essa chave é impressa no terminal para ser usada no processo de descriptografação.

### Função Criptografar Arquivo

A função `encrypt_file` recebe o caminho do arquivo e a chave, realizando o processo de leitura, criptografia, remoção do arquivo original e criação do novo arquivo criptografado.

### Função Criptografar Arquivos do Usuário

A função `encrypt_user_directories` percorre os diretórios `Documents`, `Pictures`, `Videos` e `Downloads` do usuário e criptografa todos os arquivos encontrados, utilizando a chave gerada aleatoriamente.

## Uso

### Para Criptografar Arquivos:
1. Execute o script `encrypter`.
2. O script gerará uma chave de criptografia aleatória.
3. Ele criptografará todos os arquivos nas pastas `Documents`, `Pictures`, `Videos`, e `Downloads` e os renomeará com a extensão `.dioware`.

### Para Descriptografar Arquivos:
1. Execute o script `decrypter`.
2. Insira a chave de descriptografia.
3. O script descriptografará todos os arquivos `.dioware` nas mesmas pastas mencionadas e removerá a extensão `.dioware`.

- `pyaes` - Biblioteca para criptografia AES em modo CTR.
  
Você pode instalar as dependências usando o seguinte comando:

```bash
pip install pyaes
