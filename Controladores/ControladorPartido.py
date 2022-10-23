from Modelos.Partido import Partido
class ControladorPartido():
    def __int__(self):
        print("Creando ControladorPartido")

    def index(self):
        print("Listar todos los Partidos")
        unPartido = {
            "_id": "abc123",
            "cedula": "123",
            "nombre": "Juan",
            "apellido": "Perez"
        }
        return [unPartido]

    def create(self, infoPartido):
        print("Creando un Partido")
        elPartido = Partido(infoPartido)
        return elPartido.__dict__

    def show(self, id):
        print("Mostrando un Partido con id:", id)
        elPartido = {
            "_id": id,
            "cedula": "123",
            "nombre": "Juan",
            "apellido": "Perez"
        }
        return elPartido

    def update(self, id, infoPartido):
        print("Actualizando un Partido con id:", id)
        elPartido = Partido(infoPartido)
        return elPartido.__dict__

    def delete(self, id):
        print("Eliminando un Partido con id: ", id)
        return {"deleted_count" : 1}