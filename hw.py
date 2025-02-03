# python_philosofhy = ''' Beautiful is better than ugly.
# Explicit is better than implicit.
# Simple is better than complex.
# Complex is better than complicated.
# Flat is better than nested.
# Sparse is better than dense.
# Readability counts.
# Special cases aren't special enough to break the rules.
# Although practicality beats purity.
# Unless explicitly silenced.
# In the face of ambiguity, refuse the temptation to guess.
# There should be one-- and preferably only one --obvious way to do it.
# Although that way may not be obvious at first unless you're Dutch.
# Now is better than never.
# Although never is often better than *right* now.
# If the implementation is hard to explain, it's a bad idea.
# If the implementation is easy to explain, it may be a good idea.
# Namespaces are one honking great idea -- let's do more of those!'''
#
# uppercase_philosophy = python_philosofhy.upper().replace('I', '&')
#
# all_better = uppercase_philosophy.count('BETTER')
# all_never = uppercase_philosophy.count('NEVER')
# all_is = uppercase_philosophy.count('IS')
# all_new_is = uppercase_philosophy.count('&S')
#
# print(uppercase_philosophy, '\n')
# print("Total all 'better' count", all_better)
# print("Total 'never' count", all_never)
# print("Total 'is' count", all_is)
# print("Total 'new is' count", all_new_is)

def product_of_digits(number):
    product = 1
    while number > 0:
        digit = number % 10
        product *= digit
        number //= 10
    return product
#Reveser number

def reverse_number(number):
    return int(str(number)[::-1])

#sorted digits in ascending order

def sorted_digits_asc(number):
    sorted_number = "".join(sorted(str(number)))
    return sorted_number

def main():
    number = int(input("Enter a 4-digit number: "))

    if 1000 <= number <= 9999:
        product = product_of_digits(number)
        reverse_product = reverse_number(product)
        sorted_product = sorted_digits_asc(product)

        print("Product of digits:", product)
        print("Reverse product:", reverse_product)
        print("Sorted product:", sorted_product)

    else:
        print("Sorted number is out of range")

if __name__ == "__main__":
    main()