import cv2
from pyzbar.pyzbar import decode

def main():
    cap = cv2.VideoCapture(0)  # Usa a webcam padrão

    print("Pressione 'q' para sair.")

    while True:
        ret, frame = cap.read()
        if not ret:
            print("Não foi possível acessar a câmera.")
            break

        # Decodifica códigos de barras no frame
        barcodes = decode(frame)
        for barcode in barcodes:
            x, y, w, h = barcode.rect
            # Desenha retângulo ao redor do código
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

            barcode_data = barcode.data.decode('utf-8')
            barcode_type = barcode.type
            text = f'{barcode_type}: {barcode_data}'

            print(f'Detectado: {text}')
            # Mostra texto no frame
            cv2.putText(frame, text, (x, y - 10),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 2)

        cv2.imshow('Leitor de Código de Barras', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    main()
