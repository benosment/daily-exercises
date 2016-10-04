n = int(input().strip())
words = []
for i in range(n):
    words.append(input().strip())

for i in range(n):
    print("%s %s" % (''.join(words[i][::2]), ''.join(words[i][1::2])))
