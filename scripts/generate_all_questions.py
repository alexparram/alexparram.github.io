import csv
import os

# Configuración de asignatura
subject = "CAI"

csv_path = os.path.join(os.path.dirname(__file__), "..", "csv", subject, f"{subject}_preguntas.csv")

# Define a large list of new questions
new_questions = [
    # Tema 11.1 - Localización
    {"p": "La teoría de Von Thünen (1826) basa la localización en la distancia al núcleo central (mercado).", "r": "Vertader", "j": "Modelo de anillos concéntricos alrededor de la ciudad, basado en costes de transporte y caducidad."},
    {"p": "El modelo de Weber (1929) busca maximizar los ingresos por ventas.", "r": "Fals", "j": "Busca la minimización de los costes de transporte (recursos vs mercado)."},
    {"p": "Harold Hotelling (1929) propuso la teoría de la competencia lineal.", "r": "Vertader", "j": "Explica la localización de competidores en un espacio lineal (ej. vendedores en una playa)."},
    {"p": "Los parámetros de localización de ámbito general se refieren a la ubicación dentro de una ciudad.", "r": "Fals", "j": "Se refieren a provincia o región. Los de ámbito particular se refieren al lugar en la ciudad."},
    {"p": "La disponibilidad de mano de obra es un parámetro humano de localización.", "r": "Vertader", "j": "Es un factor clave junto con el coste laboral y la conflictividad."},

    # Tema 11.2 - Polígonos
    {"p": "Un polígono industrial es un sector urbanizado con servicios para actividades industriales.", "r": "Vertader", "j": "Facilita el crecimiento industrial y minimiza el impacto ambiental."},
    {"p": "Las infraestructuras de un polígono incluyen solo agua y electricidad.", "r": "Fals", "j": "Incluyen viarios, alcantarillado, gas, comunicaciones, etc."},
    {"p": "La gestión de los polígonos industriales no es relevante para su éxito.", "r": "Fals", "j": "La gestión (mantenimiento, seguridad, servicios) es clave para la competitividad."},
    {"p": "Los polígonos industriales buscan aislar completamente la industria de las ciudades.", "r": "Fals", "j": "Buscan ordenarla, pero a menudo están conectados o integrados en áreas metropolitanas."},
    {"p": "Los 'minipolígonos' son una tipología de polígono industrial.", "r": "Vertader", "j": "Existen diversas tipologías según tamaño y ubicación."},

    # Tema 1 - Diagramas
    {"p": "El Diagrama de Definición de la Actividad se considera una 'caja negra'.", "r": "Vertader", "j": "Define inputs y outputs globales sin entrar en el detalle del proceso."},
    {"p": "En el Diagrama de Actividades, los suministros se sitúan en la parte inferior.", "r": "Fals", "j": "Los suministros van arriba. Abajo van los residuos y emisiones."},
    {"p": "Las Materias Auxiliares forman parte del producto final obtenido.", "r": "Fals", "j": "Intervienen en el proceso (ej. aceite máquinas) pero no forman parte del producto final."},
    {"p": "El Diagrama de Flujo define cuantitativamente el proceso productivo.", "r": "Vertader", "j": "Aplica cantidades a los flujos definidos en el diagrama de bloques."},
    {"p": "El Diagrama de Maquinaria aplica la maquinaria requerida a cada bloque o proceso.", "r": "Vertader", "j": "Identifica capacidad máxima, producción y consumos de cada máquina."},
    {"p": "Los residuos municipales nunca pueden proceder de una actividad industrial.", "r": "Fals", "j": "Pueden proceder de oficinas, comedores, etc. dentro de la industria (asimilables a domésticos)."},
    {"p": "El código CER para residuos municipales es 20.03.01.", "r": "Vertader", "j": "Es el código del catálogo europeo para residuos mezclados municipales."},
    {"p": "El Diagrama de Bloques define la ubicación física de las máquinas.", "r": "Fals", "j": "Define la secuencia del proceso, no la ubicación física (eso es el Layout)."},
    {"p": "La unidad de trabajo puede expresarse en 'unidades/año' o 'unidades/hora'.", "r": "Vertader", "j": "Son formas estándar de definir cuantitativamente los inputs y outputs."},
    {"p": "Los residuos industriales deben ser gestionados por una empresa acreditada.", "r": "Vertader", "j": "No pueden tirarse a la basura municipal convencional si no son asimilables."},

    # Tema 2 - Fichas Maquinas
    {"p": "El objetivo de las fichas de máquinas es cumplir con el RD 486/1997 de Seguridad y Salud.", "r": "Vertader", "j": "Establece las condiciones mínimas de seguridad y salud en los lugares de trabajo."},
    {"p": "En los croquis de las fichas se debe utilizar el sistema americano (Planta y Alzado).", "r": "Fals", "j": "Se debe utilizar el sistema europeo: Alzado y Planta."},
    {"p": "Las cotas en los planos de fichas deben estar en milímetros sin decimales.", "r": "Fals", "j": "Deben estar en metros con dos decimales (según CTE)."},
    {"p": "La potencia eléctrica a indicar en la ficha es solo la potencia nominal.", "r": "Fals", "j": "Puede ser necesario indicar la potencia absorbida o de conexión."},
    {"p": "Se deben acotar los espacios de uso propio, exclusivo y compartido.", "r": "Vertader", "j": "Es necesario para el correcto diseño del layout y seguridad."},
    {"p": "La ficha de máquina contiene información textual y gráfica.", "r": "Vertader", "j": "Incluye características técnicas y croquis de implantación."},
    {"p": "No es necesario posicionar las entradas de suministros en el croquis de la máquina.", "r": "Fals", "j": "Es vital para prever las instalaciones de conexión."},

    # Tema 3 - Distribución en Planta (Layout)
    {"p": "El objetivo de la distribución en planta es ordenar racionalmente los elementos productivos.", "r": "Vertader", "j": "Busca eficiencia, minimizar distancias y seguridad."},
    {"p": "La 'disposición por producto' agrupa máquinas similares en departamentos.", "r": "Fals", "j": "Esa es la 'disposición por proceso'. La 'por producto' sigue la secuencia de fabricación (cadena)."},
    {"p": "La distribución por producto es muy flexible ante cambios de diseño.", "r": "Fals", "j": "Es rígida; si cambia el producto, hay que cambiar toda la línea."},
    {"p": "La célula de tecnología busca combinar la eficiencia de la línea con la flexibilidad del proceso.", "r": "Vertader", "j": "Agrupa familias de piezas con procesos similares."},
    {"p": "Uno de los objetivos del layout es utilizar eficientemente el espacio cúbico (vertical).", "r": "Vertader", "j": "No solo la superficie en planta, también la altura."},
    {"p": "El Plano de Implantación define la ubicación exacta de la maquinaria.", "r": "Vertader", "j": "Verifica el aprovechamiento de la nave y define espacios."},
    {"p": "La distribución por proceso es adecuada para grandes volúmenes de un producto estandarizado.", "r": "Fals", "j": "Es adecuada para bajos volúmenes y alta variedad (lotes pequeños)."},
    {"p": "El Systematic Layout Planning (SLP) es una metodología para diseñar distribuciones.", "r": "Vertader", "j": "Es un método estándar para resolver problemas de layout."},
    {"p": "En igualdad de condiciones, es mejor la distribución que maximiza la distancia recorrida.", "r": "Fals", "j": "Se busca minimizar la distancia recorrida por materiales y personas."},
    {"p": "Un layout deficiente puede incrementar los costes de producción.", "r": "Vertader", "j": "Debido a transportes innecesarios, tiempos muertos y mayor mano de obra."},

    # Tema 4 - Terreny
    {"p": "Los suelos granulares tienen un porcentaje de finos inferior al 35%.", "r": "Vertader", "j": "Si tienen menos del 35% de limos/arcillas, dominan las propiedades granulares."},
    {"p": "Las rocas sedimentarias se forman por la solidificación del magma.", "r": "Fals", "j": "Esas son las rocas ígneas. Las sedimentarias se forman por deposición."},
    {"p": "El estudio geotécnico determina las propiedades del suelo y el nivel freático.", "r": "Vertader", "j": "Es esencial para diseñar la cimentación."},
    {"p": "La cimentación forma parte del sistema resistent del edificio.", "r": "Vertader", "j": "Transmite las cargas de la estructura al terreno."},
    {"p": "Los muros de contención no se consideran parte de la cimentación o contacto con terreno.", "r": "Fals", "j": "Son elementos de contacto con el terreno y contención de tierras."},
    {"p": "La meteorización física es un proceso de formación de suelos.", "r": "Vertader", "j": "Desintegra la roca madre en partículas más pequeñas."},
    
    # Tema 5 - Fuego (Ampliación)
    {"p": "La reacción de oxidación del hierro es una combustión rápida con llama.", "r": "Fals", "j": "Es una oxidación lenta, sin emisión de luz considerable."},
    {"p": "El comburente más común es el nitrógeno del aire.", "r": "Fals", "j": "Es el oxígeno (21% del aire)."},
    {"p": "Por debajo del 15% de oxígeno, generalmente el fuego se apaga.", "r": "Vertader", "j": "El fuego necesita una proporción mínima de oxígeno para mantenerse."},
    {"p": "La inhibición consiste en eliminar los radicales libres de la reacción en cadena.", "r": "Vertader", "j": "Es el mecanismo de extinción química (ej. polvos, halones)."},
    {"p": "La sofocación elimina el calor del fuego.", "r": "Fals", "j": "La sofocación elimina o desplaza el comburente (oxígeno)."},
    {"p": "El rango entre el Límite Inferior (LII) y Superior (LSI) es el rango de inflamabilidad.", "r": "Vertader", "j": "Solo dentro de este rango la mezcla aire-combustible puede arder."},
    {"p": "Los sólidos entran en combustión directamente en estado sólido.", "r": "Fals", "j": "Deben gasificar primero (pirólisis) para que ardan los gases."},
    {"p": "La electricidad estática puede ser una fuente de ignición.", "r": "Vertader", "j": "Puede generar chispas suficientes para iniciar la combustión."},

    # Tema 6 - Protección Pasiva
    {"p": "La protección pasiva incluye rociadores y extintores.", "r": "Fals", "j": "Esos son protección activa. La pasiva son elementos constructivos (muros, puertas)."},
    {"p": "El RD 2267/2004 aplica a establecimientos industriales.", "r": "Vertader", "j": "Es el Reglamento de Seguridad contra Incendios en Establecimientos Industriales (RSCIEI)."},
    {"p": "Un edificio Tipo C comparte estructura con otros edificios.", "r": "Fals", "j": "Tipo C es aislado (distancia > 3m). Tipo A o B comparten o están adosados."},
    {"p": "Un edificio Tipo A ocupa solo una parte de un edificio con otros usos.", "r": "Vertader", "j": "Es el caso de mayor riesgo de propagación a otros usuarios."},
    {"p": "El Nivel de Riesgo Intrínseco se calcula en base a la Carga de Fuego (Qs).", "r": "Vertader", "j": "Densidad de carga de fuego ponderada y corregida."},
    {"p": "La estabilidad al fuego se representa con la letra E.", "r": "Fals", "j": "Estabilidad es R (Resistencia mecánica). E es Integridad (paso de llamas/gases). I es Aislamiento."},
    {"p": "REI 120 significa que el elemento mantiene Resistencia, Integridad y Aislamiento por 120 min.", "r": "Vertader", "j": "Nomenclatura estándar de resistencia al fuego."},
    {"p": "La sectorización tiene como fin confinar el incendio en un espacio limitado.", "r": "Vertader", "j": "Evita la propagación a todo el edificio."},
    {"p": "Si una zona administrativa en una industria supera los 250m2, se aplica el CTE-DB-SI.", "r": "Vertader", "j": "Deja de aplicarse el RSCIEI para esa zona específica."},
    {"p": "Las zonas de alojamiento de personal no requieren sectorización independiente.", "r": "Fals", "j": "Siempre deben constituir un sector de incendio independiente."},

    # Tema 7 - Evacuación
    {"p": "El monóxido de carbono (CO) es la principal causa de muerte en incendios.", "r": "Vertader", "j": "Provoca asfixia química al unirse a la hemoglobina."},
    {"p": "La ocupación (P) se determina exclusivamente por la superficie del sector.", "r": "Fals", "j": "Se basa en la documentación laboral, aunque el CTE da densidades por defecto."},
    {"p": "En edificios Tipo B con riesgo medio/alto y >50 personas, se exigen 2 salidas.", "r": "Vertader", "j": "Requisito adicional del RSCIEI sobre el CTE."},
    {"p": "Una escalera protegida debe tener ventilación para evitar humos.", "r": "Vertader", "j": "Puede ser natural o mediante presión diferencial."},
    {"p": "La longitud máxima de recorrido de evacuación es fija e independiente del riesgo.", "r": "Fals", "j": "Depende del Nivel de Riesgo Intrínseco (Bajo, Medio, Alto). A mayor riesgo, menor distancia."},
    {"p": "Una escalera especialmente protegida cuenta con un vestíbulo de independencia.", "r": "Vertader", "j": "El vestíbulo (SAS) añade seguridad extra ante el humo."},
    {"p": "Las escaleras mecánicas pueden contabilizarse siempre como vía de evacuación.", "r": "Fals", "j": "Generalmente no, salvo excepciones muy concretas y controladas."},
    {"p": "El pánico puede ser consecuencia de la inhalación de gases tóxicos o hipoxia.", "r": "Vertader", "j": "La desorientación y falta de juicio son síntomas comunes."},
    {"p": "Las rampas no son válidas como recorrido de evacuación.", "r": "Fals", "j": "Las rampas que cumplen normativa sí son válidas."},
    {"p": "La altura de evacuación influye en la exigencia de escaleras protegidas.", "r": "Vertader", "j": "A mayor altura, más requisitos de protección para la escalera."},

    # General / Structures (Extra to reach 100)
    {"p": "El acero tiene un buen comportamiento natural ante el fuego.", "r": "Fals", "j": "Pierde resistencia rápidamente con temperatura, requiere protección."},
    {"p": "La madera es un material isótropo.", "r": "Fals", "j": "Es anisótropo (propiedades diferentes según dirección de fibra)."},
    {"p": "El hormigón pretensado utiliza armaduras activas traccionadas previamente.", "r": "Vertader", "j": "Mejora el comportamiento a tracción del hormigón."},
    {"p": "Las uniones soldadas en acero son más fáciles de ejecutar en obra que las atornilladas.", "r": "Fals", "j": "Requieren soldadores cualificados y control, las atornilladas son más rápidas en obra."},
    {"p": "La estructura debe soportar cargas fijas (peso propio) y variables (uso, viento, nieve).", "r": "Vertader", "j": "Es la función básica de sustento."},
    {"p": "En naves industriales, la estética es siempre el factor más importante.", "r": "Fals", "j": "Suele primar el coste, plazo y funcionalidad."},
    {"p": "Los forjados reticulares son unidireccionales.", "r": "Fals", "j": "Son bidireccionales, transmiten cargas en dos direcciones."},
    {"p": "La chapa colaborante actúa como encofrado y armadura de positivo.", "r": "Vertader", "j": "La chapa de acero trabaja a tracción y el hormigón a compresión."},
    {"p": "Las correas son elementos estructurales que soportan la cubierta.", "r": "Vertader", "j": "Transmiten la carga de la cubierta a los pórticos."},
    {"p": "Una cercha o armadura es un elemento estructural macizo.", "r": "Fals", "j": "Está formada por barras unidas en nudos (triangulación), es aligerada."},
    {"p": "La flecha es la deformación vertical de una viga.", "r": "Vertader", "j": "Debe limitarse por normativa."},
    {"p": "El pandeo es un fenómeno de inestabilidad en elementos traccionados.", "r": "Fals", "j": "Se produce en elementos comprimidos esbeltos (ej. pilares)."},
    {"p": "Las uniones en madera son puntos críticos de la estructura.", "r": "Vertader", "j": "Debido a la anisotropía y dificultad de transmitir momentos."},
    {"p": "El hormigón es un material que trabaja muy bien a tracción.", "r": "Fals", "j": "Trabaja bien a compresión, por eso se arma con acero para la tracción."},
    {"p": "Los pilares prefabricados de hormigón agilizan el montaje.", "r": "Vertader", "j": "Es una de las principales ventajas de la prefabricación."},
    {"p": "La carga de nieve es una acción accidental.", "r": "Fals", "j": "Es una acción variable climática, no accidental (como sismo o incendio)."},
    {"p": "El CTE es el Código Técnico de la Edificación.", "r": "Vertader", "j": "Normativa de referencia en España."},
    {"p": "La vida útil de una estructura industrial suele ser infinita.", "r": "Fals", "j": "Se diseña para una vida útil determinada (ej. 50 años)."},
    {"p": "El mantenimiento de la estructura de acero es menor que la de hormigón.", "r": "Fals", "j": "El acero suele requerir más mantenimiento (pintura) que el hormigón."}
]

def append_multiple_questions():
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
    
    print(f"Starting after ID: {last_id}")
    
    # Append
    with open(csv_path, 'a', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        count = 0
        for q in new_questions:
            last_id += 1
            # "numero", "pregunta", "tipo", "opciones", "respuesta_correcta", "justificacion"
            row = [
                last_id,
                q['p'],
                "multiple",
                "",
                q['r'],
                q['j']
            ]
            writer.writerow(row)
            count += 1
            
    print(f"Successfully added {count} new questions.")

if __name__ == "__main__":
    append_multiple_questions()
