a = set([1,2,3,4,5])
b = set([4,5,6,7,8])

print(a)
print(b)

print(a.difference(b))
# farklı elemanlar

print(b.intersection(a))
# kesişim ortak elemanlar
print(b.symmetric_difference(a))
# birleşim kümesi