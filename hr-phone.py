n = int(input().strip())
phone_numbers = {}
for i in range(n):
    name, number = input().strip().split()
    phone_numbers[name] = number

while True:
    try:
        query = input().strip()
        try:
            print("%s=%s" % (query, phone_numbers[query]))
        except KeyError:
            print("Not found")
    except EOFError:
        break
