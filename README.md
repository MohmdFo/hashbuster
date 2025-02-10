# Hash Cracker

Hash Cracker is a Python-based tool designed to help you crack MD5, SHA1, or SHA256 hashes using a wordlist. **This tool is intended for educational purposes and authorized security testing only. Unauthorized use is illegal and unethical.**

## Features

- **Multi-Algorithm Support:** Crack hashes using MD5, SHA1, or SHA256.
- **Simple CLI Interface:** Easily specify the target hash, wordlist, and hash algorithm.
- **Readable Code:** Designed for clarity and ease of modification.
- **Extensible:** Can be expanded with additional features (e.g., brute-force generation using `itertools`).

## Requirements

- Python 3.x

## Installation

1. **Clone the Repository**

   ```bash
   git clone https://github.com/MohmdFo/hashbuster.git
   ```

2. **Navigate to the Project Directory**

   ```bash
   cd hashbuster
   ```

## Usage

The script accepts three arguments:
- `<hash>`: The hash value you wish to crack.
- `<wordlist>`: The path to a text file containing candidate words (one per line).
- `-a` or `--algorithm`: The hash algorithm used (supported options: `md5`, `sha1`, `sha256`).

### Running the Script

Open your terminal and run the following command:

```bash
python run.py <hash> <wordlist> -a <algorithm>
```

#### Example

If you have a wordlist file named `10k-most-common.txt` and you want to crack the MD5 hash for the word "dragon", use the following command:

```bash
python run.py 8621ffdbc5698829397d97767ac13db3 10k-most-common.txt -a md5
```

If successful, you should see output similar to:

```
[*] Starting hash cracking using MD5 algorithm...
[+] Found the match on line 7
[+] Success! The hash corresponds to: 'dragon'
```

## Wordlist Format

Your wordlist should be a plain text file with one candidate password per line. For example:

```
password
123456
12345678
1234
qwerty
12345
dragon
```

## How It Works

1. **Hash Computation:**  
   Each candidate word from the wordlist is stripped of whitespace, encoded, and then hashed using the specified algorithm.
   
2. **Comparison:**  
   The computed hash is compared with the target hash provided by the user. If a match is found, the tool outputs the corresponding candidate word and its location in the wordlist.

3. **Feedback:**  
   If the password is found, the script prints a success message. If not, it informs the user that the password was not found in the wordlist.

## Contributing

Contributions are welcome! If you have ideas for improvements or additional features, please fork the repository and submit a pull request. Before contributing, ensure you adhere to the code style and test your changes thoroughly.

## Disclaimer

**WARNING:** This tool is for educational purposes and authorized penetration testing only. **Do not use this tool on any system or network without explicit permission.** The author is not responsible for any misuse or damage caused by this software.

## License

This project is licensed under the [MIT License](LICENSE).
