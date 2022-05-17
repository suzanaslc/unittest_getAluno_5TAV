import unittest
from tests import studentsRepositoryMock
from crud_alunos.src.services.alunoService import AlunoService


class TestStringMethods(unittest.TestCase):

    def test_getaluno(self):
        service = AlunoService(studentsRepositoryMock.school)
        print(service)
        result = service.getaluno('Sandro')
        self.assertEqual(result,
                         200)  # O cerne de cada teste é a invocação de um método assertEqual() para verificar se há um resultado esperado


if __name__ == '__main__':
    unittest.main()
