import json

def getReagentName():
    """Prompt the user to enter the reagent name."""
    while True:
        name = input("Enter the reagent name: ").strip()
        if name:
            return name  # Return the input if it's not empty.
        print("Reagent name cannot be empty. Please try again.")

def getAmount():
    """Prompt the user to enter the reagent amount."""
    while True:
        try:
            amount = float(input("Enter the amount (e.g., 50): "))
            return amount  # Convert the input to float and return.
        except ValueError:
            print("Invalid input! Please enter a valid number for the amount.")

def getUnits():
    """Prompt the user to enter the units."""
    while True:
        units = input("Enter the units (e.g., mL, g): ").strip()
        if units:
            return units  # Return the input if it's not empty.
        print("Units cannot be empty. Please try again.")

def getConcentration():
    """Prompt the user to enter concentration details if applicable."""
    has_concentration = input("Does the reagent have a concentration? (y/n): ").strip().lower()
    if has_concentration == 'y':
        while True:
            try:
                conc_value = float(input("Enter the concentration value (e.g., 95): "))
                break  # Break the loop if input is valid.
            except ValueError:
                print("Invalid input! Please enter a valid number for the concentration value.")
        
        while True:
            conc_units = input("Enter the concentration units (e.g., %, mol/L): ").strip()
            if conc_units:
                return {"value": conc_value, "units": conc_units}  # Return concentration as a dictionary.
            print("Concentration units cannot be empty. Please try again.")
    return None  # Return None if no concentration is provided.

def createReagent():
     print("\n--- Creating a New XDL Reagent ---\n")
     # Collect basic reagent details.
     name = getReagentName()
     amount = getAmount()
     units = getUnits()
     concentration = getConcentration()

     # Create a dictionary representing the reagent in XDL format.
     reagent = {
        "name": name,
        "amount": amount,
        "units": units,
        "concentration": concentration
    }
     # Display the generated XDL-compatible reagent structure.
     print("\nGenerated Reagent:")
     print(json.dumps(reagent, indent=4))
     # Optionally save the reagent details to a JSON file.
     save = input("Save this reagent to a file? (y/n): ").strip().lower()
     if save == 'y':
        filename = f"{name.replace(' ', '_')}_reagent.json"  # Create a filename based on the reagent's name.
        with open(filename, 'w') as file:
            json.dump(reagent, file, indent=4)  # Write the reagent dictionary to a JSON file.
        print(f"Reagent saved as {filename}!")  # Confirm that the file was saved.
    


# The main block to run the program.
if __name__ == "__main__":
    print("\033[1mChemical Creator Tool\033[0m V0.1\n")
    print("This tool will assist in creating Chemicals for the system")

    

    createReagent()  # Call the function to create a reagent.