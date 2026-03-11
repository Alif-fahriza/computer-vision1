import cv2

# 1. PERSIAPAN DATA (Otak Deteksi)
# Kita memanggil model deteksi wajah bawaan (Haar Cascade)
face_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# 2. PERSIAPAN VISUAL (Kamera)
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Error: Kamera tidak terdeteksi!")
    exit()

print("Jarvis Vision System Online. Tekan 'q' untuk keluar.")

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # 1. Proses Gambar
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.1, 5)

    # 2. Gambar Kotak & Teks
    for (x, y, w, h) in faces:
        # Ganti warna jadi MERAH (0, 0, 255)
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 0, 255), 2)
        cv2.putText(frame, "TARGET: USER", (x, y-10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 0, 255), 2)

    # 3. Hitung Jumlah
    jumlah_wajah = len(faces)
    cv2.putText(frame, f"Status: {jumlah_wajah} Target",
                (30, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 255), 2)

    # 4. Tampilkan Layar
    cv2.imshow('Jarvis Vision Alpha', frame)

    # 5. LOGIKA TOMBOL (KEYBOARD)
    key = cv2.waitKey(1) & 0xFF

    # Tombol 'q' untuk Quit/Keluar
    if key == ord('q'):
        break

    # Tombol 's' untuk Save/Simpan
    elif key == ord('s'):
        nama_file = "bukti_penyusup.jpg"
        cv2.imwrite(nama_file, frame)
        print(f"SUKSES! Foto disimpan sebagai: {nama_file}")

# Bersihkan memori
cap.release()
cv2.destroyAllWindows()
