# Implementação concreta da Fábrica para cenários médicos.
# Esta classe cria objetos específicos para ambientes médicos e equipamentos relacionados.

from abstract_factory.scenario_factory import ScenarioFactory
from abstract_factory.medical_environment import MedicalEnvironment
from abstract_factory.lead_apron import LeadApron


class MedicalFactory(ScenarioFactory):
    def create_environment(self):
        # Cria e retorna um ambiente médico.
        return MedicalEnvironment()

    def create_equipment(self):
        # Cria e retorna o equipamento (avental de chumbo).
        return LeadApron()
