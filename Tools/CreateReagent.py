import json
import os  # Import the os module for directory handling
import random  # Import the random module to generate IDs

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

def getState():
    """Prompt the user to enter the state of the reagent (liquid, solid, gas)."""
    valid_states = ["liquid", "solid", "gas"]
    while True:
        state = input("Enter the state of the reagent (liquid, solid, gas): ").strip().lower()
        if state in valid_states:
            return state.capitalize()  # Return the state with the first letter capitalized
        print(f"Invalid state! Please enter one of the following: {', '.join(valid_states)}")

def getChemicalFormula():
    """Prompt the user to enter the chemical formula (optional)."""
    formula = input("Enter the chemical formula (optional, press Enter to skip): ").strip()
    return formula if formula else None  # Return the input or None if empty

def getRole():
    """Prompt the user to enter the role of the reagent."""
    valid_roles = ["solvent", "catalyst", "reactant", "product", "reagent"]
    while True:
        role = input(f"Enter the role of the reagent ({', '.join(valid_roles)}): ").strip().lower()
        if role in valid_roles:
            return role.capitalize()  # Return the role with the first letter capitalized
        print(f"Invalid role! Please choose from: {', '.join(valid_roles)}")

def getSmiles():
    """Prompt the user to enter the SMILES string (optional)."""
    smiles = input("Enter the SMILES string (optional, press Enter to skip): ").strip()
    return smiles if smiles else None  # Return the input or None if empty

def generateRandomID():
    """Generate a random 4-digit ID."""
    return random.randint(100000, 999999)

def createReagent():
    print("\n--- Creating a New XDL Reagent ---\n")
    # Collect basic reagent details.
    name = getReagentName()
    amount = getAmount()
    units = getUnits()
    concentration = getConcentration()
    state = getState()  # Collect state information
    chemical_formula = getChemicalFormula()  # Collect optional chemical formula
    role = getRole()  # Collect the reagent's role
    reagent_id = generateRandomID()  # Generate a random 4-digit ID
    smiles = getSmiles()  # Collect the optional SMILES string

    # Create a dictionary representing the reagent in XDL format.
    reagent = {
        "id": reagent_id,
        "name": name,
        "amount": amount,
        "units": units,
        "concentration": concentration,
        "state": state,
        "role": role
    }

    # Add the chemical formula to the dictionary if provided.
    if chemical_formula:
        reagent["chemical_formula"] = chemical_formula
    
    # Add the SMILES string to the dictionary if provided.
    if smiles:
        reagent["smiles"] = smiles

    # Display the generated XDL-compatible reagent structure.
    print("\nGenerated Reagent:")
    print(json.dumps(reagent, indent=4))

    # Optionally save the reagent details to a JSON file.
    save = input("Save this reagent to a file? (y/n): ").strip().lower()
    if save == 'y':
        # Ensure the 'Reagents' directory exists.
        if not os.path.exists("Reagents"):
            os.makedirs("Reagents")  # Create the folder if it doesn't exist.
        
        # Define the file path within the 'Reagents' folder.
        filename = f"Reagents/{name.replace(' ', '_')}.json"
        
        # Write the reagent dictionary to the JSON file.
        with open(filename, 'w') as file:
            json.dump(reagent, file, indent=4)
        print(f"Reagent saved as {filename}!")  # Confirm that the file was saved.

# The main block to run the program.
if __name__ == "__main__":
    print("\033[1mChemical Creator Tool\033[0m V0.3\n")
    print("This tool will assist in creating Chemicals for the system")

    createReagent()  # Call the function to create a reagent.
