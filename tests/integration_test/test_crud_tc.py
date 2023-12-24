from src.constants.api_constants import BASE_URL,APIConstants,base_url

def test_crud():
    print("Calling from method outside class: "+base_url())
    print("Calling from constant: "+BASE_URL)
    url = APIConstants.base_url()
    print("Calling from static method of the class: "+url)
    obj = APIConstants()
    print("Calling from the non static method of the class: "+obj.base_url_nonStatic())

