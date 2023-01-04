import random
import time
import sys
import os
import uuid
from colorama import init, Fore, Back, Style

os.system("clear")
os.system("figlet BtcMinner")
print
print("Created By SanthM & LDZ Team")
print("Cargando...")
time.sleep(5)
llave = input("[+] License Key: ")
cuenta = input("[+] Wallet ID: ")
time.sleep(0.5)
print(Fore.GREEN+str("[+] Licencia Y Wallet Aprobadas"))
time.sleep(1)
print(Fore.WHITE+str("Iniciando..."))
time.sleep(3)



# Función para simular el proceso de minería de bitcoins
def minar_bitcoins():
  # Imprime un mensaje para indicar que se ha iniciado el proceso de minería
  print("Iniciando proceso de minería de bitcoins...")

  # Bucle infinito para simular la minería
  while True:
    # Genera un número aleatorio entre 1 y 100
    aleatorio = random.randint(1, 100)
    
    numero_aleatorio = random.uniform(0, 1)
 
    # Si el número es divisible por 7, simula que se ha encontrado un bloque
    if aleatorio % 17 == 0:

      print(Fore.GREEN+str(uuid.uuid4())+" | BTC Encontrados: "+ str(numero_aleatorio))
      
      input(Fore.GREEN+str("Presiona Enter Para Continuar...: "))

    # Si no, simula que se está buscando el siguiente bloque
    else:
      print(Fore.RED+str(uuid.uuid4())+" | Llave Invalida")

    # Duerme el proceso durante un segundo para simular el tiempo de minería
    time.sleep(0.1)

# Inicia el proceso de minería de bitcoins
minar_bitcoins()
