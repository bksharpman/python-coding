# # 1 Ratio
# i = int(input())

# a = i//1000
# b = i//100%10
# c = i//10%10
# d = i%10

# if a+d == abs(b-c):
#   print("yes")
# else:
#   print("no")


# #2 Roskomnadzor
# i = int(input())

# if i >= 18:
#   print("yes")
# else:
#   print("no")


# #3 Arithmetic progression
# a = int(input())
# b = int(input())
# c = int(input())

# if b - a == c - b:
#   print("YES")
# else:
#   print("NO")


# #4 Rook Move
# x1 = int(input())
# y1 = int(input())
# x2 = int(input())
# y2 = int(input())
# if x1==x2 or y1==y2:
#   print("Yes")
# else:
#   print("No")


# #5 King's Move
# x1 = int(input())
# y1 = int(input())
# x2 = int(input())
# y2 = int(input())

# if abs(x1 - x2) <= 1 and abs(y1 - y2) <= 1:
#   print("Yes")
# else:
#   print("No")


# #6 Average number
# a = int(input())
# b = int(input())
# c = int(input())
# if a < b and b < c or c < b and b < a:
#   print(b)
# elif b < a and a < c or c < a and a < b:
#   print(a)
# elif b < c and c < a or a < c and c < b:
#   print(c)
# else:
#   print("wtf")

# #7 Number of days
# m = int(input())
# if m == 2:
#   print("28")
# elif m in [4,6,9,11]:
#   print("30")
# else:
#   print("31")


# #8 Weigh-in ceremony
# i = int(input())

# if i <= 60:
#   print("Light Weight")
# elif i <=64:
#   print("First Welterweight")
# elif i <=69:
#   print("Welter Weight")
# else:
#   print("Heavy Weight")


# #9 Password
# p1 = input()
# p2 = input()
# if p1 == p2:
#   print("password is correct")
# else:
#   print("password is not correct")


# #10 Even or odd?
# i = int(input())

# if i%2 == 0:
#   print("Even")
# else:
#   print("Odd")

# #11 The smallest of two numbers
# n, m = int(input())
# if n > m:
#   print(m)
# else:
#   print(n)

# #12 Age Group
# i = int(input())

# if i < 14:
#   print("young")
# elif 14 < i and i <= 24:
#   print("youth")
# elif i <=59:
#   print("maturity")
# else:
#   print("old")

# #13 Triangle view
# a = int(input())
# b = int(input())
# c = int(input())

# if a == b and b == c:
#   print("Equilateral")
# elif b == a or b == c or c == a:
#   print("Isosceles")
# else:
#   print("Versatile")

