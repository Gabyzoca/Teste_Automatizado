🚀 Projeto de Teste de Software — Login SauceDemo

Este projeto faz parte da atividade prática de Testes de Software, envolvendo:

✔️ Definição de cenário de teste
✔️ Criação de casos de teste (positivo e negativo)
✔️ Implementação de teste automatizado usando Python + Selenium
✔️ Uso do navegador Microsoft Edge (compatível com Selenium 4 sem drivers externos)

🧪 1. Cenário de Teste

Cenário 01 – Login SauceDemo
Objetivo: Validar todas as funcionalidades relacionadas ao login do site SauceDemo.
Sistema Testado: https://www.saucedemo.com

Pré-requisitos:

Acesso à internet
Possuir Python instalado
Selenium instalado
Microsoft Edge instalado

📝 2. Casos de Teste
✔️ Caso de Teste Positivo – CT01

ID: CT-01
Nome: Login com credenciais válidas
Condição de Aceite: O sistema deve permitir o login e redirecionar para a página de produtos.
Pré-condições: usuário e senha válidos disponíveis.

Ação	Resultado Esperado
1. Acessar o site	Página inicial de login é exibida
2. Informar usuário válido	O campo exibe o texto digitado
3. Informar senha válida	O campo exibe texto mascarado
4. Clicar em Login	Página Products é exibida
   
❌ Caso de Teste Negativo – CT02

ID: CT-02
Nome: Login com senha inválida
Condição de Aceite: O sistema deve recusar o login e exibir mensagem de erro.

Ação	Resultado Esperado
1. Acessar o site	Página de login é exibida
2. Informar usuário válido	Campo preenchido corretamente
3. Informar senha incorreta	Campo preenchido
4. Clicar em Login	Mensagem: "Epic sadface: Username and password do not match any user"
🤖 3. Teste Automatizado (Selenium + Python)

O teste automatiza o caso CT01 (login com sucesso) utilizando Selenium 4 e Microsoft Edge.

✔️ Arquivo:

      test_login.py
      from selenium import webdriver
      from selenium.webdriver.common.by import By
      import time

    def test_login_sucesso():

    driver = webdriver.Edge()

    try:
        print("Abrindo site...")
        driver.get("https://www.saucedemo.com/")
        time.sleep(2)

        print("Preenchendo usuário...")
        user = driver.find_element(By.ID, "user-name")
        user.send_keys("standard_user")

        print("Preenchendo senha...")
        password = driver.find_element(By.ID, "password")
        password.send_keys("secret_sauce")

        print("Clicando em Login...")
        login_button = driver.find_element(By.ID, "login-button")
        login_button.click()

        time.sleep(3)

        print("Verificando resultado...")
        titulo = driver.find_element(By.CLASS_NAME, "title").text
        assert titulo == "Products"
        print("Login OK 👌")

        time.sleep(5)

    except Exception as e:
        print(f"Erro encontrado: {e}")

    finally:
        driver.quit()

test_login_sucesso()

📦 4. Instalação
1) Instalar dependências

No terminal:

pip install selenium

2) Executar o teste

Dentro da pasta do projeto:

python test_login.py

💻 5. Tecnologias Utilizadas

Python 3.14

Selenium 4

Microsoft Edge WebDriver interno

Site SauceDemo
