import os
# Configuración de asignatura
subject = "CAI"

filename = os.path.join(os.path.dirname(__file__), "..", "csv", subject, "all_theory_text.txt")
with open(filename, 'r', encoding='utf-8') as f:
    for i, line in enumerate(f):
        if "--- START OF" in line:
            print(f"{i+1}:{line.strip()}")
