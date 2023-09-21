import requests
import data
import configuration


# Создание юзера
def create_new_user():
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_USER_PATH,  # URL, части в configuration.py
                         json=data.user_body,  # тело запроса из data.py
                         headers=data.headers)  # заголовки запроса из data.py


token = create_new_user().json()["authToken"]  # токен вытащится автоматически с помощью функции создания юзера


# Создание набора
def post_new_client_kit(kit_body, auth_token):
    current_headers = data.headers.copy()   # делаем копию заголовков
    current_headers["Authorization"] = "Bearer " + auth_token  # добавляем переданный токен к копии
    return requests.post(configuration.URL_SERVICE + configuration.MAIN_KITS_PATH,  # отправляем запрос
                         json=kit_body,
                         headers=current_headers)
