import csv
import os

# Configuración de asignatura
subject = "SiF"

# File paths
output_dir = os.path.join(os.path.dirname(__file__), "..", "csv", subject)
os.makedirs(output_dir, exist_ok=True)
csv_path = os.path.join(output_dir, f"SiF_preguntas.csv")

questions = [
    # TEMA 1: INTRODUCCIÓN
    {"p": "¿Qué es un sistema de fabricación?", "tipo": "multiple", "opciones": "Conjunto de procesos y recursos para transformar material en producto|Una máquina herramienta aislada|Un software de gestión|Una cinta transportadora", "r": "Conjunto de procesos y recursos para transformar material en producto", "j": "Definición básica de sistema de fabricación."},
    {"p": "Las acciones improductivas en un ciclo de fabricación incluyen...", "tipo": "multiple", "opciones": "Carga y descarga, aproximación y retirada|Mecanizado|Soldadura|Montaje", "r": "Carga y descarga, aproximación y retirada", "j": "No aportan valor añadido al producto."},
    {"p": "La metodología DFMA significa...", "tipo": "multiple", "opciones": "Design for Manufacturing and Assembly|Design for Management and Automation|Digital Fabrication and Manual Assembly|Direct Factory Management Application", "r": "Design for Manufacturing and Assembly", "j": "Diseño orientado a facilitar la fabricación y el montaje."},
    {"p": "En una distribución orientada al producto (cadena), las máquinas se agrupan por tipo de operación.", "tipo": "multiple", "opciones":"", "r": "Fals", "j": "Eso es en distribución por proceso (taller). En cadena siguen el flujo del producto."},
    {"p": "La distribución por proceso (taller) tiene mayor flexibilidad que la línea transfer.", "tipo": "multiple", "opciones":"", "r": "Vertader", "j": "Permite fabricar mayor variedad de piezas, aunque con menor productividad."},
    {"p": "Una línea transfer es un sistema...", "tipo": "multiple", "opciones": "Rígido y de alta productividad|Flexible y de baja productividad|Flexible y alta productividad|Rígido y baja productividad", "r": "Rígido y de alta productividad", "j": "Diseñada para fabricar masivamente un único producto o muy similares."},
    {"p": "Reducir el número de fases de fabricación conlleva...", "tipo": "multiple", "opciones": "Disminución de errores y material en proceso|Aumento de stock|Mayor complejidad logística|Peor calidad", "r": "Disminución de errores y material en proceso", "j": "Menos manipulaciones y preparaciones."},
    {"p": "La sinterización es un proceso de...", "tipo": "multiple", "opciones": "Aumento de cohesión (pulvimetalurgia)|Arranque de viruta|Deformación plástica|Unión por adhesivo", "r": "Aumento de cohesión (pulvimetalurgia)", "j": "Compactación y calentamiento de polvo metálico."},
    {"p": "El rectificado es un proceso de...", "tipo": "multiple", "opciones": "Arranque de partículas (abrasivo)|Arranque de viruta|Fundición|Corte", "r": "Arranque de partículas (abrasivo)", "j": "Usa muelas abrasivas para acabados de alta precisión."},
    {"p": "Un utillaje es un elemento...", "tipo": "multiple", "opciones": "No fungible e intercambiable|Fungible e intercambiable|No fungible y no intercambiable|Fungible", "r": "No fungible e intercambiable", "j": "Ayuda a sujetar o guiar, se reaprovecha (no se gasta como la herramienta) y se cambia según la pieza."},

    # TEMA 2: MÁQUINAS CNC
    {"p": "NC significa Control Numérico y CNC Control Numérico Computerizado.", "tipo": "multiple", "opciones":"", "r": "Vertader", "j": "El CNC incorpora microprocesador."},
    {"p": "En un sistema de lazo cerrado (closed loop), existe realimentación de posición.", "tipo": "multiple", "opciones":"", "r": "Vertader", "j": "El encoder informa de la posición real para corregir errores."},
    {"p": "Los motores paso a paso se suelen usar en sistemas de...", "tipo": "multiple", "opciones": "Lazo abierto (Open loop)|Lazo cerrado|Alta potencia|Husillos principales", "r": "Lazo abierto (Open loop)", "j": "Son económicos pero pueden perder pasos si se supera el par."},
    {"p": "El 'feedrate' (F) es...", "tipo": "multiple", "opciones": "La velocidad de avance|La velocidad de giro del cabezal|La potencia|La posición", "r": "La velocidad de avance", "j": "mm/min o mm/rev."},
    {"p": "El control paraxial permite controlar la velocidad de...", "tipo": "multiple", "opciones": "Un solo eje cada vez|Varios ejes simultáneamente|Ningún eje|Solo el cabezal", "r": "Un solo eje cada vez", "j": "No permite interpolación (diagonales o curvas controladas)."},
    {"p": "El control de contorneado permite la interpolación de ejes.", "tipo": "multiple", "opciones":"", "r": "Vertader", "j": "Sincroniza varios ejes para trazar rectas o curvas en el espacio."},
    {"p": "El error de seguimiento es...", "tipo": "multiple", "opciones": "La diferencia entre la posición teórica y la real en un instante|El error de medida de la pieza|El juego de las guías|La holgura del husillo", "r": "La diferencia entre la posición teórica y la real en un instante", "j": "Retraso inherente al sistema de control."},
    {"p": "Un centro de mecanizado se diferencia de una fresadora CNC por tener...", "tipo": "multiple", "opciones": "Cambio automático de herramienta (ATC)|Más ejes|Mayor potencia|Control Fagor", "r": "Cambio automático de herramienta (ATC)", "j": "Permite realizar múltiples operaciones sin intervención manual."},
    {"p": "El código G00 indica...", "tipo": "multiple", "opciones": "Posicionamiento rápido (sin mecanizar)|Interpolación lineal|Interpolación circular|Pausa", "r": "Posicionamiento rápido (sin mecanizar)", "j": "Va a la máxima velocidad de la máquina."},
    {"p": "El código G01 indica...", "tipo": "multiple", "opciones": "Interpolación lineal a velocidad programada (F)|Posicionamiento rápido|Interpolación circular|Ciclo de taladrado", "r": "Interpolación lineal a velocidad programada (F)", "j": "Mecanizado en línea recta."},
    {"p": "El código G02 realiza una interpolación circular en sentido horario.", "tipo": "multiple", "opciones":"", "r": "Vertader", "j": "G03 es antihorario."},
    {"p": "La función M03 suele activar...", "tipo": "multiple", "opciones": "Giro del cabezal en sentido horario|Parada del cabezal|Cambio de herramienta|Refrigerante", "r": "Giro del cabezal en sentido horario", "j": "M04 antihorario, M05 parada."},
    {"p": "El decalaje de origen (G54, G55...) sirve para...", "tipo": "multiple", "opciones": "Definir el cero pieza respecto al cero máquina|Cambiar la herramienta|Compensar el radio|Definir la velocidad", "r": "Definir el cero pieza respecto al cero máquina", "j": "Facilita la programación respecto a la pieza."},
    {"p": "La compensación de radio de herramienta (G41/G42) permite programar el contorno real de la pieza.", "tipo": "multiple", "opciones":"", "r": "Vertader", "j": "El CNC calcula la trayectoria del centro de la herramienta desplazada un radio."},
    {"p": "Un ciclo fijo (ej. G81) sirve para...", "tipo": "multiple", "opciones": "Simplificar operaciones repetitivas como taladrado|Cambiar herramientas|Medir la pieza|Arrancar el sistema", "r": "Simplificar operaciones repetitivas como taladrado", "j": "Define la secuencia de movimientos con una sola línea de código."},

    # TEMA 3: MONTAJE
    {"p": "En una línea de montaje, el 'cuello de botella' es la estación con...", "tipo": "multiple", "opciones": "Mayor tiempo de ciclo|Menor tiempo de ciclo|Más operarios|Menos piezas", "r": "Mayor tiempo de ciclo", "j": "Limita la capacidad productiva de toda la línea."},
    {"p": "El equilibrado de líneas busca...", "tipo": "multiple", "opciones": "Igualar la carga de trabajo de todas las estaciones|Maximizar el stock intermedio|Reducir la velocidad|Aumentar el número de estaciones", "r": "Igualar la carga de trabajo de todas las estaciones", "j": "Para minimizar tiempos muertos y aumentar eficiencia."},
    {"p": "Un sistema 'Poka-Yoke' es...", "tipo": "multiple", "opciones": "Un sistema a prueba de errores|Una técnica de gestión japonesa|Un tipo de robot|Un sensor de visión", "r": "Un sistema a prueba de errores", "j": "Impide físicamente que se produzca el error (ej. conector que solo entra en una posición)."},
    {"p": "La alimentación de piezas en montaje automático suele usar...", "tipo": "multiple", "opciones": "Vibradores electromagnéticos (Bols)|Cintas transportadoras|AGVs|Carretillas", "r": "Vibradores electromagnéticos (Bols)", "j": "Orientan y suministran piezas pequeñas (tornillos, etc.)."},

    # TEMA 4: FABRICACIÓN AUTOMATIZADA
    {"p": "Un sensor inductivo detecta...", "tipo": "multiple", "opciones": "Materiales metálicos|Cualquier objeto|Plásticos|Líquidos", "r": "Materiales metálicos", "j": "Mediante campo magnético."},
    {"p": "Un sensor capacitivo puede detectar materiales no metálicos.", "tipo": "multiple", "opciones":"", "r": "Vertader", "j": "Detecta cambios en el dieléctrico (líquidos, plásticos, mano)."},
    {"p": "Un PLC (Programmable Logic Controller) se diseñó originalmente para sustituir...", "tipo": "multiple", "opciones": "Paneles de relés cableados|Ordenadores personales|Robots|Sistemas hidráulicos", "r": "Paneles de relés cableados", "j": "Para dar flexibilidad a la lógica de control."},
    {"p": "El lenguaje Ladder o de contactos se asemeja a...", "tipo": "multiple", "opciones": "Esquemas eléctricos tradicionales|Código C++|Python|G-Code", "r": "Esquemas eléctricos tradicionales", "j": "Facilita la transición de electricistas al PLC."},
    {"p": "SCADA significa...", "tipo": "multiple", "opciones": "Supervisory Control And Data Acquisition|System Control And Digital Automation|Standard Communication And Data Analysis|Safety Control And Device Activation", "r": "Supervisory Control And Data Acquisition", "j": "Sistema de supervisión y monitorización gráfica."},
    {"p": "Un robot SCARA tiene...", "tipo": "multiple", "opciones": "Rigidez vertical y flexibilidad en el plano horizontal|Rigidez en todos los ejes|6 grados de libertad|Movimiento cartesiano", "r": "Rigidez vertical y flexibilidad en el plano horizontal", "j": "Ideal para ensamblaje vertical (Pick & Place)."},
    {"p": "El volumen de trabajo de un robot cartesiano es...", "tipo": "multiple", "opciones": "Un prisma rectangular|Una esfera|Un cilindro|Incierto", "r": "Un prisma rectangular", "j": "Ejes X, Y, Z lineales."},
    {"p": "Un robot antropomórfico suele tener...", "tipo": "multiple", "opciones": "6 grados de libertad (rotacionales)|3 ejes lineales|Configuración paralela|4 ejes", "r": "6 grados de libertad (rotacionales)", "j": "Imita el brazo humano (cintura, hombro, codo, muñeca)."},
    {"p": "La precisión de repetibilidad de un robot es...", "tipo": "multiple", "opciones": "Su capacidad para volver al mismo punto repetidamente|La diferencia entre el punto programado y el real|Su carga máxima|Su velocidad", "r": "Su capacidad para volver al mismo punto repetidamente", "j": "Suele ser mejor que la precisión absoluta."},
    {"p": "El TCP (Tool Center Point) es...", "tipo": "multiple", "opciones": "El punto de acción de la herramienta del robot|El centro de la base|El panel de control|El software", "r": "El punto de acción de la herramienta del robot", "j": "Respecto al cual se programan las trayectorias."},

    # TEMA 5: SISTEMAS FLEXIBLES (FMS)
    {"p": "Una Célula de Fabricación Flexible (FMC) suele constar de...", "tipo": "multiple", "opciones": "Una o varias máquinas CNC, robot/cambiador palets y ordenador de control|Una línea transfer|Tornos manuales|Solo software", "r": "Una o varias máquinas CNC, robot/cambiador palets y ordenador de control", "j": "Trabaja de forma autónoma procesando piezas distintas."},
    {"p": "Un AGV (Automated Guided Vehicle) sirve para...", "tipo": "multiple", "opciones": "Transporte automático de materiales|Mecanizar piezas|Inspeccionar calidad|Soldar", "r": "Transporte automático de materiales", "j": "Filoguiado, optoguiado o láser."},
    {"p": "La Tecnología de Grupos (GT) consiste en...", "tipo": "multiple", "opciones": "Agrupar piezas similares en familias para fabricarlas juntas|Agrupar trabajadores|Agrupar máquinas por tipo|Comprar en grupo", "r": "Agrupar piezas similares en familias para fabricarlas juntas", "j": "Permite aplicar técnicas de flujo a lotes pequeños."},
    {"p": "Un Sistema de Fabricación Flexible (FMS) integra varias células mediante...", "tipo": "multiple", "opciones": "Un sistema de transporte automático y un control centralizado|Operarios manuales|Carretillas elevadoras|Cintas transportadoras rígidas", "r": "Un sistema de transporte automático y un control centralizado", "j": "Alta automatización y flexibilidad simultánea."},

    # TEMA 6: PREPARACIÓN Y SMED
    {"p": "SMED significa...", "tipo": "multiple", "opciones": "Single Minute Exchange of Die|Standard Manufacturing Equipment Design|System Maintenance and Engineering Department|Safe Manufacturing Environment Design", "r": "Single Minute Exchange of Die", "j": "Cambio de herramienta/útil en menos de 10 minutos (un solo dígito)."},
    {"p": "El objetivo del SMED es...", "tipo": "multiple", "opciones": "Reducir el tiempo de preparación para permitir lotes más pequeños|Aumentar la velocidad de corte|Reducir plantilla|Mejorar la calidad", "r": "Reducir el tiempo de preparación para permitir lotes más pequeños", "j": "Aporta flexibilidad y reduce stock."},
    {"p": "En SMED, las operaciones internas son aquellas que...", "tipo": "multiple", "opciones": "Solo se pueden hacer con la máquina parada|Se pueden hacer con la máquina en marcha|Se hacen fuera de la fábrica|No son necesarias", "r": "Solo se pueden hacer con la máquina parada", "j": "El objetivo es convertir internas en externas."},
    {"p": "En SMED, las operaciones externas se pueden realizar con la máquina produciendo.", "tipo": "multiple", "opciones":"", "r": "Vertader", "j": "Preparar el siguiente útil mientras la máquina trabaja."},
    {"p": "El sistema de sujeción 'Punto Cero' facilita el cambio rápido.", "tipo": "multiple", "opciones":"", "r": "Vertader", "j": "Garantiza la posición sin necesidad de reglar o centrar cada vez."},

    # TEMA 7: INTEGRACIÓN Y CIM
    {"p": "CIM significa...", "tipo": "multiple", "opciones": "Computer Integrated Manufacturing|Computer Intelligent Machine|Central Information Management|Control Industrial Manufacturing", "r": "Computer Integrated Manufacturing", "j": "Integración total de la fabricación por ordenador."},
    {"p": "La pirámide CIM estructura la automatización en niveles. El nivel más bajo es...", "tipo": "multiple", "opciones": "Nivel de Proceso/Campo (Sensores/Actuadores)|Nivel de Máquina|Nivel de Célula|Nivel de Fábrica", "r": "Nivel de Proceso/Campo (Sensores/Actuadores)", "j": "Donde interactúa el hardware físico."},
    {"p": "Un sistema ERP (Enterprise Resource Planning) se sitúa en el nivel de...", "tipo": "multiple", "opciones": "Gestión o empresa|Control de máquina|Célula|Campo", "r": "Gestión o empresa", "j": "Gestiona pedidos, compras, finanzas, RRHH."},
    {"p": "Un sistema MES (Manufacturing Execution System) sirve para...", "tipo": "multiple", "opciones": "Gestionar y monitorizar la producción en planta en tiempo real|Diseñar piezas|Programar PLCs|Contabilidad", "r": "Gestionar y monitorizar la producción en planta en tiempo real", "j": "Puente entre el ERP y el control de planta."},
    {"p": "Industria 4.0 se caracteriza por...", "tipo": "multiple", "opciones": "Interconectividad, Big Data, IoT y sistemas ciberfísicos|Uso de vapor|Producción en cadena eléctrica|Transistores", "r": "Interconectividad, Big Data, IoT y sistemas ciberfísicos", "j": "Cuarta revolución industrial."},
    {"p": "El 'Gemelo Digital' (Digital Twin) es...", "tipo": "multiple", "opciones": "Una réplica virtual del sistema físico para simulación y análisis|Un backup de datos|Dos máquinas iguales|Un robot duplicado", "r": "Una réplica virtual del sistema físico para simulación y análisis", "j": "Permite prever comportamientos y optimizar sin parar la producción."},

    # TEMA 8: DISEÑO PARA FABRICACIÓN
    {"p": "El Diseño para el Montaje (DFA) recomienda...", "tipo": "multiple", "opciones": "Reducir el número de piezas y unificar direcciones de montaje|Aumentar el número de tornillos|Usar piezas flexibles|Ocultar las uniones", "r": "Reducir el número de piezas y unificar direcciones de montaje", "j": "Simplifica el ensamblaje y reduce costes."},
    {"p": "La Ingeniería Concurrente implica...", "tipo": "multiple", "opciones": "Diseñar producto y proceso simultáneamente con equipos multidisciplinares|Diseñar primero y fabricar después (secuencial)|Contratar más ingenieros|Usar ordenadores rápidos", "r": "Diseñar producto y proceso simultáneamente con equipos multidisciplinares", "j": "Reduce el Time-to-Market y evita errores tardíos."},

    # TEMA 9: FABRICACIÓN DIGITAL
    {"p": "CAD significa Diseño Asistido por Ordenador.", "tipo": "multiple", "opciones":"", "r": "Vertader", "j": "Computer Aided Design."},
    {"p": "CAM significa...", "tipo": "multiple", "opciones": "Computer Aided Manufacturing|Computer Aided Mechanics|Control And Management|Computer Advanced Machine", "r": "Computer Aided Manufacturing", "j": "Generación de trayectorias (G-code) desde el modelo 3D."},
    {"p": "CAE significa Ingeniería Asistida por Ordenador (Simulación/Cálculo).", "tipo": "multiple", "opciones":"", "r": "Vertader", "j": "Computer Aided Engineering (ej. Elementos Finitos FEM)."},
    {"p": "CAPP significa...", "tipo": "multiple", "opciones": "Computer Aided Process Planning|Computer Aided Part Production|Control Automatic Part Placement|Computer Advanced Program Planning", "r": "Computer Aided Process Planning", "j": "Planificación automática de procesos (hòjas de ruta)."},
    {"p": "El formato STEP es un estándar neutro para intercambio de modelos CAD.", "tipo": "multiple", "opciones":"", "r": "Vertader", "j": "Permite pasar 3D entre distintos programas (Solidworks, Catia, etc.)."},
    {"p": "Un sistema PLM (Product Lifecycle Management) gestiona...", "tipo": "multiple", "opciones": "Toda la información del producto desde su concepción hasta su reciclaje|Solo el diseño CAD|Solo la producción|Las ventas", "r": "Toda la información del producto desde su concepción hasta su reciclaje", "j": "Gestión integral del ciclo de vida."},
]

