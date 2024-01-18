import sys
import os

current_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.join(current_dir, '..')
sys.path.append(project_root)

from apis.load_test import run_load_test
from apis.purchase_test import run_purchase_test

if __name__ == "__main__":
    num_users_load_test = 1
    num_requests_per_user_load_test = 1
    run_load_test(num_users_load_test, num_requests_per_user_load_test)

    num_users_purchase_test = 1
    run_purchase_test(num_users_purchase_test)

