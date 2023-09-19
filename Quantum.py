import qiskit
from controls.circuit_grid import CircuitGrid
class Quantum_control():
    
    
    def __init__(self,circuit_grid):
        self.circuit_grid = circuit_grid
    def select_row(self):
        row_states = []
        simulator = qiskit.BasicAer.get_backend("statevector_simulator")
        circuit = self.circuit_grid.circuit_grid_model.compute_circuit()
        transpiled_circuit = qiskit.transpile(circuit,simulator)
        state_vector = simulator.run(transpiled_circuit, shots = 100).result().get_statevector()
        for basis_state, amp in enumerate(state_vector):
            prob = amp**2
            if prob > 0:
                if basis_state == 3:
                    row_states.append("|11>")
                elif basis_state == 2:
                    row_states.append("|10>")
                elif basis_state == 1:
                    row_states.append("|01>")
                elif basis_state == 0:
                    row_states.append("|00>")
        return row_states
    def select_column(self):
        col_states = []
        simulator = qiskit.BasicAer.get_backend("statevector_simulator")
        circuit = self.circuit_grid.circuit_grid_model.compute_circuit()
        transpiled_circuit = qiskit.transpile(circuit,simulator)
        state_vector = simulator.run(transpiled_circuit, shots = 100).result().get_statevector()
        #print(list(enumerate(state_vector)))
        #[(0, (1+0j)), (1, 0j), (2, 0j), (3, 0j), (4, 0j), (5, 0j), (6, 0j), (7, 0j)]
        for basis_state, amp in enumerate(state_vector):
            prob = amp**2
            if prob > 0:
                if basis_state == 0:
                    col_states.append("|000>")
                elif basis_state == 1:
                    col_states.append("|001>")
                elif basis_state == 2:
                    col_states.append("|010>")
                elif basis_state == 3:
                    col_states.append("|011>")
                elif basis_state == 4:
                    col_states.append("|100>")
                elif basis_state == 5:
                    col_states.append("|101>")
                elif basis_state == 6:
                    col_states.append("|110>")
                elif basis_state == 7:
                    col_states.append("|111>")
        return col_states


                