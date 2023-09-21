import data
import sender_stand_request


# Функция создания тела запроса для тестов
def get_kit_body(name):
    current_body = data.kit_body.copy()  # копируем тело запроса из data.py, чтобы не изменять его прямо в файле
    current_body["name"] = name  # вставляем название набора в тело запроса из аргумента
    return current_body  # возвращаем готовое тело запроса


# Функция для позитивных тестов
def positive_assert(name):
    kit_body = get_kit_body(name)  # получаем тело для запроса
    kit_response = sender_stand_request.post_new_client_kit(kit_body,  # отправляем запрос, сохраняем ответ
                                                            sender_stand_request.token)
    assert kit_response.status_code == 201  # убеждаемся, что код ответа 201
    assert kit_response.json()["name"] == name  # убеждаемся, что API возвращает имя набора из нашего запроса


# Функция для негативных тестов
def negative_assert(name):
    kit_body = get_kit_body(name)  # получаем тело для запроса
    kit_response = sender_stand_request.post_new_client_kit(kit_body,  # отправляем запрос, сохраняем ответ
                                                            sender_stand_request.token)
    assert kit_response.status_code == 400  # убеждаемся, что код ответа 400

# <---------ТЕСТЫ--------->


# Название набора из 1 символа
def test_positive_1_symbol_name():
    positive_assert("a")


# Название набора из 511 символа
def test_positive_511_symbol_name():
    positive_assert("Abcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdab\
    cdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcda\
    bcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcd\
    abcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabc\
    dabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabC")


# Название набора - пустая строка
def test_negative_empty_name():
    negative_assert("")


# Название набора длиннее 511 символа (здесь 512)
def test_negative_name_too_long():
    negative_assert("Abcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdab\
    cdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcda\
    bcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcd\
    abcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabc\
    dabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcD")


# Название набора с англ буквами
def test_positive_eng_name():
    positive_assert("QWErty")


# Название набора с русскими буквами
def test_positive_ru_name():
    positive_assert("Мария")


# Название набора со спецсимволами
def test_positive_special_name():
    positive_assert("\"№%@\",")


# Название набора с пробелами
def test_positive_space_name():
    positive_assert(" Человек и КО ")


# Запрос без параметра name в теле
def test_negative_no_name_parameter():
    kit_response = sender_stand_request.post_new_client_kit(data.kit_body, sender_stand_request.token)
    assert kit_response.status_code == 400


# Цифры в названии набора
def test_positive_numbers_name():
    positive_assert("123")


# Число вместо строки в параметре name
def test_negative_int_name():
    negative_assert(123)
