morning_temp = float(input())
day_temp = float(input())
evening_temp = float(input())
temperatures = (morning_temp, day_temp, evening_temp)
average_temp = (temperatures[0] + temperatures[1] + temperatures[2]) / 3
print(f"{average_temp:.2f}")
