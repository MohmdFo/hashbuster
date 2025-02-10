#!/usr/bin/env python3
import argparse
import hashlib
import sys


def compute_hash(word: str, algorithm: str) -> str:
    """
    Compute the hash of a given word using the specified algorithm.
    """
    # Remove any trailing whitespace/newlines and encode the word
    word = word.strip().encode('utf-8')
    
    if algorithm == 'md5':
        return hashlib.md5(word).hexdigest()
    elif algorithm == 'sha1':
        return hashlib.sha1(word).hexdigest()
    elif algorithm == 'sha256':
        return hashlib.sha256(word).hexdigest()
    else:
        raise ValueError(f"Unsupported algorithm: {algorithm}")

def crack_hash(target_hash: str, wordlist_path: str, algorithm: str) -> str:
    """
    Attempt to crack the target_hash by comparing it to the hash of each word
    in the wordlist using the specified algorithm.
    
    Returns the matching word if found, otherwise returns None.
    """
    try:
        with open(wordlist_path, 'r', encoding='utf-8') as file:
            for line_number, word in enumerate(file, start=1):
                candidate = word.strip()
                if not candidate:
                    continue  # Skip empty lines
                candidate_hash = compute_hash(candidate, algorithm)
                if candidate_hash == target_hash:
                    print(f"[+] Found the match on line {line_number}")
                    return candidate
    except FileNotFoundError:
        print(f"Error: The wordlist file '{wordlist_path}' was not found.")
        sys.exit(1)
    except Exception as e:
        print(f"An error occurred: {e}")
        sys.exit(1)
    
    return None

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
    result = crack_hash(args.hash, args.wordlist, args.algorithm)

    if result:
        print(f"[+] Success! The hash corresponds to: '{result}'")
    else:
        print("[-] The password was not found in the wordlist.")

if __name__ == '__main__':
    main()
