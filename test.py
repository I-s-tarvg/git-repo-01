def main():
    # Initialize the status of showers (assumed all are occupied initially)
    showers = [False, False, False]  # List to track shower availability (False = occupied, True = free)

    while True:
        try:
            # Ask the user which shower they want to check (1, 2, or 3)
            shower_number = int(input("Enter the shower number (1, 2, or 3): "))
            if shower_number not in [1, 2, 3]:
                print("Invalid shower number. Please enter 1, 2, or 3.")
                continue

            # Check if the selected shower is free
            if not showers[shower_number - 1]:
                print(f"Shower {shower_number} is free. Enjoy your shower!")
                break
            else:
                print(f"Shower {shower_number} is occupied. Please wait for a shower to be free.")
        except ValueError:
            print("Invalid input. Please enter a valid shower number.")

if __name__ == "__main__":
    main()


