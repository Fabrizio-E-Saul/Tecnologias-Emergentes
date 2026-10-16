# Laboratorio 02: Librerías para Datos y Automatización

**Curso:** Tecnologías Emergentes  
**Estudiante:** [Tu Nombre]  

## Descripción del Proyecto
Este proyecto contiene la implementación de un flujo de datos que consume pronósticos del clima para la ciudad de Huancayo desde una API REST, procesa la información con NumPy y Pandas, y exporta los resultados formateados.

## Flujo de Datos
1. **Fuente:** Consumo de la API pública Open-Meteo para obtener datos meteorológicos de Huancayo.
2. **Transformación:** Procesamiento de datos con NumPy y Pandas para calcular la amplitud térmica y clasificar los días según la temperatura.
3. **Salida:** Exportación de resultados a archivos `.json` y `.csv` (`pronostico_huancayo_procesado.csv` y `resumen_por_categoria.csv`).

## Cierre de la Unidad I — Semana 3
Herramienta de automatización: organizador.py clasifica y mueve archivos
de una carpeta en subcarpetas por tipo (Documentos, Imagenes, Videos,
Comprimidos, Otros), con modo de simulacion (--dry-run) mediante argparse.
Uso:
```
python organizador.py <carpeta> [--dry-run]
```
Pruebas: test_organizador.py cubre clasificacion, movimiento real y modo
simulacion, usando la fixture tmp_path de pytest para no afectar el
sistema de archivos real. Ejecutar con: pytest -v
