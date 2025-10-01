import subprocess
import os

def testar_ping(host):
    print(f"Testando a conexão com o servidor: {host}")

    comando = ['ping','-c','2', host]
    
    resultado = subprocess. run(comando, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

    if resultado.returncode == 0:
        return True
    else:
        return False

if __name__ == "__main__":
    servidor_para_testar = '150.162.142.79'

    if testar_ping(servidor_para_testar):
        print(f"Conexão com {servidor_para_testar} bem-sucedida.")
    else:
        print(f"Falha na conexão com {servidor_para_testar}.")

