<img width="100%" bottom=50px src ="https://capsule-render.vercel.app/api?type=waving&height=100&color=FF78CB&section=header&reversal=false&descAlign=22&descAlignY=42"/>

<h1 align="center">PyPing 🐍📡</h1>

<p align="center">
  <strong>English</strong> | <a href="#pyping---verificador-de-host">Português</a>
</p>

A simple Python script to check network connectivity to a host using the `ping` command.

---

## 📝 Description

This project provides a lightweight Python script to test network connectivity with a specified host (a server, IP address, or any network device) by using the system's native `ping` command. It's a useful tool for automation scripts, network monitoring, or simply checking a server's status programmatically.

## ✨ Features

-   **Connectivity Check**: Sends ICMP packets to a target host.
-   **Simplicity**: A single function that returns `True` for success and `False` for failure.
-   **Clean Output**: The `ping` command's output is suppressed for a cleaner user experience, showing only the final success or failure message.
-   **Easy to Integrate**: Can be easily imported and used in other Python projects.

## 🚀 How to Use

### Prerequisites

-   Python 3.x
-   The `ping` command must be available in your operating system (standard on most systems).

### Running the Script

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/your-username/your-repository-name.git](https://github.com/your-username/your-repository-name.git)
    cd your-repository-name
    ```

2.  **Change the host (optional):**
    Open the script file (e.g., `ping_tester.py`) and change the value of the `host_to_test` variable to the IP address or domain you want to test.
    ```python
    if __name__ == "__main__":
        host_to_test = '8.8.8.8' # Example: Google's DNS
    ```

3.  **Run the script:**
    ```bash
    python ping_tester.py
    ```

### Example Output

If the connection is successful:
````

Testing connection to server: 8.8.8.8
Connection to 8.8.8.8 successful.

```

If the host is unreachable or a network failure occurs:
```

Testing connection to server: 192.168.1.99
Failed to connect to 192.168.1.99.

````

## 🛠️ Customization

### Cross-Platform Compatibility (Windows/Linux/macOS)

To make the script work on Windows, which uses the `-n` flag instead of `-c` for ping count, you can use the following platform-aware function:

```python
import subprocess
import platform

def test_ping(host):
    """
    Pings a host to check for connectivity.
    Returns True if the host responds, False otherwise.
    """
    param = '-n' if platform.system().lower() == 'windows' else '-c'
    command = ['ping', param, '2', host]
    
    # Suppress output by redirecting to DEVNULL
    result = subprocess.run(command, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

    return result.returncode == 0
````

## 🤝 Contributing

Contributions are welcome\! If you have ideas for improvements or find any issues, feel free to open an issue or submit a pull request.

## 📄 License

This project is distributed under the MIT License. See the `LICENSE` file for more details.

-----

<br>

<h1 align="center">PyPing 🐍📡 - Verificador de Host </h1> 

<p align="center">
  <strong>English</strong> | <a href="#-utilitário-de-ping-em-python">Português</a>
</p>

Um script simples em Python para testar a conectividade de rede com um host usando o comando `ping`.

-----

## 📝 Descrição

Este projeto oferece um script leve em Python para testar a conectividade de rede com um host específico (um servidor, endereço IP ou qualquer dispositivo de rede) usando o comando `ping` nativo do sistema. É uma ferramenta útil para scripts de automação, monitoramento de rede ou simplesmente para verificar o status de um servidor de forma programática.

## ✨ Funcionalidades

  - **Verificação de Conectividade**: Envia pacotes ICMP para um host de destino.
  - **Simplicidade**: Uma única função que retorna `True` para sucesso e `False` para falha.
  - **Saída Limpa**: A saída do comando `ping` é suprimida para uma experiência de usuário mais limpa, mostrando apenas a mensagem final de sucesso ou falha.
  - **Fácil de Integrar**: Pode ser facilmente importado e utilizado em outros projetos Python.

## 🚀 Como Usar

### Pré-requisitos

  - Python 3.x
  - O comando `ping` deve estar disponível no seu sistema operacional (padrão na maioria dos sistemas).

### Executando o Script

1.  **Clone o repositório:**

    ```bash
    git clone [https://github.com/seu-usuario/seu-repositorio.git](https://github.com/seu-usuario/seu-repositorio.git)
    cd seu-repositorio
    ```

2.  **Altere o host (opcional):**
    Abra o arquivo do script (ex: `ping_tester.py`) e altere o valor da variável `servidor_para_testar` para o endereço IP ou domínio que você deseja testar.

    ```python
    if __name__ == "__main__":
        servidor_para_testar = '8.8.8.8' # Exemplo: DNS do Google
    ```

3.  **Execute o script:**

    ```bash
    python ping_tester.py
    ```

### Exemplo de Saída

Se a conexão for bem-sucedida:

```
Testando a conexão com o servidor: 8.8.8.8
Conexão com 8.8.8.8 bem-sucedida.
```

Se o host estiver inacessível ou houver uma falha na rede:

```
Testando a conexão com o servidor: 192.168.1.99
Falha na conexão com 192.168.1.99.
```

## 🛠️ Customização

### Compatibilidade Multiplataforma (Windows/Linux/macOS)

Para fazer o script funcionar no Windows, que usa a flag `-n` em vez de `-c` para a contagem de pings, você pode usar a seguinte função adaptada:

```python
import subprocess
import platform

def testar_ping(host):
    """
    Envia um ping a um host para verificar a conectividade.
    Retorna True se o host responder, caso contrário, False.
    """
    param = '-n' if platform.system().lower() == 'windows' else '-c'
    comando = ['ping', param, '2', host]
    
    # Suprime a saída redirecionando para DEVNULL
    resultado = subprocess.run(comando, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

    return resultado.returncode == 0
```

## 🤝 Como Contribuir

Contribuições são bem-vindas\! Se você tiver ideias para melhorias ou encontrar algum problema, sinta-se à vontade para abrir uma *issue* ou enviar um *pull request*.

## 📄 Licença

Este projeto é distribuído sob a Licença MIT. Veja o arquivo `LICENSE` para mais detalhes.

<img width="100%" bottom=50px src ="https://capsule-render.vercel.app/api?type=waving&height=100&color=FF78CB&section=footer&reversal=false&descAlign=22&descAlignY=42"/>
