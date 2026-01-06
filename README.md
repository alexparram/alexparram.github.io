# 📚 Sistema de Estudio para Examen CAI

Sistema completo para extraer preguntas de PDF y estudiar de forma interactiva.

## 🚀 Cómo usar

### Paso 1: Extraer preguntas del PDF

Ejecuta el script de Python para extraer todas las preguntas del PDF y guardarlas en CSV:

```bash
python extract_questions.py
```

Esto creará el archivo `preguntas.csv` con todas las preguntas extraídas del PDF.

### Paso 2: Estudiar con la interfaz web

**Opción A - Usando el script automático (RECOMENDADO):**

Simplemente haz doble clic en:
```
iniciar_servidor.bat
```

Esto iniciará un servidor web local y abrirá automáticamente la interfaz de estudio en tu navegador.

**Opción B - Manual:**

```bash
# Iniciar servidor HTTP local
python -m http.server 8000

# Luego abre en tu navegador:
# http://localhost:8000/estudiar.html
```

## 📁 Archivos del sistema

- **extract_questions.py** - Script de Python que extrae preguntas del PDF
- **preguntas.csv** - Archivo CSV con todas las preguntas (generado automáticamente)
- **estudiar.html** - Interfaz web interactiva para estudiar
- **iniciar_servidor.bat** - Script para iniciar el servidor fácilmente

## ✨ Características de la interfaz

- ✅ Diseño moderno con gradientes y animaciones
- ✅ Navegación pregunta por pregunta
- ✅ Feedback inmediato de respuestas correctas/incorrectas
- ✅ Contador de progreso y estadísticas
- ✅ Botón para ver la respuesta correcta
- ✅ Navegación con teclado (flechas ← →)
- ✅ Barra de progreso visual

## 🎯 Controles

- **Click en opción** - Seleccionar y verificar respuesta
- **Siguiente →** - Ir a la siguiente pregunta
- **← Anterior** - Volver a la pregunta anterior
- **💡 Ver Respuesta** - Mostrar la respuesta correcta sin seleccionar
- **Tecla →** - Siguiente pregunta
- **Tecla ←** - Pregunta anterior

## ⚙️ Requisitos

- Python 3.x
- Biblioteca pdfplumber (instalada automáticamente si usas pip)

## 🔧 Solución de problemas

**Si el CSV no carga:**
- Asegúrate de usar el servidor HTTP local (iniciar_servidor.bat)
- No abras estudiar.html directamente desde el explorador de archivos

**Si no se extraen preguntas:**
- Verifica que el archivo PDF esté en la misma carpeta
- Revisa la estructura del PDF (debe contener texto extraíble)

## 📊 Datos extraídos

El CSV contiene las siguientes columnas:
- **numero** - Número de la pregunta
- **pregunta** - Texto de la pregunta
- **tipo** - Tipo de pregunta (verdadero_falso, multiple)
- **opciones** - Opciones de respuesta
- **respuesta_correcta** - La respuesta correcta

¡Buena suerte con tu estudio! 🎓
