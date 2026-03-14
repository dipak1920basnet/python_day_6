# Partial Guidance Exercise

# starting a state
def main():
    expenses = [12, 8, 15, 5, 20]
    list_len = len(expenses)

    print_all_expense(expenses)
    print(f"total expense: {total_expensess(expenses, list_len)}")
    print(f"average expense: {average_expense(expenses, list_len)}")
    print(f"largest expense: {largest_expense(expenses, largest_expense)}")



"""

Program must:

1️⃣ print every expense
2️⃣ compute total expense
3️⃣ compute average expense
4️⃣ find largest expense

"""
def print_all_expense(expenses):
    for i in expenses:
        print(i)

def total_expensess(expenses, list_len):
    total_expense = 0
    for i in range(list_len):
        expense= expenses[i]
        if  expense>= 0:
            total_expense += expense
    return total_expense
    
def average_expense(total,list_length):
    return total/list_length

def largest_expense(expense_list, list_len):
    largest = 0
    for i in range(list_len):
        expense = expense_list[i]
        if  expense> largest:
            largest = expense
    return largest


if __name__ == "__main__":
    main()