# 🎵 AI Music & Multimodal Telegram Bot

Ushbu bot Telegram orqali YouTube-dan qo'shiqlar qidirish, yuklab olish va Google Gemini AI yordamida rasm va audiolarni tahlil qilish imkonini beradi.

## ✨ Imkoniyatlar
* 🔍 **Musiqa qidirish:** YouTube-dan nomi yoki ijrochisi bo'yicha qidirish.
* 🎧 **Audio yuklash:** YouTube-dan eng yuqori sifatli audio (MP3) formatda yuklash.
* 🤖 **AI Tahlil (Gemini 2.0 Flash):** * Rasmlarni ko'rish va ta'riflash.
    * Ovozli xabarlarni (voice) eshitish va matnga o'girish.
* 📊 **Janrlar bo'yicha TOP 10:** Turli tillardagi eng hit qo'shiqlarni bir tugma orqali yuklash.

## 🛠 Texnologiyalar
* **Python 3.12**
* **Aiogram 3.x** (Telegram Bot Framework)
* **Google GenAI** (Gemini API)
* **yt-dlp** (YouTube-dan yuklash uchun)
* **FFmpeg** (Audioni qayta ishlash uchun)

## 🚀 O'rnatish va ishga tushirish

1.  **Repository-ni nusxalash:**
    ```bash
    git clone [https://github.com/FOYDALANUVCHI_NOMINGIZ/REPO_NOMINGIZ.git](https://github.com/FOYDALANUVCHI_NOMINGIZ/REPO_NOMINGIZ.git)
    cd REPO_NOMINGIZ
    ```

2.  **Kutubxonalarni o'rnatish:**
    ```bash
    pip install -r requirements.txt
    ```

3.  **FFmpeg o'rnatilganligini tekshiring:**
    
    Tizimingizda FFmpeg o'rnatilgan va PATH-ga qo'shilgan bo'lishi shart.

4.  **Tokenlarni sozlash:**
    `main.py` fayliga o'zingizning Telegram Bot Token va Gemini API kalitingizni kiriting.

5.  **Ishga tushirish:**
    ```bash
    python main.py
    ```

## 📝 Muhim eslatma
Ushbu bot bepul serverlarda (Render, Railway) ishlashi uchun `Build Script` orqali FFmpeg o'rnatilishi talab qilinadi. Barcha yuklangan fayllar foydalanuvchiga yuborilgach, server xotirasini to'ldirmaslik uchun avtomatik o'chiriladi.
