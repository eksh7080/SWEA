# 1545
# n = int(input())
# for i in range(n, 0-1, -1):
#     print(i)

# 2019
# n = int(input())
# sum = 1
# print(1, end=" ")
# for i in range(1, n+1):
    
#     sum *= 2

#     print(sum, end=" ")

# n = int(input())

# for i in range(0, n+1):
    
#     i = 2**i

#     print(i, end=" ")

# 1936
# a,b = input().split()
# a = int(a)
# b = int(b)

# if a == 1 and b == 3:
#     print("a")
# elif b == 1 and a == 3:
#     print("b")
# elif a < b:
#     print("b")
# elif a > b:
#     print("a")

# 1933
# yak = int(input())

# for i in range(1, yak+1):
#     if yak % i == 0:
#         print(i, end=" ")


# 1938
# a,b = input().split()
# a = int(a)
# b = int(b)

# print(a+b)
# print(a-b)
# print(a*b)
# print("%d"%float(a/b))

# 2025
# n = int(input())
# sum = 0
# for i in range(1, n+1):
#     sum += i

# print(sum)

# 2027
# print("#++++")
# print("+#+++")
# print("++#++")
# print("+++#+")
# print("++++#")

# 2029
# test = int(input())
# for i in range(1, test+1):
#     a,b = map(int, input().split())
#     print("#%d"%i, a//b, a%b,sep=" ")

# 2043
# p,k = map(int, input().split())
# cnt = 0
# for i in range(k, p+1):
#     cnt+=1
# print(cnt)

# 2046
# num=int(input())

# for i in range(num):
#     print("#",end="")

# 2047
# text = str(input())
# print(text.upper())

# 2050
# alpa = input().upper()
# for i in alpa:
#     print(ord(i)-64)

# 2056

test = int(input())
for i in range(1, test+1):
    birth = input()
    year = birth[:4]
    month = birth[4:6]
    day = birth[6:]

    year = int(year)
    month = int(month)
    day = int(day)

    # if (month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12) and (day > 32):
    #     print("-1")
    # elif month == 2 and day > 28:
    #     print("-1")
    # elif (month == 4 or month == 6 or month == 9 or month == 11) and (day > 30):
    #     print("-1")
    # elif month == 00:
    #     print("-1")
    # else:
    #     print("#%d"%i,"%04d/%02d/%02d"%(year,month,day))

    if month in [1,3,5,7,8,10,12] and (day > 32):
        print("#%d -1"%i)
    elif month in [4,6,9,11] and (day > 30):
        print("#%d -1"%i)
    elif month == 2 and day > 28:
        print("#%d -1"%i)
    elif month == 00:
        print("#%d -1"%i)
    else:
        print("#%d %04d/%02d/%02d"%(i,year,month,day))











