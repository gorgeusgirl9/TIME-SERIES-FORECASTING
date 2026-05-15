isse senedi gibi volatilite (oynaklık) oranı yüksek verilerde, anlık dalgalanmaların ötesindeki ana yönü (Trend) matematiksel olarak modellemek ve gelecekteki olası fiyat çizgisini tahmin etmektir.

📊 Teknik Metrikler
Model: Linear Regression (Trend Analysis)

Metrik: MAE (Mean Absolute Error). Tahminlerin gerçek kapanış fiyatlarından ortalama kaç dolar saptığını ölçmek için kullanılmıştır.

🔑 En İyi Çözümün Anahtarı
Date-to-Ordinal Transformation: Makine öğrenmesi modelleri datetime nesnelerini doğrudan anlayamaz. Bu yüzden tarihler, regresyon modeline uygun sayısal (ordinal) formata dönüştürülmüştür.

Kronolojik Bölme (Shuffle=False): Zaman serilerinde verinin sırası bozulmamalıdır. Modelin "gelecekten bilgi sızdırmasını" (Data Leakage) önlemek için veriler rastgele karıştırılmadan, takvim sırasına göre eğitim ve test setlerine ayrılmıştır.

💡 Kazanımlar ve Notlar
Trend Analizi: Hisse senetlerinde kısa vadeli tahminlerin gürültüye çok açık olduğu, ancak uzun vadeli trendlerin doğrusal modellerle dahi yüksek doğrulukla takip edilebildiği gözlemlenmiştir.

Dinamik Dosya Yönetimi: Geliştirme sürecinde karşılaşılan klasör yolu hataları, os kütüphanesi ve raw string (r'') kullanılarak profesyonelce çözülmüştür.

Görselleştirme: Tahmin edilen kırmızı trend hattı ile gerçek veri noktalarının karşılaştırılması, modelin genel piyasa yönünü başarıyla yakaladığını kanıtlamıştır.
