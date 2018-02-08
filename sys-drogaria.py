#SISTEMA FARMACIA // LTSoftware

import time
import os

blue = "\33[36;1m"
red = "\33[31;1m"
yellow = "\33[33;1m"
green = "\33[32;1m"


#CADASTRO DE CLIENTES:
def cadastroCliente():
    nome = str(input("\33[36;1m\nNOME: "))
    cep = str(input("\33[36;1m\nCEP: "))
    telefone = str(input("\33[36;1m\nTELEFONE: "))
    cliente = ("\nNOME: "+nome+" CEP: "+cep+" TELEFONE: "+telefone+"\n")
    arq = open('/sdcard/qpython/drogaria/clientes.txt','a')
    arq.write(cliente)
    arq.close()
    print(green,"CLIENTE ADICIONADO!")
    print(red,"1.",blue,"ADICIONAR OUTRO")
    print(red,"2.",blue,"VOLTAR")
    esc = int(input("\33[33m--> \33[36m"))
    if esc == 1:
        os.system("clear")
        cadastroCliente()
    elif esc == 2:
        os.system("clear")
        menuPrincipal()
    else:
        os.system("clear")
        menuPrincipal()
#CADASTRO REMEDIOS:
def cadastroRemedios():
    nome = str(input("\33[36;1m\nNOME: "))
    quantidade = str(input("\33[36;1m\nQUANTIDADE: : "))
    empresa = str(input("\33[36;1m\nEMPRESA: "))
    remedio = ("\nNOME: "+nome+" QUANTIDADE: "+quantidade+" EMPRESA: "+empresa+"\n")
    arq = open('/sdcard/qpython/drogaria/remedios.txt','a')
    arq.write(remedio)
    arq.close()
    print(green,"MEDICAMENTO ADICIONADO!")
    print(red,"1.",blue,"ADICIONAR OUTRO")
    print(red,"2.",blue,"VOLTAR")
    esc = int(input("\33[33m--> \33[36m"))
    if esc == 1:
        os.system("clear")
        cadastroRemedios()
    elif esc == 2:
        os.system("clear")
        menuPrincipal()
    else:
        os.system("clear")
        menuPrincipal()
#CONSULTA REMEDIOS
def consultaRemedios():
    arq = open('/sdcard/qpython/drogaria/remedios.txt','r')
    remedios = arq.read()
    print(remedios)
    print(red,"\n1.",blue,"VOLTAR")
    esc = int(input("\33[33m>>> \33[36m"))
    if esc==1:
        os.system("clear")
        menuPrincipal()
    else:
        os.system("clear")
        consultaRemedios()
#CONSULTAR CLIENTES
def consultaCliente():
    arq = open('/sdcard/qpython/drogaria/clientes.txt','r')
    clientes = arq.read()
    print(clientes)
    print(red,"\n1.",blue,"VOLTAR")
    esc = int(input("\33[33m>>> \33[36m"))
    if esc==1:
        os.system("clear")
        menuPrincipal()
    else:
        os.system("clear")
        consultaCliente()
#MENU DE INICIO:
def menuPrincipal():
    os.system("clear")
    print(blue,"   ====================")
    print("   |    ",red,"DROGARIA ",blue,"   |")
    print("    ====================")
    print(red,"\n 1.",blue,"CADASTRAR CLIENTE")
    print(red,"2.",blue,"CONSULTAR CLIENTES")
    print(red,"3.",blue,"CADASTRAR NOVO MEDICAMENTO")
    print(red,"4.",blue,"CONSULTAR MEDICAMENTOS")
    esc = int(input("\33[33;1m >>> \33[31;1m"))
    if(esc==1):
        os.system("clear")
        cadastroCliente()
    if esc == 2:
        os.system("clear")
        consultaCliente()
    elif(esc==3):
        os.system("clear")
        cadastroRemedios()
    elif(esc==4):
        os.system("clear")
        consultaRemedios()
    else:
        print(red,"ESCOLHA INVALIDA")
menuPrincipal()