def all_variants(text):
    v = len(text)
    for i in range(v):
        for j in range(i + 1, v + 1):
            yield text[i:j]

a = all_variants("abc")
for i in a:
    print(i)