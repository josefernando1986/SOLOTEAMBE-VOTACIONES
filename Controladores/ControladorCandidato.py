from Repositorios.RepositorioCandidato import RepositorioCandidato
from Modelos.Candidato import Candidato
class ControladorCandidato():
    def __init__(self):
        self.repositorioCandidato = RepositorioCandidato()

    def index(self):
        print("Listar todos los Candidatos")
        unCandidato={
            "_id": "abc123",
            "cedula": "123",
            "nombre": "Juan",
            "apellido": "Perez"
        }
        return [unCandidato]

    def create(self, infoCandidato):
        nuevoCandidato = Candidato(infoCandidato)
        return self.repositorioCandidato.save(nuevoCandidato)

    def show(self, id):
        print("Mostrando un candidato con id:", id)
        elCandidato = {
            "_id": id,
            "cedula": "123",
            "nombre": "Juan",
            "apellido": "Perez"
        }
        return elCandidato

    def update(self, id, infoCandidato):
        print("Actualizando un candidato con id:", id)
        elCandidato = Candidato(infoCandidato)
        return elCandidato.__dict__

    def delete(self, id):
        print("Eliminando un candidato con id: ", id)
        return {"deleted_count" : 1}