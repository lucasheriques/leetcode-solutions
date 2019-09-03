# Given a non-empty string of lowercase letters and a non-negative integer
# value representing a key, write a function that returns a new string obtained
# by shifting every letter in the input string by k positions in the alphabet,
# where k is the key. Note that letters should "wrap" around the alphabet in
# other words, the letter "z" shifted by 1 returns the letter "a".


# O(n) time | O(n) space
def caesarCipherEncryptor(string, key):
    chars = [char for char in string]
    key %= 26

    for idx in range(len(chars)):
        chars[idx] = shift_letter(chars[idx], key)

    return "".join(chars)


def shift_letter(char, shifts):
    new_char = ord(char) + shifts

    if new_char > ord('z'):
        new_char -= 26

    return chr(new_char)
