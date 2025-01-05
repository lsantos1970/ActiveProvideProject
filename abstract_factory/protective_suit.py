# Implementação concreta do equipamento: fato de proteção.
# Define o comportamento do equipamento no cenário industrial.

from abstract_factory.equipment import Equipment

class ProtectiveSuit(Equipment):
    def operate(self):
        # Retorna a ação realizada pelo fato de proteção.
        return "Fato de proteção em uso."
