def palindrome(s):
    s = "".join(char.lower() for char in s if char.isalnum())

    while len(s) > 1:
        if s[0] == s[-1]:
            s = s[1:-1]
        else:
            print("Не палиндром")
            return
    print("Палиндром")


palindrome("а роза упала на лапу азора")
palindrome("гойда")
palindrome("abca")
palindrome("aacaa")
