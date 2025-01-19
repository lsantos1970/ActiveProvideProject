# strategy/medical_strategy.py
from typing import List, Dict

class MedicalAnalysisStrategy:
    """Estratégia para calcular análises no cenário médico."""
    def calculate(self, data: List[float]) -> Dict[str, float]:
        avg_time = sum(data) / len(data)
        exceeded_limit = sum(1 for d in data if d > 50)
        return {
            "average_time": avg_time,
            "exceeded_limit_count": exceeded_limit
        }
