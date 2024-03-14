def cm_to_inches(cm):
    return cm / 2.54

def main():
    cm_length = float(input("Enter a length in centimeters (cm): "))

    if cm_length < 0:
        print("Invalid entry. Length cannot be negative.")
    else:
        inches_length = cm_to_inches(cm_length)
        print(f"{cm_length} centimeters is equal to {inches_length:.2f} inches.")

if __name__ == "__main__":
    main()
