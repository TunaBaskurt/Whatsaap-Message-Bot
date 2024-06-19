import pywhatkit as kit
import time
import re

def send_message(num, message, hour, minute):
    try:
        kit.sendwhatmsg(num, message, hour, minute)
        print(f"Mesaj gönderildi: {num} -> {message}")
    except Exception as e:
        print(f"Mesaj gönderme hatası: {e}")

if __name__ == "__main__":
    # Kullanıcıdan numara ve mesaj bilgilerini alalım
    raw_phone_number = input("Mesaj göndermek istediğiniz telefon numarasını ülke kodu ile birlikte girin (örn: +905321234567): ")
    message = input("Göndermek istediğiniz mesajı girin: ")

    # Numara temizleme
    cleaned_phone_number = raw_phone_number.replace(" ", "")  # Boşlukları kaldır

    # Alternatif: Daha fazla temizlik yapabiliriz
    cleaned_phone_number = re.sub(r'\D', '', cleaned_phone_number)  # Tüm sayısal olmayan karakterleri kaldır

    # Numaranın başına tekrar '+' işaretini ekleyin (ülke kodu için gerekli olabilir)
    if not cleaned_phone_number.startswith('+'):
        cleaned_phone_number = '+' + cleaned_phone_number

    # Mevcut saat ve dakikayı alalım
    current_time = time.localtime()
    hour = current_time.tm_hour
    minute = current_time.tm_min + 2  # Şu andan 2 dakika sonrası

    # Eğer dakika 60'ı geçerse, saati ve dakikayı güncelle
    if minute >= 60:
        minute -= 60
        hour += 1

    # Mesaj gönderme işlemi
    send_message(cleaned_phone_number, message, hour, minute)
