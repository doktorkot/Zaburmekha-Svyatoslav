result = []

def divider(a, b):
    if a < b:
        raise ValueError
    if b > 100:
        raise IndexError
    return a / b

data = [10, 2, 2, 5, 18, 0, 15, 8, 4]

for key in data:
    try:
        res = divider(key, data[key])
        result.append(res)
    except (ValueError, IndexError, Exception):
        result.append(None)

print(result)