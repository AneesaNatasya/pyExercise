def convert_to_Min(seconds):
    minutes = seconds // 60
    remaining_seconds = seconds % 60
    return minutes, remaining_seconds

def main():
    seconds = int(input("Enter the number of seconds: "))
    minutes, remaining_seconds = convert_to_Min(seconds)
    
    print(f"{seconds} seconds is {minutes} minutes and {remaining_seconds} seconds.")

if __name__ == "__main__":
    main()
