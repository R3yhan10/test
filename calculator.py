def calculate(operation, num1, num2):
    if operation == "add":
        return num1 + num2
    elif operation == "subtract":
        return num1 - num2
    elif operation == "multiply":
        return num1 * num2
    elif operation == "divide":
        if num2 != 0:
            return num1 / num2
        else:
            raise ValueError("Cannot divide by zero.")
    else:
        raise ValueError("Invalid operation. Supported operations are: add, subtract, multiply, divide.")


def main():
    print("Operasi yang tersedia: add, subtract, multiply, divide")
    operation = input("Pilih operasi: ").strip().lower()

    try:
        num1 = float(input("Masukkan angka pertama: "))
        num2 = float(input("Masukkan angka kedua: "))
        result = calculate(operation, num1, num2)
        print(f"Hasil: {result}")
    except ValueError as error:
        print(f"Input tidak valid: {error}")


if __name__ == "__main__":
    main()              