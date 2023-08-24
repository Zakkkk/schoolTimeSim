import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

# Given data points (with quotations)
data = {
    "0": 0, "1": 0, "2": 0, "3": 0, "4": 0, "5": 316, "6": 892, "7": 1758, "8": 2911, "9": 4361, "10": 6243, "11": 8602, "12": 11305, "13": 14476, "14": 18049,
    "15": 22273, "16": 27300, "17": 32875, "18": 39138, "19": 46106, "20": 53530, "21": 61715, "22": 70453, "23": 79827,
    "24": 89777, "25": 100358, "26": 111154, "27": 122113, "28": 133108, "29": 144254, "30": 155605, "31": 166823,
    "32": 178001, "33": 188875, "34": 199576, "35": 210171, "36": 220277, "37": 229602, "38": 238325, "39": 246481,
    "40": 253917, "41": 260865, "42": 267163, "43": 272703, "44": 277488, "45": 281772, "46": 285401, "47": 288572,
    "48": 291300, "49": 293691, "50": 295543, "51": 297068, "52": 298228, "53": 299114, "54": 299690, "55": 300000, "56": 300000, "57": 300000, "58":300000, "59": 300000, "60": 300000
}

# Extract x and y data from the dictionary
x_data = np.array(list(map(int, data.keys())))
y_data = np.array(list(data.values()))

# Define the model function
def model(x, A, k, r):
    return A / (1 + k * np.exp(-r * x))

# Perform curve fitting with initial parameter guesses
initial_guess = (300000, 125, 0.164)  # Initial guesses for A, k, and r
params, covariance = curve_fit(model, x_data, y_data, p0=initial_guess, maxfev=10000)

# Estimated parameters
A_est, k_est, r_est = params

# Generate y values for the fitted model
y_estimated = model(x_data, A_est, k_est, r_est)

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
print(f"Estimated k: {k_est}")
print(f"Estimated r: {r_est}")