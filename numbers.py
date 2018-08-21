list_of_numbers = []
for i in range(5):
    numbers = int(input("number: "))
    list_of_numbers.append(numbers)

print("the first number is {}".format(list_of_numbers[0]))
print("the last number is ", list_of_numbers[-1])
print("the smallest number is ", min(list_of_numbers))
print("the biggest number is ", max(list_of_numbers))
print("the average is ", sum(list_of_numbers) / len(list_of_numbers))
