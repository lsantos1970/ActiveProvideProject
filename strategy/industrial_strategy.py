# strategy/industrial_strategy.py
from typing import List, Dict

class IndustrialAnalysisStrategy:
    """Estratégia para calcular análises no cenário industrial."""
    def calculate(self, data: List[float]) -> Dict[str, float]:
        avg_distance = sum(data) / len(data)
        max_time = max(data)
        return {
            "average_distance": avg_distance,
            "max_time": max_time
        }
