from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
import asyncio

# ВСТАВЬ СВОЙ TOKEN
TOKEN = "8530047129:AAGKilPDhiyy0Id1LhAY3f4CABiFi1TQ8Fs"

bot = Bot(token=TOKEN)
dp = Dispatcher()

# КНОПКИ
keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="📅 Расписание")],
        [KeyboardButton(text="📄 Справки и документы")],
        [KeyboardButton(text="🩺 Санитарная книжка")],
        [KeyboardButton(text="📞 Контакты")],
        [KeyboardButton(text="📱 Instagram колледжа")],
    ],
    resize_keyboard=True
)

# СТАРТ
@dp.message(Command("start"))
async def start(message: types.Message):
    await message.answer(
        "👋 Добро пожаловать в Telegram-бот помощник куратора\n"
        "Темиртауского высшего медицинского колледжа 🏥\n\n"
        "Выберите нужный раздел 👇",
        reply_markup=keyboard
    )

# ОТВЕТЫ
@dp.message()
async def answers(message: types.Message):

    text = message.text

    # РАСПИСАНИЕ
    if text == "📅 Расписание":
        await message.answer(
            "📅 Расписание занятий:\n\n"
            "https://temirmedcollege.kz/ru/расписание2/"
        )

    # СПРАВКИ
    elif text == "📄 Справки и документы":
        await message.answer(
            "📄 Медицинские справки и больничные необходимо "
            "направлять в учебную часть секретарю.\n\n"
            "⚠️ Обязательно подпишите группу на справке."
        )

    # САНИТАРНАЯ КНИЖКА
    elif text == "🩺 Санитарная книжка":
        await message.answer(
            "🩺 Оформление санитарной книжки проходит в несколько этапов:\n\n"

            "1️⃣ ФШК (флюорография)\n"
            "Необходимо проверить:\n"
            "• есть ли действующий снимок\n"
            "• стоит ли печать ФШК\n"
            "• не истёк ли срок действия\n\n"

            "При необходимости обследование проходят "
            "в поликлинике по месту прикрепления.\n\n"

            "2️⃣ СПИД-центр\n"
            "📍 ул. Байсеитовой 21\n\n"
            "Сдаются анализы на:\n"
            "• ВИЧ\n"
            "• гепатиты\n\n"
            "💰 Стоимость около 6000 тг.\n\n"

            "3️⃣ Кожно-венерологический диспансер\n"
            "📍 ул. Чайковского 22\n"
            "(вход с торца Многопрофильной больницы, 2 этаж)\n\n"

            "При себе иметь:\n"
            "• удостоверение личности\n"
            "• кал для анализа\n"
            "• санитарную книжку\n\n"

            "В диспансере:\n"
            "• сдают бактериологический анализ\n"
            "• проходят терапевта\n"
            "• получают допуск на 6 месяцев\n\n"

            "💰 Стоимость обследования около 7000 тг.\n\n"

            "⚠️ После завершения всех этапов необходимо "
            "забрать санитарную книжку и предоставить её "
            "в двадцатых числах мая.\n\n"

            "Дополнительную информацию можно получить "
            "у заведующей практикой."
        )

    # КОНТАКТЫ
    elif text == "📞 Контакты":
        await message.answer(
            "📞 Контакты колледжа:\n\n"

            "📚 Учебная часть – 95-67-02\n"
            "🏥 ОПК – 95-64-69\n"
            "💰 Бухгалтерия – 96-66-65\n"
            "👥 Отдел кадров – 44-77-03\n"
            "📌 Приёмная директора – 95-64-88"
        )

    # INSTAGRAM
    elif text == "📱 Instagram колледжа":
        await message.answer(
            "📱 Instagram колледжа:\n"
            "https://www.instagram.com/temirmedcollege"
        )

    else:
        await message.answer(
            "Пожалуйста, выберите кнопку ниже 👇"
        )

# ЗАПУСК БОТА
async def main():
    print("Бот запущен ✅")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())