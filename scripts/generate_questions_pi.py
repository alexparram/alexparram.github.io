import csv
import os

# Configuración de asignatura
subject = "Projectes d'Instalacions"

# File paths
# Saving to csv/Projectes d'Instalacions/PI_preguntas.csv
output_dir = os.path.join(os.path.dirname(__file__), "..", "csv", subject)
os.makedirs(output_dir, exist_ok=True)
csv_path = os.path.join(output_dir, f"PI_preguntas.csv")

questions = [
    # TEMA 3: AFS i ACS
    {
        "p": "¿Cuál es la función principal de una red de fontanería AFS?",
        "tipo": "multiple",
        "opciones": "Portar agua del punto de captación al de consumo garantizando caudal, presión y calidad|Evacuar aguas residuales|Recoger aguas pluviales|Tratar el agua residual",
        "r": "Portar agua del punto de captación al de consumo garantizando caudal, presión y calidad",
        "j": "La función es el suministro (abastament), no el saneamiento."
    },
    {
        "p": "En una red ramificada, una avería corta el suministro en todos los puntos aguas abajo.",
        "tipo": "multiple",
        "opciones": "",
        "r": "Vertader",
        "j": "Es una de las principales desventajas de las redes ramificadas frente a las malladas."
    },
    {
        "p": "La red mallada tiene como inconveniente un cálculo más complejo.",
        "tipo": "multiple",
        "opciones": "",
        "r": "Vertader",
        "j": "Requiere métodos iterativos (Cross) o software específico debido a los múltiples caminos de flujo."
    },
    {
        "p": "¿Qué tipo de acometida garantiza la potabilidad del agua suministrada?",
        "tipo": "multiple",
        "opciones": "Acometida de compañía|Captación privada de pozo|Captación de río|Recogida de pluviales",
        "r": "Acometida de compañía",
        "j": "La compañía suministradora es responsable legal de la calidad y potabilidad hasta el contador."
    },
    {
        "p": "El Código Técnico de la Edificación (CTE) regula el suministro de agua para procesos industriales.",
        "tipo": "multiple",
        "opciones": "",
        "r": "Fals",
        "j": "El CTE-DB-HS4 regula el uso 'sanitario' (doméstico/terciario). El proceso industrial se rige por su propia ingeniería."
    },
    {
        "p": "¿Qué elemento es obligatorio para evitar el retorno de agua de la instalación interior a la red pública?",
        "tipo": "multiple",
        "opciones": "Válvula de retención|Filtro|Contador|Grifo de comprobación",
        "r": "Válvula de retención",
        "j": "Impide la contaminación de la red pública por retorno (antirretorno)."
    },
    {
        "p": "¿Cuál es la presión mínima de suministro en puntos de consumo habituales según CTE?",
        "tipo": "multiple",
        "opciones": "1 bar (100 kPa)|3 bar (300 kPa)|5 bar (500 kPa)|0.5 bar (50 kPa)",
        "r": "1 bar (100 kPa)",
        "j": "El mínimo es 1 bar para grifos comunes (1.5 bar para fluxores)."
    },
    {
        "p": "Un exceso de presión (más de 5 bar) en la red puede provocar...",
        "tipo": "multiple",
        "opciones": "Ruido, vibraciones y reducción de vida útil|Mayor confort|Menor consumo de agua|Mejor calidad del agua",
        "r": "Ruido, vibraciones y reducción de vida útil",
        "j": "También provoca un exceso de consumo innecesario. Se deben instalar reductoras de presión."
    },
    {
        "p": "El polipropileno (PP) permite unión por soldadura (termofusión).",
        "tipo": "multiple",
        "opciones": "",
        "r": "Vertader",
        "j": "La termofusión crea uniones muy seguras y estancas, eliminando juntas mecánicas."
    },
    {
        "p": "El acero galvanizado puede estar en contacto directo con tuberías de cobre.",
        "tipo": "multiple",
        "opciones": "",
        "r": "Fals",
        "j": "Se produce el par galvánico (electrólisis) que corroe el acero. Se necesita manguito dieléctrico."
    },
    {
        "p": "¿Qué tratamiento elimina la dureza (cal y magnesio) del agua?",
        "tipo": "multiple",
        "opciones": "Descalcificación|Cloración|Filtración|Osmosis inversa",
        "r": "Descalcificación",
        "j": "Mediante resinas de intercambio iónico (intercambia Ca/Mg por Na)."
    },
    {
        "p": "La ósmosis inversa utiliza membranas semipermeables para desmineralizar el agua.",
        "tipo": "multiple",
        "opciones": "",
        "r": "Vertader",
        "j": "Retiene sales disueltas aplicando presión superior a la osmótica."
    },
    {
        "p": "La legionela prolifera especialmente a temperaturas entre...",
        "tipo": "multiple",
        "opciones": "20ºC y 45ºC|50ºC y 70ºC|0ºC y 10ºC|>70ºC",
        "r": "20ºC y 45ºC",
        "j": "Es su rango óptimo de crecimiento. A partir de 50ºC deja de multiplicarse y a 70ºC muere instantáneamente."
    },
    {
        "p": "En un sistema de ACS con acumulación, el agua acumulada debe mantenerse a...",
        "tipo": "multiple",
        "opciones": "60ºC|45ºC|35ºC|90ºC",
        "r": "60ºC",
        "j": "Para prevenir la legionela según normativa (RD 865/2003 y CTE)."
    },
    {
        "p": "El retorno de ACS es obligatorio si la tubería de ida supera los...",
        "tipo": "multiple",
        "opciones": "15 metros|5 metros|50 metros|Siempre es obligatorio",
        "r": "15 metros",
        "j": "Para evitar tirar agua fría esperando que salga caliente y confort del usuario."
    },
    # TEMA 4: SANEAMIENTO
    {
        "p": "El sistema separativo de alcantarillado recoge aguas pluviales y residuales en la misma red.",
        "tipo": "multiple",
        "opciones": "",
        "r": "Fals",
        "j": "Eso es el sistema unitario. El separativo usa redes independientes."
    },
    {
        "p": "¿Qué elemento hidráulico evita el paso de malos olores desde la alcantarilla?",
        "tipo": "multiple",
        "opciones": "Sifón|Bajante|Arqueta|Canalón",
        "r": "Sifón",
        "j": "Mediante el cierre hidráulico (agua retenida)."
    },
    {
        "p": "La ventilación primaria de las bajantes sirve para...",
        "tipo": "multiple",
        "opciones": "Evitar el desifonamiento por pistón o aspiración|Eliminar olores|Aumentar el caudal|Filtrar el agua",
        "r": "Evitar el desifonamiento por pistón o aspiración",
        "j": "Equilibra presiones en la bajante para no romper el cierre hidráulico."
    },
    {
        "p": "Las aguas negras proceden de...",
        "tipo": "multiple",
        "opciones": "Inodoros y urinarios (fecales)|Duchas y lavabos|Cocinas|Lluvia",
        "r": "Inodoros y urinarios (fecales)",
        "j": "Contienen materia orgánica fecal. Las de duchas/cocinas son aguas grises."
    },
    {
        "p": "Un pozo de registro se debe colocar en los cambios de dirección de colectores enterrados.",
        "tipo": "multiple",
        "opciones": "",
        "r": "Vertader",
        "j": "Para permitir el acceso y mantenimiento/limpieza."
    },
    {
        "p": "El PVC es un material habitual en redes de saneamiento pequeñas y medianas.",
        "tipo": "multiple",
        "opciones": "",
        "r": "Vertader",
        "j": "Es ligero, barato y liso, muy usado en edificación."
    },
    {
        "p": "La pendiente mínima recomendada para un colector de aguas residuales es del...",
        "tipo": "multiple",
        "opciones": "1 - 2%|0%|10%|0.1%",
        "r": "1 - 2%",
        "j": "Para garantizar la velocidad de autolimpieza sin erosionar excesivamente."
    },
    # TEMA 5: ELECTRICITAT BT
    {
        "p": "El Reglamento Electrotécnico de Baja Tensión (REBT) es el RD 842/2002.",
        "tipo": "multiple",
        "opciones": "",
        "r": "Vertader",
        "j": "Es la normativa marco actual en España para BT."
    },
    {
        "p": "Baja Tensión en corriente alterna es hasta...",
        "tipo": "multiple",
        "opciones": "1000 V|1500 V|50 V|230 V",
        "r": "1000 V",
        "j": "Entre 50 y 1000 V en AC se considera Baja Tensión habitual."
    },
    {
        "p": "La tensión nominal monofásica en España es de 230 V.",
        "tipo": "multiple",
        "opciones": "",
        "r": "Vertader",
        "j": "Y la trifásica es 400 V."
    },
    {
        "p": "¿Qué dispositivo protege contra sobrecargas y cortocircuitos?",
        "tipo": "multiple",
        "opciones": "Interruptor Magnetotérmico (PIA)|Interruptor Diferencial|Fusible (solo corto)|Pararrayos",
        "r": "Interruptor Magnetotérmico (PIA)",
        "j": "Parte térmica (sobrecarga) y magnética (cortocircuito)."
    },
    {
        "p": "¿Qué dispositivo protege a las personas contra contactos indirectos (fugas)?",
        "tipo": "multiple",
        "opciones": "Interruptor Diferencial|Magnetotérmico|ICP|Contador",
        "r": "Interruptor Diferencial",
        "j": "Detecta la diferencia de corriente entre fase y neutro (fuga a tierra)."
    },
    {
        "p": "El código de colores para la fase en instalaciones trifásicas puede ser...",
        "tipo": "multiple",
        "opciones": "Marrón, Negro, Gris|Azul, Amarillo, Verde|Rojo, Blanco, Azul|Todo Negro",
        "r": "Marrón, Negro, Gris",
        "j": "Son los colores normalizados para L1, L2, L3."
    },
    {
        "p": "El conductor neutro debe ser de color...",
        "tipo": "multiple",
        "opciones": "Azul|Amarillo-Verde|Negro|Marrón",
        "r": "Azul",
        "j": "Normativa de identificación de conductores."
    },
    {
        "p": "El conductor de protección (Tierra) debe ser de color...",
        "tipo": "multiple",
        "opciones": "Amarillo y Verde|Azul|Negro|Gris",
        "r": "Amarillo y Verde",
        "j": "Identificación exclusiva para tierra."
    },
    {
        "p": "La potencia eléctrica activa se mide en...",
        "tipo": "multiple",
        "opciones": "Vatios (W) o kW|Voltiamperios (VA)|Var|Amperios (A)",
        "r": "Vatios (W) o kW",
        "j": "P = V * I * cos(phi)."
    },
    {
        "p": "El factor de potencia (cos phi) ideal es...",
        "tipo": "multiple",
        "opciones": "1|0|0.5|Infinito",
        "r": "1",
        "j": "Indica aprovechamiento total de la energía sin reactiva."
    },
    {
        "p": "En un sistema trifásico equilibrado, la corriente por el neutro es cero.",
        "tipo": "multiple",
        "opciones": "",
        "r": "Vertader",
        "j": "La suma vectorial de las tres fases desfasadas 120º es nula."
    },
    {
        "p": "¿Qué caída de tensión máxima se permite en alumbrado desde el cuadro general según REBT?",
        "tipo": "multiple",
        "opciones": "3%|5%|10%|1%",
        "r": "3%",
        "j": "Para otros usos suele ser 5%."
    },
    {
        "p": "Un esquema unifilar representa...",
        "tipo": "multiple",
        "opciones": "Todos los conductores con una sola línea y símbolos|La posición física real de los cables|El esquema de mando y potencia separado|La instalación de agua",
        "r": "Todos los conductores con una sola línea y símbolos",
        "j": "Simplifica la lectura de circuitos eléctricos."
    },
    {
        "p": "El tubo corrugado empotrado tipo 'forroplast' (negro) está prohibido en instalaciones interiores.",
        "tipo": "multiple",
        "opciones": "",
        "r": "Vertader",
        "j": "Por ser propagador de la llama. Se deben usar tubos no propagadores (habitualmente gris)."
    },
    # TEMA 6: ENLLUMENAT
    {
        "p": "El flujo luminoso se mide en...",
        "tipo": "multiple",
        "opciones": "Lúmenes (lm)|Lux (lx)|Candelas (cd)|Watios (W)",
        "r": "Lúmenes (lm)",
        "j": "Es la cantidad total de luz emitida por una fuente."
    },
    {
        "p": "La iluminancia o nivel de iluminación se mide en...",
        "tipo": "multiple",
        "opciones": "Lux (lx)|Lúmenes (lm)|Candelas (cd)|Watios (W)",
        "r": "Lux (lx)",
        "j": "Lúmenes por metro cuadrado (lm/m2)."
    },
    {
        "p": "La temperatura de color de una luz cálida es...",
        "tipo": "multiple",
        "opciones": "< 3300 K (ej. 2700K - 3000K)|> 5300 K (ej. 6000K)|4000 K|No tiene temperatura",
        "r": "< 3300 K (ej. 2700K - 3000K)",
        "j": "Tonos rojizos/amarillentos. Luz fría es > 5000K (azulada)."
    },
    {
        "p": "El Índice de Reproducción Cromática (IRC o Ra) indica la fidelidad de los colores.",
        "tipo": "multiple",
        "opciones": "",
        "r": "Vertader",
        "j": "Ra 100 es la luz solar (perfecta). Ra > 80 es bueno para interiores."
    },
    {
        "p": "Las lámparas LED tienen una vida útil inferior a las incandescentes.",
        "tipo": "multiple",
        "opciones": "",
        "r": "Fals",
        "j": "Las LED duran mucho más (15.000-50.000h) vs Incandescentes (1.000h)."
    },
    {
        "p": "La eficacia luminosa relaciona los lúmenes emitidos con la potencia consumida (lm/W).",
        "tipo": "multiple",
        "opciones": "",
        "r": "Vertader",
        "j": "Mide el rendimiento energético de la fuente de luz."
    },
    {
        "p": "¿Qué tipo de lámpara requiere un equipo de arranque (cebador/balasto)?",
        "tipo": "multiple",
        "opciones": "Fluorescente / Descarga|Incandescente|Halógena directa a red|Vela",
        "r": "Fluorescente / Descarga",
        "j": "Necesitan limitar la corriente y picos para ionizar el gas."
    },
    {
        "p": "El deslumbramiento (UGR) debe controlarse en oficinas.",
        "tipo": "multiple",
        "opciones": "",
        "r": "Vertader",
        "j": "Para evitar fatiga visual y reflejos en pantallas."
    },
    {
        "p": "La contaminación lumínica es la emisión de luz hacia el cielo (hemisferio superior).",
        "tipo": "multiple",
        "opciones": "",
        "r": "Vertader",
        "j": "Desperdicio de energía y afecta a la observación astronómica y ecosistemas."
    },
    # TEMA 7: BMS (Building Management Systems)
    {
        "p": "¿Qué significa BMS?",
        "tipo": "multiple",
        "opciones": "Building Management System|Basic Maintenance Service|Better Material Standard|Bio Mechanical System",
        "r": "Building Management System",
        "j": "Sistema de gestión integral del edificio (Domótica/Inmótica)."
    },
    {
        "p": "Un sistema BMS centralizado tiene un único controlador principal.",
        "tipo": "multiple",
        "opciones": "",
        "r": "Vertader",
        "j": "Si falla la central, cae todo el sistema. A diferencia del distribuido."
    },
    {
        "p": "El protocolo KNX es un estándar abierto para automatización de edificios.",
        "tipo": "multiple",
        "opciones": "",
        "r": "Vertader",
        "j": "Permite interoperabilidad entre dispositivos de distintos fabricantes."
    },
    {
        "p": "En un sistema BMS, los sensores son elementos de...",
        "tipo": "multiple",
        "opciones": "Entrada (Input)|Salida (Output)|Proceso|Cableado",
        "r": "Entrada (Input)",
        "j": "Captan información (temperatura, presencia, luz) para el sistema."
    },
    {
        "p": "Los actuadores son elementos que ejecutan las órdenes (encender luz, cerrar persiana).",
        "tipo": "multiple",
        "opciones": "",
        "r": "Vertader",
        "j": "Son elementos de Salida."
    },
    # EXTRAS MEZCLADOS
    {
        "p": "La bomba de calor aerotérmica es un sistema renovable para ACS.",
        "tipo": "multiple",
        "opciones": "",
        "r": "Vertader",
        "j": "Extrae energía del aire ambiente con alto rendimiento (COP)."
    },
    {
        "p": "El depósito de expansión en ACS absorbe las variaciones de volumen del agua al calentarse.",
        "tipo": "multiple",
        "opciones": "",
        "r": "Vertader",
        "j": "El agua se dilata al calentar y necesita ese espacio para no reventar la tubería."
    },
    {
        "p": "Las tuberías de PPR (polipropileno random) son verdes habitualmente.",
        "tipo": "multiple",
        "opciones": "",
        "r": "Vertader",
        "j": "Color característico, aunque no exclusivo."
    },
    {
        "p": "En saneamiento, el 'cierre hidráulico' suele medir 50 mm.",
        "tipo": "multiple",
        "opciones": "",
        "r": "Vertader",
        "j": "Altura mínima de agua para garantizar que no pasen olores."
    },
    {
        "p": "La aparamenta eléctrica debe tener un grado IP adecuado al entorno.",
        "tipo": "multiple",
        "opciones": "",
        "r": "Vertader",
        "j": "IP (Ingress Protection) contra polvo y agua (ej. IP44, IP65)."
    },
    {
        "p": "¿Qué IP indica protección total contra polvo y chorros de agua?",
        "tipo": "multiple",
        "opciones": "IP65|IP20|IP00|IP40",
        "r": "IP65",
        "j": "6=Polvo estanco, 5=Chorros de agua."
    },
    {
        "p": "Los cables libres de halógenos (LSZH) son obligatorios en locales de pública concurrencia.",
        "tipo": "multiple",
        "opciones": "",
        "r": "Vertader",
        "j": "No emiten gases tóxicos ni humos opacos en caso de incendio."
    },
    {
        "p": "El diámetro de una tubería de saneamiento se calcula para que vaya a sección llena.",
        "tipo": "multiple",
        "opciones": "",
        "r": "Fals",
        "j": "Se calcula a sección parcial (habitualmente 50-70%) para permitir ventilación."
    },
    {
        "p": "La 'Toma de Tierra' conecta las masas metálicas al terreno.",
        "tipo": "multiple",
        "opciones": "",
        "r": "Vertader",
        "j": "Para derivar corrientes de fuga y proteger a las personas."
    },
    {
        "p": "El diferencial salta cuando hay un cortocircuito entre fase y neutro.",
        "tipo": "multiple",
        "opciones": "",
        "r": "Fals",
        "j": "Ahí salta el magnetotérmico. El diferencial salta por fugas a tierra."
    },
    {
        "p": "DALI es un protocolo para control de iluminación.",
        "tipo": "multiple",
        "opciones": "",
        "r": "Vertader",
        "j": "Digital Addressable Lighting Interface."
    },
    {
        "p": "El caudal simultáneo es la suma aritmética de todos los caudales instalados.",
        "tipo": "multiple",
        "opciones": "",
        "r": "Fals",
        "j": "Se aplica un coeficiente de simultaneidad, ya que no todo se usa a la vez."
    },
    {
        "p": "Las aguas grises pueden reutilizarse para cisternas de inodoro tras tratamiento simple.",
        "tipo": "multiple",
        "opciones": "",
        "r": "Vertader",
        "j": "Ahorro de agua potable."
    }
]

