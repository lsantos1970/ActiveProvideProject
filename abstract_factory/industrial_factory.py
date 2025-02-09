# Implementação concreta da Fábrica para cenários industriais.
# Esta classe cria objetos específicos para ambientes industriais e equipamentos relacionados.

from abstract_factory.industrial_environment import IndustrialEnvironment
from abstract_factory.protective_suit import ProtectiveSuit

class IndustrialFactory:
    def create_environment(self):
        # Cria e retorna um ambiente industrial.
        return IndustrialEnvironment()

    def create_equipment(self):
        # Cria e retorna o equipamento (fato de proteção).
        return ProtectiveSuit()
