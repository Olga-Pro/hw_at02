# Подсчет количества гласных в строке
def count_vowels(s: str) -> int:
    vowels = "аеёиоуыэюяАЕЁИОУЫЭЮЯaeiouAEIOU"
    count = 0
    for char in s:
        if char in vowels:
            count += 1
    return count