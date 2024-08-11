import numpy as np
import string


def generate_random(length, use_symbols=False, use_advanced_symbols=False, seed=None):
    if seed is not None:
        np.random.seed(seed)

    characters = string.ascii_letters + string.digits
    basic_symbols = "!@#$&"
    advanced_symbols = "~`'./<>%?*=+();:\"[]{}\\|-_^"

    if use_symbols:
        characters += basic_symbols
        if use_advanced_symbols:
            characters += advanced_symbols
    if use_advanced_symbols:
        characters += basic_symbols
        characters += advanced_symbols


    password = ''.join(np.random.choice(list(characters), size=length))
    return password