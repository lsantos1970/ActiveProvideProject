# Interface para a Fábrica Abstrata. Define os métodos necessários
# para criar objetos de ambiente e equipamento.
class ScenarioFactory:
    def create_environment(self):
        raise NotImplementedError("create_environment() deve ser implementado.")

    def create_equipment(self):
        raise NotImplementedError("create_equipment() deve ser implementado.")
