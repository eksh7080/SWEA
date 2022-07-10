# 1204

# test = int(input())

# for i in range(1, test+1):
#     num = int(input())
#     case = list(map(int, input().split()))
#     number = [0] * 101

#     for j in case:
#         number[j] += 1

#     maxNum = max(number)
#     arr = []
#     for k in range(len(number)):
#         if number[k] == maxNum:
#             arr.append(k)


#     print("#%d"%num, max(arr))

# 1284
test = int(input())

for i in range(1, test+1):
    p,q,r,s,w = list(map(int, input().split()))

    p_charge = p*w
    q_charge = q
    w_charge = (w-r)*s+q

    charge = (q_charge if w <= r else w_charge)


    print("#%d"%i, p_charge if p_charge < charge else charge)

























