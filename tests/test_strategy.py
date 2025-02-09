import pytest
from strategy.analysis_context import AnalysisContext
from strategy.medical_strategy import MedicalAnalysisStrategy
from strategy.industrial_strategy import IndustrialAnalysisStrategy

# Teste para a estratégia de análise médica
def test_medical_analysis_strategy():
    """
    Testa a estratégia de análise médica utilizando o AnalysisContext.
    Verifica se os cálculos de tempo médio e contagem de excedências de limite estão corretos.
    """
    strategy = MedicalAnalysisStrategy()  # Inicializa a estratégia médica
    context = AnalysisContext()  # Cria o contexto de análise
    context.set_strategy(strategy)  # Define a estratégia no contexto
    data = [10, 20, 30]  # Dados simulados para análise
    result = context.execute_analysis(data)  # Executa a análise com os dados fornecidos
    assert result == {"average_time": 20.0, "exceeded_limit_count": 0}  # Verifica o resultado

# Teste para a estratégia de análise industrial
def test_industrial_analysis_strategy():
    """
    Testa a estratégia de análise industrial utilizando o AnalysisContext.
    Verifica se os cálculos de distância média e tempo máximo estão corretos.
    """
    strategy = IndustrialAnalysisStrategy()  # Inicializa a estratégia industrial
    context = AnalysisContext()  # Cria o contexto de análise
    context.set_strategy(strategy)  # Define a estratégia no contexto
    data = [5.5, 7.2, 10.8]  # Dados simulados para análise
    result = context.execute_analysis(data)  # Executa a análise com os dados fornecidos
    assert result == {"average_distance": 7.833333333333333, "max_time": 10.8}  # Verifica o resultado

