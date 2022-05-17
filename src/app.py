from flask import Flask, abort, jsonify

from crud_alunos.src.services.alunoService import AlunoService
from crud_alunos.src.services.professorService import ProfessorService

from crud_alunos.src.tests import studentsRepositoryMock
from crud_alunos.src.tests import teachersRepositoryMock


app = Flask(__name__)


@app.route("/alunos/<nome>", methods=["GET"])
def getalunorota(nome):
    aluno_service = AlunoService(studentsRepositoryMock.school)
    aluno = aluno_service.getaluno(nome)
    if aluno is False:
        response = jsonify({'message': "Não encontrado"})
        response.status_code = 404
        return response
    return aluno

@app.route("/professores/<nome>", methods=["GET"])
def getprofessoresrota(nome):
    professor_service = ProfessorService(teachersRepositoryMock.employees)
    professor = professor_service.getprofessor(nome)
    if professor is False:
        response = jsonify({'message': "Não encontrado"})
        response.status_code = 404
        return response
    return professor
if __name__ == "__main__":
    app.run()
