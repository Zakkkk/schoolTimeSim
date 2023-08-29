import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

# Given data points (with quotations)
data = {
    "0": 150, "30": 1700, "60": 1000, "90": 550, "120": 300
}

# Extract x and y data from the dictionary
x_data = np.array(list(map(int, data.keys())))
y_data = np.array(list(data.values()))

# Define the model function
def model(x, A, b, c):
    return A * x**b * np.exp(-c * x)

# Perform curve fitting with initial parameter guesses
initial_guess = (0.05, 4, 0.1)  # Initial guesses for A, k, and r
params, covariance = curve_fit(model, x_data, y_data, p0=initial_guess, maxfev=10000)

# Estimated parameters
A_est, b_est, c_est = params

# Generate y values for the fitted model
y_estimated = model(x_data, A_est, b_est, c_est)

# Plot the original data and the estimated model
plt.figure(figsize=(10, 6))
plt.scatter(x_data, y_data, label='Data Points', color='blue', marker='o')
plt.plot(x_data, y_estimated, label='Estimated Model', color='red', linestyle='--')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.title('Data Points and Estimated Model')
plt.grid(True)
plt.show()

# Output estimated parameters
print(f"Estimated A: {A_est}")
print(f"Estimated b: {b_est}")
print(f"Estimated c: {c_est}")