import json
import unittest

from crud_alunos.src.app import app


class TestFlask(unittest.TestCase):
    def setUp(self):
        app.config['TESTING'] = True
        self.app = app.test_client()

    def testgetaluno(self):
        response = self.app.get('/alunos/Sandro', method='GET')
        assert response.status_code == 200
