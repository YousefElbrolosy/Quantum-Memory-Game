import qiskit
import numpy as np
from controls.circuit_grid import CircuitGrid
class Quantum_control():
    
    def __init__(self,circuit_grid):
        self.circuit_grid = circuit_grid
        self.superpositon_flag_2 = False
        self.superpositon_flag_3 = False
        self.prob_2 = []
        self.prob_3 = []
        self.state_vector_2 = []
        self.state_vector_3 = []
    def select_row(self):
        row_states = []
        simulator = qiskit.BasicAer.get_backend("statevector_simulator")
        circuit = self.circuit_grid.circuit_grid_model.compute_circuit()
        transpiled_circuit = qiskit.transpile(circuit,simulator)
        state_vector = simulator.run(transpiled_circuit, shots = 100).result().get_statevector()
        #print("row state_vector is", list(enumerate(state_vector)))
        for basis_state, amp in enumerate(state_vector):
            if np.imag(amp) == 0:    
                prob = np.real(amp**2)
            else:
                prob = np.abs(amp)
            if prob > 0:
                self.prob_2.append(prob)
                if basis_state == 3:
                    row_states.append("|11>")
                elif basis_state == 2:
                    row_states.append("|10>")
                elif basis_state == 1:
                    row_states.append("|01>")
                elif basis_state == 0:
                    row_states.append("|00>")
                if prob == 1:
                    self.superpositon_flag_2 = False
                else:
                    self.superpositon_flag_2 = True
        #print(self.all_prob_2)

        self.state_vector_2 = list(state_vector)
        #print("state_vector_2 now is: " + str(self.state_vector_2))
        return row_states
    def select_column(self):
        col_states = []
        simulator = qiskit.BasicAer.get_backend("statevector_simulator")
        circuit = self.circuit_grid.circuit_grid_model.compute_circuit()
        transpiled_circuit = qiskit.transpile(circuit,simulator)
        state_vector = simulator.run(transpiled_circuit, shots = 100).result().get_statevector()
        #print("column state_vector is", list(enumerate(state_vector)))
        #[(0, (1+0j)), (1, 0j), (2, 0j), (3, 0j), (4, 0j), (5, 0j), (6, 0j), (7, 0j)]
        for basis_state, amp in enumerate(state_vector):
            prob = np.abs(amp)
            if prob > 0:
                self.prob_3.append(prob)
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
                if prob == 1:
                    self.superpositon_flag_3 = False
                else:
                    self.superpositon_flag_3 = True
        self.state_vector_3 = list(state_vector)
        #print("state_vector_3 now is:" + str(self.state_vector_3))
        return col_states

    def main():
        ket0 = [[0.4999999999999999+0j],[0j],[0j] , [0.4999999999999999+0j], [0j] , [ 0.4999999999999999+0j] , [0.4999999999999999+0j] ,[0j]]
        bra0 = [0.4999999999999999+0j,0j,0j , 0.4999999999999999+0j, 0j, 0.4999999999999999+0j , 0.4999999999999999+0j ,0j]
        density_matrix = np.outer(bra0,ket0)
        print(density_matrix)
        for i in range(8):
            for j in range(8):
                if i != j and density_matrix[i][j] != 0:
                    entangled = True
                    break

        # Determine if the state is entangled
        if entangled:
            print("The state is entangled.")
        else:
            print("The state is separable.")
                # Print the density matrix
        
        # Assuming you have the density matrix calculated and stored in 'density_matrix'

        # Initialize a list to store entangled states
        entangled_states = []

        # Iterate through the density matrix to find non-zero off-diagonal elements
        for i in range(8):
            for j in range(8):
                if i != j and density_matrix[i][j] != 0:
                    entangled_states.append((i, j))

        # Print the list of entangled states
        print("Entangled states:")
        for state_pair in entangled_states:
            print(f"|{state_pair[0]}> is entangled with |{state_pair[1]}>")
    if __name__ == '__main__':
        main()            