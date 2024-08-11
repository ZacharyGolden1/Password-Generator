import argparse
from random_password import generate_random
from memorizable_password import generate_memorizable

def main():
    parser = argparse.ArgumentParser(description="Generate a random password")
    parser.add_argument("--length", default=8, type=int, help="Length of the password, defaults to 8")
    parser.add_argument("--seed", type=int, help="Seed for random number generation")
    parser.add_argument("--symbols", action="store_true", help="Include basic symbols in the password")
    parser.add_argument("--advanced-symbols", action="store_true", help="Include advanced symbols in the password")
    parser.add_argument("--memorizable", action="store_true", help="Generate a more easily memorizable password. When this flag is set the length flag now delineates the number of one nouns in the password")

    args = parser.parse_args()

    if args.memorizable:
        password = generate_memorizable(args.length, args.seed)
    else:
        password = generate_random(args.length, args.symbols, args.advanced_symbols, args.seed)
    print(f"Generated password: {password}")

if __name__ == "__main__":
    main()