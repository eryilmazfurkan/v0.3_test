# Raspberry Pi Projesi İçin Kurulum Talimatları

Bu proje, bir Raspberry Pi üzerinde çalışacak şekilde tasarlanmıştır. Aşağıdaki adımları takip ederek projeyi kurabilir ve çalıştırabilirsiniz.

## 1. Sanal Ortam Oluşturma

İlk olarak, bir sanal ortam (virtual environment) oluşturmanız gerekmektedir. Terminalde aşağıdaki komutları sırasıyla çalıştırın:

```bash
python -m venv venv
source venv/bin/activate
``` 

## 2. GitHub'dan Kodları İndirme

GitHub'daki kodları bilgisayarınıza çekmek için terminalde aşağıdaki komutu çalıştırın:

```bash
git clone git@github.com:eryilmazfurkan/v0.3_test.git
```

## 3. Config Dosyasını Güncelleme

Projeyi indirdikten sonra, config dosyasını güncellemek için terminalde aşağıdaki komutu çalıştırın:

```bash
python add_config.py
```

## 4. Gerekli Kütüphaneleri Yükleme

Gerekli kütüphane ve paketleri yüklemek için terminalde aşağıdaki komutu çalıştırın:

```bash
python install_lib.py
```

## 5. TBM Testi

TBM testini gerçekleştirmek için terminalde aşağıdaki adımları takip edin:

```bash
cd /ws/tbm/eltt2
sudo ./eltt2 -g
```

Bu adımları tamamladıktan sonra projeniz çalışmaya hazır olacaktır. Herhangi bir sorunla karşılaşırsanız lütfen belgelere veya proje sahibine başvurun.