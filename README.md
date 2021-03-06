# Task: Python Basic

### 1. Combine several Lists

- [x] Combine all elements inside this List into readable sentence.

first = ['Behind', 'every', 'great', 'man']
second = ['is', 'a', 'woman']
third = ['rolling', 'her', 'eyes']

```python
first = ['Behind', 'every', 'great', 'man']
second = ['is', 'a', 'woman']
third = ['rolling', 'her', 'eyes']
```

Expexted Output :

```bash
Behind every great man is a woman rolling her eyes
```

### 2. Merge List

- [x] There a 2 list with ordered element of each other. Combine these 2 lists into a dictionary, list A is the key, and list B is the value. Then sort the dictionary by value in descending order.

```python
menus = ["chicken strip", "beef burger", "steakhouse", "mushroom swiss", "whopper"] # List A
price = [15,10,12,20,30] # List B
```

Expected output :

```bash
{"beef burger" : 10, "steakhouse" : 12, "chicken strip" : 15, "mushroom swiss" : 20, "whopper" : 30}
```

### 3. Char Counter

- [x] Given a string and count how many occurrence of each character of the string. The output is a dictionary data type, key for chars and value is sum of the chars. The character only letter, not space, or any symbols. Example :

```python
text_1 = "Mammals"
text_2 = "Bruiser build"
```

Expected output :

```bash
{'m': '***', 'a': '**', 'l': '*', 's': '*'}
{'b': '**', 'r': '**', 'u': '**', 'i': '**', 's': '*', 'e': '*', 'l': '*', 'd': '*'}
```

### 4. Bubble Sort

- [x] Implement bubble sort algorithm in python. Example:

```python
def bubble_sort(items) :
	# write your code here ...
numbers = [12,3,5,4,8,9]
bubble_sort(numbers)
```

Expected output :

```bash
Step 1 : [3, 12, 4, 5, 8, 9]
Step 2 : [3, 4, 12, 5, 8, 9]
Step 3 : [3, 4, 5, 12, 8, 9]
Step 4 : [3, 4, 5, 8, 12, 9]
Step 5 : [3, 4, 5, 8, 9, 12]
```

### 5. Masking

- [x] Given a string "23dn3ir30fd2eddd", please change all the characters with \* (asterisk) except last 3 characters. Write a function to solve this. Example :

```python
secret_text = "23dn3ir30fd2eddd"
masking(secret_text)
```

Expected output :

```bash
*************ddd
```

### 6. Missing Letter

- [x] If there is a list of ordered letters, and one of them is missing. Find out the missing letter! Example :

```python
list_letters_first = ["c","d","e","g","h"]
list_letters_second = ["X","Z"]
```

Expected output :

```bash
list_letters_first = f
list_letters_second = Y
```

### 7. Sorting Odd Numbers

- [x] Given a list of even and odd numbers. Sort the odd numbers, without change even numbers position. p.s : zero is an even number. Example :

```python
numbers = [9,4,2,4,1,5,3,0]
sort_odd(numbers)
```

Expected output :

```bash
[1, 4, 2, 4, 3, 5, 9, 0]
```
