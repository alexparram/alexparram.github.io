import pdfplumber
import glob
import sys

# Configurar la codificación de salida
sys.stdout.reconfigure(encoding='utf-8')

import os

# Configuración de asignatura
subject = "CAI"

# Encuentra el archivo PDF en ../apuntes/CAI
pdf_pattern = os.path.join(os.path.dirname(__file__), "..", "apuntes", subject, "*.pdf")
pdf_files = glob.glob(pdf_pattern)
if not pdf_files:
    print(f"No se encontró ningún archivo PDF en {pdf_pattern}")
    exit(1)

pdf_path = pdf_files[0]
print(f"Usando archivo: {pdf_path}")
print()

with pdfplumber.open(pdf_path) as pdf:
    print(f"Total de páginas: {len(pdf.pages)}")
    print("\n" + "="*80)
    print("PRIMERAS 5 PÁGINAS:")
    print("="*80 + "\n")
    
    # Muestra el contenido de las primeras 5 páginas y guarda en archivo ../csv/CAI/debug_pdf_text.txt
    output_path = os.path.join(os.path.dirname(__file__), "..", "csv", subject, "debug_pdf_text.txt")
    with open(output_path, "w", encoding="utf-8") as f:
        for i in range(min(5, len(pdf.pages))):
            page = pdf.pages[i]
            text = page.extract_text()
            if text:
                header = f"\n{'='*80}\nPÁGINA {i+1}\n{'='*80}\n"
                print(header)
                print(text)
                f.write(header)
                f.write(text)
                f.write("\n")
