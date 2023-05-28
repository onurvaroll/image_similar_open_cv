import os
import cv2
import numpy as np

def main():
    image_files = os.listdir(r"C:/Users/onurv/Desktop/Algoritma Analizi/ks2_2/image")  
    # Görüntülerin olduğu dizini belirtiyoruz

    resimler = []
    taranan_resimler = {}

    for i, image_file in enumerate(image_files):
        image_path = os.path.join(r"C:/Users/onurv/Desktop/Algoritma Analizi/ks2_2/image", image_file)
        resimler.append(cv2.imread(image_path))

        # Görüntüleri ön belleğe kaydediyoruz
        gray_image = cv2.cvtColor(resimler[i], cv2.COLOR_BGR2GRAY)
        processed_image = cv2.matchTemplate(gray_image, gray_image, cv2.TM_CCOEFF_NORMED)
        taranan_resimler[i] = processed_image

    benzerlik_listesi = benzer_resimleri_bul(resimler, taranan_resimler)
    
    # benzerlik oranları ile resimleri ekrana yazdırıyoruz
    for benzerlik in benzerlik_listesi:
        print("Image 1: " + benzerlik[0])
        print("Image 2: " + benzerlik[1])
        print("benzerlik: " + str(benzerlik[2]))
        print()

    input()

def benzer_resimleri_bul(resimler, taranan_resimler):
    benzerlik_listesi = []

    for i in range(len(resimler)):
        for j in range(i + 1, len(resimler)):
            benzerlik = benzerlik_hesaplama(taranan_resimler[i], taranan_resimler[j])
            benzerlik_listesi.append((str(i), str(j), benzerlik))

    benzerlik_listesi.sort(key=lambda x: x[2], reverse=True)  # Benzerlik oranına göre listeyi sıralar

    return benzerlik_listesi

def benzerlik_hesaplama(taranan_resim_1, taranan_resim_2):
    _, deger1, _, _ = cv2.minMaxLoc(taranan_resim_1)
    _, deger2, _, _ = cv2.minMaxLoc(taranan_resim_2)

    return max(deger1, deger2)

if __name__ == "__main__":
    main()
