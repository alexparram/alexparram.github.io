import csv
import os

# Configuración de asignatura
subject = "Projectes d'Instalacions"

# File paths
csv_path = os.path.join(os.path.dirname(__file__), "..", "csv", subject, f"PI_preguntas.csv")

new_questions = [
    # ELECTRICITO - REBT AVANZADO
    {"p": "¿Cuál es la potencia máxima prevista para un grado de electrificación básico según REBT?", "tipo": "multiple", "opciones": "5750 W|7360 W|9200 W|3450 W", "r": "5750 W", "j": "Si supera 5750 W pasa a ser electrificación elevada."},
    {"p": "¿Qué circuito corresponde a la cocina y horno en electrificación básica?", "tipo": "multiple", "opciones": "C3|C1|C2|C4", "r": "C3", "j": "C1:Ilum, C2:Tomas, C3:Cocina/Horno, C4:Lavadora/Termo, C5:Baño/Cocina."},
    {"p": "La sección mínima de conductores para el circuito C1 (Iluminación) es...", "tipo": "multiple", "opciones": "1.5 mm2|2.5 mm2|4 mm2|6 mm2", "r": "1.5 mm2", "j": "Protegido con PIA de 10A."},
    {"p": "La sección mínima para el circuito C3 (Cocina/Horno) es habitualmente...", "tipo": "multiple", "opciones": "6 mm2|4 mm2|2.5 mm2|10 mm2", "r": "6 mm2", "j": "Protegido con PIA de 25A."},
    {"p": "¿Cuál es la tensión de seguridad en locales húmedos?", "tipo": "multiple", "opciones": "24 V|50 V|230 V|12 V", "r": "24 V", "j": "En locales secos es 50 V."},
    {"p": "El volumen 1 en un baño con bañera llega hasta una altura de...", "tipo": "multiple", "opciones": "2.25 m|3.00 m|Techo|0.60 m", "r": "2.25 m", "j": "Desde el suelo de la bañera hasta 2.25m."},
    {"p": "En el Volumen 2 de un baño, ¿se permiten enchufes o tomas de corriente?", "tipo": "multiple", "opciones": "No, salvo afeitadoras con trafo aislamiento|Sí, cualquiera IP44|Sí, cualquiera IP65|Sí, con diferencial 10mA", "r": "No, salvo afeitadoras con trafo aislamiento", "j": "Generalmente prohibidos tomas estándar 230V."},
    {"p": "El conductor de protección en una derivación individual de 16mm2 (fases) debe ser de...", "tipo": "multiple", "opciones": "16 mm2|10 mm2|6 mm2|Igual a la fase", "r": "16 mm2", "j": "Hasta 16mm2 de fase, la tierra es igual a la fase. A partir de 16mm2 es S/2 (con mín 16)."},
    {"p": "La caída de tensión máxima permitida en Derivación Individual para contadores concentrados es...", "tipo": "multiple", "opciones": "1.0 %|0.5 %|1.5 %|3.0 %", "r": "1.0 %", "j": "Para contadores centralizados. Si es único usuario es 1.5%."},
    {"p": "Un interruptor diferencial de 'Clase AC' es adecuado para...", "tipo": "multiple", "opciones": "Corrientes alternas senoidales normales|Corrientes pulsantes|Corrientes continuas|Cargas informáticas pesadas", "r": "Corrientes alternas senoidales normales", "j": "El estándar. Para electrónica/ordenadores se recomienda Clase A (inmunizado)."},
    {"p": "El número máximo de puntos de utilización (tomas) en el circuito C2 es de...", "tipo": "multiple", "opciones": "20|30|10|Ilimitado", "r": "20", "j": "Según ITC-BT-25."},
    {"p": "¿Qué diámetro exterior mínimo tiene el tubo para una Derivación Individual estándar?", "tipo": "multiple", "opciones": "32 mm|20 mm|40 mm|25 mm", "r": "32 mm", "j": "Mínimo normativo para DI."},

    # FONTANERIA - CTE HS4
    {"p": "El caudal instantáneo mínimo para un lavabo es de...", "tipo": "multiple", "opciones": "0.10 l/s|0.05 l/s|0.20 l/s|0.30 l/s", "r": "0.10 l/s", "j": "Según tabla CTE DB HS4."},
    {"p": "El caudal instantáneo mínimo para una ducha es de...", "tipo": "multiple", "opciones": "0.20 l/s|0.10 l/s|0.30 l/s|0.50 l/s", "r": "0.20 l/s", "j": "Igual que una bañera pequeña (0.20) o grande (0.30)."},
    {"p": "La velocidad del agua en tuberías metálicas no debe superar...", "tipo": "multiple", "opciones": "2.0 m/s|3.0 m/s|1.0 m/s|1.5 m/s", "r": "2.0 m/s", "j": "Para evitar erosión y ruido. En plásticos se admite algo más."},
    {"p": "En una red de retorno de ACS, el caudal se calcula para que la caída de temperatura no supere...", "tipo": "multiple", "opciones": "3 ºC|5 ºC|1 ºC|10 ºC", "r": "3 ºC", "j": "Entre la salida del acumulador y el punto más alejado."},
    {"p": "El fluxor requiere un caudal instantáneo mucho mayor que una cisterna.", "tipo": "multiple", "opciones":"", "r": "Vertader", "j": "Aprox 1.25 l/s vs 0.10 l/s de cisterna. Requiere cálculo especial."},
    {"p": "Las llaves de paso de cuarto húmedo deben estar entre...", "tipo": "multiple", "opciones": "Arriba, accesibles|Suelo|Techo falso|Fuera del cuarto", "r": "Arriba, accesibles", "j": "Deben ser accesibles para el usuario para corte de mantenimiento."},
    {"p": "El Polietileno Reticulado (PEX) tiene 'memoria térmica'.", "tipo": "multiple", "opciones":"", "r": "Vertader", "j": "Si se dobla, aplicando calor recupera su forma original."},
    {"p": "Las pruebas de estanqueidad en tuberías se hacen a una presión de...", "tipo": "multiple", "opciones": "1.5 veces la de trabajo (mín 6 bar)|Igual a la de trabajo|100 bar|1 bar", "r": "1.5 veces la de trabajo (mín 6 bar)", "j": "Para asegurar resistencia."},

    # SANEAMIENTO - CTE HS5
    {"p": "La ventilación secundaria en bajantes es obligatoria en edificios de más de...", "tipo": "multiple", "opciones": "7 plantas|3 plantas|5 plantas|10 plantas", "r": "7 plantas", "j": "O si hay más de 11 plantas si los ramales son cortos. Evita sobrepresiones."},
    {"p": "La ventilación terciaria ventila...", "tipo": "multiple", "opciones": "Los propios cierres hidráulicos (sifones)|La bajante|El colector|La arqueta", "r": "Los propios cierres hidráulicos (sifones)", "j": "Protege el cierre hidráulico localmente contra desifonamiento."},
    {"p": "El diámetro mínimo de una bajante de residuales es habitualmente...", "tipo": "multiple", "opciones": "110 mm|90 mm|75 mm|50 mm", "r": "110 mm", "j": "Para inodoros suele ser 110mm."},
    {"p": "La arqueta a pie de bajante debe ser registrable.", "tipo": "multiple", "opciones":"", "r": "Vertader", "j": "Punto crítico de atascos (cambio de vertical a horizontal)."},
    {"p": "Un bombeo de aguas fecales debe tener obligatoriamente...", "tipo": "multiple", "opciones": "Ventilación propia|Trituradora|Filtro de arena|Cloración", "r": "Ventilación propia", "j": "Para evacuar gases acumulados en el depósito de bombeo."},
    {"p": "Las válvulas de aireación pueden sustituir a la ventilación primaria.", "tipo": "multiple", "opciones":"", "r": "Fals", "j": "Pueden complementar o sustituir secundaria/terciaria en ciertos casos, pero la primaria (salida a cubierta) es necesaria para el alivio."},
    
    # CLIMATIZACIÓN - RITE
    {"p": "La Calidad de Aire Interior (IDA) para oficinas es...", "tipo": "multiple", "opciones": "IDA 2|IDA 1|IDA 3|IDA 4", "r": "IDA 2", "j": "Aire de buena calidad (Oficinas, enseñanza, residencias)."},
    {"p": "IDA 1 se requiere en...", "tipo": "multiple", "opciones": "Hospitales, clínicas|Cines|Gimnasios|Oficinas", "r": "Hospitales, clínicas", "j": "Aire de óptima calidad."},
    {"p": "El filtro ODA se refiere a la calidad del aire...", "tipo": "multiple", "opciones": "Exterior (Outdoor Air)|Interior (Indoor Air)|Expulsado|Recirculado", "r": "Exterior (Outdoor Air)", "j": "Clasifica la suciedad del aire exterior (ODA 1 puro, ODA 3 sucio)."},
    {"p": "El recuperador de calor es obligatorio cuando el caudal de aire expulsado es superior a...", "tipo": "multiple", "opciones": "0.28 m3/s (aprox 1000 m3/h)|0.5 m3/s|1.0 m3/s|Siempre", "r": "0.28 m3/s (aprox 1000 m3/h)", "j": "RITE IT 1.2.4.5.2."},
    {"p": "El COP define el rendimiento en modo...", "tipo": "multiple", "opciones": "Calefacción|Refrigeración|Ventilación|Deshumectación", "r": "Calefacción", "j": "Coefficient of Performance. Para frío es EER."},
    {"p": "Un sistema VRV (Volumen de Refrigerante Variable) permite...", "tipo": "multiple", "opciones": "Conectar múltiples unidades interiores a una exterior y control individual|Solo una unidad interior|Usar agua como fluido caloportador|Ventilar sin climatizar", "r": "Conectar múltiples unidades interiores a una exterior y control individual", "j": "Muy eficiente para edificios de oficinas."},
    {"p": "El suelo radiante se recomienda combinar con...", "tipo": "multiple", "opciones": "Bomba de calor aerotérmica/geotérmica|Radiadores eléctricos|Caldera de vapor|Estufas de leña", "r": "Bomba de calor aerotérmica/geotérmica", "j": "Por trabajar ambos a baja temperatura Eficiente."},
    
    # SOLAR / RENOVABLES - CTE HE
    {"p": "La contribución solar mínima para ACS en zona climática IV suele ser...", "tipo": "multiple", "opciones": "70 %|30 %|100 %|50 %", "r": "70 %", "j": "Depende del volumen, pero suele ser 60-70%."},
    {"p": "El fluido del circuito primario solar debe llevar...", "tipo": "multiple", "opciones": "Anticongelante (Glicol)|Solo agua|Aceite|Aire", "r": "Anticongelante (Glicol)", "j": "Para evitar congelación en invierno y rotura de paneles."},
    {"p": "La inclinación óptima de paneles solares térmicos para ACS todo el año es...", "tipo": "multiple", "opciones": "Latitud geográfica aprox (40º en BCN)|0º (Horizontales)|90º (Verticales)|15º", "r": "Latitud geográfica aprox (40º en BCN)", "j": "Maximiza captación anual. Para calefacción (invierno) se inclinan más (Latitud + 10º)."},
    {"p": "El 'efecto termosifón' permite la circulación natural del fluido sin bomba.", "tipo": "multiple", "opciones":"", "r": "Vertader", "j": "El agua caliente sube por densidad. El depósito debe estar más alto que el panel."},
    {"p": "Un MPPT en un inversor fotovoltaico sirve para...", "tipo": "multiple", "opciones": "Seguir el punto de máxima potencia del panel|Transformar DC a AC|Desconectar la batería|Monitorizar la temperatura", "r": "Seguir el punto de máxima potencia del panel", "j": "Optimiza el rendimiento del string fotovoltaico."},
    {"p": "El vertido cero impide inyectar excedentes a la red.", "tipo": "multiple", "opciones":"", "r": "Vertader", "j": "Mediante un sistema antivertido que regula el inversor."},
    
    # TELECOMUNICACIONES - ICT
    {"p": "El RITI (Recinto de Instalaciones de Telecomunicaciones Inferior) aloja...", "tipo": "multiple", "opciones": "Registros de operadores de telefonía, fibra y coaxial|Cabecera de TV satélite|Solo contadores eléctricos|Bombas de agua", "r": "Registros de operadores de telefonía, fibra y coaxial", "j": "Es el punto de entrada desde la calle."},
    {"p": "El RITS (Superior) aloja principalmente...", "tipo": "multiple", "opciones": "Cabeceras de TV terrestre y satélite|Telefonía|Fibra óptica|Videoportero", "r": "Cabecera de TV terrestre y satélite", "j": "Cerca de las antenas en cubierta."},
    {"p": "La red de dispersión enlaza...", "tipo": "multiple", "opciones": "La red de distribución con la red interior de usuario (PAU)|La antena con el RITS|El RITI con el RITS|La arqueta con el RITI", "r": "La red de dispersión enlaza la red de distribución con el PAU.", "j": "Es el tramo final que entra en la vivienda."},
    {"p": "El PAU (Punto de Acceso al Usuario) se sitúa en...", "tipo": "multiple", "opciones": "El Registro de Terminación de Red (RTR) en la entrada de la vivienda|El salón|El RITI|El rellano", "r": "El Registro de Terminación de Red (RTR) en la entrada de la vivienda", "j": "Frontera entre la comunidad y el usuario."},
    {"p": "El cable de pares trenzados Cat 6 permite velocidades de hasta...", "tipo": "multiple", "opciones": "1 Gbps (o 10Gbps en cortas)|100 Mbps|10 Mbps|100 Gbps", "r": "1 Gbps (o 10Gbps en cortas)", "j": "Estándar Gigabit Ethernet."},
    {"p": "El cable coaxial para TV terrestre suele tener una impedancia de...", "tipo": "multiple", "opciones": "75 Ohmios|50 Ohmios|100 Ohmios|8 Ohmios", "r": "75 Ohmios", "j": "Estándar RG-6 o RG-59 para TV. (50 Ohmios es para radio/wifi)."},
    {"p": "En una ICT, se debe dejar previsión de _ cables coaxiales por vivienda.", "tipo": "multiple", "opciones": "2|1|3|0", "r": "2", "j": "Uno para RTV terrestre y otro para Satélite/Cable, hasta el PAU."},

    # MEASUREMENT & TOOLS
    {"p": "Para medir el aislamiento de una instalación se usa un...", "tipo": "multiple", "opciones": "Megóhmetro (Megger)|Multímetro|Telurometro|Luxómetro", "r": "Megóhmetro (Megger)", "j": "Aplica alta tensión DC (500V/1000V) para medir resistencia de aislamiento."},
    {"p": "El Telurómetro mide...", "tipo": "multiple", "opciones": "La resistencia de la toma de tierra|La continuidad|La tensión|El aislamiento", "r": "La resistencia de la toma de tierra", "j": "Imprescindible para verificar la puesta a tierra."},
    {"p": "La continuidad del conductor de protección se verifica con...", "tipo": "multiple", "opciones": "Un ohmímetro y corriente de 200mA|Un voltímetro|Un luxómetro|La mano", "r": "Un ohmímetro y corriente de 200mA", "j": "Para asegurar que la tierra llega bien a todos los enchufes."},

    # EXTRAS MEZCLADOS
    {"p": "La iluminación de emergencia debe proporcionar al menos...", "tipo": "multiple", "opciones": "1 lux en el eje de evacuación|10 lux|50 lux|0.5 lux", "r": "1 lux en el eje de evacuación", "j": "Mínimo CTE-DB-SUA."},
    {"p": "En el cuadro general de mando y protección, el IGA es...", "tipo": "multiple", "opciones": "Interruptor General Automático|Interruptor General de Alimentación|Indice General de Aislamiento|Interruptor de Gas", "r": "Interruptor General Automático", "j": "Corta toda la instalación y protege derivación individual."},
    {"p": "El PCS (Protector Contra Sobretensiones) protege contra...", "tipo": "multiple", "opciones": "Picos de tensión (rayos, maniobras)|Cortocircuitos|Derivaciones|Sobrecargas", "r": "Picos de tensión (rayos, maniobras)", "j": "Protege electrónica sensible. Obligatorio si hay pararrayos o línea aérea."},
    {"p": "¿Qué es una instalación domótica con topología en estrella?", "tipo": "multiple", "opciones": "Todos los cables van a un cuadro central|Los elementos se conectan en serie|No usa cables|Es inalámbrica", "r": "Todos los cables van a un cuadro central", "j": "Típico de sistemas centralizados. KNX suele ser bus (línea/árbol)."},
    {"p": "Un detector de humo óptico es eficaz para...", "tipo": "multiple", "opciones": "Humos visibles (fuegos lentos)|Fuegos rápidos sin humo|Fuegos de alcohol|Gases", "r": "Humos visibles (fuegos lentos)", "j": "Detecta oscurecimiento o dispersión de luz."},
    {"p": "Un detector termovelocimétrico salta por...", "tipo": "multiple", "opciones": "Un aumento rápido de temperatura|Llegar a una temperatura fija|Humo|Llama", "r": "Un aumento rápido de temperatura", "j": "Detecta la velocidad de subida (gradiente)."},
    {"p": "En climatización, un sistema a 2 tubos permite...", "tipo": "multiple", "opciones": "Frío O Calor en todo el edificio a la vez|Frío Y Calor simultáneo en distintas zonas|Solo Frío|Solo Calor", "r": "Frío O Calor en todo el edificio a la vez", "j": "Con 4 tubos se puede tener zonas en frío y zonas en calor simultáneamente."},
    {"p": "El fancoil es una unidad terminal de...", "tipo": "multiple", "opciones": "Agua-Aire|Refrigerante-Aire|Aire-Aire|Agua-Agua", "r": "Agua-Aire", "j": "Le llega agua (fría/caliente) y tiene un ventilador."},
    {"p": "La 'clase de reacción al fuego' de un cable (ej. Cca-s1,d1,a1) define...", "tipo": "multiple", "opciones": "Su comportamiento como combustible (propagación, humos, gotas, acidez)|Su resistencia a seguir funcionando|Su aislamiento eléctrico|Su color", "r": "Su comportamiento como combustible (propagación, humos, gotas, acidez)", "j": "Reglamento CPR (Construction Products Regulation)."},
    {"p": "Un cable AS (Alta Seguridad) aguanta el fuego y permite seguir funcionando (Resistencia).", "tipo": "multiple", "opciones":"", "r": "Vertader", "j": "Denominado RF (Resistente al Fuego). Importante diferenciar reacción vs resistencia."},
    {"p": "El esquema de conexión a tierra TT es el obligatorio en viviendas en España.", "tipo": "multiple", "opciones":"", "r": "Vertader", "j": "Neutro a tierra en trafo, Masas a tierra local. Diferencial imprescindible."},
    {"p": "En una vivienda, la toma de tierra del edificio se conecta al borne principal de tierra.", "tipo": "multiple", "opciones":"", "r": "Vertader", "j": "De ahí sale a la derivación individual."},
    {"p": "Si toco un cable de fase pelado, estoy sufriendo un contacto...", "tipo": "multiple", "opciones": "Directo|Indirecto|Inducido|Capacitivo", "r": "Directo", "j": "Tocar partes activas es contacto directo. Tocar carcasa con fuga es indirecto."},
    {"p": "El grado de protección IK mide...", "tipo": "multiple", "opciones": "Resistencia a impactos mecánicos|Protección contra agua|Aislamiento térmico|Protección solar", "r": "Resistencia a impactos mecánicos", "j": "Escala IK00 a IK10 (martillazo)."},
    {"p": "Un diferencial de 30mA se considera de...", "tipo": "multiple", "opciones": "Alta sensibilidad|Baja sensibilidad|Industrial|Retardado", "r": "Alta sensibilidad", "j": "Protege a las personas (fibrilación). 300mA es para riesgo incendio o industrial."},
    {"p": "La resistividad del terreno se mide en...", "tipo": "multiple", "opciones": "Ohmios metro|Ohmios|Voltios|Siemens", "r": "Ohmios metro", "j": "Característica del suelo."},
    {"p": "Para mejorar una toma de tierra se puede...", "tipo": "multiple", "opciones": "Añadir más picas, profundizar o usar geles conductores|Echar agua salada temporalmente (no definitivo)|Poner picas más cortas|Aislar las picas", "r": "Añadir más picas, profundizar o usar geles conductores", "j": "Busca bajar la resistencia de contacto."},
    {"p": "El 'anillo de distribución' en fontanería garantiza presión más uniforme.", "tipo": "multiple", "opciones":"", "r": "Vertader", "j": "Alimenta desde dos lados."},
    {"p": "La 'Junta de dilatación' en tuberías absorbe los cambios de longitud por temperatura.", "tipo": "multiple", "opciones":"", "r": "Vertader", "j": "Mediante liras o fuelles."},
    {"p": "El 'golpe de ariete' se produce por...", "tipo": "multiple", "opciones": "Cierre brusco de válvulas|Exceso de caudal|Baja presión|Aire en la tubería", "r": "Cierre brusco de válvulas", "j": "Onda de presión que puede romper tuberías. Se evita con dispositivos antiariete."},
    {"p": "Una bomba centrífuga no debe funcionar en seco.", "tipo": "multiple", "opciones":"", "r": "Vertader", "j": "Se quema el sello mecánico por falta de lubricación/refrigeración."},
    {"p": "La cavitación en bombas produce...", "tipo": "multiple", "opciones": "Ruido, erosión y pérdida de rendimiento|Mejor bombeo|Aumento de presión|Enfriamiento", "r": "Ruido, erosión y pérdida de rendimiento", "j": "Formación de burbujas de vapor por baja presión en aspiración."},
    {"p": "El vaso de expansión cerrado tiene una membrana y gas (aire/nitrógeno).", "tipo": "multiple", "opciones":"", "r": "Vertader", "j": "Absorbe la dilatación del agua en calefacción/ACS."},
    {"p": "En un suelo radiante, el paso de tubos es más estrecho cerca de las ventanas.", "tipo": "multiple", "opciones":"", "r": "Vertader", "j": "Para combatir la mayor pérdida térmica por el vidrio."},
    {"p": "El equilibrado hidráulico es necesario para que todos los radiadores calienten igual.", "tipo": "multiple", "opciones":"", "r": "Vertader", "j": "Evita que el agua haga 'cortocircuito' por el camino más fácil."},
    {"p": "Una válvula termostática en radiador regula la temperatura de la habitación.", "tipo": "multiple", "opciones":"", "r": "Vertader", "j": "Abre o cierra el caudal según Tª ambiente."},
    {"p": "La biomasa (pellets) tiene balance de CO2 neutro teóricamente.", "tipo": "multiple", "opciones":"", "r": "Vertader", "j": "El CO2 emitido es el que capturó el árbol al crecer."},
    {"p": "Una instalación de gas butano requiere rejilla de ventilación inferior.", "tipo": "multiple", "opciones":"", "r": "Vertader", "j": "El gas pesa más que el aire y se acumula abajo."},
    {"p": "El 'tiro' de una chimenea depende de la diferencia de temperatura y altura.", "tipo": "multiple", "opciones":"", "r": "Vertader", "j": "Aire caliente sube por densidad."},
    {"p": "La energía reactiva se penaliza en la factura eléctrica industrial.", "tipo": "multiple", "opciones":"", "r": "Vertader", "j": "Si el cos phi es bajo (<0.95). Se corrige con baterías de condensadores."},
    {"p": "Un vatímetro mide potencia reactiva.", "tipo": "multiple", "opciones":"", "r": "Fals", "j": "Mide activa (W). El varímetro mide reactiva (var)."},
    {"p": "La selectividad protecciones asegura que salte solo el disyuntor más cercano al fallo.", "tipo": "multiple", "opciones":"", "r": "Vertader", "j": "Evita apagones generales por un fallo local."},
    {"p": "El ICP (Interruptor de Control de Potencia) ya está integrado en el contador digital.", "tipo": "multiple", "opciones":"", "r": "Vertader", "j": "Antes era un aparato físico en el cuadro."},
    {"p": "La tarifa de acceso 2.0TD tiene discriminación horaria en 3 periodos (Punta, Llano, Valle).", "tipo": "multiple", "opciones":"", "r": "Vertader", "j": "Estándar actual para <15kW."},
    {"p": "El periodo Valle es el más caro.", "tipo": "multiple", "opciones":"", "r": "Fals", "j": "Es el más barato (noche y fines de semana). Punta es el caro."},
    {"p": "En una ICT, el cable de acometida entra por la arqueta de entrada.", "tipo": "multiple", "opciones":"", "r": "Vertader", "j": "Punto de conexión con operadores."},
    {"p": "La red de alimentación en ICT une el RITI con el RITS.", "tipo": "multiple", "opciones":"", "r": "Fals", "j": "Esa es la red de distribución? No, alimentación es operador->RITI. La que sube es distribución/dispersión vertical."},
    {"p": "La mezcla de señales TV SAT y Terrestre se hace mediante...", "tipo": "multiple", "opciones": "Mezclador diplexor|Amplificador|Derivador|PAU", "r": "Mezclador diplexor", "j": "Permite bajar un solo cable con ambas frecuencias."},
    {"p": "La banda de frecuencias de TV Terrestre (UHF) va de...", "tipo": "multiple", "opciones": "470 a 790 MHz (ahora menos por 5G)|88 a 108 MHz|5 a 2150 MHz|2.4 GHz", "r": "470 a 790 MHz (ahora menos por 5G)", "j": "Recorte por Dividendo Digital (700MHz)."},
    {"p": "La atenuación de un cable coaxial aumenta con la frecuencia.", "tipo": "multiple", "opciones":"", "r": "Vertader", "j": "Pierde más señal en frecuencias altas (Satélite) que bajas."},
    {"p": "El cable de pares de cobre telefónico tradicional se llama...", "tipo": "multiple", "opciones": "Par trenzado Cat3 (o par telefónico)|Coaxial|Fibra|Guíaondas", "r": "Par trenzado Cat3 (o par telefónico)", "j": "Uso en telefonía básica (POTS)."}
]

