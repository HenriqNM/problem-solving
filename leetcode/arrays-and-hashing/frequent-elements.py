from collections import Counter
a = [1,2,3,4,4,4,5,6,5,5,5,5]
cnt = Counter(a)
print(max(cnt.values()))