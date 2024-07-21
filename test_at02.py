import pytest
from main_at02 import count_vowels

def test_only_vowels():  # Только гласные
    assert count_vowels("аеёиоуыэюяAEIOU") == 15

def test_no_vowels():  # Только согласные
    assert count_vowels("bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ") == 0

def test_mixed_string():  # Гласные и согласные
    assert count_vowels("Привет, как дела? Hello, how are you?") == 12

def test_empty_string():  # Пустая строка
    assert count_vowels("") == 0

def test_upper_and_lower_case():  # Гласные и согласные - прописные и строчные
    assert count_vowels("АаБвГдЕеЖзИиОоУуЫыЭэЮюЯя") == 18