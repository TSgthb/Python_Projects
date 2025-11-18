<p align="left">
  	<img alt="Static Badge" src="https://img.shields.io/badge/version-beta_v1.0-blue?style=for-the-badge" />
</p>

# Conveyance Receipts Generator

<p align="justify">
The <b>Receipts Generator</b> is a Python-based automation tool designed to streamline the process of generating receipts from conveyance data stored in an Excel sheet. It converts each record into a <b>PDF receipt</b>, transforms the PDFs into <b>cropped images</b>, and finally compresses all images into a <b>ZIP folder</b> for easy sharing and archival.
</p>

## Use Cases

This tool is ideal for:
- Automating **receipt generation** for expense reporting.
- **Reducing manual effort** in creating and organizing receipts for audits or reimbursements.

## Functionality

The script performs the following tasks:

1. **Data Extraction**
- The current version of code only supports Excel file with a single sheet. It reads conveyance details from the Excel sheet named `clean`. The column names are not required, however the data must be in the following sequence:
- Expected columns:
  - **Date**: Trip date.
  - **Source**: Starting location.
  - **Destination**: Ending location.
  - **Amount**: Expense amount of the trip.
  - **Vehicle**: Mode of transport.
Check out an example sheet for reference, [here](https://github.com/TSgthb/Python_Projects/blob/main/Conveyance%20Receipts%20Generator/Datasets/CONVEYANCE_Dec_21.xlsx).

2. **PDF Generation**
- Creates a **PDF receipt** for each record using the `reportlab` library's `pdfgen` module. Check out this [link](https://docs.reportlab.com/reportlab/userguide/ch2_graphics/) to know more about the library.
- It includes:
  - Trip date and bill number.
  - Source and destination.
  - Amount and payment details.
  - A header and footer with branding and thank-you note.

3. **PDF to Image Conversion**
- Converts each generated PDF into a **PNG image** using `pdf2image` module. Click [here](https://pdf2image.readthedocs.io/en/latest/index.html) to know more.
- Crops the image to a predefined region for a clean receipt view.

4. **ZIP Folder Creation**
- Compresses all cropped images into a single **ZIP file** for easy distribution.

## Prerequisites

1. Make sure you have Python installed:
```pwsh
python --version
```

2. Install the following Python libraries:
```pwsh
pip install pandas reportlab pdf2image pillow
```

3. The current version of the script is heavily dependant on the hardquoted file paths. The script:

- Creates PDFs for all the records in the same folder the script is running from. 
- Converts all the PDFs to cropped images under a specific folder (named `pdf2image`) under the same folder where the script has been hosted. This operation requires the images folder (here named, `pdf2image`) to be created beforehand under the script's hosting folder.
- Converts all the edited images into a singular ZIP folder and generates it under the same directory as the script.
  > _**Note**: The paths (except for the input file) can be changed from the script only._

- Install `poppler` and add `\bin` folder to the path. Check out [this](https://pdf2image.readthedocs.io/en/latest/installation.html#installing-poppler) for more information.

## How to Run

1. Download the script and save it at the preferred location.
2. Run the script:

```pwsh
python recieptsgenerator.py
```

_**Note**: Specify the file path where you have saved the script._

![launch](https://github.com/TSgthb/Python_Projects/blob/main/Conveyance%20Receipts%20Generator/Images/start_script.png)

![interfact](https://github.com/TSgthb/Python_Projects/blob/main/Conveyance%20Receipts%20Generator/Images/start_script_interface.png)

3. Provide the full path to the Excel file when prompted. Ensure no quotes are given to the path.

![path](https://github.com/TSgthb/Python_Projects/blob/main/Conveyance%20Receipts%20Generator/Images/file_path.png)

4. The script gives a message on console and will:

- Generate PDFs for each record.
- Generate convert PDFs to cropped images.
- Create a ZIP folder containing all images.

![output](https://github.com/TSgthb/Python_Projects/blob/main/Conveyance%20Receipts%20Generator/Images/files_created.png)

![output_explorer](https://github.com/TSgthb/Python_Projects/blob/main/Conveyance%20Receipts%20Generator/Images/files_created_explorer.png)

## Planned Enhancements

1. Add GUI interface for non-technical users.
2. Support for custom templates for receipts.
3. Support for CSV files and other delimited text files.
