# 🖥️ Sistem Kontrol Aracı

Yerel ağ (UNC) klasörlerine ve çeşitli internet sitelerine erişimi anlık olarak izleyen bir masaüstü uygulaması.

## 🚀 Özellikler

- ✅ İnternet bağlantısı kontrolü (`google.com`)
- ✅ Kurumsal sitelere erişim durumu kontrolü:
  - [bolge01.dsi.gov.tr](https://bolge01.dsi.gov.tr/)
  - [belgenet.dsi.gov.tr](https://belgenet.dsi.gov.tr/edys-web/sistemeGiris.xhtml)
- ✅ Yerel ağdaki UNC klasörüne bağlantı kontrolü (`\\b101ftp\paylasim`)
- ✅ Erişim sorunlarını **yetki**, **bağlantı**, **yol** gibi sebeplere göre ayırt edebilme
- ✅ Şık ve kullanıcı dostu PyQt5 arayüzü
- ✅ Zaman damgalı erişim güncellemeleri

## 🧠 Nasıl Çalışır?

- Uygulama başlatıldığında bir `Worker` thread'i aktif olur.
- Bu thread, belirlenen sitelere ve UNC klasörüne belirli aralıklarla erişmeyi dener.
- Başarı durumu GUI'de kullanıcıya renkli kartlar ve saat bilgisiyle gösterilir.
- UNC klasörüne erişilemiyorsa hata tipi loglanır:
  - ❌ Ağ bağlantısı sorunu
  - 🔐 Yetki reddi
  - 📁 Paylaşım bulunamadı

## 📂 Proje Yapısı

```
├── main.py               # Ana uygulama ve arayüz yönetimi
├── Worker.py             # Erişim kontrollerini yapan thread
├── test1.ui/.py          # PyQt5 arayüz dosyası
├── images_rc.py          # Kaynak görseller (ikon vb.)
├── test.ico              # Uygulama simgesi
└── README.md             # Proje açıklaması
```

## 🛠️ Gereksinimler

- Python 3.7+
- PyQt5
- requests

Kurmak için:

```bash
pip install -r requirements.txt
```

`requirements.txt` içeriği:
```
PyQt5
requests
```

## ▶️ Uygulamayı Çalıştırma

```bash
python main.py
```

## 🧪 Test Edilen UNC Yapısı

```
\\b101ftp\paylasim
```

Bu UNC yolundaki klasöre erişim olup olmadığı kontrol edilir. Erişim yoksa, aşağıdaki hata kodlarına göre neden belirlenmeye çalışılır:

| Hata Kodu | Açıklama                          |
|-----------|-----------------------------------|
| 5         | Erişim reddedildi (yetki yok)     |
| 53        | Sunucuya erişilemiyor (network)   |
| 67        | Paylaşım adı hatalı veya yok      |

## 📌 Notlar

- `file_check()` fonksiyonu sadece Windows üzerinde çalışır (çünkü `ctypes.windll` kullanır).
- `os.path.exists()` çağrısı UNC klasörünü test eder.
- Uygulama sürekli çalışacak şekilde yapılandırılmıştır, `thread` içinde sonsuz döngü mevcuttur.

## 📷 Arayüzden Görüntü

> (Ekran görüntüsü buraya eklenebilir)
