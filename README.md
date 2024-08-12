## Usage 
Use the command below to run the script.
```
    python3 main.py
```
Below is a list of the flags and their descriptions in order to modify features of the password.

| **Flag**              | **Description**                                                                                 |
|-----------------------|-------------------------------------------------------------------------------------------------|
| `--length`            | Length of the password, defaults to 8                                                           |
| `--seed`              | Seed for random number generation                                                               |
| `--symbols`           | Include basic symbols in the password                                                           |
| `--advanced-symbols`  | Include advanced symbols in the password                                                        |
| `--memorizable`       | Generate a more easily memorizable password. When this flag is set, the length flag now delineates the number of short (<7 letter) nouns in the password. Note that when this flag is set the symbols and advanced-symbols flags no longer have an effect |

## More Example Commands
```
python3 main.py --memorizable --length 3
python3 main.py --symbols --length 20
```

## Dependencies
numpy
nltk
