import random

#part1
def find_locations(c, s):
    pos = ()
    for i in range(len(s)):
        if c == s[i]:
            rpos = pos + (i,)
    return pos

#part2 MAIN PROGRAM 
f_v = open('vocabulary.txt', 'a')
list_w = input('Insert the words separated by the \';\' character: ')
words = list_w.split(';')
for w in words:
    w = w.strip()
    if (w.isalpha()):
        f_v.write(w.upper() + "\n")
f_v.close()


#part3
user = input('Insert your nickname: ')
score = 100

f_v = open('vocabulary.txt', 'r')
words = f_v.readlines()
f_v.close()
word = random.choice(words).strip()
mask = '_'*len(word)

#part4
while(mask != word):
    print('Guess:', mask)
    
    char_user = input('Choose a character: ').upper()    
    if char_user not in word:
        #not correct
        dice = random.randint(1, 6)
        print('Dice roll:', dice)
        if dice != 6:
            score -= 10
    elif char_user in mask:
        #user already chose this character
        print('Already guessed')
    else:
        #correct, new character
        positions = find_locations(char_user, word)
        for i in positions:
            mask = mask[:i] + char_user + mask[(i+1):]
        print('Great!')
    
    if (score <= 0):
        print('You lost!')
        break
    
    print('Score:', score)
    print()
if mask == word:
    print("You guessed the word:", word, "! Final score:", score)
 
#part5 
scores = open('scores.txt', 'a+')
scores.seek(0)

scores_list = list()  # create a list where each element is a pair [score, 'Username']
for line in scores:
    s = line.split()
    # convert the score to integer
    s[0] = int(s[0])
    scores_list.append(s)

if scores_list == [] or score >= min(scores_list)[0]:
    # arrived at the end of the list
    scores.write(str(score) + ' ' + user + '\n')
    # insert the new pair into the list
    scores_list.append([score, user])

scores.close()

#scores_list.sort(reverse=True)
#for s in scores_list:
#    print(s[1], s[0], sep='\t')    