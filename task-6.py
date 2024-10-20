items = {
    "pizza": {"cost": 50, "calories": 300},
    "hamburger": {"cost": 40, "calories": 250},
    "hot-dog": {"cost": 30, "calories": 200},
    "pepsi": {"cost": 10, "calories": 100},
    "cola": {"cost": 15, "calories": 220},
    "potato": {"cost": 25, "calories": 350}
}

# Жадібний алгоритм
def greedy_algorithm(items, budget):
    # Сортуємо страви за спаданням співвідношення калорій до вартості
    sorted_items = sorted(items.items(), key=lambda x: x[1]['calories'] / x[1]['cost'], reverse=True)
    total_calories = 0
    selected_items = []

    for item, info in sorted_items:
        if budget >= info['cost']:
            selected_items.append(item)
            total_calories += info['calories']
            budget -= info['cost']

    return selected_items, total_calories

# Динамічне програмування (Knapsack problem)
def dynamic_programming(items, budget):
    n = len(items)
    item_list = list(items.items())

    # Створюємо таблицю для динамічного програмування
    dp = [[0 for _ in range(budget + 1)] for _ in range(n + 1)]

    # Заповнюємо таблицю
    for i in range(1, n + 1):
        name, info = item_list[i - 1]
        cost = info['cost']
        calories = info['calories']

        for w in range(budget + 1):
            if cost <= w:
                dp[i][w] = max(dp[i - 1][w], dp[i - 1][w - cost] + calories)
            else:
                dp[i][w] = dp[i - 1][w]

    # Тепер потрібно знайти, які страви були обрані
    selected_items = []
    w = budget
    total_calories = dp[n][budget]

    for i in range(n, 0, -1):
        if dp[i][w] != dp[i - 1][w]:
            name = item_list[i - 1][0]
            selected_items.append(name)
            w -= items[name]['cost']

    return selected_items, total_calories

# Приклад використання
budget = 100

# Використання жадібного алгоритму
selected_items_greedy, total_calories_greedy = greedy_algorithm(items, budget)
print("Жадібний алгоритм:")
print("Обрані страви:", selected_items_greedy)
print("Загальна кількість калорій:", total_calories_greedy)

# Використання алгоритму динамічного програмування
selected_items_dp, total_calories_dp = dynamic_programming(items, budget)
print("\nДинамічне програмування:")
print("Обрані страви:", selected_items_dp)
print("Загальна кількість калорій:", total_calories_dp)
