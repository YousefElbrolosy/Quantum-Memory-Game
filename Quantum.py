import qiskit
from controls.circuit_grid import CircuitGrid
class Quantum_control():
    def __init__(self,circuit_grid):
        self.circuit_grid = circuit_grid
    def select_row(self):
        simulator = qiskit.BasicAer.get_backend("statevector_simulator")
        circuit = self.circuit_grid.circuit_grid_model.compute_circuit()
        transpiled_circuit = qiskit.transpile(circuit,simulator)
        state_vector = simulator.run(transpiled_circuit, shots = 100).result().get_statevector()
        for basis_state, amp in enumerate(state_vector):
            prob = amp**2
            if prob == 1:
                if basis_state == 3:
                    return "|11>"
                elif basis_state == 2:
                    return "|10>"
                elif basis_state == 1:
                    return "|01>"
                elif basis_state == 0:
                    return "|00>"
    def select_column(self):
        simulator = qiskit.BasicAer.get_backend("statevector_simulator")
        circuit = self.circuit_grid.circuit_grid_model.compute_circuit()
        transpiled_circuit = qiskit.transpile(circuit,simulator)
        state_vector = simulator.run(transpiled_circuit, shots = 100).result().get_statevector()
        for basis_state, amp in enumerate(state_vector):
            prob = amp**2
            if prob == 1:
                if basis_state == 0:
                    return "|000>"
                elif basis_state == 1:
                    return "|001>"
                elif basis_state == 2:
                    return "|010>"
                elif basis_state == 3:
                    return "|011>"
                elif basis_state == 4:
                    return "|100>"
                elif basis_state == 5:
                    return "|101>"
                elif basis_state == 6:
                    return "|110>"
                elif basis_state == 7:
                    return "|111>"
                