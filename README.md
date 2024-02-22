# API Load Test
Este projeto consiste em scripts para realizar testes de carga em API, simulando múltiplos usuários realizando compras e consultas simultaneamente.

# Pré-requisitos
Certifique-se de ter Python instalado no seu ambiente de desenvolvimento.
pip install -r requirements.txt

# Configuração
Edite o arquivo config.py para configurar a URL base, endpoint de compra, e corpo da solicitação.
Execute os testes usando os scripts fornecidos.

# Executando os Testes
Para executar os testes de carga, use os seguintes comandos no terminal:
python3 apis/purchase_test.py

# Teste de Consultas
python3 apis/load_test.py

# Configuração Avançada
Você pode ajustar o número de usuários simultâneos e outros parâmetros diretamente nos scripts.

# No arquivo purchase_test.py ou load_test.py
num_users = 10
run_purchase_test(num_users)  # ou run_load_test(num_users)

# Arquitetura do projeto
__init__.py: Um arquivo vazio indicando que apis/ deve ser tratado como um pacote.
config.py: Arquivo para configurar variáveis da API.
endpoints.py: Arquivo para configurar os endpoints da API.
load_test.py: Script principal para o teste de carga.
purchase_test.py: Script para o teste de compras.
report_generator.py: Módulo para a geração de relatórios em PDF.
__init__.py: Um arquivo vazio indicando que a pasta principal (API_Load_Test/) deve ser tratada como um pacote.
requirements.txt: Arquivo contendo as dependências do projeto.
