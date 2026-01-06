import os
# Configuración de asignatura
subject = "CAI"

filename = os.path.join(os.path.dirname(__file__), "..", "csv", subject, "all_theory_text.txt")
output_filename = os.path.join(os.path.dirname(__file__), "..", "csv", subject, "headers_map.txt")

with open(filename, 'r', encoding='utf-8') as f:
    with open(output_filename, "w", encoding="utf-8") as out:
        for i, line in enumerate(f):
            if "--- START OF" in line:
                out.write(f"{i+1}:{line}")
