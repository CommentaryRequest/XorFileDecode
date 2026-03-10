#!/usr/bin/env python3

import argparse

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("key", type=str)
    parser.add_argument("encfile", type=str)
    parser.add_argument("output", type=str)
    args = parser.parse_args()

    key = bytes.fromhex(args.key)
    with open(args.encfile, "rb") as f:
        data = bytearray(f.read())
    for i in range(len(data)):
        data[i] ^= key[i % len(key)]
    with open(args.output, "wb") as f:
        f.write(data)

if __name__ == "__main__":
    main()
