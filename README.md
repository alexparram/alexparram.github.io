# 📚 Plataforma de Estudio para Examenes Multirespuesta

¡Hola! 👋 Esta es una herramienta web diseñada para ayudarnos a preparar los exámenes tipo test de las asignaturas. Permite cargar preguntas desde archivos CSV y practicar de forma interactiva.

## 🚀 Cómo usar

Simplemente abre el enlace de la web (si estás viendo esto en GitHub, ve a la sección "Deployments" o al enlace de GitHub Pages).

1.  **Selecciona una asignatura**: Haz clic en una de las tarjetas (CAI, SiF, MT, PI).
2.  **Empieza a practicar**: Se cargarán las preguntas y podrás responderlas una a una.
3.  **Modos de estudio**: Puedes cambiar el modo de estudio en el menú desplegable de arriba a la derecha.

## 🧠 Modos de Estudio

*   **Modo Normal**: Las preguntas aparecen en orden secuencial (1, 2, 3...). Ideal para un primer repaso.
*   **Modo Aleatorio**: El orden de las preguntas se mezcla completamente al azar.
*   **Modo Inteligente (Algorithm Mode)**: 🚀 **¡Recomendado!**
    *   Este modo utiliza un algoritmo de probabilidad para priorizar las preguntas que fallas.
    *   Si fallas una pregunta, aumentan las posibilidades de que vuelva a salir pronto.
    *   Si aciertas, la probabilidad de que aparezca disminuye.
    *   Perfecto para asegurar que repasas lo que realmente te cuesta más.

## ⌨️ Controles

*   **Click en opción**: Seleccionar respuesta.
*   **Espacio**: Confirmar selección (si hay una seleccionada).
*   **Flecha Derecha (→)**: Siguiente pregunta.
*   **Flecha Izquierda (←)**: Pregunta anterior.
*   **Número (1-4)**: Seleccionar opción 1-4 rápidamente.

## 🔧 Detalles Técnicos (Opcional)

Si quieres ejecutar esto en tu propio ordenador (localmente):

1.  Descarga el código.
2.  Abre una terminal en la carpeta.
3.  Ejecuta: `python -m http.server 8000`
4.  Abre en tu navegador: `http://localhost:8000`

---
¡Mucha suerte con los exámenes! 🎓
