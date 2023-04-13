def encode(plain: str) -> list[int]:
    return [ord(elem) - 96 for elem in plain]


def decoded(encoded: list[int]) -> str:
    return "".join(chr(elem + 96) for elem in encoded)


def main():
    encoded = encode(input("-> ").strip().lower())

    print("Encoded", encoded)
    print("Decoded", decoded(encoded))


if __name__ == '__main__':
    main()
