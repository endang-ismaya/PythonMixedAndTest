"""
DRY : Don't repeat yourself
Write one time, use many times
"""

# Sorted function
# ---------------
int_items = [123, 13.24, 3213, 323.23, 9942]
new_items = sorted(int_items, reverse=True)
another_items = sorted(int_items, reverse=False)
print(int_items)
print(int_items.sort(reverse=False))
print(new_items)
print(another_items)

# calculation
print(sum(int_items))
total = sum(int_items)
avg = total/len(int_items)

print(float("{0:.2f}".format(avg)))

