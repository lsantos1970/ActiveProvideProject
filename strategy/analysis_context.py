# strategy/analysis_context.py
from strategy.medical_strategy import MedicalAnalysisStrategy
from strategy.industrial_strategy import IndustrialAnalysisStrategy
from typing import List, Dict

class AnalysisContext:
    """Contexto que utiliza a estratégia para realizar o cálculo."""
    def __init__(self):
        self._strategy = None

    def set_strategy(self, strategy) -> None:
        """Define a estratégia a ser usada."""
        self._strategy = strategy

    def execute_analysis(self, data: List[float]) -> Dict[str, float]:
        """Executa a análise usando a estratégia definida."""
        if not self._strategy:
            raise ValueError("Nenhuma estratégia foi definida!")
        return self._strategy.calculate(data)
