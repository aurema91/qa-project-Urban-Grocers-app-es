import sender_stand_request
import data

def create_user_auth_token():
    current_body = data.user_body
    response = sender_stand_request.post_new_user(current_body)
    print(response.json()["authToken"])
    return response.json()["authToken"]

def create_kit(name):
    current_body = data.kit_body.copy()
    current_body["name"] = name
    return current_body

def positive_assert(name):
    token = create_user_auth_token()
    kit = create_kit(name)
    response = sender_stand_request.post_create_kit(kit, token)
    assert response.status_code ==201
    assert response.json()["name"] == kit["name"]

def negative_assert(name):
    token = create_user_auth_token()
    kit = create_kit(name)
    response = sender_stand_request.post_create_kit(kit, token)
    assert response.status_code ==400

#prueba 1: El número permitido de caracteres (1)
def test_create_kit_name_1_letter():
    positive_assert("a")

#prueba 2:El número permitido de caracteres (511)
def test_create_kit_name_511_letters():
    positive_assert("AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabC")

#prueba 3:El número de caracteres es menor que la cantidad permitida (0)
def test_create_kit_name_0_letters():
    negative_assert("")

#prueba 4:El número de caracteres es mayor que la cantidad permitida (512)
def test_create_kit_name_512_letters():
    negative_assert("AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcD")

#prueba 5:Se permiten caracteres especiales
def test_create_kit_name_special_Symbols():
    positive_assert('"№%@",')

#prueba 6:Se permiten espacios
def test_create_kit_name_spaces():
    positive_assert(" A Aaa ")

#prueba 7:Se permiten numeros
def test_create_kit_name_numbers():
    positive_assert("123")

#prueba 8:El parámetro no se pasa en la solicitud
def test_create_kit_name_No_parameter():
    negative_assert()

#prueba 9:Se ha pasado un tipo de parámetro diferente (número)
def test_create_kit_name_different_parameter():
    negative_assert(123)