# Ensure plenty of questions
# I have listed about 75 manual questions above.
# I will repeat generic logic to ensure we hit 100 or simply rely on the quality of these 75 strong ones?
# User asked for "otras 100". I should provide 100.
# I will generate 25 more quick drill questions.

quick_drills = [
    {"p": "El reglamento de gas es el RIGLO.", "tipo": "multiple", "opciones":"", "r": "Fals", "j": "Es el Reglamento Técnico de Distribución y Utilización de Combustibles Gaseosos (RD 919/2006)."},
    {"p": "La presión del gas natural en vivienda es de 20-22 mbar.", "tipo": "multiple", "opciones":"", "r": "Vertader", "j": "Baja presión domestica."},
    {"p": "Un vatio es igual a un julio por segundo.", "tipo": "multiple", "opciones":"", "r": "Vertader", "j": "Definición física de potencia."},
    {"p": "La Ley de Ohm es V = I * R.", "tipo": "multiple", "opciones":"", "r": "Vertader", "j": "Física básica."},
    {"p": "La frecuencia de la red en Europa es 60 Hz.", "tipo": "multiple", "opciones":"", "r": "Fals", "j": "Es 50 Hz. 60 Hz es América."},
    {"p": "Un sistema fotovoltaico aislado necesita baterías obligatoriamente para la noche.", "tipo": "multiple", "opciones":"", "r": "Vertader", "j": "Si no hay red, se necesita acumulación."},
    {"p": "El agua caliente pesa menos que la fría.", "tipo": "multiple", "opciones":"", "r": "Vertader", "j": "Menor densidad, estratifica arriba."},
    {"p": "El PVC se puede usar para ACS.", "tipo": "multiple", "opciones":"", "r": "Fals", "j": "No aguanta temperatura (se ablanda >60ºC). Se usa CPVC o PPR/PEX."},
    {"p": "Una caldera estanca coge el aire de la habitación.", "tipo": "multiple", "opciones":"", "r": "Fals", "j": "Lo coge del exterior por tubo coaxial."},
    {"p": "El rendimiento de una caldera de condensación puede superar el 100% (sobre PCI).", "tipo": "multiple", "opciones":"", "r": "Vertader", "j": "Al recuperar el calor latente del vapor de agua."},
    {"p": "El aire primario en climatización es aire tratado exterior.", "tipo": "multiple", "opciones":"", "r": "Vertader", "j": "Para ventilación."},
    {"p": "Un difusor rotacional mezcla bien el aire impulsado con el ambiente.", "tipo": "multiple", "opciones":"", "r": "Vertader", "j": "Alta inducción."},
    {"p": "La rejilla de retorno suele tener dimensión mayor que la impulsión.", "tipo": "multiple", "opciones":"", "r": "Vertader", "j": "Para menor velocidad y ruido."},
    {"p": "El plenum es una caja de distribución de aire.", "tipo": "multiple", "opciones":"", "r": "Vertader", "j": "Antes de la rejilla o difusor."},
    {"p": "El caudalímetro mide la presión.", "tipo": "multiple", "opciones":"", "r": "Fals", "j": "Mide el caudal."},
    {"p": "El preostato actúa por presión.", "tipo": "multiple", "opciones":"", "r": "Vertader", "j": "Interruptor de presión."},
    {"p": "El termostato actúa por temperatura.", "tipo": "multiple", "opciones":"", "r": "Vertader", "j": "Interruptor de temperatura."},
    {"p": "Una electroválvula se abre/cierra eléctricamente.", "tipo": "multiple", "opciones":"", "r": "Vertader", "j": "Control automático."},
    {"p": "El contactor sirve para maniobrar potencias elevadas.", "tipo": "multiple", "opciones":"", "r": "Vertader", "j": "El relé es para maniobra (poca potencia)."},
    {"p": "La categoría AC-3 de un contactor es para cargas resistivas.", "tipo": "multiple", "opciones":"", "r": "Fals", "j": "AC-1 resistivas. AC-3 motores (inductivas)."},
    {"p": "El guardamotor protege contra cortocircuito y sobrecarga del motor.", "tipo": "multiple", "opciones":"", "r": "Vertader", "j": "Todo en uno ajustado al motor."},
    {"p": "El arranque estrella-triángulo reduce la corriente de arranque.", "tipo": "multiple", "opciones":"", "r": "Vertader", "j": "Arranca a menor tensión (1/raiz3)."},
    {"p": "Un variador de frecuencia controla la velocidad de un motor AC.", "tipo": "multiple", "opciones":"", "r": "Vertader", "j": "Variando Hz."},
    {"p": "La bomba de calor absorbe calor del foco frío.", "tipo": "multiple", "opciones":"", "r": "Vertader", "j": "Principios termodinámicos. Parece magia pero es física."},
    {"p": "El refrigerante R-32 es más ecológico que el R-410A.", "tipo": "multiple", "opciones":"", "r": "Vertader", "j": "Menor PCA (Potencial Calentamiento Atmosférico)."},
    {"p": "La unidad interior de un aire acondicionado condensa agua en verano.", "tipo": "multiple", "opciones":"", "r": "Vertader", "j": "Deshumidifica el aire al enfriarlo. Necesita desagüe."},
    {"p": "La unidad exterior condensa agua en invierno (calefacción).", "tipo": "multiple", "opciones":"", "r": "Vertader", "j": "La batería exterior se enfría y condensa/escarcha."},
    {"p": "Es legal unir tierras de antena y eléctrica.", "tipo": "multiple", "opciones":"", "r": "Vertader", "j": "Es obligatorio (equipotencialidad)."},
    {"p": "La toma de tierra debe ser independiente para el pararrayos.", "tipo": "multiple", "opciones":"", "r": "Fals", "j": "Se recomienda unir todas las tierras bajo tierra para equipotencialidad, aunque tenga su pica propia."},
    {"p": "El lux es lumen partido por metro cuadrado.", "tipo": "multiple", "opciones":"", "r": "Vertader", "j": "Definición exacta."}
]

new_questions.extend(quick_drills)

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
                q['tipo'],
                q.get('opciones', ''),
                q['r'],
                q['j']
            ])
            
    print(f"Successfully appended {len(new_questions)} questions.")

if __name__ == "__main__":
    append_to_csv()
