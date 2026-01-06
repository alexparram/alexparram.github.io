import csv
import os

# Configuración de asignatura
subject = "CAI"

# File paths
csv_path = os.path.join(os.path.dirname(__file__), "..", "csv", subject, f"{subject}_preguntas.csv")
text_path = os.path.join(os.path.dirname(__file__), "..", "csv", subject, "all_theory_text.txt")

# Define 100+ new questions
new_questions = [
    # Tema 11.3 - Urbanisme Planning
    {"p": "El Planeamiento Urbanístico Municipal es competencia exclusiva del Estado.", "r": "Fals", "j": "Es competencia municipal (con aprobación definitiva autonómica)."},
    {"p": "Los Planes Directores Urbanísticos (PDU) tienen un ámbito supramunicipal.", "r": "Vertader", "j": "Coordinan la planificación de varios municipios o comarcas."},
    {"p": "El POUM clasifica el suelo en Urbano, Urbanizable y No Urbanizable.", "r": "Vertader", "j": "Es la función básica de clasificación del suelo del planeamiento general."},
    {"p": "Un Plan Parcial desarrolla la ordenación de un sector de suelo urbano consolidado.", "r": "Fals", "j": "Los Planes Parciales desarrollan suelo urbanizable. En urbano se usan Planes Especiales o de Mejora Urbana."},
    {"p": "La 'Clasificación' del suelo determina su régimen jurídico básico (Urbano/Urbanizable...).", "r": "Vertader", "j": "Divide el término municipal en estas clases."},
    {"p": "La 'Calificación' del suelo asigna usos y tipologías edificatorias (zonas).", "r": "Vertader", "j": "Define qué se puede construir (industrial, residencial, verde...) en cada zona."},
    {"p": "Un solar es una parcela que cuenta con todos los servicios urbanísticos básicos.", "r": "Vertader", "j": "Acceso rodado, agua, saneamiento y suministro eléctrico."},
    {"p": "El suelo urbanizable delimitado puede edificarse directamente sin plan parcial.", "r": "Fals", "j": "Requiere desarrollo mediante Plan Parcial y Proyecto de Reparcelación/Urbanización."},
    {"p": "Los Planes Especiales Urbanísticos pueden utilizarse para proteger recintos históricos.", "r": "Vertader", "j": "Es una de sus funciones (PE de protección del patrimonio)."},
    {"p": "La licencia de obras la concede el colegio de arquitectos.", "r": "Fals", "j": "La concede el Ayuntamiento."},
    {"p": "El Proyecto de Urbanización define las obras de viales y servicios, no la edificación.", "r": "Vertader", "j": "Se centra en el espacio público e infraestructuras."},
    {"p": "En el suelo no urbanizable está prohibida cualquier tipo de construcción.", "r": "Fals", "j": "Se permiten construcciones ligadas a la explotación agrícola/ganadera o de interés público, con limitaciones."},
    {"p": "El aprovechamiento urbanístico se expresa habitualmente en m2 de techo / m2 de suelo.", "r": "Vertader", "j": "Es el índice de edificabilidad."},
    {"p": "La reparcelación tiene como objeto distribuir justamente los beneficios y cargas del planeamiento.", "r": "Vertader", "j": "Equidistribución entre propietarios del sector."},
    {"p": "La cesión de suelo para zonas verdes y equipamientos es obligatoria y gratuita.", "r": "Vertader", "j": "Es una de las cargas de la transformación urbanística."},
    {"p": "La actividad industrial se puede implantar en cualquier zona calificada como residencial.", "r": "Fals", "j": "Solo si es compatible (ej. talleres pequeños), pero la industria pesada requiere zona industrial."},
    {"p": "El Catastro es un registro administrativo que depende del Ministerio de Hacienda.", "r": "Vertader", "j": "Recoge la descripción física, económica y jurídica de los bienes inmuebles."},
    {"p": "La referencia catastral es un identificador único de cada inmueble.", "r": "Vertader", "j": "Permite localizarlo inequívocamente."},

    # CAS - Estructuras
    {"p": "La función primaria de una estructura es aislar térmicamente el edificio.", "r": "Fals", "j": "Su función es resistir cargas. El aislamiento es función de los cerramientos."},
    {"p": "Una estructura debe ser estable, resistente y rígida (poco deformable).", "r": "Vertader", "j": "Son los tres requisitos básicos de la mecánica estructural."},
    {"p": "El factor económico no suele influir en el diseño de estructuras industriales.", "r": "Fals", "j": "Es determinante. Se busca la solución más rentable que cumpla los requisitos."},
    {"p": "El acero resiste muy bien la tracción pero mal la compresión por pandeo.", "r": "Vertader", "j": "Los elementos esbeltos de acero pandean fácilmente a compresión."},
    {"p": "El hormigón en masa (sin armar) resiste perfectamente los esfuerzos de tracción.", "r": "Fals", "j": "Su resistencia a tracción es despreciable; por eso se arma con acero."},
    {"p": "El hormigón pretensado reduce la fisuración respecto al hormigón armado convencional.", "r": "Vertader", "j": "La compresión inicial cierra las posibles fisuras de tracción."},
    {"p": "El peso específico del acero es aproximadamente 7850 kg/m3.", "r": "Vertader", "j": "Es mucho más denso que el hormigón (2500 kg/m3)."},
    {"p": "Las uniones soldadas permiten mayor tolerancia en el montaje que las atornilladas.", "r": "Vertader", "j": "Se puede ajustar in situ soldando. Los tornillos requieren agujeros precisos (o rasgados)."},
    {"p": "La estructura metálica requiere menos mantenimiento que la de hormigón.", "r": "Fals", "j": "Requiere protección periódica contra corrosión y fuego."},
    {"p": "El forjado colaborante utiliza chapa grecada y hormigón.", "r": "Vertader", "j": "Forman una sección mixta."},
    {"p": "Un forjado unidireccional transmite la carga en dos direcciones perpendiculares.", "r": "Fals", "j": "Solo en una dirección, hacia las vigas de apoyo."},
    {"p": "Las placas alveolares son elementos prefabricados de hormigón pretensado.", "r": "Vertader", "j": "Muy usadas en industria por sus grandes luces y capacidad de carga."},
    {"p": "La capa de compresión en un forjado de viguetas tiene función de reparto de cargas.", "r": "Vertader", "j": "Evita el punzonamiento y solidariza el conjunto."},
    {"p": "Los forjados reticulares son un tipo de forjado bidireccional.", "r": "Vertader", "j": "Forman una retícula de nervios en dos direcciones."},
    {"p": "La bovedilla es el elemento resistente principal del forjado.", "r": "Fals", "j": "Es un elemento aligerante. El resistente es la vigueta/nervio."},
    {"p": "En estructuras industriales, la estética suele primar sobre la funcionalidad.", "r": "Fals", "j": "La funcionalidad y el coste son prioritarios."},
    {"p": "La madera laminada encolada permite salvar luces mayores que la madera aserrada maciza.", "r": "Vertader", "j": "Permite fabricar vigas de gran canto y longitud sin defectos."},
    {"p": "El pandeo lateral (vuelco) es un riesgo en vigas metálicas esbeltas.", "r": "Vertader", "j": "Requiere arriostramiento lateral."},
    {"p": "Las correas suelen ser perfiles conformados en frío (tipo Z o C).", "r": "Vertader", "j": "Son ligeros y eficientes para soportar la cubierta."},
    {"p": "Un pórtico triarticulado es una estructura isostática.", "r": "Vertader", "j": "Tiene tres articulaciones (dos en apoyos, una en clave), determinable por estática."},
    
    # Diagramas (Detailed)
    {"p": "En el Diagrama de Bloques, los almacenes se representan como triángulos invertidos habitualmente.", "r": "Vertader", "j": "Es una convención común (aunque el texto dice que se consideran procesos/bloques, la forma gráfica suele diferir)."},
    {"p": "Un output doméstico de una industria puede ser el papel de oficina.", "r": "Vertader", "j": "Es un residuo asimilable a urbano."},
    {"p": "El agua de proceso siempre se convierte en vapor y no genera vertido.", "r": "Fals", "j": "Muchas veces genera aguas residuales industriales que requieren depuración."},
    {"p": "La capacidad de producción de una máquina nunca puede superar la de la línea.", "r": "Fals", "j": "Puede tener mayor capacidad y trabajar menos horas (cuello de botella en otro lado)."},
    {"p": "El diagrama de flujo debe indicar las cantidades de materia que pasan por cada línea.", "r": "Vertader", "j": "Es su diferencia principal con el de bloques simple."},
    {"p": "Los residuos peligrosos se pueden mezclar con los banales para ahorrar costes.", "r": "Fals", "j": "Está terminantemente prohibido y penado. Deben gestionarse por separado."},
    {"p": "El Balance de Materias cumple que Entradas = Salidas + Acumulación.", "r": "Vertader", "j": "Principio de conservación de la masa (Lavoisier)."},
    {"p": "En un diagrama de bloques, las flechas indican la dirección del flujo de materiales.", "r": "Vertader", "j": "Conectan los procesos secuencialmente."},
    
    # Fuego / Pasiva / Evacuacion (More Depth)
    {"p": "La temperatura de autoignición siempre es menor que la de inflamación.", "r": "Fals", "j": "Es mayor. Es la temperatura a la que arde espontáneamente sin llama externa."},
    {"p": "Una reacción endotérmica desprende calor.", "r": "Fals", "j": "Absorbe calor. La combustión es exotérmica."},
    {"p": "El 'flashover' es la ignición súbita generalizada de todos las superficies combustibles.", "r": "Vertader", "j": "Marca el paso a la fase de incendio totalmente desarrollado."},
    {"p": "Los detectores iónicos son más rápidos para humos invisibles que los ópticos.", "r": "Vertader", "j": "Detectan partículas más pequeñas de combustión rápida."},
    {"p": "Una BIE de 25mm es de manguera semirrígida.", "r": "Vertader", "j": "Permite usarse sin desenrollar del todo. La de 45mm es plana."},
    {"p": "Los rociadores automáticos (sprinklers) se activan todos a la vez por defecto.", "r": "Fals", "j": "Se activan individualmente por temperatura (fusible), salvo sistemas de diluvio."},
    {"p": "La resistencia al fuego 'EI' garantiza estabilidad mecánica.", "r": "Fals", "j": "Garantiza Integridad (E) y Aislamiento (I). La Estabilidad es 'R'."},
    {"p": "Un muro cortafuegos debe resistir el fuego y además el empuje mecánico por impacto.", "r": "Vertader", "j": "Debe mantener la sectorización incluso ante colapso estructural parcial."},
    {"p": "Las puertas cortafuego deben tener un dispositivo de cierre automático.", "r": "Vertader", "j": "Si están abiertas no sirven. Deben cerrarse tras el paso o por alarma."},
    {"p": "La señalización de evacuación debe ser fotoluminiscente.", "r": "Vertader", "j": "Para ser visible en caso de fallo de iluminación."},
    {"p": "El alumbrado de emergencia debe garantizar 1 lux en el eje de los recorridos.", "r": "Vertader", "j": "Mínimo normativo para evacuación."},
    {"p": "En un edificio industrial Tipo A, la estructura compartida debe tener resistencia al fuego aumentada.", "r": "Vertader", "j": "Para proteger a los otros usuarios del edificio."},
    {"p": "El cálculo de la carga de fuego ponderada tiene en cuenta la peligrosidad de los combustibles (Ra).", "r": "Vertader", "j": "Coeficiente de peligrosidad según la actividad."},
    {"p": "El tiempo de evacuación no depende del ancho de las salidas.", "r": "Fals", "j": "Depende directamente del ancho (hipótesis de flujo de personas)."},
    {"p": "Una salida de emergencia puede estar bloqueada con llave durante la jornada laboral.", "r": "Fals", "j": "Debe ser abrible fácilmente desde el interior (barra antipánico)."},
    {"p": "La presión diferencial en escaleras evita la entrada de humo.", "r": "Vertader", "j": "Mantiene la escalera a sobrepresión respecto al sector incendiado."},
    {"p": "Los extintores de CO2 son idóneos para cuadros eléctricos.", "r": "Vertader", "j": "No dejan residuo y no son conductores (gas dieléctrico)."},
    {"p": "Un extintor de agua es apto para fuegos de gasolina (Clase B).", "r": "Fals", "j": "El agua extiende el líquido inflamable. Se requiere espuma o polvo."},

    # Layout y Fichas (More Depth)
    {"p": "El diagrama de recorrido (spaghetti chart) ayuda a identificar ineficiencias en el movimiento.", "r": "Vertader", "j": "Visualiza el caos de trayectorias en planta."},
    {"p": "En la distribución en U, la entrada y salida de materiales están próximas.", "r": "Vertader", "j": "Facilita compartir muelles y personal de logística."},
    {"p": "La ficha de máquina debe incluir el peso del equipo.", "r": "Vertader", "j": "Dato crítico para calcular la sobrecarga en forjados."},
    {"p": "El 'layout' detallado incluye la posición de las tomas de corriente y aire.", "r": "Vertader", "j": "Necesario para la instalación de servicios a maquinaria."},
    {"p": "Los pasillos de circulación de carretillas deben tener el mismo ancho que la carretilla.", "r": "Fals", "j": "Deben tener holgura de seguridad (ej. ancho + 1 metro)."},
    {"p": "Es recomendable situar las zonas de oficinas cerca de las zonas más ruidosas de la fábrica.", "r": "Fals", "j": "Se busca lo contrario: confort acústico y separación de riesgos."},
    {"p": "La ubicación de los vestuarios debe minimizar el tiempo de acceso al puesto de trabajo.", "r": "Vertader", "j": "Eficiencia en cambios de turno."},
    
    # Terreno (Specifics)
    {"p": "El nivel freático indica la profundidad a la que se encuentra agua subterránea.", "r": "Vertader", "j": "Afecta a la excavación y cimentación (impermeabilización)."},
    {"p": "Un terreno de relleno antrópico es ideal para cimentar sin tratamiento.", "r": "Fals", "j": "Suele ser inestable y asentable. Requiere mejora o cimentación profunda."},
    {"p": "La cohesión es una propiedad típica de las arenas limpias.", "r": "Fals", "j": "Las arenas no tienen cohesión (suelos granulares). Es típica de arcillas."},
    {"p": "El ensayo Proctor determina la compacidad óptima de un suelo para relleno.", "r": "Vertader", "j": "Relaciona humedad y densidad."},

    # Extras to reach 100
    {"p": "El CTE-DB-SI es el Documento Básico de Seguridad en caso de Incendio.", "r": "Vertader", "j": "Normativa marco de edificación (no industrial específica)."},
    {"p": "Un lucernario en cubierta puede actuar como exutorio de humos si está diseñado para ello.", "r": "Vertader", "j": "Deben tener apertura automática o fusible."},
    {"p": "Las naves nido son aquellas que no tienen actividad definida.", "r": "Vertader", "j": "Se construyen para alquiler/venta genérica."},
    {"p": "La altura libre de una nave limita la altura de estanterías y maquinaria.", "r": "Vertader", "j": "Parámetro geométrico restrictivo."},
    {"p": "El pavimento industrial debe resistir el punzonamiento de las estanterías.", "r": "Vertader", "j": "Cargas concentradas muy altas en las patas."},
    {"p": "Las juntas de dilatación en estructura son necesarias en edificios muy largos.", "r": "Vertader", "j": "Para absorber movimientos térmicos y evitar fisuras."},
    {"p": "La iluminación natural en industria no es recomendable.", "r": "Fals", "j": "Es muy recomendable por ahorro energético y confort, evitando deslumbramientos."},
    {"p": "Un puente grúa apoya sobre las vigas carrileras.", "r": "Vertader", "j": "Estructura auxiliar para movimiento de cargas pesadas."},
    {"p": "La carga de viento succiona (tira hacia arriba) las cubiertas ligeras.", "r": "Vertader", "j": "Efecto de succión, riesgo de desprendimiento."},
    {"p": "El aislamiento térmico en cubierta evita condensaciones interiores.", "r": "Vertader", "j": "Punto frío donde condensa la humedad del proceso."},
    {"p": "El amianto (fibrocemento antiguo) es un material peligroso que debe retirarse por especialistas.", "r": "Vertader", "j": "Cancerígeno, normativa estricta de desamiantado."},
    {"p": "Las instalaciones de aire comprimido suelen ser anillos cerrados para mantener presión.", "r": "Vertader", "j": "Evitan caídas de presión al final de línea."},
    {"p": "El factor de forma de un edificio influye en sus pérdidas energéticas.", "r": "Vertader", "j": "Más compacidad = menos superficie de transmisión térmica."},
    {"p": "La edificabilidad neta se aplica sobre la parcela, descontando cesiones.", "r": "Vertader", "j": "Diferencia con la bruta (sobre el sector)."},
    {"p": "El retranqueo es la separación obligatoria de la edificación a los lindes.", "r": "Vertader", "j": "Parámetro urbanístico común."},
    {"p": "La altura reguladora máxima limita la altura de cornisa del edificio.", "r": "Vertader", "j": "No se puede sobrepasar, salvo excepciones tecnológicas."},
    {"p": "El uso permitido principal define la actividad mayoritaria de la zona.", "r": "Vertader", "j": "Puede haber usos compatibles o prohibidos."},
    {"p": "La licencia de primera ocupación verifica que la obra coincide con el proyecto.", "r": "Vertader", "j": "Trámite final para legalizar el uso."},
    {"p": "El proyecto de actividad sirve para obtener la licencia ambiental o de apertura.", "r": "Vertader", "j": "Justifica cumplimiento de normativas de la actividad (ruido, fuego, residuos)."},
    {"p": "El visado colegial garantiza la calidad técnica del proyecto.", "r": "Fals", "j": "Garantiza la habilitación del autor y la integridad formal, no la corrección técnica profunda."},
    {"p": "El director de obra dirige la ejecución material de la obra.", "r": "Fals", "j": "Ese es el Director de Ejecución (Aparejador). El Director de Obra (Arquitecto/Ingeniero) dirige la obra en aspectos técnicos/estéticos/urbanísticos."},
    {"p": "El Estudio de Seguridad y Salud es obligatorio en proyectos de obras.", "r": "Vertader", "j": "Evalúa riesgos laborales durante la construcción."},
    {"p": "La coordinación de actividades empresariales es necesaria cuando concurren varias empresas.", "r": "Vertader", "j": "Prevención de riesgos compartidos."},
    {"p": "Un residuo inerte es aquel que no experimenta transformaciones físicas, químicas o biológicas significativas.", "r": "Vertader", "j": "Escombros limpios, vidrio, etc."},
    {"p": "La regla de las 3R es: Reciclar, Reutilizar, Revalorizar.", "r": "Fals", "j": "Es Reducir, Reutilizar, Reciclar."},
    {"p": "La economía circular busca mantener los productos y materiales en uso el mayor tiempo posible.", "r": "Vertader", "j": "Minimizar residuos y extracción de recursos."},
    {"p": "El análisis de ciclo de vida (ACV) evalúa el impacto ambiental desde la cuna a la tumba.", "r": "Vertader", "j": "Metodología estándar de sostenibilidad."},
    {"p": "La certificación energética es obligatoria para edificios industriales.", "r": "Fals", "j": "Solo para las zonas de oficinas o si están climatizados/son para personas. Naves almacén/producción suelen estar exentas."},
    {"p": "El marcado CE es obligatorio para los productos de construcción.", "r": "Vertader", "j": "Garantía de conformidad europea."},
    {"p": "La dirección facultativa está compuesta únicamente por el constructor.", "r": "Fals", "j": "La forman el Director de Obra y el Director de Ejecución."},
    {"p": "El Libro del Edificio recoge la documentación final de obra y mantenimiento.", "r": "Vertader", "j": "Se entrega al propietario al finalizar."},
    {"p": "Una nave 'llave en mano' incluye proyecto, construcción y puesta en marcha.", "r": "Vertader", "j": "Modalidad de contrato integral."},
    {"p": "El Project Manager actúa como representante de la propiedad.", "r": "Vertader", "j": "Gestiona costes, plazos y calidad en nombre del cliente."}
]

def append_to_csv():
    # Find last ID
    last_id = 0
    if os.path.exists(csv_path):
        with open(csv_path, 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                try:
                    num = int(row['numero'])
                    if num > last_id:
                        last_id = num
                except:
                    pass
    
    print(f"Adding {len(new_questions)} questions starting at ID {last_id + 1}")
    
    with open(csv_path, 'a', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        for q in new_questions:
            last_id += 1
            # numero,pregunta,tipo,opciones,respuesta_correcta,justificacion
            writer.writerow([
                last_id,
                q['p'],
                "multiple",
                "",
                q['r'],
                q['j']
            ])
            
    print("Done.")

if __name__ == "__main__":
    append_to_csv()
