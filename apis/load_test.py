import requests
import time
from apis.config import configurations
from report_generator import generate_pdf_summary

results = []

def make_request(user_id):
    # Constrói a URL completa
    url = f"{configurations['base_url']}{configurations['endpoint']}"

    try:
        start_time = time.time()

        if configurations["request_type"].upper() == "POST":
            response = requests.post(
                url,
                json=configurations["request_body"],
                headers={
                    "Content-Type": "application/json"
                }
            )
        elif configurations["request_type"].upper() == "GET":
            response = requests.get(url)
        else:
            print("Tipo de requisição não suportado.")
            return

        # Calcula o tempo de resposta
        elapsed_time = time.time() - start_time

        # Exibe os resultados
        if response.status_code == 200:
            print(
                f"Usuário {user_id}: Requisição para {url} bem-sucedida, "
                f"Status Code 200, Tempo de Resposta: {elapsed_time:.2f} segundos"
            )
        else:
            print(
                f"Usuário {user_id}: Requisição para {url} falhou, "
                f"Status Code {response.status_code}"
            )
    except Exception as e:
        print(f"Erro na solicitação do usuário {user_id} para o endpoint {url}: {e}")

def run_load_test(num_users, num_requests_per_user):
    start_time = time.time()

    for user_id in range(1, num_users + 1):
        for _ in range(num_requests_per_user):
            make_request(user_id)

    elapsed_time = time.time() - start_time
    print(f"Teste de carga concluído para {num_users} usuários, "
          f"{num_requests_per_user} requisições por usuário, "
          f"Tempo total: {elapsed_time:.2f} segundos.")

generate_pdf_summary(results)
