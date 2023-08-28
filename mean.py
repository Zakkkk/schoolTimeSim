import statistics

data = {5:1007,6:2045,7:2907,8:3950,9:4870,10:6209,11:7762,12:9103,13:10628,14:12029,15:14301,16:16429,17:18588,18:20772,19:23034,20:24497,21:26973,22:28818,23:31257,24:33603,25:35517,26:36211,27:36400,28:36866,29:36948,30:37935,31:37077,32:37020,33:36324,34:35910,35:35641,36:33189,37:31502,38:29153,39:27008,40:24789,41:23159,42:20906,43:18674,44:16656,45:14189,46:11943,47:10636,48:9134,49:7712,50:6306,51:4836,52:3892,53:2891,54:1894,55:900}

# Calculate the mean
total = sum(time * freq for time, freq in data.items())
total_freq = sum(data.values())
mean = total / total_freq

# Calculate the median
values_sorted = sorted([time for time, freq in data.items() for _ in range(freq)])
median = statistics.median(values_sorted)

# Calculate the mode
mode = statistics.mode(values_sorted)

# Calculate the standard deviation
std_dev = statistics.stdev(values_sorted)

print("Mean:", mean)
print("Median:", median)
print("Mode:", mode)
print("Standard Deviation:", std_dev)
