import matplotlib.pyplot as plt

def fib(n):
    seq = [0, 1]
    for _ in range(n-2):
        seq.append(seq[-1] + seq[-2])
    return seq

data = fib(10)
plt.plot(data, marker='o')
plt.title("Fibonacci Sequence")
plt.grid()
plt.show()

