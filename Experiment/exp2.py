def automaton(s):
    state = 0

    for ch in s:
        if state == 0:
            if ch == 'a':
                state = 1
            else:
                state = 0

        elif state == 1:
            if ch == 'a':
                state = 1
            else:
                state = 2

        elif state == 2:
            if ch == 'a':
                state = 1
            else:
                state = 0

    return state == 2


s = input("Enter a string: ")

if automaton(s):
    print("String Accepted")
else:
    print("String Rejected")
