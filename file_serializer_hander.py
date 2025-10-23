from abc import ABC, abstractmethod


# ABC => abstract base class
# This what we would call an `interface` in many other programming  languages
class FileSerializerHandler(ABC):
    @abstractmethod
    def serialize(self, data):
        pass

    @abstractmethod
    def deserialize(self, data):
        pass

    def write(self, data):
        # w => write, b => byte
        with open(self.filename, "wb") as file:
            file.write(self.serialize(data))

    def read(self):
        # r => read, b => byte
        with open(self.filename, "rb") as file:
            return self.deserialize(file.read())