# Quick drills and variations to reach ~200 count
extras = [
    # CNC G-Codes
    {"p": "G04 es el código de pausa (Dwell).", "tipo": "multiple", "opciones":"", "r": "Vertader", "j": "Detiene el avance un tiempo determinado."},
    {"p": "G17 selecciona el plano XY.", "tipo": "multiple", "opciones":"", "r": "Vertader", "j": "G18 XZ, G19 YZ."},
    {"p": "G20/G21 selecciona unidades (Pulgadas/Milímetros).", "tipo": "multiple", "opciones":"", "r": "Vertader", "j": "Normalmente G21 para mm."},
    {"p": "G28 vuelve al Home (Punto de referencia).", "tipo": "multiple", "opciones":"", "r": "Vertader", "j": "Retorno a referencia máquina."},
    {"p": "G40 cancela la compensación de radio.", "tipo": "multiple", "opciones":"", "r": "Vertader", "j": "Desactiva G41/G42."},
    {"p": "G43 compensa la longitud de la herramienta.", "tipo": "multiple", "opciones":"", "r": "Vertader", "j": "Compensación de altura H."},
    {"p": "G90 indica coordenadas absolutas.", "tipo": "multiple", "opciones":"", "r": "Vertader", "j": "Respecto al origen."},
    {"p": "G91 indica coordenadas incrementales.", "tipo": "multiple", "opciones":"", "r": "Vertader", "j": "Respecto al punto anterior."},
    {"p": "G94 define el avance en mm/min.", "tipo": "multiple", "opciones":"", "r": "Vertader", "j": "G95 en mm/rev."},
    {"p": "M00 es parada programada (incondicional).", "tipo": "multiple", "opciones":"", "r": "Vertader", "j": "Detiene el programa hasta pulsar marcha."},
    {"p": "M01 es parada opcional.", "tipo": "multiple", "opciones":"", "r": "Vertader", "j": "Solo para si el switch 'Optional Stop' está activo."},
    {"p": "M06 cambia la herramienta.", "tipo": "multiple", "opciones":"", "r": "Vertader", "j": "Ejecuta el cambio físico."},
    {"p": "M08 enciende refrigerante (Coolant On).", "tipo": "multiple", "opciones":"", "r": "Vertader", "j": "M09 lo apaga."},
    {"p": "M30 finaliza el programa y rebobina.", "tipo": "multiple", "opciones":"", "r": "Vertader", "j": "Vuelve al inicio."},
    
    # Robotics
    {"p": "La cinemática directa calcula la posición del TCP a partir de los ángulos de las articulaciones.", "tipo": "multiple", "opciones":"", "r": "Vertader", "j": "Ángulos -> Coord Cartesianas."},
    {"p": "La cinemática inversa calcula los ángulos necesarios para lograr una posición TCP.", "tipo": "multiple", "opciones":"", "r": "Vertader", "j": "Coord Cartesianas -> Ángulos."},
    {"p": "La singularidad de un robot es una posición donde pierde grados de libertad o control.", "tipo": "multiple", "opciones":"", "r": "Vertader", "j": "Suele provocar movimientos bruscos o error."},
    {"p": "El 'teach pendant' es el mando de programación manual del robot.", "tipo": "multiple", "opciones":"", "r": "Vertader", "j": "Consola de enseñanza."},
    {"p": "Un robot colaborativo (Cobot) puede trabajar junto a humanos sin vallado (bajo condiciones).", "tipo": "multiple", "opciones":"", "r": "Vertader", "j": "Tienen sensores de fuerza/par y limitaciones de potencia."},
    
    # Automation
    {"p": "Un sensor fotoeléctrico de barrera tiene emisor y receptor separados.", "tipo": "multiple", "opciones":"", "r": "Vertader", "j": "Detecta cuando se corta el haz."},
    {"p": "Un sensor reflex tiene emisor y receptor en el mismo cuerpo y usa espejo.", "tipo": "multiple", "opciones":"", "r": "Vertader", "j": "Más fácil de cablear."},
    {"p": "Los sensores PNP son comunes en Europa.", "tipo": "multiple", "opciones":"", "r": "Vertader", "j": "Conmutan a positivo (+24V). NPN conmuta a 0V."},
    {"p": "GRAFCET es un diagrama funcional para representar automatismos secuenciales.", "tipo": "multiple", "opciones":"", "r": "Vertader", "j": "Etapas, Transiciones y Acciones."},
    {"p": "Una etapa activa en GRAFCET habilita sus transiciones posteriores.", "tipo": "multiple", "opciones":"", "r": "Vertader", "j": "Regla de evolución."},
    
    # General
    {"p": "El Just in Time (JIT) busca reducir el stock a cero.", "tipo": "multiple", "opciones":"", "r": "Vertader", "j": "Producir lo necesario en el momento necesario."},
    {"p": "Kanban es una tarjeta o señal para controlar el flujo pull (tirar) de producción.", "tipo": "multiple", "opciones":"", "r": "Vertader", "j": "Herramienta visual del JIT."},
    {"p": "El control de calidad estadístico (SPC) usa gráficos de control.", "tipo": "multiple", "opciones":"", "r": "Vertader", "j": "Para detectar desviaciones del proceso."},
    {"p": "Six Sigma busca reducir la variabilidad del proceso (3.4 defectos por millón).", "tipo": "multiple", "opciones":"", "r": "Vertader", "j": "Metodología de mejora calidad."},
    {"p": "El mantenimiento correctivo se hace cuando la máquina se rompe.", "tipo": "multiple", "opciones":"", "r": "Vertader", "j": "No planificado."},
    {"p": "El mantenimiento preventivo se hace por tiempo o ciclos.", "tipo": "multiple", "opciones":"", "r": "Vertader", "j": "Planificado para evitar averías."},
    {"p": "El mantenimiento predictivo se basa en monitorizar el estado (vibraciones, temperatura).", "tipo": "multiple", "opciones":"", "r": "Vertader", "j": "Para intervenir justo antes del fallo."},
    {"p": "TPM significa Total Productive Maintenance.", "tipo": "multiple", "opciones":"", "r": "Vertader", "j": "Involucra a todos los operarios en el mantenimiento."},
    {"p": "OEE (Overall Equipment Effectiveness) mide la eficiencia global (Disponibilidad x Rendimiento x Calidad).", "tipo": "multiple", "opciones":"", "r": "Vertader", "j": "Indicador clave en TPM."},
    {"p": "Andon es un sistema de señales visuales/sonoras para alertar problemas.", "tipo": "multiple", "opciones":"", "r": "Vertader", "j": "Semáforos en máquinas."},
    {"p": "Kaizen significa mejora continua.", "tipo": "multiple", "opciones":"", "r": "Vertader", "j": "Filosofía japonesa."},
    {"p": "5S es una técnica de orden y limpieza.", "tipo": "multiple", "opciones":"", "r": "Vertader", "j": "Seiri, Seiton, Seiso, Seiketsu, Shitsuke."},
    {"p": "El layout en U favorece el trabajo en equipo y la flexibilidad.", "tipo": "multiple", "opciones":"", "r": "Vertader", "j": "Entrada y salida cercanas."},
    {"p": "El diagrama de Gantt sirve para planificar tareas en el tiempo.", "tipo": "multiple", "opciones":"", "r": "Vertader", "j": "Gestión de proyectos/producción."},
    {"p": "El MRP (Material Requirements Planning) calcula qué materiales comprar y cuándo.", "tipo": "multiple", "opciones":"", "r": "Vertader", "j": "Basado en lista de materiales y demanda."},
    {"p": "El MRP II incluye también capacidad y recursos (dinero, máquinas).", "tipo": "multiple", "opciones":"", "r": "Vertader", "j": "Evolución del MRP."},
    {"p": "El RFID usa ondas de radio para identificar etiquetas.", "tipo": "multiple", "opciones":"", "r": "Vertader", "j": "Radio Frequency Identification (alternativa al código de barras)."},
    {"p": "El código de barras requiere línea de visión directa.", "tipo": "multiple", "opciones":"", "r": "Vertader", "j": "El láser debe ver la etiqueta. RFID no."},
]

