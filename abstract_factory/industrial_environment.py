# Implementação concreta do ambiente industrial.
# Fornece uma descrição específica do ambiente industrial.

from abstract_factory.environment import Environment

class IndustrialEnvironment(Environment):
    def get_description(self):
        # Retorna uma descrição do ambiente industrial.
        return "Ambiente industrial com equipamentos de radioproteção."
