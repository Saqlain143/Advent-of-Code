def run_part1():
  with open("input.txt", "r") as file:
    lines = file.readlines()
    total_sum = 0
    for line in lines:
      digits = [int(char) for char in line if char.isdigit()]
      number = int(f"{digits[0]}{digits[-1]}")
      total_sum += number
  return total_sum

print(run_part1())
