#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Extractor de preguntas de PDF a CSV
Extrae preguntas de un cuestionario en PDF y las guarda en formato CSV
"""

import pdfplumber
import csv
import re
import glob
import sys

# Configurar la codificación de salida
sys.stdout.reconfigure(encoding='utf-8')

def extract_questions_from_pdf(pdf_path):
    """
    Extrae preguntas del PDF y las estructura en una lista
    """
    questions = []
    
    with pdfplumber.open(pdf_path) as pdf:
        full_text = ""
        print(f"Procesando {len(pdf.pages)} páginas...")
        for page_num, page in enumerate(pdf.pages, 1):
            text = page.extract_text()
            if text:
                full_text += text + "\n"
            if page_num % 10 == 0:
                print(f"  Procesadas {page_num} páginas...")
        
        # Patrones de parada
        stop_patterns = [
            r'Trieu-ne una:',
            r'Puntuació\s+\d+,\d+',
            r'sobre\s+\d+,\d+',
            r'Respostes',
            r'Vertader\s*?',
            r'Fals\s*?'
        ]
        
        # Dividir por bloques que comienzan con "Pregunta"
        # Usamos regex para encontrar el inicio de cada bloque de pregunta
        # El patrón busca un número seguido de "Pregunta"
        blocks = re.split(r'\n\d+\s+Pregunta\s+', "\n" + full_text)
        
        for idx, block in enumerate(blocks):
            if not block.strip() or idx == 0: # El primer bloque suele ser el encabezado del PDF
                continue
                
            question_data = {
                'numero': len(questions) + 1,
                'pregunta': '',
                'tipo': 'multiple',
                'opciones': '',
                'respuesta_correcta': ''
            }
            
            # Extraer respuesta correcta primero (suele estar al final del bloque)
            ans_match = re.search(r"La resposta correcta és\s+['\"]([^'\"]+)['\"]", block)
            if ans_match:
                question_data['respuesta_correcta'] = ans_match.group(1)
            
            # Limpiar el texto de la pregunta
            # El texto de la pregunta está al principio del bloque, antes de los patrones de parada
            lines = block.split('\n')
            question_lines = []
            
            for line in lines:
                line = line.strip()
                if not line:
                    continue
                
                # Si encontramos un patrón de parada, dejamos de acumular para la pregunta
                if any(re.search(pat, line, re.IGNORECASE) for pat in stop_patterns):
                    break
                
                # Limpiar "Correcte" o "Incorrecte" que a veces aparece al inicio de líneas fragmentadas
                line = re.sub(r'^(Correcte|Incorrecte)\s+', '', line)
                
                # Ignorar líneas que son solo "Correcte", "Incorrecte" o marcas de navegación
                if line.lower() in ['correcte', 'incorrecte', '', '◄', 'salta a...']:
                    continue
                
                question_lines.append(line)
            
            full_q_text = " ".join(question_lines)
            # Limpieza final
            full_q_text = re.sub(r'\s+', ' ', full_q_text).strip()
            
            if full_q_text:
                question_data['pregunta'] = full_q_text
                questions.append(question_data)
    
    return questions

def save_to_csv(questions, csv_path):
    """
    Guarda las preguntas en formato CSV
    """
    with open(csv_path, 'w', newline='', encoding='utf-8') as csvfile:
        fieldnames = ['numero', 'pregunta', 'tipo', 'opciones', 'respuesta_correcta']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        
        writer.writeheader()
        for question in questions:
            writer.writerow(question)
    
    print(f"\n✓ Guardadas {len(questions)} preguntas en {csv_path}")

def main():
    # Configuración de asignatura
    subject = "CAI"
    
    # Encontrar archivo PDF en ../apuntes/CAI
    pdf_pattern = os.path.join(os.path.dirname(__file__), "..", "apuntes", subject, "*.pdf")
    pdf_files = glob.glob(pdf_pattern)
    if not pdf_files:
        print(f"❌ No se encontró ningún archivo PDF en {pdf_pattern}")
        return
    
    pdf_path = pdf_files[0]
    print(f"📄 Usando archivo: {pdf_path}\n")
    
    # Extraer preguntas
    print("🔍 Extrayendo preguntas del PDF...")
    questions = extract_questions_from_pdf(pdf_path)
    
    if not questions:
        print("❌ No se encontraron preguntas en el PDF")
        return
    
    # Guardar en CSV ../csv/CAI/CAI_preguntas.csv
    output_dir = os.path.join(os.path.dirname(__file__), "..", "csv", subject)
    os.makedirs(output_dir, exist_ok=True)
    csv_path = os.path.join(output_dir, f"{subject}_preguntas.csv")
    save_to_csv(questions, csv_path)
    
    # Mostrar muestra
    print("\n📋 Muestra de las primeras 3 preguntas extraídas:")
    print("="*80)
    for q in questions[:3]:
        print(f"\nPregunta {q['numero']}:")
        print(f"  Texto: {q['pregunta'][:100]}...")
        print(f"  Tipo: {q['tipo']}")
        print(f"  Respuesta: {q['respuesta_correcta']}")
    print("="*80)

if __name__ == "__main__":
    main()
