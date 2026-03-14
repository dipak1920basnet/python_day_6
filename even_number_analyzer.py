def main():
    numbers = [3, 8, 11, 14, 7, 20, 5]
    print(f"total even numbers: {get_total_even_numbers(numbers)}")
    print(f"sum of even numbers: {even_sum(numbers)}")
    print_even(numbers)
    
def get_total_even_numbers(numbers):
    total_even = 0
    for i in numbers:
        if i % 2 == 0:
            total_even += 1
    return total_even

def even_sum(numbers):
    total_even_sum = 0
    for i in numbers:
        if i % 2 == 0:
            total_even_sum += i
    return total_even_sum

def print_even(numbers):
    for i in numbers:
        if i % 2 == 0:
            print(i)
if __name__ == "__main__":
    main()