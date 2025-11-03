wildlife-detection
Wildlife road detection GUI (simulated detections) — Python/Tkinter + OpenCV
---
# Wildlife Detection

Detección de fauna en carreteras — GUI en Python (simulación)

![Wildlife Detection](https://media.tenor.com/zvFLAFYSTroAAAAM/crossing-the-street-deer.gif)

Descripción
- Aplicación GUI en Python que simula detección de animales en la vía usando OpenCV y Tkinter.
- Pensada como demo/prototipo. La detección es simulada; en producción se puede sustituir por un modelo real (p. ej. YOLOv8).

Características
- Interfaz multilenguaje (es/en/it/fr/de/ru).
- Simulación configurable de detecciones (sensibilidad, confianza mínima).
- Visualización de video con anotaciones y alertas visuales.
- Manejo seguro de hilos y limpieza al cerrar la app (implementado).

Requisitos
- Python 3.8+
- Dependencias (requirements.txt):
  - opencv-python
  - Pillow
  - numpy

Instalación
1. Clonar el repositorio:
   git clone https://github.com/<tu-usuario>/wildlife-detection.git
2. Crear y activar virtualenv (recomendado):
   python -m venv venv
   source venv/bin/activate  # Linux/macOS
   venv\Scripts\activate     # Windows
3. Instalar dependencias:
   pip install -r requirements.txt

Uso
- Ejecutar la GUI:
  python wildlife_detection.py
- Seleccionar idioma, ajustar sensibilidad y confianza, y pulsar "Start Detection".
- Nota: la app intenta abrir la cámara por defecto (cámara 0). Para usar un archivo de vídeo edita el código o añade opción de CLI.

Archivos incluidos
- wildlife_detection.py — código principal (GUI + simulador de detección).
- README.md — este archivo.
- requirements.txt — dependencias.
- .gitignore — ignorar entornos virtuales y archivos temporales.
- LICENSE — Licencia GNU.
  
![Wildlife Detection1](Captura_deteccion.jpg)


Contribuir
- Pull requests bienvenidos. Para cambios importantes, abre un issue primero para discutir la propuesta.
- Respeta las buenas prácticas: tests, linters y type hints cuando corresponda.

Licencia
-GNU License — ver archivo LICENSE para el texto completo.
