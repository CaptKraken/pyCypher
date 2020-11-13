from ascii import top, breaker, about, story
import sys
from os import system
system('title '+ 'pyCypher')
#dictionary
dict = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
        'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r',
        's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


# functions
# processing
def perform(msg, shift):
    new_msg = ''
    for letter in msg:
        if letter not in dict:
            new_msg += letter
        else:
            position = dict.index(letter)
            if opt == 'e':
                npos = position + shift
            if opt == 'd':
                npos = position - shift
            new_msg += dict[npos]
    print(f'{breaker}\nthe message is ▼\n{new_msg}')
    end()


# restarting
def end():
    print(breaker)
    ans = input('do you want to run again? y/n:\n>>> ')[:1].lower()
    if ans == 'y':
        state = True
    elif ans == 'n':
        sys.exit()
    else:
        print('''>>> unrecognized command.
enter \'y\' or \'n\' only.''')
        end()


# inputing
def cont():
    msg = input('type your message:\n>>> ').lower()
    try:
        shift = int(input('type the shift number:\n>>> '))
        if shift > 25:
            shift = shift % 25
        else:
            shift = shift
        perform(msg, shift)
    except:
        print('''>>> error: enter numbers only.
restarting...''')
        end()


# main
print(top)
state = True
while state:
    opt = input("choose menu:\n>>> ")[:1]
    if opt == 'e':
        print('► encode')
        cont()
    elif opt == 'd':
        print('► decode')
        cont()
    elif opt == 'a':
        print(
            f'''{story}\n   In cryptography, a Caesar cipher, also known as Caesar's cipher, the shift cipher,
Caesar's code or Caesar shift, is one of the simplest and most widely known encryption
techniques. It is a type of substitution cipher in which each letter in the plaintext
is replaced by a letter some fixed number of positions down the alphabet. 
\n   For example, with a left shift of 3, D would be replaced by A, E would become B,
and so on. The method is named after Julius Caesar, who used it in his private
correspondence.
[source: https://en.wikipedia.org/wiki/Caesar_cipher]
{about}\n► created on 13/Nov/2020\n► a Caesar Cipher en/decoder\n► made with Python3\n► by KIM SONG @CaptKrakenatic''')
        end()
    elif opt == 'q':
        sys.exit()
    else:
        print('>>> unrecognized command.\n>> here are your choices: e to encode, d to decode, a to read about page, q to quit <<')
        state = True
