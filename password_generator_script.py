import numpy as np
import argparse
import string

def generate_password(length, use_symbols=False, use_advanced_symbols=False, seed=None):
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

def main():
    parser = argparse.ArgumentParser(description="Generate a random password.")
    parser.add_argument("--length", default=8, type=int, help="Length of the password, defaults to 8")
    parser.add_argument("--seed", type=int, help="Seed for random number generation")
    parser.add_argument("--symbols", action="store_true", help="Include basic symbols in the password")
    parser.add_argument("--advanced-symbols", action="store_true", help="Include advanced symbols in the password")

    args = parser.parse_args()

    password = generate_password(args.length, args.symbols, args.advanced_symbols, args.seed)
    print(f"Generated password: {password}")

if __name__ == "__main__":
    main()