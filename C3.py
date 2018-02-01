sentence = input("please enter a sentence:")
words= []
for word in sentence:
    words.append(word)

abc = {}
for item in words:
    if item in abc:
        abc[item] = abc.get(item)+1
    else:
        abc[item] = 1

s = [(k, abc[k]) for k in sorted(abc, key=abc.get, reverse=True)]
for k,v in s:
    print(str(k)+':'+str(v))
