kata = 'malam'
len_kata = len(kata)
is_palindrome = False
for i in range(0,len_kata):
    if kata[i] == kata[-i-1]:
        is_palindrome = True
    else:
        is_palindrome = False
        break
print(f"Is word '{kata}' a palindrome? = {is_palindrome}")