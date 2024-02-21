import random
def count_my_numbers(input_array:list[int]) -> dict:
    my_counts:dict = {}
    for number in input_array:
        try:
            my_counts[number] = my_counts[number] + 1
        except KeyError:
            my_counts[number] = 1
    return my_counts


my_array:list[int] = []
for i in range(100):
    my_array.append(random.randint(1,101))    

print(count_my_numbers(my_array))