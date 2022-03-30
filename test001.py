# # Q2
# result = 0
# i = 1
# print(1)
# while i <= 10:
#     print(i)
#     if i % 3 == 0:
#         result += i 
#         print(result)
#         i += i

# print(result) #166833

#Q3
i = 0
while True:
    i += 1
    if i >= 5: break
    # print("%c" % *)
 
# Q4
# for i in range(1, 101):
#     print(i)

# Q5
a = [70, 60, 55, 75, 95, 80, 85, 100]
total = 0
for score in a:
    total += score

average = total / len(a)
print(average)

# Q6
number = [1,2,3,4,5]
result = [n * 2 for n in number if n % 2 == 1]
print(result)
