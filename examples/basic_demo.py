from src.pqc import ALGORITHMS, SECURITY_LEVELS, compare_security, generate_demo_seed, hash_bytes


def main() -> None:
    print("=== Criptografía Postcuántica ===")
    print("\nAlgoritmos relevantes:")
    for name, description in ALGORITHMS.items():
        print(f"- {name}: {description}")

    print("\nNiveles de seguridad:")
    for level, meaning in SECURITY_LEVELS.items():
        print(f"- {level}: {meaning}")

    print("\nResumen conceptual:")
    for item in compare_security():
        print(f"- {item}")

    sample = b"demo-postquantum"
    print(f"\nHash SHA-256: {hash_bytes(sample)}")
    print(f"Semilla demostrativa: {generate_demo_seed('pqc-demo')}")


if __name__ == "__main__":
    main()
