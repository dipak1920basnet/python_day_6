scores = [72, 85, 90, 66, 78]

for score in scores:
    print(score)

total = 0

for score in scores:
    total = total + score

average = total / len(scores)

print("Total:", total)
print("Average:", average)

highest = scores[0]

for score in scores:
    if score > highest:
        highest = score