import qiskit
import numpy as np
from qiskit import QuantumCircuit
from qiskit.transpiler.passes.synthesis import SolovayKitaev
from qiskit.quantum_info import Operator

matrix1 = np.array([[1j, 0],
                    [0, -1j]])
matrix2 = np.array([[0, 1],
                    [-1, 0]])
# Print the matrices
print("Matrix 1:")
print(matrix1)
print("\nMatrix 2:")
print(matrix2)

C_4_matrices = [matrix1, matrix2]
C_4_operators = [Operator(matrix) for matrix in C_4_matrices]
circuit = QuantumCircuit(2)
for op in C_4_operators:
    circuit.unitary(op, [0,1], label='C_4')
print("Original circuit:")
print(circuit.draw())
skd = SolovayKitaev(recursion_degree=3)  
discretized = skd(circuit)
print("Discretized circuit:")
print(discretized.draw())
error = np.linalg.norm(Operator(circuit).data - Operator(discretized).data)
print("Error:", error)

T_4 = np.array([[1, 1 - 1j], [1 + 1j, -1]])
T_4 = (1/np.sqrt(3))*T_4
T_4_Operator = Operator(T_4)
circuit2 = QuantumCircuit(2)
circuit2.unitary(Operator(T_4), [0,1], label='T_4')
print("Original circuit:")
print(circuit2.draw())
skd = SolovayKitaev(recursion_degree=3)  
discretized = skd(circuit2)
print("Discretized circuit:")
print(discretized.draw())
error = np.linalg.norm(Operator(circuit2).data - Operator(discretized).data)
print("Error:", error)
