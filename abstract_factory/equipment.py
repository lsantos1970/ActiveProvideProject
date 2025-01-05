# Produto abstrato para representar um equipamento.
# As subclasses devem implementar o método operate().

class Equipment:
    def operate(self):
        raise NotImplementedError("operate() deve ser implementado.")
