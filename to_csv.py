import argparse
import csv
import json

def convert_json_to_csv(json_file, csv_file):
    # Open the JSON file and load the data
    with open(json_file, encoding="utf-8") as file:
        data = json.load(file)

    # Extracting data from the JSON
    items = data.get("itemListElement", [])

    # CSV header
    csv_header = ["name", "price", "addressLocality"]

    # Open the CSV file for writing
    with open(csv_file, mode="w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)

        # Write the header
        writer.writerow(csv_header)

        # Write data for each item
        for item in items:
            product = item.get("item", {})
            name = product.get("name", "")
            price = product.get("offers", {}).get("price", "")
            address_locality = product.get("offers", {}).get("availableAtOrFrom", {}).get("address", {}).get("addressLocality", "")

            # Write the data to the CSV file
            writer.writerow([name, price, address_locality])

    print(f"CSV data written to {csv_file}")

if __name__ == "__main__":
    # Create argument parser
    parser = argparse.ArgumentParser(description="Convert JSON to CSV")

    # Add arguments
    parser.add_argument("json_file", help="Path to the input JSON file")
    parser.add_argument("csv_file", help="Name of the output CSV file")

    # Parse the command-line arguments
    args = parser.parse_args()

    # Call the function with the provided arguments
    convert_json_to_csv(args.json_file, args.csv_file)
