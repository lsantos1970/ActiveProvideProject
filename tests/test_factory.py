import pytest
from abstract_factory.scenario_factory import ScenarioCreator

def test_medical_scenario_creation():
    creator = ScenarioCreator("medical")
    scenario = creator.create_scenario()
    assert "Ambiente médico" in scenario["environment"]
    assert "Avental de Chumbo" in scenario["equipment"]

def test_industrial_scenario_creation():
    creator = ScenarioCreator("industrial")
    scenario = creator.create_scenario()
    assert "Ambiente industrial" in scenario["environment"]
    assert "Fato de proteção" in scenario["equipment"]
