# n = int(input("Enter a positive integer: ")) №1
# num = 2
# while num <= n:
#     print(num)
#     num += 2


# n = int(input("Enter a positive integer: ")) №2
# fact = 1
# while n > 0:
#     fact *= n
#     n -= 1
# print("Factorial:", fact)


# while True:                                  №3
#     num = int(input("Enter a number (or 42 to exit): "))
#     if num == 42:
#         break


# string = input("Enter a string: ")
# count = string.count('a')
# counta = string.count('A')
# print("Number of 'a's:", count)
# print("Number of 'A's:", counta)


# num = int(input("Enter a number: "))         №5
# sum_of_digits = 0
# while num > 0:
#     digit = num % 10
#     sum_of_digits += digit
#     num //= 10
# print("Sum of digits:", sum_of_digits)


# N = int(input("Enter the number of Fibonacci numbers to print: ")) №6
# a, b = 0, 1
# count = 0
# while count < N:
#     print(a, end=" ")
#     a, b = b, a + b
#     count += 1


# string = input("Enter a string: ")                      №7
# reversed_string = string[::-1]
# print("Reversed string:", reversed_string)


# sum_of_odd = 0                                          №8
# while True:
#     num = int(input("Enter a number (0 to stop): "))
#     if num == 0:
#         break
#     if num % 2 == 0:
#         continue
#     sum_of_odd += num
# print("Sum of odd numbers:", sum_of_odd)


# import random                                           №ч

# target_number = random.randint(1, 100)
# while True:
#     guess = int(input("Guess the number (between 1 and 100): "))
#     if guess < target_number:
#         print("Too small")
#     elif guess > target_number:
#         print("Too large")
#     else:
#         print("Congratulations! You guessed the number.")
#         break


# string = input("Enter a string: ")                      №10
# if string == string[::-1]:
#     print("Palindrome")
# else:
#     print("Not a palindrome")


# X = float(input("Enter a number (X): "))                №11
# Y = int(input("Enter the power (Y): "))
# result = 1.0
# while Y > 0:
#     result *= X
#     Y -= 1
# print(f"{X} to the power of {Y} is {result}")


# N = int(input("Enter a positive integer (N): "))        №12

# def is_prime(num):
#     if num <= 1:
#         return False
#     if num == 2:
#         return True
#     if num % 2 == 0:
#         return False
#     divisor = 3
#     while divisor * divisor <= num:
#         if num % divisor == 0:
#             return False
#         divisor += 2
#     return True

# num = 2
# print("Prime numbers in the range 1 to", N, ":")
# while num <= N:
#     if is_prime(num):
#         print(num, end=" ")
#     num += 1


# num = input("Enter a number: ")                         №13
# reversed_num = num[::-1]
# print("Reversed number:", reversed_num)


# def is_prime(num):                                      №14
#     if num <= 1:
#         return False
#     if num == 2:
#         return True
#     if num % 2 == 0:
#         return False
#     divisor = 3
#     while divisor * divisor <= num:
#         if num % divisor == 0:
#             return False
#         divisor += 2
#     return True

# num = int(input("Enter a number: "))
# if is_prime(num):
#     print("It's a prime number.")
# else:
#     print("It's not a prime number.")
#     next_prime = num + 1
#     while True:
#         if is_prime(next_prime):
#             print("Next prime number:", next_prime)
#             break
#         next_prime += 1


# def caesar_cipher(text, shift):                   №15
#     encrypted_text = ""
#     for char in text:
#         if char.isalpha():
#             is_upper = char.isupper()
#             char = char.lower()
#             char_code = ord(char) - ord('a')
#             char_code = (char_code + shift) % 26
#             char = chr(char_code + ord('a'))
#             if is_upper:
#                 char = char.upper()
#         encrypted_text += char
#     return encrypted_text

# text = input("Enter a string: ")
# shift = int(input("Enter the shift value: "))
# encrypted_text = caesar_cipher(text, shift)
# print("Encrypted string:", encrypted_text)
