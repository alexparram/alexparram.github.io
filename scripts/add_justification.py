import csv
import os

# Configuración de asignatura
subject = "CAI"

input_file = os.path.join(os.path.dirname(__file__), "..", "csv", subject, f"{subject}_preguntas.csv")
temp_file = os.path.join(os.path.dirname(__file__), "..", "csv", subject, f"{subject}_preguntas_temp.csv")

with open(input_file, 'r', encoding='utf-8') as f:
    reader = csv.reader(f)
    rows = list(reader)

if not rows:
    print("CSV empty")
    exit()

header = rows[0]
if 'justificacion' not in header:
    header.append('justificacion')
    
    # Add empty justification to all existing rows
    for row in rows[1:]:
        # Ensure row has enough columns for the existing header before appending
        while len(row) < len(header) - 1:
            row.append('')
        row.append('') # The new justification column

with open(input_file, 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerow(header)
    writer.writerows(rows[1:])

print("Added 'justificacion' column.")
