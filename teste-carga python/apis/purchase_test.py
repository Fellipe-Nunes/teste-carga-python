import threading
import requests
import time
from config import configurations

def make_purchase(user_id):
    url = f"{configurations['base_url']}{configurations['endpoint_purchase']}"

    try:
        start_time = time.time()

        response = requests.post(
            url,
            json=configurations["purchase_body"],
            headers={"Content-Type": "application/json"}
        )

        elapsed_time = time.time() - start_time

        if response.status_code in [200, 201]:
            print(
                f"Usuário {user_id}: Compra realizada com sucesso em {url}, "
                f"Status Code {response.status_code}, Tempo de Resposta: {elapsed_time:.2f} segundos"
            )
        else:
            print(
                f"Usuário {user_id}: Falha na compra em {url}, "
                f"Status Code {response.status_code}"
            )
    except Exception as e:
        print(f"Erro na compra do usuário {user_id} no endpoint {url}: {e}")

def run_purchase_test(num_users):
    threads = []

    for user_id in range(1, num_users + 1):
        thread = threading.Thread(target=make_purchase, args=(user_id,))
        threads.append(thread)

    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()

if __name__ == "__main__":
    num_users = 50  # Número de usuários simultâneos
    run_purchase_test(num_users)
