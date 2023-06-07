import random
import string
import time

st = time.time()
et = ""

def shuffle():
    new_string = ''
    while len(new_string) < 25:
        system_random = random.SystemRandom()
        pick = system_random.randint(0, 25)
        letter = s[pick]

        if letter in new_string:
            letter = s[pick]
        
        new_string += letter
    return new_string

try:
    alpha = string.ascii_uppercase
    s = '' + alpha
    perm_count = 403291461126605635584000000

    possibles = []
    combo = shuffle() + "\n"
    possibles.append(combo)
    while perm_count > 0:
        scramble = shuffle()
        for each in possibles:
            if scramble in each:
                break
        possibles.append(scramble + "\n")
        perm_count -= 1

    a = open('all-words.txt', 'r')
    a_list = a.readlines()
    a.close()

    remaining = []
    for each in possibles:
        end = 29
        for word in a_list:
            while end > 1 and end != 4:
                word_check = each[0:end]
                if word_check in word:
                    remaining.append(word_check)
                end -= 1

    f = open('final.txt', 'a+')
    for each in remaining:
        f.write(each + "\n")
except Exception as e:
    print(str(e))
finally:
    et = time.time()
elapsed_time = et - st
print('Execution time:', elapsed_time, 'seconds')