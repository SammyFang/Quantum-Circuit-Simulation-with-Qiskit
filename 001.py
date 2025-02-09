import numpy as np
import matplotlib as plt
from qiskit import QuantumCircuit, transpile
from qiskit.providers.aer import AerSimulator
from qiskit.visualization import plot_histogram
from matplotlib import pyplot as plt
simulator = AerSimulator()
circuit = QuantumCircuit(4, 4)
circuit.h(0)
circuit.cx(0, 2)
circuit.measure([0,2], [0,2])
circuit.draw('mpl')
plt.show()

compiled_circuit = transpile(circuit, simulator)
job = simulator.run(compiled_circuit, shots=1000)
result = job.result()
counts = result.get_counts(circuit)
print(f"\nTotal count for 00 and 11 are : {counts}\n")
plot_histogram(counts)
plt.show()


