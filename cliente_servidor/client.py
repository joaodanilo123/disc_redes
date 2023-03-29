import socket
import os

# Defina o host e a porta para se conectar
HOST = 'localhost'
PORT = 8000

# Crie um objeto de soquete e se conecte ao servidor
socket_cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket_cliente.connect((HOST, PORT))

# Solicite ao usuário o nome do arquivo desejado
nome_arquivo = input("Digite o nome do arquivo que deseja baixar: ")

# Envie o nome do arquivo ao servidor
socket_cliente.sendall(nome_arquivo.encode())

# Receba o conteudo do arquivo do servidor
resposta = socket_cliente.recv(1024).decode()

# Verifique se o arquivo existe no servidor ou se foi enviado uma mensagem de erro
if resposta:
    print(f"Recebendo o arquivo {nome_arquivo} e gravando na pasta 'arquivos_client'..")
    
    arquivo = open(f"./arquivos_client/{nome_arquivo}", "w");
    arquivo.write(resposta)
    arquivo.close()
