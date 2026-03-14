def main():
    scores = [91, 82, 75, 68, 95, 88, 73]
    A,B,C,D = count_grade(scores)
    print(f"A: {A}")
    print(f"B: {B}")
    print(f"C: {C}")
    print(f"Below 70: {D}")s

def count_grade(scores):
    A = 0
    B = 0
    C = 0
    D = 0
    for i in scores:
        if i >= 90:
            A += 1
        elif i >= 80:
            B += 1
        elif i >= 70:
            C += 1
        else:
            D += 1

if __name__ == "__main__":
    main()