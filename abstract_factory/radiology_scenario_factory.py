# radiology_scenario_factory.py

# Importação das classes específicas para os cenários médicos e industriais
from medical_products import MedicalEnvironment, XRayMachine, AdjustRadiationExposure
from industrial_products import IndustrialEnvironment, ProtectiveSuit, MonitorRadiationLevels

# Classe abstrata base para a fábrica de cenários radiológicos
class RadiologyScenarioFactory:
    """
    Classe base abstrata para criação de diferentes cenários radiológicos.
    Define os métodos que devem ser implementados pelas fábricas concretas.
    """
    def create_environment(self):
        """
        Método abstrato para criar o ambiente específico do cenário.
        Deve ser implementado nas subclasses.
        """
        pass

    def create_equipment(self):
        """
        Método abstrato para criar o equipamento específico do cenário.
        Deve ser implementado nas subclasses.
        """
        pass

    def create_task(self):
        """
        Método abstrato para criar a tarefa específica do cenário.
        Deve ser implementado nas subclasses.
        """
        pass

# Fábrica concreta para cenários médicos
class MedicalScenarioFactory(RadiologyScenarioFactory):
    """
    Classe concreta que implementa a fábrica para cenários médicos.
    Responsável por criar os componentes específicos do ambiente médico.
    """
    def create_environment(self):
        """
        Cria e retorna o ambiente médico.
        """
        return MedicalEnvironment()

    def create_equipment(self):
        """
        Cria e retorna o equipamento médico (máquina de raio-X).
        """
        return XRayMachine()

    def create_task(self):
        """
        Cria e retorna a tarefa médica (ajustar a exposição à radiação).
        """
        return AdjustRadiationExposure()

# Fábrica concreta para cenários industriais
class IndustrialScenarioFactory(RadiologyScenarioFactory):
    """
    Classe concreta que implementa a fábrica para cenários industriais.
    Responsável por criar os componentes específicos do ambiente industrial.
    """
    def create_environment(self):
        """
        Cria e retorna o ambiente industrial.
        """
        return IndustrialEnvironment()

    def create_equipment(self):
        """
        Cria e retorna o equipamento industrial (traje de proteção).
        """
        return ProtectiveSuit()

    def create_task(self):
        """
        Cria e retorna a tarefa industrial (monitorar níveis de radiação).
        """
        return MonitorRadiationLevels()
