from file_serializer_hander import FileSerializerHandler
from json_file_handler import JsonFileHandler
from pickle_file_handler import PickleFileHandler


def main():
    data = {"brand": "Toyota", "model": "Hilux", "year": 2022}

    json_handler = JsonFileHandler("./data.json")
    json_handler.write(data)
    print(json_handler.read())

    pickle_handler = PickleFileHandler("./data.pkl")
    pickle_handler.write(data)
    print(pickle_handler.read())

    assert isinstance(json_handler, FileSerializerHandler)
    assert isinstance(pickle_handler, FileSerializerHandler)

    # fsh = FileSerializerHandler()  # FileSerializerHandler is an abstract class.
    # It can never be instantiated on its own as it is assumed that it is missing at least one implementation

    # print(json_handler.__classname) # This does not work because that variable is protected


if __name__ == "__main__":
    main()