# Duplicate logic to reach 200+
# I have ~100 distinct questions defined above.
# I will replicate some common variations or logic to ensure volume if needed, 
# but for quality distinct questions, I will add more specific ones below.

more_questions = [
    {"p": "Una fresadora de 3 ejes tiene X, Y, Z.", "tipo": "multiple", "opciones":"", "r": "Vertader", "j": "Básicos."},
    {"p": "Un torno CNC básico tiene 2 ejes: X y Z.", "tipo": "multiple", "opciones":"", "r": "Vertader", "j": "X (diámetro), Z (longitud)."},
    {"p": "En un torno, el eje X controla el diámetro.", "tipo": "multiple", "opciones":"", "r": "Vertader", "j": "Transversal."},
    {"p": "En un torno, el eje Z es el eje de giro del cabezal.", "tipo": "multiple", "opciones":"", "r": "Vertader", "j": "Longitudinal."},
    {"p": "La Regla de la Mano Derecha define los ejes en CNC.", "tipo": "multiple", "opciones":"", "r": "Vertader", "j": "Dedo pulgar X, índice Y, medio Z."},
    {"p": "El eje rotativo alrededor de X se llama A.", "tipo": "multiple", "opciones":"", "r": "Vertader", "j": "Convención ISO."},
    {"p": "El eje rotativo alrededor de Y se llama B.", "tipo": "multiple", "opciones":"", "r": "Vertader", "j": "Convención ISO."},
    {"p": "El eje rotativo alrededor de Z se llama C.", "tipo": "multiple", "opciones":"", "r": "Vertader", "j": "Convención ISO."},
    {"p": "Una máquina de 5 ejes puede mecanizar geometrías complejas (álabes).", "tipo": "multiple", "opciones":"", "r": "Vertader", "j": "Orienta la herramienta."},
    {"p": "La electroerosión por hilo (WEDM) usa un hilo conductor para cortar.", "tipo": "multiple", "opciones":"", "r": "Vertader", "j": "Por descargas eléctricas."},
    {"p": "La electroerosión solo funciona con materiales conductores.", "tipo": "multiple", "opciones":"", "r": "Vertader", "j": "Necesita circuito eléctrico."},
    {"p": "El corte por láser puede cortar metal y plástico.", "tipo": "multiple", "opciones":"", "r": "Vertader", "j": "Térmico."},
    {"p": "El corte por chorro de agua no afecta térmicamente al material.", "tipo": "multiple", "opciones":"", "r": "Vertader", "j": "Proceso en frío (abrasivo)."},
    {"p": "La inyección de plástico es un proceso de ciclo rápido.", "tipo": "multiple", "opciones":"", "r": "Vertader", "j": "Alta producción."},
    {"p": "El molde de inyección suele refrigerarse con agua.", "tipo": "multiple", "opciones":"", "r": "Vertader", "j": "Para solidificar rápido."},
    {"p": "La impresión 3D FDM usa filamento plástico.", "tipo": "multiple", "opciones":"", "r": "Vertader", "j": "Fused Deposition Modeling."},
    {"p": "El SLA usa resina líquida y láser UV.", "tipo": "multiple", "opciones":"", "r": "Vertader", "j": "Estereolitografía."},
    {"p": "El SLS usa polvo y láser.", "tipo": "multiple", "opciones":"", "r": "Vertader", "j": "Sinterizado Selectivo Láser."},
    {"p": "En automatización, NO (Normally Open) significa abierto en reposo.", "tipo": "multiple", "opciones":"", "r": "Vertader", "j": "Cierra al activar."},
    {"p": "NC (Normally Closed) significa cerrado en reposo.", "tipo": "multiple", "opciones":"", "r": "Vertader", "j": "Abre al activar."},
    {"p": "Una electroválvula monoestable tiene retorno por muelle.", "tipo": "multiple", "opciones":"", "r": "Vertader", "j": "Necesita señal continua para estar activa."},
    {"p": "Una electroválvula biestable tiene memoria de posición.", "tipo": "multiple", "opciones":"", "r": "Vertader", "j": "Cambia con un pulso."},
    {"p": "El cilindro neumático de simple efecto tiene un solo orificio de aire.", "tipo": "multiple", "opciones":"", "r": "Vertader", "j": "Retorno muelle."},
    {"p": "El cilindro de doble efecto tiene dos orificios (avance/retroceso).", "tipo": "multiple", "opciones":"", "r": "Vertader", "j": "Aire para ir, aire para volver."},
    {"p": "El final de carrera es un sensor de contacto.", "tipo": "multiple", "opciones":"", "r": "Vertader", "j": "Mecánico."},
    {"p": "Un encoder absoluto recuerda la posición al apagar.", "tipo": "multiple", "opciones":"", "r": "Vertader", "j": "No necesita búsqueda de referencia."},
    {"p": "Un encoder incremental necesita buscar referencia al encender.", "tipo": "multiple", "opciones":"", "r": "Vertader", "j": "Cuenta pulsos desde cero."},
    {"p": "El servomotor es ideal para control preciso de posición.", "tipo": "multiple", "opciones":"", "r": "Vertader", "j": "CNC y robots."},
    {"p": "El motor trifásico asíncrono es el más robusto para industria general.", "tipo": "multiple", "opciones":"", "r": "Vertader", "j": "Jaula de ardilla."},
    {"p": "Un contactor tiene contactos de potencia y auxiliares.", "tipo": "multiple", "opciones":"", "r": "Vertader", "j": "Potencia para motor, auxiliares para mando."},
    {"p": "La seta de emergencia debe ser roja sobre fondo amarillo.", "tipo": "multiple", "opciones":"", "r": "Vertader", "j": "Normativa seguridad."},
    {"p": "La seta de emergencia debe tener enclavamiento mecánico.", "tipo": "multiple", "opciones":"", "r": "Vertader", "j": "Hay que desenclavar para rearmar."},
    {"p": "El relé de seguridad supervisa la parada de emergencia.", "tipo": "multiple", "opciones":"", "r": "Vertader", "j": "Doble canal redundante."},
    {"p": "Una barrera inmaterial protege al operario sin contacto físico.", "tipo": "multiple", "opciones":"", "r": "Vertader", "j": "Cortina de luz."},
    {"p": "El mando a dos manos obliga a tener las manos ocupadas para prensar.", "tipo": "multiple", "opciones":"", "r": "Vertader", "j": "Seguridad prensas."},
    {"p": "La ISO 9001 es la norma de gestión de calidad.", "tipo": "multiple", "opciones":"", "r": "Vertader", "j": "Estándar mundial."},
    {"p": "La ISO 14001 es la norma de gestión ambiental.", "tipo": "multiple", "opciones":"", "r": "Vertader", "j": "Medio ambiente."},
    {"p": "El diagrama de Ishikawa (Espina de Pescado) analiza causas-efecto.", "tipo": "multiple", "opciones":"", "r": "Vertader", "j": "Herramienta calidad."},
    {"p": "El Pareto dice que el 80% de problemas viene del 20% de causas.", "tipo": "multiple", "opciones":"", "r": "Vertader", "j": "Priorizar."},
    {"p": "AMFE significa Análisis Modal de Fallos y Efectos.", "tipo": "multiple", "opciones":"", "r": "Vertader", "j": "FMEA en inglés. Prever riesgos."},
    {"p": "El tiempo de ciclo es el tiempo entre dos piezas buenas consecutivas.", "tipo": "multiple", "opciones":"", "r": "Vertader", "j": "Cadencia producción."},
    {"p": "El tiempo de tacto (Takt Time) es el ritmo de la demanda del cliente.", "tipo": "multiple", "opciones":"", "r": "Vertader", "j": "La producción debe ajustarse al Takt."},
    {"p": "Si Ciclo > Takt, hay que producir más rápido.", "tipo": "multiple", "opciones":"", "r": "Vertader", "j": "O no llegamos a la demanda."},
    {"p": "El stock de seguridad cubre variaciones imprevistas.", "tipo": "multiple", "opciones":"", "r": "Vertader", "j": "Amortiguador."},
    {"p": "El cuello de botella determina la capacidad máxima del sistema.", "tipo": "multiple", "opciones":"", "r": "Vertader", "j": "La cadena es tan fuerte como el eslabón débil."},
    {"p": "La trazabilidad permite saber el historial de una pieza.", "tipo": "multiple", "opciones":"", "r": "Vertader", "j": "Lote, fecha, máquina, materiales."},
    {"p": "Un plano de conjunto muestra cómo van montadas las piezas.", "tipo": "multiple", "opciones":"", "r": "Vertader", "j": "Visión general."},
    {"p": "El despiece son los planos individuales de cada componente.", "tipo": "multiple", "opciones":"", "r": "Vertader", "j": "Para fabricar."},
    {"p": "La tolerancia geométrica controla forma y posición.", "tipo": "multiple", "opciones":"", "r": "Vertader", "j": "Rectitud, planitud, perpendicularidad..."},
    {"p": "La tolerancia dimensional controla medidas (largo, diámetro).", "tipo": "multiple", "opciones":"", "r": "Vertader", "j": "+/- mm."},
    {"p": "El ajuste H7/g6 es un ajuste con juego (móvil).", "tipo": "multiple", "opciones":"", "r": "Vertader", "j": "Agujero base H, eje g (menor)."},
    {"p": "El ajuste H7/p6 es un ajuste con apriete (fijo).", "tipo": "multiple", "opciones":"", "r": "Vertader", "j": "Eje p (mayor)."},
    {"p": "La rugosidad Ra mide la media aritmética de desviaciones del perfil.", "tipo": "multiple", "opciones":"", "r": "Vertader", "j": "Micrómetros."},
    {"p": "El micrómetro es más preciso que el pie de rey.", "tipo": "multiple", "opciones":"", "r": "Vertader", "j": "Centésima/Milésima vs Décima/Centésima."},
    {"p": "El comparador mide diferencias de medida.", "tipo": "multiple", "opciones":"", "r": "Vertader", "j": "No absoluto, sino relativo o forma."},
    {"p": "El goniómetro mide ángulos.", "tipo": "multiple", "opciones":"", "r": "Vertader", "j": "Grados."},
    {"p": "La MMC (CMM) mide coordenadas 3D automáticamente.", "tipo": "multiple", "opciones":"", "r": "Vertader", "j": "Control calidad preciso."}
]

questions.extend(extras)
questions.extend(more_questions)

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
