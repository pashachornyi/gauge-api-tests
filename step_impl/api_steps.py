from getgauge.python import step, data_store
import requests
from pydantic import BaseModel

BASE_URL = "https://jsonplaceholder.typicode.com"


class UserSchema(BaseModel):
    id: int
    name: str
    email: str


@step("Отправить GET запрос на <endpoint>")
def send_get_request(endpoint):
    response = requests.get(BASE_URL + endpoint)
    data_store.scenario["response"] = response


@step("Проверить, что статус код равен <expected_code>")
def check_status_code(expected_code):
    actual = data_store.scenario["response"].status_code
    assert actual == int(
        expected_code), f"Ожидали {expected_code}, получили {actual}"


@step("Проверить, что в ответе есть поле <field_name>")
def check_field_present(field_name):
    data = data_store.scenario["response"].json()
    if isinstance(data, list):
        data = data[0]
    assert field_name in data, f"Поле {field_name} не найдено в ответе"


@step("Отправить POST запрос на <endpoint> с заголовком <title>")
def send_post_request(endpoint, title):
    payload = {"title": title}
    response = requests.post(BASE_URL + endpoint, json=payload)
    data_store.scenario["response"] = response


@step("Отправить DELETE запрос на <endpoint>")
def send_delete_request(endpoint):
    response = requests.delete(BASE_URL + endpoint)
    data_store.scenario["response"] = response


@step("Проверить, что ответ соответствует схеме пользователя")
def check_user_schema():
    data = data_store.scenario["response"].json()
    if isinstance(data, list):
        data = data[0]
    UserSchema(**data)
