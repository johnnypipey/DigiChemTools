import json
import os  # To handle directory creation and file operations
import random  # To generate the equipment ID

def generateEquipmentID():
    """Generate a random 6-digit equipment ID."""
    return random.randint(100000, 999999)  # Return a random 6-digit number

def getEquipmentName():
    """Prompt the user to enter the equipment name."""
    while True:
        name = input("Enter the equipment name (e.g., Beaker, Flask): ").strip()
        if name:
            return name  # Return if input is not empty
        print("Equipment name cannot be empty. Please try again.")

def getEquipmentType():
    """Prompt the user to enter the equipment type."""
    while True:
        eq_type = input("Enter the equipment type (e.g., Glassware, Measuring): ").strip()
        if eq_type:
            return eq_type  # Return if input is not empty
        print("Equipment type cannot be empty. Please try again.")

def getCapacity():
    """Prompt the user to enter the equipment capacity."""
    while True:
        try:
            capacity = float(input("Enter the capacity (e.g., 500 for 500 mL): "))
            return capacity  # Convert to float and return
        except ValueError:
            print("Invalid input! Please enter a valid number for the capacity.")

def getCapacityUnits():
    """Prompt the user to enter the capacity units."""
    while True:
        units = input("Enter the capacity units (e.g., mL, L): ").strip()
        if units:
            return units  # Return if input is not empty
        print("Capacity units cannot be empty. Please try again.")

def getMaterial():
    """Prompt the user to enter the material of the equipment."""
    while True:
        material = input("Enter the material (e.g., Glass, Plastic): ").strip()
        if material:
            return material  # Return if input is not empty
        print("Material cannot be empty. Please try again.")

def getAdditionalFeatures():
    """Prompt the user to enter any additional features."""
    features = input("Enter any additional features or notes (optional): ").strip()
    return features if features else None  # Return the input or None if empty

def getAssignedChemical():
    """Prompt the user to enter an assigned chemical (optional)."""
    chemical = input("Enter the chemical assigned to this equipment (optional, press Enter to skip): ").strip()
    return chemical if chemical else None  # Return the input or None if empty

def createEquipment():
    print("\n--- Creating a New Equipment Entry ---\n")
    # Collect equipment details
    equipment_id = generateEquipmentID()  # Generate a unique ID
    name = getEquipmentName()
    eq_type = getEquipmentType()
    capacity = getCapacity()
    capacity_units = getCapacityUnits()
    material = getMaterial()
    features = getAdditionalFeatures()
    assigned_chemical = getAssignedChemical()  # Collect optional assigned chemical

    # Create a dictionary representing the equipment details
    equipment = {
        "id": equipment_id,
        "name": name,
        "type": eq_type,
        "capacity": f"{capacity} {capacity_units}",
        "material": material,
        "additional_features": features
    }

    # Add the assigned chemical to the dictionary if provided
    if assigned_chemical:
        equipment["assigned_chemical"] = assigned_chemical

    # Display the generated equipment structure
    print("\nGenerated Equipment:")
    print(json.dumps(equipment, indent=4))

    # Optionally save the equipment details to a JSON file
    save = input("Save this equipment to a file? (y/n): ").strip().lower()
    if save == 'y':
        # Ensure the 'Equipment' directory exists
        if not os.path.exists("Equipment"):
            os.makedirs("Equipment")  # Create the folder if it doesn't exist
        
        # Define the file path within the 'Equipment' folder
        filename = f"Equipment/{name.replace(' ', '_')}.json"
        
        # Write the equipment dictionary to the JSON file
        with open(filename, 'w') as file:
            json.dump(equipment, file, indent=4)
        print(f"Equipment saved as {filename}!")  # Confirm that the file was saved

# The main block to run the program
if __name__ == "__main__":
    print("\033[1mLab Equipment Creator Tool\033[0m V1.0\n")
    print("This tool will assist in creating Lab Equipment entries for the system.\n")
    createEquipment()  # Call the function to create equipment
