#!/usr/bin/env python3
import argparse
from services import HashCracker


def main():
    parser = argparse.ArgumentParser(
        description="Hash Cracker: A tool to crack MD5, SHA1, or SHA256 hashes using a wordlist."
    )
    parser.add_argument(
        "hash",
        help="The hash to crack (e.g., a 32-character MD5 hash)"
    )
    parser.add_argument(
        "wordlist",
        help="Path to the wordlist file (one candidate per line)"
    )
    parser.add_argument(
        "-a", "--algorithm",
        choices=["md5", "sha1", "sha256"],
        required=True,
        help="The hash algorithm used to generate the hash"
    )
    args = parser.parse_args()

    print(f"[*] Starting hash cracking using {args.algorithm.upper()} algorithm...")
    cracker = HashCracker(args.hash, args.wordlist, args.algorithm)
    result = cracker.crack()

    if result:
        print(f"[+] Success! The hash corresponds to: '{result}'")
    else:
        print("[-] The password was not found in the wordlist.")

if __name__ == '__main__':
    main()
