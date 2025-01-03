from collections import Counter

def calculate_similarity_score(left_list, right_list):
    # Create a frequency counter for the right list
    right_counter = Counter(right_list)
    
    # Initialize the similarity score
    similarity_score = 0
    
    # For each number in the left list, multiply it by its frequency in the right list
    for num in left_list:
        similarity_score += num * right_counter.get(num, 0)  # Use 0 if the number is not in the right list
    
    return similarity_score

def main():
    # Read the input from 'input.txt' file
    with open('/Users/abidshakir/Advent-of-Code/2024/DAY 01/input.txt', 'r') as file:
        lines = file.readlines()

    # Separate the two lists
    left_list = []
    right_list = []

    # Split the lines and populate both lists
    for line in lines:
        left, right = map(int, line.split())
        left_list.append(left)
        right_list.append(right)

    # Calculate and print the similarity score
    similarity_score = calculate_similarity_score(left_list, right_list)
    print(f"Similarity score: {similarity_score}")

if __name__ == "__main__":
    main()