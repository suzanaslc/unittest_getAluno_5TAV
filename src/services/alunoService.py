import json

from flask import Response


class AlunoService:
    def __init__(self, arr):
        self.arr = arr

    def getaluno(self, name):
        for k in self.arr:
            if name == k.get('name'):
                return json.dumps(k)
        return False


