import pandas as pd
import matplotlib.pyplot as plt


def csvRaporlama(dosya):
    df= pd.read_csv(dosya)
    rapor = df.describe() #istedigimiz ozetleri almamiza yarayan metod.
    print(rapor)
    rapor.to_csv("rapor.csv", index = True)
    df["maas"].plot(kind="hist")
    plt.show()
    return rapor

if __name__ == "__main__":
    dosyaAdi = input("Analiz edilecek `ornekCsv.csv` dosyasinin adini giriniz : ")
    rapor = csvRaporlama(dosyaAdi)
    raporAdi = input("Kayit edilecek raporun adi ne olsun ? ")
    rapor.to_csv(raporAdi, index=True)
    print(f"Raporunuz {raporAdi} olarak kaydedildi.")