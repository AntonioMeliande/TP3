#código do tp3
from time import sleep
import psutil
import socket

info_cpu = psutil.cpu_percent(interval=1)
info_memoria = psutil.virtual_memory()
info_disco = psutil.disk_usage('.')
disco_total = round(info_disco[0]/(1024 * 1024 * 1024))
disco_uso_porcentagem = (info_disco[3])
disco_disponivel = round(info_disco[2]/(1024 * 1024 * 1024))
info_hostname = socket.gethostname()
info_rede = socket.gethostbyname(info_hostname)

opção = 0
print('Bem vindo ao gerenciador!')
while opção != 6:
    print('''
    [1] Processador
    [2] Memória
    [3] Disco
    [4] IP
    [5] Estatísticas
    [6] Sair do programa
    ''')
    opção = int(input('Informe a opção desejada: '))
    if opção == 1:
        print(f'\nUso da Cpu {info_cpu}%')

    elif opção == 2:
        print('\nPorcentagem do uso de memória: {} %'.format(info_memoria[2]))

    elif opção == 3:
        print(f'\nTamanho do disco: {disco_total} GB, Utilizado: {disco_uso_porcentagem} %, Disponivel: {disco_disponivel} GB')

    elif opção == 4:
        print('\nEndereço IP:', info_rede)

    elif opção == 5:
        print('\nEstatísticas:\nUso da CPU: {}%\nUso da Memória: {}%\nEspaço em disco disponível: {} GB\nEndereço IP: {}'.format(info_cpu, info_memoria[2], disco_disponivel, info_rede))

    elif opção == 6:
        print('\nFinalizando....')

    else:
        print('Opção invalida. Tente novamente!')
    print('_-_-_-' *20)
    sleep(2)
print('Fim do programa! Obrigado por utilizar o gerenciador!')
