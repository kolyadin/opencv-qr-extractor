class Optimizer:
    decoded_data = None
    optimizers = []

    def registerOptimizer(self, optimizer):
        self.optimizers.append(optimizer)

    def run(self):
        return len(self.optimizers)
