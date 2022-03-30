# Q1
# a:b:c:d
# a#b#c#d
# hint : use split and join

str = "a:b:c:d"
test = str.split(":")
c = "#".join(test)
print(c)
# test2 = test.join("#")
# print(test2)

#Q2
# 딕셔너리 값 추출하기
a = {'A':90, 'B':80}
a.get('C', 70)

#Q3
a = [1,2,3]

#Q4
A = [20,55,67,82,45,33,90,87,100,25]
sum = 0
for jeomsu in A:
    if (jeomsu >= 50):
        sum += jeomsu

print(sum) #481

# Q5 pibonacci
n = 10
pibo = [0, 1]
a = 1
i = 2
while (a<=n):
    a = pibo[i-2] + pibo[i-1]
    print(a)
    pibo = pibo + [a]
    i += 1

print(pibo)

# Q6 total data
# 65,45,2,3,45,8

#Q7 gugudan
input = 2
arr = []
for i in range(1,10):
    arr.extend([input*i])

print(arr)

#Q8 reverse save

#Q14
input = 'aaabbcccccca'







