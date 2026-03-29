#!/bin/python3

# I know, it's AI generated. But it's fucking good! But hey, atleast I added a comment and only made it support wl-clipboard so other people can't use it!

import sys
from decimal import Decimal, getcontext
import subprocess

def compute_pi(digits):
    getcontext().prec = digits + 2

    C = 426880 * Decimal(10005).sqrt()

    M = 1
    L = 13591409
    X = 1
    K = 6
    S = Decimal(L)

    for i in range(1, digits // 14 + 1):
        M = (M * (K**3 - 16*K)) // (i**3)
        L += 545140134
        X *= -262537412640768000
        S += Decimal(M * L) / X
        K += 12

    pi = C / S
    return str(pi)[:digits + 2]


def copy_to_clipboard(text):
    # Try common Linux clipboard tools
    try:
        subprocess.run(["wl-copy"], input=text.encode(), check=True)
    except:
        print("No clipboard tool found (wl-copy / xclip / xsel)")
        print(text)


def main():
    if len(sys.argv) != 2:
        print("Usage: pi-gen <digits>")
        sys.exit(1)

    digits = int(sys.argv[1])
    pi = compute_pi(digits)

    copy_to_clipboard(pi)
    print(f"π ({digits} digits) copied to clipboard ✅")


if __name__ == "__main__":
    main()
