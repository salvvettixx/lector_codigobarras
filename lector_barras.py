import cv2
from pyzbar import pyzbar
import time
import sys

# Forzar salida inmediata en consola
print("--- TEST: EL PROGRAMA HA INICIADO ---")
sys.stdout.flush()

def main():
    # Inicializar la cámara (0 es usualmente la cámara integrada)
    print("[INFO] Iniciando cámara...")
    sys.stdout.flush()
    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        print("[ERROR] No se pudo abrir la cámara. Verifica que no esté en uso por otra app.")
        return

    print("[INFO] Lector listo. Presiona 'q' en la ventana de video para salir.")
    sys.stdout.flush()

    while True:
        # Leer un frame de la cámara
        ret, frame = cap.read()
        if not ret:
            print("[ERROR] No se pudo recibir el frame.")
            break

        # Buscar códigos de barras en el frame
        barcodes = pyzbar.decode(frame)

        # Iterar sobre los códigos detectados
        for barcode in barcodes:
            # Extraer los puntos del perímetro (bounding box)
            (x, y, w, h) = barcode.rect
            
            # Dibujar un rectángulo alrededor del código de barras
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

            # El dato del código de barras es un objeto bytes, lo convertimos a string
            barcode_data = barcode.data.decode("utf-8")
            barcode_type = barcode.type

            # Mostrar el contenido y tipo en la terminal
            print(f"[DETECTADO] Tipo: {barcode_type}, Datos: {barcode_data}")
            sys.stdout.flush()

            # Dibujar el texto sobre la imagen
            text = f"{barcode_data} ({barcode_type})"
            cv2.putText(frame, text, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 
                        0.5, (0, 255, 0), 2)

        # Ver el resultado en pantalla
        cv2.imshow("Lector de Codigo de Barras 1D", frame)

        # Salir si se presiona la tecla 'q'
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Limpiar al finalizar
    print("[INFO] Cerrando lector...")
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
