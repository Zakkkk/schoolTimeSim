import statistics

data = {
    "5": 1007, "6": 2045, "7": 2907, "8": 3950, "9": 4870, "10": 6209, "11": 7762,
    "12": 9103, "13": 10628, "14": 12029, "15": 14301, "16": 16429, "17": 18588,
    "18": 20772, "19": 23034, "20": 24497, "21": 26973, "22": 28818, "23": 31257,
    "24": 33603, "25": 35517, "26": 36211, "27": 36400, "28": 36866, "29": 36948,
    "30": 37935, "31": 37077, "32": 37020, "33": 36324, "34": 35910, "35": 35641,
    "36": 33189, "37": 31502, "38": 29153, "39": 27008, "40": 24789, "41": 23159,
    "42": 20906, "43": 18674, "44": 16656, "45": 14189, "46": 11943, "47": 10636,
    "48": 9134, "49": 7712, "50": 6306, "51": 4836, "52": 3892, "53": 2891, "54": 1894,
    "55": 900
}

# Extract the values from the data dictionary
values = list(data.values())

# Calculate mean, median, and standard deviation
mean = statistics.mean(values)
median = statistics.median(values)
std_dev = statistics.stdev(values)

# Print the results
print(f"Mean: {mean}")
print(f"Median: {median}")
print(f"Standard Deviation: {std_dev}")