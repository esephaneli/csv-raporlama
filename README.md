# CSV Raporlama

Bu Python projesi, verilen bir **CSV dosyasındaki sayısal sütunlar** için
otomatik özet istatistikleri çıkarır ve sonucu yeni bir CSV dosyasına kaydeder.
Ayrıca seçilen sütun (ör: `maas`) için histogram grafiği çizer.

## Özellikler
- `pandas.describe()` ile ortalama, standart sapma, min–max vb. temel istatistikler.
- Sonuçları otomatik olarak `rapor.csv` (veya kullanıcı belirlediği isim) dosyasına kaydetme.
- Belirlenen sütun için histogram grafiği.
