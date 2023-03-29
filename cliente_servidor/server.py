import socket
import os

# Defina o host e a porta para escutar
HOST = 'localhost'
PORT = 8000

# Crie um objeto de soquete e vincule-o ao host e à porta
socket_servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket_servidor.bind((HOST, PORT))

# Configure o servidor para ouvir conexões de entrada
socket_servidor.listen()

print(f"Escutando conexões de entrada em {HOST}:{PORT}...")

# Função para enviar o arquivo ao cliente
def enviar_arquivo(nome_arquivo, socket_cliente):
    try:
        # Abra o arquivo em modo binário
        arquivo = open(nome_arquivo, 'r')

        # Leia todo o conteúdo do arquivo
        conteudo = arquivo.read()

        # Envie o conteudo para o cliente
        socket_cliente.sendall(str(conteudo).encode())

        # Espere um sinal do cliente para iniciar o envio do conteúdo
        socket_cliente.recv(1024)

        # Envie o conteúdo do arquivo para o cliente
        socket_cliente.sendall(conteudo)

        # Feche o arquivo
        arquivo.close()

        print(f"Arquivo {nome_arquivo} enviado com sucesso para o cliente!")
    except FileNotFoundError:
        # Envie uma mensagem para o cliente informando que o arquivo não existe
        mensagem = f"O arquivo {nome_arquivo} não existe no servidor."
        socket_cliente.sendall(mensagem.encode())
        print(mensagem)


# Aceite conexões de entrada e receba solicitações de arquivos
while True:
    socket_cliente, endereco = socket_servidor.accept()
    print(f"Conexão estabelecida a partir de {endereco}")

    # Receba o nome do arquivo solicitado pelo cliente
    nome_arquivo = socket_cliente.recv(1024).decode()

    # Verifique se o arquivo existe no servidor e envie-o ao cliente ou envie uma mensagem de erro
    if os.path.exists(nome_arquivo):
        enviar_arquivo(nome_arquivo, socket_cliente)
    else:
        mensagem = f"O arquivo {nome_arquivo} não existe no servidor."
        socket_cliente.sendall(mensagem.encode())
        print(mensagem)

    # Feche a conexão do socket do cliente
    socket_cliente.close()
