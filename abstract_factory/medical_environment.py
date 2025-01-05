# Implementação concreta do ambiente médico.
# Fornece uma descrição específica do ambiente médico.

from abstract_factory.environment import Environment

class MedicalEnvironment(Environment):
    def get_description(self):
        # Retorna uma descrição do ambiente médico.
        return "Ambiente médico configurado para radiologia."
