from Modelos.Mesa import Mesa
class ControladorMesa():
    def __int__(self):
        print("Creando ControladorMesa")

    def index(self):
        print("Listar todos los Mesas")
        unMesa = {
            "_id": "abc123",
            "cedula": "123",
            "nombre": "Juan",
            "apellido": "Perez"
        }
        return [unMesa]

    def create(self, infoMesa):
        print("Creando un Mesa")
        elMesa = Mesa(infoMesa)
        return elMesa.__dict__

    def show(self, id):
        print("Mostrando un Mesa con id:", id)
        elMesa = {
            "_id": id,
            "cedula": "123",
            "nombre": "Juan",
            "apellido": "Perez"
        }
        return elMesa

    def update(self, id, infoMesa):
        print("Actualizando un Mesa con id:", id)
        elMesa = Mesa(infoMesa)
        return elMesa.__dict__

    def delete(self, id):
        print("Eliminando un Mesa con id: ", id)
        return {"deleted_count" : 1}