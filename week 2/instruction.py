from time import sleep
 
def print_slow(txt):
    for x in txt:                     # cycle through the text one character at a time
        print(x, end='', flush=True)  # print one character, no new line, flush buffer
        sleep(0.09)
    print() # go to new line

print_slow("Hello. I'm feeling a bit slow today")