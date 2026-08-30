from getgauge.python import step
import requests

BASE_URL = "https://jsonplaceholder.typicode.com"

response_holder = {}


@step("Отправить GET запрос на <endpoint>")
def send_get_request(endpoint):
    response = requests.get(BASE_URL + endpoint)
    response_holder["response"] = response


@step("Проверить, что статус код равен <expected_code>")
def check_status_code(expected_code):
    actual = response_holder["response"].status_code
    assert actual == int(
        expected_code), f"Ожидали {expected_code}, получили {actual}"


@step("Проверить, что в ответе есть поле <field_name>")
def check_field_present(field_name):
    data = response_holder["response"].json()
    if isinstance(data, list):
        data = data[0]
    assert field_name in data, f"Поле {field_name} не найдено в ответе"
