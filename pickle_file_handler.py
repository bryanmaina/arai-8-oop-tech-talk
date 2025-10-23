from pickle import dumps, loads

from file_serializer_hander import FileSerializerHandler


class PickleFileHandler(FileSerializerHandler):
    def __init__(self, filename) -> None:
        self.filename = filename

    def serialize(self, data):
        return dumps(data)

    def deserialize(self, data):
        return loads(data)
