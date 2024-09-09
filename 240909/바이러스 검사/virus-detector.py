def getInput():
    n = int(input())
    customer = list(map(int, input().split()))
    leader, follower = map(int, input().split())

    return n, customer, leader, follower

answer = 0
n, customer, leader, follower = getInput()

for custom in customer:
    custom -= leader
    answer += 1

    if custom > 0:
        if custom%follower == 0:
            answer += custom//follower
        else:
            answer += custom//follower + 1

print(answer)