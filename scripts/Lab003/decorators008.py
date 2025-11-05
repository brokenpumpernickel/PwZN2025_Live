# class Ising:
#     def calculate_energy(self):
#         self.hamiltonian()

# ising = Ising()

# def hamiltonian():
#     print("Calculating Hamiltonian...")

# ising.hamiltonian = hamiltonian
# ising.calculate_energy()

class Ising:
    def calculate_energy(self):
        self._hamiltonian()

    def hamiltonian(self, func):
        self._hamiltonian = func
        return func
    
ising = Ising()

@ising.hamiltonian
def hamiltonian():
    print("Calculating Hamiltonian...")

ising.calculate_energy()