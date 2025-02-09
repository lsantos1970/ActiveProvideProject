import pytest
from abstract_factory.scenario_factory import ScenarioCreator

# Teste para a criação de um cenário médico
def test_medical_scenario_creation():
    """
    Testa a criação de um cenário médico utilizando o ScenarioCreator.
    Verifica se o ambiente e o equipamento criados correspondem ao contexto médico.
    """
    creator = ScenarioCreator("medical")  # Inicializa o criador de cenários com tipo "medical"
    scenario = creator.create_scenario()  # Cria o cenário
    assert "Ambiente médico" in scenario["environment"]  # Verifica a descrição do ambiente
    assert "Avental de Chumbo" in scenario["equipment"]  # Verifica o equipamento criado

# Teste para a criação de um cenário industrial
def test_industrial_scenario_creation():
    """
    Testa a criação de um cenário industrial utilizando o ScenarioCreator.
    Verifica se o ambiente e o equipamento criados correspondem ao contexto industrial.
    """
    creator = ScenarioCreator("industrial")  # Inicializa o criador de cenários com tipo "industrial"
    scenario = creator.create_scenario()  # Cria o cenário
    assert "Ambiente industrial" in scenario["environment"]  # Verifica a descrição do ambiente
    assert "Fato de proteção" in scenario["equipment"]  # Verifica o equipamento criado
