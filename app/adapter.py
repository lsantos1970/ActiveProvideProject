class RESTToFactoryAdapter:
    """
    Adapter para traduzir solicitações HTTP do servidor REST para chamadas ao Abstract Factory.
    """
    def __init__(self, factory):
        self.factory = factory

    def process_request(self, data):
        """
        Processa a solicitação e usa a factory para criar o ambiente e o equipamento.
        """
        environment = self.factory.create_environment()
        equipment = self.factory.create_equipment()
        return {
            "environment_description": environment.get_description(),
            "equipment_operation": equipment.operate()
        }
