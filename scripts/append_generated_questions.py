import csv
import os
# Configuración de asignatura
subject = "CAI"

csv_path = os.path.join(os.path.dirname(__file__), "..", "csv", subject, f"{subject}_preguntas.csv")

# Define the new questions
new_questions = [
    {
        "pregunta": "La norma UNE 13943:2018 define la combustión como una reacción química endotérmica.",
        "tipo": "multiple",
        "opciones": "",
        "respuesta_correcta": "Fals",
        "justificacion": "Se define como una reacción química exotérmica (desprende calor) de oxidación-reducción."
    },
    {
        "pregunta": "Los tres elementos del triángulo del fuego son Combustible, Comburente y Nitrógeno.",
        "tipo": "multiple",
        "opciones": "",
        "respuesta_correcta": "Fals",
        "justificacion": "Los elementos son Combustible, Comburente y Energía de Activación (calor)."
    },
    {
        "pregunta": "El tetraedro del fuego añade la 'Reacción en cadena' para explicar por qué se mantiene y progresa el fuego.",
        "tipo": "multiple",
        "opciones": "",
        "respuesta_correcta": "Vertader",
        "justificacion": "El cuarto elemento, la reacción en cadena, explica el mantenimiento del fuego más allá de la ignición inicial."
    },
    {
        "pregunta": "El punto de inflamación es la temperatura mínima para que la mezcla arda y se mantenga sin la fuente de ignición.",
        "tipo": "multiple",
        "opciones": "",
        "respuesta_correcta": "Fals",
        "justificacion": "Ese es el punto de ignición. El punto de inflamación solo permite que arda brevemente mientras está la fuente."
    },
    {
        "pregunta": "Por debajo del Límite Inferior de Inflamabilidad (LII), la mezcla es demasiado rica en combustible para arder.",
        "tipo": "multiple",
        "opciones": "",
        "respuesta_correcta": "Fals",
        "justificacion": "Por debajo del LII, la mezcla es demasiado pobre en combustible."
    },
    {
        "pregunta": "El método de extinción por enfriamiento consiste en eliminar el comburente.",
        "tipo": "multiple",
        "opciones": "",
        "respuesta_correcta": "Fals",
        "justificacion": "El enfriamiento consiste en eliminar la energía (calor). La eliminación del comburente es la sofocación."
    },
    {
        "pregunta": "La protección activa contra incendios tiene un papel principalmente preventivo.",
        "tipo": "multiple",
        "opciones": "",
        "respuesta_correcta": "Fals",
        "justificacion": "La protección activa desempeña un papel curativo (detección y extinción). La preventiva es la pasiva."
    },
    {
        "pregunta": "La protección pasiva tiene como objetivo permitir la evacuación y confinar el fuego.",
        "tipo": "multiple",
        "opciones": "",
        "respuesta_correcta": "Vertader",
        "justificacion": "Busca resistir el incendio un tiempo determinado para facilitar la evacuación y evitar la propagación."
    },
    {
        "pregunta": "Una función primaria de la estructura es aislar térmicamente el edificio de forma directa.",
        "tipo": "multiple",
        "opciones": "",
        "respuesta_correcta": "Fals",
        "justificacion": "La estructura lo hace de forma indirecta al sustentar fachadas y cubiertas."
    },
    {
        "pregunta": "En las estructuras industriales, el factor económico suele ser el más determinante.",
        "tipo": "multiple",
        "opciones": "",
        "respuesta_correcta": "Vertader",
        "justificacion": "Minimizar costes y plazos suele ser la prioridad en la industria."
    },
    {
        "pregunta": "Las estructuras de hormigón requieren siempre pintura ignífuga para alcanzar alta resistencia al fuego.",
        "tipo": "multiple",
        "opciones": "",
        "respuesta_correcta": "Fals",
        "justificacion": "No requieren pintura si cuentan con los recubrimientos de hormigón adecuados."
    },
    {
        "pregunta": "El acero permite montajes rápidos pero requiere mantenimiento y protección contra el fuego.",
        "tipo": "multiple",
        "opciones": "",
        "respuesta_correcta": "Vertader",
        "justificacion": "Es ligero y rápido, pero vulnerable a la corrosión y al fuego."
    },
    {
        "pregunta": "Los forjados unidireccionales transmiten las cargas en dos direcciones.",
        "tipo": "multiple",
        "opciones": "",
        "respuesta_correcta": "Fals",
        "justificacion": "Transmiten cargas en una sola dirección hacia las vigas."
    },
    {
        "pregunta": "Las placas alveolares son adecuadas para grandes luces y sobrecargas.",
        "tipo": "multiple",
        "opciones": "",
        "respuesta_correcta": "Vertader",
        "justificacion": "Se usan habitualmente en aparcamientos y almacenes por su alta capacidad."
    },
    {
        "pregunta": "El forjado de chapa colaborante destaca por su excelente comportamiento térmico y ante el fuego.",
        "tipo": "multiple",
        "opciones": "",
        "respuesta_correcta": "Fals",
        "justificacion": "Tiene mal comportamiento térmico, acústico y frente al fuego."
    }
]

def append_questions():
    # Read existing last ID
    last_id = 0
    existing_rows = []
    
    if os.path.exists(csv_path):
        with open(csv_path, 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            existing_rows = list(reader)
            for row in existing_rows:
                try:
                    num = int(row['numero'])
                    if num > last_id:
                        last_id = num
                except:
                    pass
    
    print(f"Last ID found: {last_id}")
    
    # Append new questions
    with open(csv_path, 'a', newline='', encoding='utf-8') as f:
        # If file was empty/new, write header, but we assume it exists and has header because we read it
        writer = csv.writer(f)
        
        count = 0
        for q in new_questions:
            last_id += 1
            row = [
                last_id,
                q['pregunta'],
                q['tipo'],
                q['opciones'],
                q['respuesta_correcta'],
                q['justificacion']
            ]
            writer.writerow(row)
            count += 1
            
    print(f"Added {count} new questions to {csv_path}")

if __name__ == "__main__":
    append_questions()
