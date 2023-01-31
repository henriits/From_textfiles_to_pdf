import pandas as pd
import glob
from fpdf import FPDF
from pathlib import Path

# Create a list of text filepaths

filepaths = glob.glob("textfiles/*.txt")

# Create one PDF file , if multiple files, this should be inside for loop
pdf = FPDF(orientation="P", unit="mm", format="A4")

for filepath in filepaths:
    df = pd.read_fwf(filepath)

    pdf.set_auto_page_break(auto=False, margin=0)
    pdf.add_page()

    # Get filename without extension and convert to Capitalise case
    filename = Path(filepath).stem.capitalize()

    pdf.set_font(family="Times", size=16, style="B")
    pdf.cell(w=50, h=8, txt=filename)

    # Line below is used to create separate files
    # pdf.output(f"PDFs/{filename.lower()}.pdf")

# Here we put all into one pdf file
pdf.output("PDFs/output.pdf")
