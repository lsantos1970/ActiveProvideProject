# Implementação concreta do equipamento: avental de chumbo.
# Define o comportamento do equipamento no cenário médico.

from abstract_factory.equipment import Equipment

class LeadApron(Equipment):
    def operate(self):
        # Retorna a ação realizada pelo avental de chumbo.
        return "Avental de Chumbo em uso."
