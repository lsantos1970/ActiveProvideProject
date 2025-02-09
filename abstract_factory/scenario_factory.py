from abc import ABC, abstractmethod

class ScenarioFactory(ABC):
    """Classe abstrata para criação de cenários"""

    @abstractmethod
    def create_environment(self):
        pass

    @abstractmethod
    def create_equipment(self):
        pass

class ScenarioCreator:
    """Classe responsável por criar cenários médicos ou industriais dinamicamente"""

    def __init__(self, scenario_type):
        # Importação local para evitar importação cíclica
        if scenario_type == "medical":
            from abstract_factory.medical_factory import MedicalFactory
            self.factory = MedicalFactory()
        elif scenario_type == "industrial":
            from abstract_factory.industrial_factory import IndustrialFactory
            self.factory = IndustrialFactory()
        else:
            raise ValueError("Tipo de cenário inválido")

    def create_scenario(self):
        """Cria o ambiente e o equipamento do cenário"""
        environment = self.factory.create_environment()
        equipment = self.factory.create_equipment()
        return {
            "environment": environment.get_description(),
            "equipment": equipment.operate()
        }
