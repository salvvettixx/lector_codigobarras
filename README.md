# 📸 OmniScan: Lector Pro de Códigos de Barras 1D

![Python](https://img.shields.io/badge/Python-3.8+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![OpenCV](https://img.shields.io/badge/OpenCV-4.x-5C3EE8?style=for-the-badge&logo=opencv&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Stable-brightgreen?style=for-the-badge)

**OmniScan** es una solución de escritorio ligera y eficiente para la lectura y decodificación de códigos de barras 1D en tiempo real. Utilizando el poder de **OpenCV** para el procesamiento de visión por computadora y **PyZbar** para la decodificación lógica, este script permite transformar cualquier webcam en un escáner industrial.

---

## 🌟 Características Principales

*   **⚡ Decodificación en Tiempo Real:** Procesamiento fluido de frames directamente desde la cámara web.
*   **🎯 Alta Precisión:** Utiliza algoritmos de localización para identificar códigos incluso en condiciones de luz subóptimas.
*   **📦 Soporte Multiformato:** Compatible con EAN-13, UPC-A, Code 128, Code 39, ITF y más.
*   **🎨 Interfaz Visual Dinámica:** Superposición de recuadros y etiquetas de texto sobre el video en vivo.
*   **📊 Log de Datos:** Salida detallada por consola para integraciones con otros sistemas o bases de datos.

---

## 🛠️ Stack Tecnológico

| Herramienta | Función |
| :--- | :--- |
| **Python** | Lenguaje núcleo del proyecto. |
| **OpenCV** | Gestión de video, procesamiento de imagen y dibujo en pantalla. |
| **PyZbar** | Librería especializada en decodificación de simbologías 1D. |

---

## 🚀 Guía de Inicio Rápido

### Requisitos Previos

- Python 3.8 o superior instalado.
- Una cámara web integrada o externa conectada.

### Instalación

1.  **Clonar el repositorio:**
    ```bash
    git clone https://github.com/salvvettixx/lector-codigo-barras.git
    cd lector-codigo-barras
    ```

2.  **Configurar el entorno (Opcional pero recomendado):**
    ```bash
    python -m venv venv
    source venv/bin/activate  # En Windows: venv\Scripts\activate
    ```

3.  **Instalar dependencias:**
    ```bash
    pip install -r requirements.txt
    ```

### Ejecución

Lanza la aplicación con un solo comando:

```bash
python lector_barras.py
```

*   **Salir:** Presiona la tecla `q` mientras la ventana de video está activa.

---

## 📖 Cómo funciona

El flujo de procesamiento sigue estos pasos:
1. **Captura:** Se obtiene el flujo de video crudo.
2. **Escaneo:** Se analizan los frames en busca de patrones de barras.
3. **Decodificación:** Se extrae el valor numérico/alfanumérico.
4. **Visualización:** Se dibuja un polígono delimitador y se muestra el dato en pantalla.

---

## 🌐 Demo & Documentación (GitHub Pages)

Puedes encontrar una guía interactiva y ejemplos de códigos de barras para probar en nuestra página oficial:
👉 [**Visitar OmniScan Web**](https://salvvettixx.github.io/lector-codigo-barras/)

---

## 📝 Licencia

Este proyecto está bajo la Licencia MIT. Siéntete libre de usarlo, modificarlo y distribuirlo.

---
Developed with 🚀 by [salvvettixx](https://github.com/salvvettixx)
