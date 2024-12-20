# Read the input from the file 'input.txt'
with open('/Users/abidshakir/Advent-of-Code/2024/DAY 02/input.txt', 'r') as file:
    lines = file.readlines()

# Function to check if a report is safe (Part One)
def is_safe_report(report):
    # Convert the report to a list of integers
    levels = list(map(int, report.split()))
    
    # Check the differences between adjacent levels
    differences = [abs(levels[i] - levels[i+1]) for i in range(len(levels) - 1)]
    
    # Condition 1: Check if all differences are between 1 and 3 (inclusive)
    if any(d < 1 or d > 3 for d in differences):
        return False
    
    # Condition 2: Check if the report is either strictly increasing or strictly decreasing
    is_increasing = all(levels[i] < levels[i+1] for i in range(len(levels) - 1))
    is_decreasing = all(levels[i] > levels[i+1] for i in range(len(levels) - 1))
    
    # The report is safe if it is either strictly increasing or strictly decreasing
    return is_increasing or is_decreasing

# Function to check if a report can be made safe by removing one level (Part Two)
def can_be_safe_by_removing_one(report):
    levels = list(map(int, report.split()))
    
    # Try removing one element at a time and check if the resulting sequence is safe
    for i in range(len(levels)):
        modified_report = levels[:i] + levels[i+1:]  # Remove the i-th level
        if is_safe_report(' '.join(map(str, modified_report))):
            return True
    return False

# Count safe reports (either naturally safe or safe by removing one bad level)
safe_report_count_part_one = 0
safe_report_count_part_two = 0

for line in lines:
    stripped_line = line.strip()
    
    # Part One: Check if the report is safe
    if is_safe_report(stripped_line):
        safe_report_count_part_one += 1
    
    # Part Two: Check if the report is safe, either naturally or by removing one level
    if is_safe_report(stripped_line) or can_be_safe_by_removing_one(stripped_line):
        safe_report_count_part_two += 1

# Output the results for both parts
print(f"Number of safe reports (Part One): {safe_report_count_part_one}")
print(f"Number of safe reports (Part Two): {safe_report_count_part_two}")
