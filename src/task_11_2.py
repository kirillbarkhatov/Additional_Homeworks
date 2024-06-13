def is_palindrome(func):
    def wrapper(string):
        if string.lower() == string[::-1].lower():
            return func(string)
        raise ValueError("Argument must be a palindrome")

    return wrapper


@is_palindrome
def reverse_string(string):
    return string[::-1]

# print(reverse_string('racecar')) # "racecar"
# print(reverse_string('Racecar'))
print(reverse_string('hello'))