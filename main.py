from sha256_tool import hash_text_sha256, verify_hash

def main():
    while True:
        print("\n=== SHA-256 Cryptography Tool ===")
        print("1. Hash Text")
        print("2. Verify Text Against Hash")
        print("0. Exit")
        choice = input("Enter your choice: ").strip()

        if choice == '1':
            text = input("Enter text to hash: ")
            hash_result = hash_text_sha256(text)
            print(f"SHA-256 Hash:\n{hash_result}")

        elif choice == '2':
            text = input("Enter original text: ")
            expected_hash = input("Enter SHA-256 hash to verify against: ").strip()
            if verify_hash(text, expected_hash):
                print("✅ Match: Hash verified.")
            else:
                print("❌ Mismatch: Hash does not match.")

        elif choice == '0':
            print("Exiting.")
            break

        else:
            print("Invalid option. Please choose 0, 1, or 2.")

if __name__ == "__main__":
    main()
