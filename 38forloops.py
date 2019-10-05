word = "hello"
for letter in word:
    print(letter)
sentence = "now is the time for all good people to come to aid"   
count = 0
for letter in sentence:
    if letter == 'a' or letter == 'e' or letter == 'i' or letter == 'o' or letter == 'u':
        count = count + 1
print('The number of vowel is ' + str(count))        
                                                             