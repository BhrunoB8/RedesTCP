#!/bin/bash
import os
import subprocess
import time

#ATENÇÃO: rodar este arquivo na pasta onde se encontram os arquivos abaixo.
#cada chamada de cliente é para uma das opções do sistema
os.system("start cmd /k" f'python server.py --ip 127.0.0.1 --port 1234')
time.sleep(1)
os.system("start cmd /k" f'python client.py')
time.sleep(1)
os.system("start cmd /k" f'python client.py')
time.sleep(1)
os.system("start cmd /k" f'python client.py')
time.sleep(1)
os.system("start cmd /k" f'python client.py')