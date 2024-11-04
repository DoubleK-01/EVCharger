
# EV Charger API

Bu proje, Elektrikli Araç Şarj Cihazı (EVC) için basit bir API sunmaktadır. 
Flask framework'ü kullanılarak geliştirilmiştir ve SQLite veritabanı ile kullanıcı doğrulama işlemleri gerçekleştirmektedir. 
İlgili proje eğitim ve geliştirme amaçlı güvenlik zafiyeti içermektedir.

## Özellikler

- **Kullanıcı Doğrulama**: API anahtarı ile kullanıcı girişi.
- **Şarj Durumu İzleme**: Şarj cihazının bağlanma durumu ve şarj süreci bilgileri.
- **Şarj Başlatma ve Durdurma**: API son noktaları aracılığıyla şarj işlemini yönetme.

## Gereksinimler

- Python 3.x
- Flask
- SQLite

## Kurulum

### Gerekli Dosyaların Kurulumu

1. **Python ve pip'i kontrol edin**:
   Python ve pip'in sisteminizde kurulu olduğunu kontrol edin. Terminal veya komut istemcisine aşağıdaki komutları yazın:
   ```bash
   python --version
   pip --version
   ```

2. **Depoyu klonlayın**:
   GitHub deposunu bilgisayarınıza klonlayın:
   ```bash
   git clone https://github.com/DoubleK-01/EVCharger.git
   cd ev-charger-api
   ```

3. **Gerekli paketleri yükleyin**:
   Flask ve diğer gerekli kütüphaneleri yüklemek için aşağıdaki komutu çalıştırın:
   ```bash
   pip install Flask
   ```

4. **Veritabanı tablosunu oluşturun**:
   Uygulama başlatıldığında, gerekli kullanıcı tablosu otomatik olarak oluşturulacaktır.

## Kullanım

1. **Uygulamayı başlatın**:
   Terminalde, proje dizininde aşağıdaki komutu çalıştırarak uygulamayı başlatın:
   ```bash
   python3 http_server.py
   ```

2. **Tarayıcıda açın**:
   Tarayıcınızı açın ve `http://127.0.0.1:5000` adresine gidin.

3. **Giriş yapın**:
   - Giriş sayfasında API anahtarını girin ("admin") ve "Giriş Yap" butonuna tıklayın.

4. **Şarj Durumunu Kontrol Edin**:
   - Şarj durumu bilgilerini almak için `GET /status` isteği gönderin.

5. **Şarj İşlemini Başlatın**:
   - Şarj işlemini başlatmak için `POST /start_charging` isteği gönderin. Bu isteği yapmak için `X-API-KEY` başlığında "admin" değeri kullanmalısınız.
   
   Örnek cURL isteği:
   ```bash
   curl -X POST http://localhost:5000/start_charging -H "X-API-KEY: admin"
   ```

6. **Şarj İşlemini Durdurun**:
   - Şarj işlemini durdurmak için `POST /stop_charging` isteği gönderin. Yine, `X-API-KEY` başlığında "admin" değeri kullanmalısınız.

   Örnek cURL isteği:
   ```bash
   curl -X POST http://localhost:5000/stop_charging -H "X-API-KEY: admin"
   ```

## Güvenlik Notları

- **SQL Enjeksiyonu**: SQL sorgularında SQL enjeksiyon saldırılarına karşı korunmak için parametrik sorgular kullanılmalıdır. Ancak ilgili projede bu kısımlar biliçli olarak açık bırakılmıştır.
- **API Anahtarları**: API anahtarlarının güvenli bir şekilde saklanması ve yetkisiz erişimden korunması gerekmektedir. Ancak ilgili projede bu kısımlar biliçli olarak açık bırakılmıştır.

## Katkıda Bulunma

Herhangi bir katkıda bulunmak isterseniz, lütfen yeni bir dal (branch) oluşturun ve değişikliklerinizi gönderin (pull request).

## Lisans

Bu proje [MIT Lisansı](LICENSE) altında lisanslanmıştır. Lisans, bu yazılımın kopyalanmasını, dağıtılmasını ve değiştirilmesini sağlar, ancak proje ile birlikte sağlanan lisans şartlarına uymanız gerekmektedir.

## Sorumluluk Reddi

Bu proje, eğitim ve geliştirme amaçlı olarak sağlanmıştır. Kullanıcıların bu projeyi kullanırken kendi sorumluluklarını kabul etmeleri gerekmektedir. Bu proje, herhangi bir garanti verilmeden "olduğu gibi" sağlanmaktadır. Projenin kullanımı sonucunda meydana gelen herhangi bir zarar veya kayıptan yazar sorumlu değildir.

## Gizlilik Politikası

Bu proje, kullanıcıların verilerini toplamakta veya işlemekte değildir. Ancak, kullanıcıların API anahtarları gibi kişisel bilgileri güvende tutmaları ve paylaşmamaları gerekmektedir. Kullanıcı verileri, bu projede saklanmamaktadır.

## Katkıda Bulunma

Bu projeye katkıda bulunmak isteyenler, lütfen yeni bir dal (branch) oluşturun ve değişikliklerinizi gönderin (pull request). Tüm katkılar, projenin yazarları tarafından gözden geçirilecek ve uygun görüldüğünde projeye dahil edilecektir.
