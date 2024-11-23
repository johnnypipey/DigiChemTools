

# Tools

The DigiChemTool suite

Please find explanations for the tools included within the suite




## Create Reagent (CreateReagen.py)

📦 Chemical Creator Tool - Version 0.1

A user-friendly command-line tool designed to simplify the process of creating chemical reagents in XDL-compatible format. This interactive script allows users to input reagent details, including name, amount, units, and optional concentration, and generates structured JSON files ready for further use in chemical automation workflows.

🚀 **Key Features:**

* **Interactive Input Prompts:** 

    Guides the user through each step, ensuring accurate and consistent data entry.

* **Validation and Error Handling:** 

    Ensures valid numerical entries for amounts and concentrations while preventing empty inputs.

* **XDL-Compatible Output:** 

    Automatically formats the collected data into a JSON structure compatible with XDL specifications.

* **File Saving Option:** 

    Easily save generated reagent details as JSON files, named dynamically based on the reagent.

🛠️ **How to use:**

    1. Run the Script:
    Launch the program from your command line or IDE.

    2. Input Reagent Details:
    Follow the prompts to enter:

    * Reagent name
    * Amount (numeric)
    * Units (e.g., mL, g)
    * Optional concentration details

    3. Review and Save:
    Review the generated JSON output and choose whether to save it to a file.

💡 **Example JSON Output:**

```
{
    "name": "Acetone",
    "amount": 100.0,
    "units": "mL",
    "concentration": {
        "value": 95.0,
        "units": "%"
    }
}
```
