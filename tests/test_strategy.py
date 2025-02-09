import pytest
from strategy.analysis_context import AnalysisContext
from strategy.medical_strategy import MedicalAnalysisStrategy
from strategy.industrial_strategy import IndustrialAnalysisStrategy

def test_medical_analysis_strategy():
    strategy = MedicalAnalysisStrategy()
    context = AnalysisContext()
    context.set_strategy(strategy)
    data = [10, 20, 30]
    result = context.execute_analysis(data)
    assert result == {"average_time": 20.0, "exceeded_limit_count": 0}

def test_industrial_analysis_strategy():
    strategy = IndustrialAnalysisStrategy()
    context = AnalysisContext()
    context.set_strategy(strategy)
    data = [5.5, 7.2, 10.8]
    result = context.execute_analysis(data)
    assert result == {"average_distance": 7.833333333333333, "max_time": 10.8}
