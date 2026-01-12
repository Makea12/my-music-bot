import os
import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, FSInputFile
from aiogram.filters import Command
import yt_dlp

API_TOKEN = "1234567890"
bot = Bot(token=API_TOKEN)
dp = Dispatcher()

FFMPEG_PATH = r'C:\ffmpeg\ffmpeg-8.0.1-full_build\bin'


# --- MENYULAR ---
def main_menu():
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="🎤 Qosiqti Izlew", callback_data="search_mp3")],
        [InlineKeyboardButton(text="🌏 Tiller boyinsha (10 Xit)", callback_data="select_genre")]
    ])


def genre_menu():
    return InlineKeyboardMarkup(inline_keyboard=[
        [
            InlineKeyboardButton(text="🇺🇿 O'zbekshe", callback_data="genre:o'zbekcha yangi xit qo'shiqlar"),
            InlineKeyboardButton(text="🇷🇺 Orissha", callback_data="genre:русские хиты 2026")
        ],
        [
            InlineKeyboardButton(text="🇰🇿 Qazaqsha", callback_data="genre:казакша хит андер"),
            InlineKeyboardButton(text="🏜 Qaraqalpaqsha", callback_data="genre:qoraqalpoq xit qo'shiqlar")
        ],
        [InlineKeyboardButton(text="🔥 Club/Bass", callback_data="genre:club bass music 2026")],
        [InlineKeyboardButton(text="⬅️ arqag'a", callback_data="back_to_main")]
    ])


# --- ASOSIY ISHLASH QISMI ---

@dp.message(Command("start"))
async def start(message: types.Message):
    await message.answer("Sa'lem! 👋\nKerekli bo'limdi saylan':", reply_markup=main_menu())


@dp.callback_query()
async def callbacks(call: types.CallbackQuery):
    if call.data == "search_mp3":
        await call.message.answer("🎵 Qosiq ati yaki Orinlawshini jazin' (Men sizge en' masin tabaman):")

    elif call.data == "select_genre":
        await call.message.edit_text("Qaysi tildegi 10 dana en' xit qosiqti Qa'leysiz? 👇", reply_markup=genre_menu())

    elif call.data == "back_to_main":
        await call.message.edit_text("Bas Menyu:", reply_markup=main_menu())

    elif call.data.startswith("genre:"):
        genre_query = call.data.split(":")[1]
        await call.message.answer(f"🚀 {genre_query} boyinsha 10 dana qosiq tayarlanbaqta...")
        # Janr uchun 10 ta yuklash
        await music_downloader(call.message, genre_query, count=10)

    await call.answer()


# Matn ko'rinishida qidirish (Faqat 1 ta qo'shiq)
@dp.message()
async def text_search(message: types.Message):
    if message.text:
        await message.answer(f"🎶 '{message.text}' Qosig'i Izlenbekte ...")
        await music_downloader(message, message.text, count=1)


# --- YUKLOVCHI FUNKSIYA ---
async def music_downloader(message: types.Message, query: str, count: int):
    ydl_opts = {
        'format': 'bestaudio/best',
        'cookiefile': 'cookies.txt',  # FAQAT SHU QATOR QOLSIN
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        'outtmpl': 'downloads/%(title)s.%(ext)s',
    'noplaylist': True,
    'default_search': 'ytsearch1',

    }
        # 'cookiesfrombrowser': ('chrome',),  <-- Buni o'chirib turing, yuqoridagi ishonchliroq


    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            # count o'zgaruvchisi orqali nechtaligi aniqlanadi
            info = ydl.extract_info(f"ytsearch{count}:{query}", download=True)

            # Agar faqat 1 ta bo'lsa, uni list ichiga olamiz
            entries = info['entries'] if 'entries' in info else [info]

            for entry in entries:
                filename = ydl.prepare_filename(entry)
                base, _ = os.path.splitext(filename)
                mp3_file = base + ".mp3"

                if os.path.exists(mp3_file):
                    audio = FSInputFile(mp3_file)
                    await message.answer_audio(audio, caption=f"🎵 {entry['title']}\n@sizdin'_botin'iz")
                    os.remove(mp3_file)

        await message.answer(f"✅ Juklew Tamamlandi: {count} ta fayl.")

    except Exception as e:
        await message.answer(f"😢 Qatelik: {e}")


if __name__ == "__main__":

    asyncio.run(dp.start_polling(bot))
