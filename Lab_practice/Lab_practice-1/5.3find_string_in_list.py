List1 = ['apple', 'banana', 'mango', 'orange', 'grape', 'pineapple', 'kiwi', 'watermelon', 'pear', 'peach']
search_string = 'mango'

for fruit in List1:
    if fruit == search_string:
        print(f"'{search_string}' is found in the list.")
        break
else:
    print(f"'{search_string}'is not found in the list.")
