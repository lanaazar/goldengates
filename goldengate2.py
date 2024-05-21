import qiskit
import numpy as np
from qiskit import QuantumCircuit
from qiskit.transpiler.passes.synthesis import SolovayKitaev
from qiskit.quantum_info import Operator

M1 = np.array([[1, 0],
               [0, 1]])
M2 = (1/np.sqrt(2)) * np.array([[1, 1],
                                 [1j, -1j]])
M3 = (1/np.sqrt(2)) * np.array([[1, -1j],
                                 [1, 1j]])
C_3_matrices = [M1, M2, M3]
print("The C_3 matrix:")
print(C_3_matrices)
C_3_operators = [Operator(matrix) for matrix in C_3_matrices]
circuit = QuantumCircuit(11)
for op in C_3_operators:
    circuit.unitary(op, [0,1,2,3,4,5,6,7,8,9,10], label='C_3')
print("Original circuit:")
print(circuit.draw())
skd = SolovayKitaev(recursion_degree=7)  
discretized = skd(circuit)
print("Discretized circuit:")
print(discretized.draw())
error = np.linalg.norm(Operator(circuit).data - Operator(discretized).data)
print("Error:", error)

T_3 = np.array([[0, np.sqrt(2)], [1 + 1j, 0]])
T_3 = (1/np.sqrt(2)) * T_3
T_3_Operator = Operator(T_3)
circuit2 = QuantumCircuit(5)
circuit2.unitary(Operator(T_3), [0,1,2,3,4], label='T_3')
print("Original circuit:")
print(circuit2.draw())
skd = SolovayKitaev(recursion_degree=3)  
discretized = skd(circuit2)
print("Discretized circuit:")
print(discretized.draw())
error = np.linalg.norm(Operator(circuit2).data - Operator(discretized).data)
print("Error:", error)
