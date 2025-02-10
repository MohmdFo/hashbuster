import hashlib


class HashUtils:
    @staticmethod
    def compute_hash(word: str, algorithm: str) -> str:
        """
        Compute the hash of a given word using the specified algorithm.
        """

        word = word.strip().encode('utf-8')

        if algorithm == 'md5':
            return hashlib.md5(word).hexdigest()
        elif algorithm == 'sha1':
            return hashlib.sha1(word).hexdigest()
        elif algorithm == 'sha256':
            return hashlib.sha256(word).hexdigest()
        else:
            raise ValueError(f"Unsupported algorithm: {algorithm}")
