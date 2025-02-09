# scenario_factory.py

# Importação da biblioteca abc para definir classes e métodos abstratos
from abc import ABC, abstractmethod

# Classe base abstrata para criação de cenários
class ScenarioFactory(ABC):
    """
    Classe abstrata que define a interface para as fábricas de cenários.
    Obriga as subclasses a implementar os métodos para criar o ambiente
    e o equipamento específicos do cenário.
    """

    @abstractmethod
    def create_environment(self):
        """
        Método abstrato para criar o ambiente do cenário.
        Deve ser implementado pelas subclasses.
        """
        pass

    @abstractmethod
    def create_equipment(self):
        """
        Método abstrato para criar o equipamento do cenário.
        Deve ser implementado pelas subclasses.
        """
        pass

# Classe responsável por criar cenários dinamicamente
class ScenarioCreator:
    """
    Classe responsável por instanciar a fábrica apropriada (médica ou industrial)
    com base no tipo de cenário fornecido. Usa a fábrica para criar o ambiente
    e o equipamento específicos do cenário.
    """

    def __init__(self, scenario_type):
        """
        Inicializa o criador do cenário com o tipo especificado (médico ou industrial).
        Importações locais são utilizadas para evitar importação cíclica.
        
        Args:
            scenario_type (str): Tipo de cenário ('medical' ou 'industrial').
        
        Raises:
            ValueError: Se o tipo de cenário for inválido.
        """
        if scenario_type == "medical":
            from abstract_factory.medical_factory import MedicalFactory
            self.factory = MedicalFactory()
        elif scenario_type == "industrial":
            from abstract_factory.industrial_factory import IndustrialFactory
            self.factory = IndustrialFactory()
        else:
            raise ValueError("Tipo de cenário inválido")

    def create_scenario(self):
        """
        Usa a fábrica selecionada para criar o ambiente e o equipamento
        do cenário e retorna uma descrição dos componentes criados.

        Returns:
            dict: Dicionário contendo as descrições do ambiente e do equipamento.
        """
        # Criação do ambiente através da fábrica
        environment = self.factory.create_environment()
        # Criação do equipamento através da fábrica
        equipment = self.factory.create_equipment()
        # Retorna as descrições do ambiente e do equipamento criados
        return {
            "environment": environment.get_description(),
            "equipment": equipment.operate()
        }
