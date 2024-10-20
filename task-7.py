import random
import numpy as np
import matplotlib.pyplot as plt

num_simulations = 100000

sums = np.zeros(11)

for _ in range(num_simulations):
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)
    sum_dice = dice1 + dice2
    sums[sum_dice - 2] += 1

probabilities = sums / num_simulations * 100

sum_values = list(range(2, 13))

analytical_probabilities = [2.78, 5.56, 8.33, 11.11, 13.89, 16.67, 13.89, 11.11, 8.33, 5.56, 2.78]

plt.figure(figsize=(10, 6))
plt.bar(sum_values, probabilities, color='blue', alpha=0.7, label='Метод Монте-Карло')
plt.plot(sum_values, analytical_probabilities, color='red', marker='o', label='Аналітичні імовірності', linewidth=1, markersize=3 )
plt.xlabel('Сума чисел на кубиках')
plt.ylabel('Ймовірність (%)')
plt.title('Ймовірності сум чисел при киданні двох кубиків (Метод Монте-Карло)')
plt.legend()
plt.grid(True)
plt.show()

for i, prob in zip(sum_values, probabilities):
    print(f"Сума: {i}, Ймовірність (Monte Carlo): {prob:.2f}%")
