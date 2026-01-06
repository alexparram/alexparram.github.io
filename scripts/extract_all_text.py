import glob
import pdfplumber
import os

# Configuración de asignatura
subject = "Maquines Termiques"

# Define directories
# PDFs are now in ../apuntes/CAI
pdf_dir = os.path.join(os.path.dirname(__file__), "..", "apuntes", subject)
# Output text file in ../csv/CAI/
output_dir = os.path.join(os.path.dirname(__file__), "..", "csv", subject)
os.makedirs(output_dir, exist_ok=True)
output_file = os.path.join(output_dir, "all_theory_text.txt")

pdf_files = glob.glob(os.path.join(pdf_dir, "*.pdf"))

with open(output_file, "w", encoding="utf-8") as f:
    for pdf_path in pdf_files:
        try:
            print(f"Processing: {os.path.basename(pdf_path)}")
            f.write(f"\n\n--- START OF {os.path.basename(pdf_path)} ---\n\n")
            with pdfplumber.open(pdf_path) as pdf:
                for page in pdf.pages:
                    text = page.extract_text()
                    if text:
                        f.write(text)
                        f.write("\n")
            f.write(f"\n\n--- END OF {os.path.basename(pdf_path)} ---\n\n")
        except Exception as e:
            print(f"Error reading {pdf_path}: {e}")

print("Done extracting text.")
