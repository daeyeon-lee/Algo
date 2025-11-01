score = int(input())

if 90 <= score <= 100:
    ans = "A"
elif 80<= score <=89:
    ans = "B"
elif 70<= score <=79:
    ans = "C"
elif 60<= score <=69:
    ans = "D"
elif score <= 60:
    ans = "F"

print(ans)