import sys
from .hash_utils import HashUtils


class HashCracker:
    def __init__(self, target_hash: str, wordlist_path: str, algorithm: str):
        self.target_hash = target_hash
        self.wordlist_path = wordlist_path
        self.algorithm = algorithm

    def crack(self) -> str:
        """
        Attempt to crack the target_hash by comparing it to the hash of each word
        in the wordlist using the specified algorithm.
        
        Returns the matching word if found, otherwise returns None.
        """
        try:
            with open(self.wordlist_path, 'r', encoding='utf-8') as file:
                for line_number, word in enumerate(file, start=1):
                    candidate = word.strip()
                    if not candidate:
                        continue  # Skip empty lines
                    candidate_hash = HashUtils.compute_hash(candidate, self.algorithm)
                    if candidate_hash == self.target_hash:
                        print(f"[+] Found the match on line {line_number}")
                        return candidate
        except FileNotFoundError:
            print(f"Error: The wordlist file '{self.wordlist_path}' was not found.")
            sys.exit(1)
        except Exception as e:
            print(f"An error occurred: {e}")
            sys.exit(1)
        
        return None
