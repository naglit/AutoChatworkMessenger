
from mimetypes import init


class message:
    def __init__(self, id, to, body):
        self.__id = id
        self.__to = to
        self.__body = body