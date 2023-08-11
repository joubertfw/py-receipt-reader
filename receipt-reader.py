import cv2
import pytesseract
import json
import re

pytesseract.pytesseract.tesseract_cmd = r'<path_to_tesseract_executable>'

# Function to extract text from the image using OCR
def extract_text_from_image(image_path):
    # Load the image using OpenCV
    image = cv2.imread(image_path)
    # Convert the image to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # Apply image preprocessing (if needed)
    # ...
    # Use Tesseract to extract text from the image
    text = pytesseract.image_to_string(gray)

    return text

# Function to process the extracted text and extract products
def process_text(text):
    # Process the text and extract products
    # You can use regular expressions or other techniques to extract the relevant information from the text

    products = []

    # Example of regex for Continente receipts
    results = re.findall("(((IS|\(C\)|\(B\))\s+([A-Z0-9.]+\s)+)(\d+,\d+))", text)

    for result in results:
        products.append({'prod': result[1], 'price': result[4]})

    # Products are extracted as a list of objects
    return products

# Function to convert products to JSON
def products_to_json(products):
    # Convert the products to JSON format
    data = {'products': products}
    json_data = json.dumps(data, indent=4)

    return json_data

# Path to the market receipt image
receipt_image_path = 'receipt.jpg'

# Extract text from the image
extracted_text = extract_text_from_image(receipt_image_path)

# Process the extracted text and extract products
extracted_products = process_text(extracted_text)

# Convert products to JSON
json_output = products_to_json(extracted_products)

# Print the JSON output
print(json_output)

