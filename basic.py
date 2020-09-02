import operator
import string

# 1. Combine Several Lists
def combine_several_lists():
    first = ['Behind', 'every', 'great', 'man']
    second = ['is', 'a', 'woman']
    third = ['rolling', 'her', 'eyes']
    combine = first + second + third
    print(' '.join(combine))
# combine_several_lists()



# 2. Merge List
def merge_list():
    menus = ["chicken strip", "beef burger", "steakhouse", "mushroom swiss", "whopper"] # List A
    price = [15,10,12,20,30] # List B
    obj = {menus[i]: price[i] for i in range(len(menus))}
    sorted_obj = dict(sorted(obj.items(), key=operator.itemgetter(1)))
    print(sorted_obj)
# merge_list()



# 3. Char Counter
def char_counter(text):
    sym = '*'
    obj = {}   
    for i in text.lower(): 
        if i in obj: 
            obj[i] += '*'
        else:
            obj[i] = '*'
    print(str(obj))
# char_counter("Mammals")
# char_counter("Bruiser build")



# 4. Bubble Sort
def bubble_sort(numbers): 
    n = len(numbers) 
    for i in range(n-1): 
        for j in range(0, n-i-1): 
            if numbers[j] > numbers[j+1]: 
                numbers[j], numbers[j+1] = numbers[j+1], numbers[j]
                print("Step", j+1 , ":", numbers)
numbers = [12,3,5,4,8,9]  
# bubble_sort(numbers)



# 5. Masking
def masking(secret):
    result = ''
    for i in range(len(secret)):
        mask = len(secret) - i > 3
        if mask is not True:
            result += secret[i]
        else:
            result += '*'
    print(result)
secret = "23dn3ir30fd2eddd"
# masking(secret)



# 6. Missing Letter
def missing_letter(miss):
    missing = string.ascii_lowercase if miss[0] == 'a' else string.ascii_uppercase
    for letter in missing[missing.index(miss[0]):]:
        if letter not in miss: return letter[0]
list_letters_first = ["a","b","c","d","e","g","h"]
list_letters_second = ["X","Z"]
# print(f"list_letters_first = {missing_letter(list_letters_first)}")
# print(f"list_letters_second = {missing_letter(list_letters_second)}")



# 7. Sorting Odd Numbers
def sorting_odd_numbers(numbers):
    odds = iter(sorted(i for i in numbers if i % 2))
    print([next(odds) if i % 2 else i for i in numbers])
numbers = [9,4,2,4,1,5,3,0]
# sorting_odd_numbers(numbers)