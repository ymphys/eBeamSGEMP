````markdown
# User Idea: Calculate and Plot Time-Dependent EM Field

## Overview
Develop a simulation that **computes the time-dependent electromagnetic field (E and B fields)** for a relativistic charged particle using the provided analytic expressions. Then **plot the field strength vs. time** over a user-specified time window.  
The goal is to create a **fully functional Python-based simulation**, runnable in a single `.py` file, producing a visual plot (Matplotlib) directly in VS Code or any Python environment.

---

## Simulation Requirements

### 1. **Physics Model**
Implement the following field expressions exactly:

\[
E_x=-\frac{e}{4\pi\epsilon_0}\frac{1-\beta^2}{(1-\beta^2\sin^2\theta)^{3/2}}\frac{d}{R^2},\quad 
E_y=0,\quad 
E_z=-\frac{e}{4\pi\epsilon_0}\frac{1-\beta^2}{(1-\beta^2\sin^2\theta)^{3/2}}\frac{v(t-t_0)-z_0}{R^2}
\]

\[
B_x=0,\quad B_y=\frac{v}{c^2}E_x,\quad B_z=0
\]

with definitions:

- \( \beta = \sqrt{1 - 1/\gamma^2} \)
- \( \gamma = \text{Ek}/0.511 + 1 \)
- \( v = \beta C \)
- \( R = \sqrt{d^2 + (v(t - t_0) - z_0)^2} \)
- \( \sin\theta = d / R \)

### 2. **Parameters (with defaults)**
```python
Ek = 10.0    # MeV
d = 1.0      # m
t_0 = -1e9
z_0 = t_0 / C
````

### 3. **Constants**

```python
Q_E = 1.6e-19        # Coulombs
EPSILON_0 = 8.854e-12
PI = 3.141592653589793
M_E = 9.109e-31
C = 3e8
```

---

## Environment & Libraries

### Required Libraries

* **NumPy** for numerical computation
* **Matplotlib** for plotting

### Execution Environment

* Single `.py` file
* Fully runnable in VS Code
* Plot must appear in a pop-up window when executed

---

## Instructions for the Code Generator (LLM)

### 1. Structure the Simulation

* Compute all constants first.
* Create a time array (e.g., using `np.linspace(t_start, t_end, N)`).
* Loop or vectorize evaluation of:

  * (\gamma, \beta, v)
  * (R(t))
  * (\sin\theta(t))
  * Field components (E_x, E_z, B_y)

### 2. Output Quantities

The LLM must compute:

* Full vector fields *(E_x(t), E_y(t), E_z(t))*
* Magnetic field *(B_x(t), B_y(t), B_z(t))*
* Optionally, field magnitude:
  [
  |E(t)| = \sqrt{E_x^2 + E_y^2 + E_z^2}
  ]

### 3. Plotting Requirements

* Plot **field strength vs. time** (choose |E| or a component — clarify in comments).
* Add:

  * Axis labels
  * Title
  * Grid

### 4. Output Format

* A single Python script with:

  * Well-commented code
  * Clear sections: constants, parameters, functions, calculation, plotting
* Should run immediately with no missing dependencies.

### 5. Troubleshooting Notes

Include a comment block such as:

```python
# If the plot window does not appear, confirm that:
# 1. Matplotlib backend is working (try `pip install matplotlib`)
# 2. VS Code "Python: Use System Backend" setting is enabled
# 3. You're running the script, not sending to REPL
```

---

## Final Deliverable

**Generate a complete Python script** that:

1. Takes the above formulas and constants
2. Computes E-field and B-field vs. time
3. Plots the requested field quantity
4. Runs directly in VS Code with zero modification

Use clean function structure and comments to guide users.
