# config_manager.py
class ConfigManager:
    """Classe responsável por gerir as configurações dos cenários"""

    def __init__(self, scenario_type: str, threshold: int, max_time: int, suggested_distance: float):
        self.scenario_type = scenario_type
        self.threshold = threshold
        self.max_time = max_time
        self.suggested_distance = suggested_distance

    def get_config(self):
        """Devolve as configurações do cenário"""
        return {
            "scenario_type": self.scenario_type,
            "radiation_threshold": self.threshold,
            "max_time": self.max_time,
            "suggested_distance": self.suggested_distance
        }
