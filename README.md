# 🧑‍💻 Quantum Circuit Simulation with Qiskit

## 📌 Project Overview  
This project demonstrates how to build and simulate **quantum circuits** using **Qiskit** and the **IBM Qiskit Aer Simulator**. The implementation includes a simple quantum **entanglement circuit**, where a qubit undergoes a **Hadamard gate** and is then entangled with another qubit via a **CNOT gate**. The results are visualized using **matplotlib**.

---
## 🚀 Installation & Execution

### 1️⃣ Install Dependencies  
Ensure that Python 3 is installed, then install the required packages:  
```bash
pip install qiskit matplotlib
```

### 2️⃣ Run the Script
Execute the Python script:

bash python 001.py
After running the script, you will see both the quantum circuit diagram and the measurement result histogram.

## 📊 Execution Results  

### 1️⃣ Quantum Circuit Diagram  

### 2️⃣ Measurement Result Histogram  

The measurement results indicate that **q0 and q2 are entangled**, following quantum entanglement principles. Ideally, their states should be equally distributed between `00` and `11`, which aligns with the simulated results.  

---

## 🔥 Future Enhancements  
- ✅ **Increase qubit count** - Extend the circuit to include more qubits  
- ✅ **Experiment with additional quantum gates** - Implement T-gate, SWAP gate, etc.  
- ✅ **Run on real IBM Quantum hardware** - Deploy the circuit on actual quantum computers  
- ✅ **Develop a Web Dashboard** - Visualize results using Flask or Dash  

---

## 🎯 Technologies Used  
- **Qiskit** - IBM’s quantum computing framework  
- **Matplotlib** - Used for quantum circuit and result visualization  
- **Python 3** - Main programming language  

---

## 🎓 References  
- [Qiskit Official Documentation](https://qiskit.org/documentation/)  
- [IBM Quantum Experience](https://quantum-computing.ibm.com/)  
