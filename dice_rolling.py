import random

def dice_rolling_simulator():
    print(
        """
            🎲 Welcome to the Dice Rolling Simulator! 🎲
        """
        )
    
    try:
        # Get user inputs for the number of sides and rolls
        sides = int(input("Enter the number of sides on the dice: "))
        rolls = int(input("Enter the number of rolls: "))
        
        # Validate inputs
        if sides < 1 or rolls < 1:
            print("Please enter positive integers for sides and rolls.")
            return
        
        print(f"\nRolling a {sides}-sided dice {rolls} time(s):\n")
        
        # Simulate dice rolls
        results = []
        for _ in range(rolls):
            roll = random.randint(1, sides)
            results.append(roll)
            print(f"Roll {_ + 1}: {roll}")
        
        # Display results
        print("\nSummary:")
        print(f"Total Rolls: {rolls}")
        print(f"Results: {results}")
    
    except ValueError:
        print("Invalid input! Please enter integers for sides and rolls.")

# Run the dice rolling simulator
dice_rolling_simulator()
