from json import dumps, loads

from file_serializer_hander import FileSerializerHandler


class JsonFileHandler(FileSerializerHandler):
    def __init__(self, filename) -> None:
        self.filename = filename
        self.__classname = "JsonFileHandler"

    def serialize(self, data):
        return dumps(data).encode("utf-8")

    def deserialize(self, data):
        return loads(data.decode("utf-8"))
