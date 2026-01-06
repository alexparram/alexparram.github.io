
import csv
import os

# Configuración de asignatura
subject = "CAI"

# File path
csv_path = os.path.join(os.path.dirname(__file__), "..", "csv", subject, f"{subject}_preguntas.csv")

# Manually created justifications for questions 1-91 based on common knowledge/logic
# Since we don't have the exact source text easily mapped for these old questions yet.
justifications = {
    1: "El POUM (Pla d’Ordenació Urbanística Municipal) es el instrumento de planeamiento general que organiza integralmente el territorio del municipio.",
    2: "El suelo urbanizable es aquel que requiere de transformación urbanística (plan parcial, reparcelación, urbanización) para ser apto para la edificación. No es apto directamente.",
    3: "Un solar es una parcela de suelo urbano que además está urbanizada (tiene servicios: agua, luz, acceso rodado..). No todo suelo urbano es solar (ej. urbano no consolidado).",
    4: "Los PDU (Planes Directores Urbanísticos) tienen alcance supramunicipal y coordinan infraestructuras y protección del territorio.",
    5: "El suelo urbano se divide en Consolidado (solar) y No Consolidado (necesita reforma interior o completar urbanización). Delimitado/No delimitado aplica más a urbanizable.",
    6: "Las figuras son Planes Directores, POUM, Normas Subsidiarias, etc. Lo citado (alineación, aislada) son sistemas de ordenación de la edificación.",
    7: "La reparcelación permite la sustitución por indemnización o traslado de aprovechamiento en ciertos casos.",
    8: "El POUM define también la estructura general, cataloga bienes, prevé infraestructuras, etc. No es su 'única' función clasificar.",
    9: "Suelo No Urbanizable es aquel protegido por sus valores o riesgos, impropio para el desarrollo urbano.",
    10: "El certificado suele informar del régimen urbanístico vigente.",
    11: "El forjado colaborante es un sistema mixto hormigón-acero, habitualmente unidireccional (la chapa grecada marca la dirección).",
    12: "Es el camino de cargas: Forjado -> Vigas (o Soportes) -> Pilares -> Cimentación -> Terreno.",
    13: "Ventajas clave de la estructura metálica. Desventaja: protección fuego y corrosión.",
    14: "Los bidireccionales pueden ser in situ (losa maciza) o reticulares (casetones in situ o recuperables).",
    15: "La madera es anisotrópica (distintas propiedades según dirección), lo que complica las uniones y la transmisión de esfuerzos.",
    16: "Todos esos factores (económico, estético, plazo, disponibilidad) son determinantes en la elección estructural.",
    17: "El hormigón tiene buena resistencia al fuego por sí mismo (recubrimiento). El acero sí requiere pintura o protección casi siempre.",
    18: "La chapa trabaja a tracción (positivo) y sirve de encofrado perdido.",
    19: "Los casetones recuperables son típicos de forjados reticulares (bidireccionales), crean los nervios en dos direcciones.",
    20: "Las bovedillas se usan entre viguetas en forjados unidireccionales. En reticulares se usan casetones.",
    21: "Suelos granulares (cohesión nula o baja): gravas y arenas. Suelos finos (cohesivos): limos y arcillas.",
    22: "Suelos finos tienen >35% de paso por tamiz #200 (0.075mm).",
    23: "Las arcillas son duras en seco pero pierden resistencia con humedad y consolidan lentamente (asientos diferidos).",
    24: "El CTE obliga a realizar el estudio geotécnico.",
    25: "La tensión admisible es el parámetro clave para dimensionar la cimentación.",
    26: "Zapatas superficiales suelen estar a poca profundidad. Si hay que ir más profundo se usan pozos o pilotes.",
    27: "Cimentación profunda (pilotes) transmite por punta y por rozamiento lateral (fuste).",
    28: "Semiprofundas (pozos) son intermedias.",
    29: "Describe el ensayo SPT (Standard Penetration Test).",
    30: "Limos son finos, con poca plasticidad comparados con arcillas.",
    31: "Protección activa = Detección + Extinción (actúa).",
    32: "Protección pasiva = Resistencia estructural + Sectorización + Evacuación (previene/contiene).",
    33: "Detectores y rociadores son Activa. Pasiva son puertas RF, muros, etc.",
    34: "El RSCIEI (RD 2267/2004) regula la seguridad industrial.",
    35: "Establece 5 tipos: A, B, C, D, E.",
    36: "Si comparte edificio es Tipo A.",
    37: "Tipo E es espacio abierto (patio), Tipo D es abierto con cubierta.",
    38: "Definición correcta de sector de incendio.",
    39: "Tipo C es en edificio aislado (>3m). Si está adosado es Tipo B.",
    40: "Correcto, forman parte de la arquitectura y construcción (Pasiva).",
    41: "Aislamiento es 'I'. Integridad (paso de llamas) es 'E'.",
    42: "Capacidad portante es 'R' (Resistencia mecánica).",
    43: "Correcto, 'I' impide la transmisión de calor a la cara no expuesta.",
    44: "Nivel de Riesgo Intrínseco: Bajo (1,2), Medio (3,4,5), Alto (6,7,8).",
    45: "Las tablas del RSCIEI limitan la superficie máx. del sector según Tipología y Riesgo.",
    46: "Mirar tabla RSCIEI. Para Tipo B Riesgo Medio suelo ser menor, o depende de si hay rociadores.",
    47: "Definición estándar de fuego.",
    48: "Falta la Energía de Activación. La Reacción en Cadena es del Tetraedro.",
    49: "Si falta uno, no hay fuego (Triángulo).",
    50: "La energía de activación inicia. La reacción en cadena mantiene.",
    51: "Comburente es el que oxida (oxígeno). Combustible es el que arde.",
    52: "Al revés. Combustible arde, Comburente oxida.",
    53: "Tetraedro es para explicar la llama y la continuidad.",
    54: "Clase A: Sólidos (brasas).",
    55: "Clase B: Líquidos.",
    56: "Químico que actúa sobre el fuego.",
    57: "Dilución o Desalimentación disminuye el combustible. O dilución de mezcla de gases.",
    58: "Inhibición ataca la reacción en cadena (radicales libres).",
    59: "Eso es Autoignición. Inflamación requiere llama externa (flash point).",
    60: "Definición de punto de inflamación vs ignición.",
    61: "Minimizar transporte es un objetivo clave del Layout.",
    62: "Flujos limpios y seguros.",
    63: "Facilita la carga/descarga.",
    64: "Implantación Proceso incluye zonas auxiliares. Maquinaria es más específico.",
    65: "Distribución en Planta es el plano general. Implantación proceso es más de la zona fabril.",
    66: "Accesos, carga/descarga, conexión con viales.",
    67: "Optimización del espacio.",
    68: "Seguridad y ergonomía, menos desplazamientos innecesarios.",
    69: "Normativa básica de seguridad laboral.",
    70: "Obligatorio vestuarios si hay ropa especial.",
    71: "Si no hay ropa especial, basta con colgadores.",
    72: "Altura mínima suele ser 2,5m o 3m. 2m es muy poco.",
    73: "Son 2m2 superficie libre por trabajador y 10m3 volumen.",
    74: "Plano general de toda la actividad.",
    75: "El plano de parcela debe incluir todo lo que hay en ella.",
    76: "Justificación urbanística es necesaria.",
    77: "No hay pregunta. Se asume falsa/vacía.",
    78: "El transporte se define mejor en el Diagrama de Flujo o Recorrido.",
    79: "Maquinaria se centra en las máquinas. El transporte es flujo.",
    80: "Almacenes también tienen capacidad.",
    81: "Unidades físicas por tiempo (kg/h, u/h).",
    82: "Potencia Instalada es la suma total. La de contratación/diseño aplica simultaneidad.",
    83: "Espacio compartido (ej. pasillo entre máquinas).",
    84: "Mantenimiento requiere acceso, puede solaparse con pasillos pero debe estar previsto.",
    85: "Pregunta vacía.",
    86: "Faltan los valores correctos (2.5m altura, 2m2 sup libre).",
    87: "Espacio propio es el volumen físico de la máquina. Lo descrito parece 'espacio de evolución' o similar.",
    88: "Misma que la 72.",
    89: "Definición de punto de inflamación/ignición repetida.",
    90: "Definición correcta Activa.",
    91: "Definición correcta Pasiva."
}

rows = []
header = []

if os.path.exists(csv_path):
    with open(csv_path, 'r', encoding='utf-8') as f:
        reader = csv.reader(f)
        all_rows = list(reader)
        if all_rows:
            header = all_rows[0]
            rows = all_rows[1:]

if 'justificacion' not in header:
    header.append('justificacion')
    for row in rows:
        row.append('')

just_idx = header.index('justificacion')
num_idx = header.index('numero')

updated_count = 0
for row in rows:
    try:
        num = int(row[num_idx])
        if num in justifications:
            # Only update if empty or override? User asked to add.
            current_val = row[just_idx].strip()
            if not current_val:
                row[just_idx] = justifications[num]
                updated_count += 1
    except:
        pass

with open(csv_path, 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerow(header)
    writer.writerows(rows)

print(f"Updated {updated_count} rows with justifications.")
