import json  # To handle JSON operations
import segno  # To create QR codes

def read_json_and_generate_qr():
    """Read a JSON file and generate a QR code based on its content."""
    # Ask the user for the JSON file name
    filename = input("Enter the name of the JSON file (with .json extension): ").strip()
    
    try:
        # Open and read the JSON file
        with open(filename, 'r') as file:
            data = json.load(file)  # Load the JSON data
        
        # Convert the JSON data to a formatted string for the QR code
        json_string = json.dumps(data, indent=4)
        print("\nData read from JSON file:")
        print(json_string)
        
        # Create a QR code from the JSON string
        qrcode = segno.make(json_string)
        
        # Save the QR code as an image
        qr_filename = filename.replace(".json", "_qrcode.png")  # Create a new filename for the QR code
        qrcode.save(qr_filename, scale=8)  # Save the QR code image with a specified scale
        print(f"\nQR code saved as {qr_filename}!")
    
    except FileNotFoundError:
        print("Error: The specified file does not exist. Please check the filename and try again.")
    except json.JSONDecodeError:
        print("Error: The file does not contain valid JSON data.")

# The main block to run the program
if __name__ == "__main__":
    read_json_and_generate_qr()  # Call the function to read JSON and generate the QR code
