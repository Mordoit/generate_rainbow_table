#!/usr/bin/env python

__author__ = "Mordoit"
__version__ = "1.0.3"
__email__ = "mordoit@protonmail.com"


# Import library
import hashlib
import sys
import os


def error():  # Print the error and exit the program
    print("generate_rainbow.py\n-------------------\nAuthor: Mordoit \n \nalgorithm supported is the same than the hashlib \nsha1, md5, sha224, sha256, sha384, sha512, blake2b, blake2s, sha3_224, sha3_256, sha3_384, sha3_512 \ngenerate_rainbow.py 'algorithmm' 'path' \n\nExemple: generate_rainbow.py md5 ./password.txt")
    exit()


def main():  # Controler
    check()
    rainbow()


def check():  # Check if all the parameter are correct and supported
    exists = os.path.isfile(file)
    support_arg = ["sha1", "md5", "sha224", "sha256", "sha384", "sha512",
                   "blake2b", "blake2s", "sha3_224", "sha3_256", "sha3_384", "sha3_512"]
    if algo not in support_arg and not exists:
        error()


def rainbow():  # Generate the rainbow table
    with open(output, "w") as out:
        with open(file) as f:
            generate = "out.write(hashlib." + algo + \
                "(line.encode('utf-8', errors='ignore')).hexdigest() + '\t' + line)"
            for line in f:
                exec(generate)

# Help page
if sys.argv[1] == "help" or sys.argv[2] == "help":
    error()

# Set parameter as variable
algo = sys.argv[1]
file = sys.argv[2]

# Generate the name of the output
output = algo + "_rainbow.txt"
if __name__ == '__main__':
    main()
