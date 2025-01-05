# Produto abstrato para representar um ambiente.
# As subclasses devem implementar o método get_description().

class Environment:
    def get_description(self):
        raise NotImplementedError("get_description() deve ser implementado.")
