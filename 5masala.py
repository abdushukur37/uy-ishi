# 5--------
def find_nearest_vowel(letter: str) -> str:
    vowels="aeiou"
    if len(letter)!=1 or letter not in "abcdefghijklmnopqrstuvwxyz":
        return "faqat bitta kichik harf bo‘lishi kerak"
    nearest=vowels[0]
    min_distance=abs(ord(letter)-ord(nearest))
    for vowel in vowels:
        distance=abs(ord(letter)-ord(vowel))
        if distance<min_distance:
            min_distance=distance
            nearest=vowel
    return nearest
print(find_nearest_vowel("k"))