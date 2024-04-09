import matplotlib.pyplot as plt

# Values of X
X = [1, 3, 5, 9, 11]

# Probabilities
p = [0.15, 0.3, 0.2, 0.1, 0.25]

# Calculate cumulative probabilities
cumulative_prob = [0] * len(X)
cumulative_prob[0] = p[0]
for i in range(1, len(X)):
    cumulative_prob[i] = cumulative_prob[i - 1] + p[i]

# Plotting the integral function
plt.step(X, cumulative_prob, where='post', label='F(x)')
plt.xlabel('X')
plt.ylabel('F(x)')
plt.title('Integral Function of the Random Variable X')
plt.xticks(X)
plt.yticks(cumulative_prob)
plt.grid(True)
plt.legend()
plt.show()
