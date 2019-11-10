word = 'lintang'
word2 = ''
voc = list('aiueo')
for c in word:
    if c in voc:
        word2 += 'o'
    else:
        word2 += c
print(word2)