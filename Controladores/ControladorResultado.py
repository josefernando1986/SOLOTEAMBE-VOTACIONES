from Repositorios.RepositorioResultado import RepositorioResultado
from Repositorios.RepositorioMesa import RepositorioMesa
from Repositorios.RepositorioCandidato import RepositorioCandidato
from Modelos.Resultado import Resultado
from Modelos.Mesa import Mesa
from Modelos.Candidato import Candidato

class ControladorResultado():
    def __init__(self):
        self.repositorioResultado = RepositorioResultado()
        self.repositorioCandidato = RepositorioCandidato()
        self.repositorioMesa = RepositorioMesa()


    def index(self):
        return self.repositorioResultado.findAll()

    """
    Asignacion Candidato y mesa a resultado
    """


    def create(self, infoResultado, id_candidato, id_mesa):
        nuevoResultado = Resultado(infoResultado)
        elCandidato = Candidato(self.repositorioCandidato.findById(id_candidato))
        laMesa = Mesa(self.repositorioMesa.findById(id_mesa))
        nuevoResultado.candidato = elCandidato
        nuevoResultado.laMesa = laMesa
        return self.repositorioResultado.save(nuevoResultado)

    def show(self, id):
        elResultado = Resultado(self.repositorioResultado.findById(id))
        return elResultado.__dict__

    """
    Modificacion de resultados (Candidato y Mesa)
    """

    def update(self, id, infoResultado, id_candidato, id_mesa):
        elResultado = Resultado(self.repositorioResultado.findById(id))
        elResultado.votos = infoResultado["votos"]
        elCandidato = Candidato(self.repositorioCandidato.findById(id_candidato))
        laMesa = Mesa(self.repositorioMesa.findById(id_mesa))
        elResultado.candidato = elCandidato
        elResultado.mesa = laMesa
        return self.repositorioResultado.save(elResultado)

    def delete(self, id):
        return self.repositorioResultado.delete(id)