# Rellenar hasta llegar a 50+ preguntas con variaciones rápidas para tener base.
# He puesto manualmente ~46 preguntas bien definidas arriba.
# Voy a añadir más preguntas tipo test generadas lógicamente para completar.

extra_questions = [
    {"p": "La resistividad del cobre es menor que la del aluminio.", "tipo": "multiple", "opciones":"", "r": "Vertader", "j": "El cobre conduce mejor."},
    {"p": "El aluminio se usa en líneas de distribución por su menor peso y coste.", "tipo": "multiple", "opciones":"", "r": "Vertader", "j": "Aunque conduce peor que el cobre, compensa en grandes secciones."},
    {"p": "Una luminaria IP20 es apta para exterior.", "tipo": "multiple", "opciones":"", "r": "Fals", "j": "IP20 no protege contra agua. Exterior requiere IP44/54/65."},
    {"p": "La luz de emergencia debe durar al menos 1 hora tras corte de luz.", "tipo": "multiple", "opciones":"", "r": "Vertader", "j": "Normativa básica de emergencia."},
    {"p": "El reglamento de baja tensión exige 5 conductores en líneas trifásicas con neutro.", "tipo": "multiple", "opciones":"", "r": "Vertader", "j": "3 Fases + Neutro + Tierra."},
    {"p": "La acometida eléctrica finaliza en la Caja General de Protección (CGP).", "tipo": "multiple", "opciones":"", "r": "Vertader", "j": "Es el punto de conexión con la red de distribución."},
    {"p": "El contador eléctrico inteligente permite la telegestión.", "tipo": "multiple", "opciones":"", "r": "Vertader", "j": "Lectura remota y corte."},
    {"p": "La bañera necesita conexión equipotencial suplementaria.", "tipo": "multiple", "opciones":"", "r": "Vertader", "j": "Para evitar diferencias de potencial en zona húmeda."},
    {"p": "Los volúmenes de prohibición en baños limitan dónde instalar enchufes.", "tipo": "multiple", "opciones":"", "r": "Vertader", "j": "Volumen 0, 1, 2 y 3."},
    {"p": "En el volumen 0 (interior bañera) se pueden instalar luminarias 230V IP68.", "tipo": "multiple", "opciones":"", "r": "Fals", "j": "Solo pequeña tensión de seguridad (MBTS, 12V)."},
    {"p": "El RITE regula las instalaciones térmicas (Calefacción/Clima/ACS).", "tipo": "multiple", "opciones":"", "r": "Vertader", "j": "Reglamento de Instalaciones Térmicas en los Edificios."},
    {"p": "La ventilación híbrida combina ventilación natural y mecánica.", "tipo": "multiple", "opciones":"", "r": "Vertader", "j": "Actúa mecánicamente cuando las condiciones naturales no bastan."},
    {"p": "El caudal de ventilación en viviendas suele ser por admisión en zonas secas y extracción en húmedas.", "tipo": "multiple", "opciones":"", "r": "Vertader", "j": "Sistema de flujo estándar CTE-DB-HS3."},
    {"p": "Las campanas de cocina deben tener conducto independiente de la ventilación general.", "tipo": "multiple", "opciones":"", "r": "Vertader", "j": "Por grasas y riesgo de incendio."},
    {"p": "El aire acondicionado tipo Split consta de unidad interior y exterior.", "tipo": "multiple", "opciones":"", "r": "Vertader", "j": "Evaporadora dentro, Condensadora fuera."},
    {"p": "El suelo radiante trabaja a alta temperatura (80ºC).", "tipo": "multiple", "opciones":"", "r": "Fals", "j": "Trabaja a baja temperatura (30-45ºC) para confort y eficiencia."},
    {"p": "La aerotermia tiene rendimiento superior a 1 (COP > 1).", "tipo": "multiple", "opciones":"", "r": "Vertader", "j": "Mueve más energía térmica que la eléctrica que consume."},
    {"p": "El DB-HE obliga a contribución renovable para ACS.", "tipo": "multiple", "opciones":"", "r": "Vertader", "j": "Solar térmica o alternativa (aerotermia)."},
    {"p": "Los paneles fotovoltaicos generan ACS directamente.", "tipo": "multiple", "opciones":"", "r": "Fals", "j": "Generan electricidad. Los térmicos generan ACS."},
    {"p": "El inversor fotovoltaico convierte corriente continua en alterna.", "tipo": "multiple", "opciones":"", "r": "Vertader", "j": "DC de paneles a AC de red."},
    {"p": "Las baterías solares almacenan energía en kWh.", "tipo": "multiple", "opciones":"", "r": "Vertader", "j": "Capacidad de energía."},
    {"p": "El autoconsumo con excedentes permite verter energía a la red.", "tipo": "multiple", "opciones":"", "r": "Vertader", "j": "Y recibir compensación."},
    {"p": "La ICT regula las infraestructuras de telecomunicaciones.", "tipo": "multiple", "opciones":"", "r": "Vertader", "j": "Infraestructura Común de Telecomunicaciones."},
    {"p": "La fibra óptica es inmune a interferencias electromagnéticas.", "tipo": "multiple", "opciones":"", "r": "Vertader", "j": "Transmite luz, no electricidad."},
    {"p": "El cable coaxial se usa para señal de TV.", "tipo": "multiple", "opciones":"", "r": "Vertader", "j": "Estándar en antena."},
    {"p": "El par trenzado (UTP/FTP) se usa para redes de datos.", "tipo": "multiple", "opciones":"", "r": "Vertader", "j": "Ethernet RJ45."},
    {"p": "Un RACK es un armario para alojar equipos de telecomunicaciones.", "tipo": "multiple", "opciones":"", "r": "Vertader", "j": "Medida estándar 19 pulgadas."},
    {"p": "El SAI (UPS) proporciona energía en caso de corte eléctrico.", "tipo": "multiple", "opciones":"", "r": "Vertader", "j": "Sistema de Alimentación Ininterrumpida."},
    {"p": "El grupo electrógeno usa combustible para generar electricidad.", "tipo": "multiple", "opciones":"", "r": "Vertader", "j": "Motor diésel habitualmente."},
    {"p": "La domótica se refiere a la automatización de viviendas.", "tipo": "multiple", "opciones":"", "r": "Vertader", "j": "Inmótica es para edificios terciarios."},
    {"p": "Los detectores de presencia ahorran energía en iluminación.", "tipo": "multiple", "opciones":"", "r": "Vertader", "j": "Apagan si no hay nadie."},
    {"p": "Un luxómetro mide la intensidad de corriente.", "tipo": "multiple", "opciones":"", "r": "Fals", "j": "Mide iluminancia (lux)."},
    {"p": "El multímetro (polímetro) mide Voltios, Amperios y Ohmios.", "tipo": "multiple", "opciones":"", "r": "Vertader", "j": "Herramienta básica electricista."},
    {"p": "La pinza amperimétrica mide intensidad sin cortar el cable.", "tipo": "multiple", "opciones":"", "r": "Vertader", "j": "Por inducción magnética."},
    {"p": "El megger sirve para medir aislamiento.", "tipo": "multiple", "opciones":"", "r": "Vertader", "j": "Resistencia muy alta de aislamiento."},
    {"p": "La resistencia de tierra debe ser lo más alta posible.", "tipo": "multiple", "opciones":"", "r": "Fals", "j": "Lo más baja posible para facilitar la descarga."},
    {"p": "Una pica de tierra es un electrodo en contacto con el terreno.", "tipo": "multiple", "opciones":"", "r": "Vertader", "j": "Acero cobreado habitualmente."},
    {"p": "El anillo conductor alrededor del edificio es un buen electrodo de tierra.", "tipo": "multiple", "opciones":"", "r": "Vertader", "j": "Mejor que picas aisladas."},
    {"p": "Los pararrayos con dispositivo de cebado tienen mayor radio de protección.", "tipo": "multiple", "opciones":"", "r": "Vertader", "j": "Adelantan el trazador ascendente."},
    {"p": "El PSI (Prevención y Seguridad en caso de Incendio) incluye detección y alarma.", "tipo": "multiple", "opciones":"", "r": "Vertader", "j": "Parte de instalaciones de seguridad."},
    {"p": "Un pulsador de alarma manual debe ser de color verde.", "tipo": "multiple", "opciones":"", "r": "Fals", "j": "Rojo. Verde suele ser apertura de puerta emergencia."},
    {"p": "La sirena de incendio debe tener sonido bitonal.", "tipo": "multiple", "opciones":"", "r": "Vertader", "j": "Para distinguirla de otras alarmas."},
    {"p": "La central de incendios supervisa las líneas de detectores.", "tipo": "multiple", "opciones":"", "r": "Vertader", "j": "Avisa de avería o línea abierta."},
    {"p": "El gas natural es más denso que el aire (pesa más).", "tipo": "multiple", "opciones":"", "r": "Fals", "j": "Es más ligero (metano), tiende a subir. El butano/propano pesa más."},
    {"p": "La rejilla de ventilación para Gas Natural debe estar en parte superior.", "tipo": "multiple", "opciones":"", "r": "Vertader", "j": "Porque el gas sube si hay fuga."},
    {"p": "La válvula solenoide de gas corta el suministro si detecta fuga.", "tipo": "multiple", "opciones":"", "r": "Vertader", "j": "Vinculada a sensor de gas."},
    {"p": "Las tuberías de gas se pintan obligatoriamente de azul.", "tipo": "multiple", "opciones":"", "r": "Fals", "j": "Suelen ser amarillo o vainilla. Agua es azul o verde."}
]

questions.extend(extra_questions)

def write_csv():
    with open(csv_path, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(["numero", "pregunta", "tipo", "opciones", "respuesta_correcta", "justificacion"])
        
        for i, q in enumerate(questions):
            writer.writerow([
                i + 1,
                q['p'],
                q['tipo'],
                q.get('opciones', ''),
                q['r'],
                q['j']
            ])
            
    print(f"Generated {len(questions)} questions in {csv_path}")

if __name__ == "__main__":
    write_csv()
