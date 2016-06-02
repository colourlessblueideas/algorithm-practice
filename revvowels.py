"""
Write a function that takes a string as input and reverse only the vowels of a string.
"""

def reverseVowels(s):
        vowels = "aeiouAEIOU"
        extracted = []
        result = []
        for chr in s:
            if chr in vowels:
                extracted.append(chr)
        extracted.reverse()
        index = 0
        for chr in s:
            if chr in vowels:
                result.append(extracted[index])
                index += 1
            else:
                result.append(chr)
        return "".join(result)