import asyncio
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import (
    Application,
    CommandHandler,
    CallbackQueryHandler,
    ContextTypes
)

# 🔑 ТОКЕН БОТА (замени на свой!)
BOT_TOKEN = '7758163554:AAHjfK-ocLWV7FMW6vR0P7BKQLA5CXdjcb8'

# Список бустов
BOOSTS_LIST = [
    ("💎 Буст +100 трофеев", "50 руб"),
    ("🔥 Буст +300 трофеев", "250 руб"),
    ("⚡ Буст +500 трофеев", "400 руб"),
    ("🚀 Буст с Нуля до Алмаза", "200 руб"),
    ("🏆 Буст от Алмаза до Эпика", "150 руб"),
    ("👑 Буст с Нуля до Эпика", "700 руб"),
    ("✨ Буст с Эпика до Мифика", "650 руб"),
    ("🎯 Буст 1 бойца до макс. ранга (1000 кубков)", "400 руб"),
    ("🎯 Буст 3 боевцов до макс. ранга (1000 кубков)", "1000 руб"),
    ("🎯 Буст 5 бойцов до макс. ранга (1000 кубков)", "1800 руб"),
    ("🛡️ Буст 10 бойцов до макс. ранга (1000 кубков)", "3700 руб"),
    ("🛐 Ящик от Bazzer Shop (Входит рандомные: бп, гемы, акции)", "3000 руб"),
]

# Приветствие
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("🚀 Бусты", callback_data='boosts')],
        [InlineKeyboardButton("❓ Помощь", callback_data='help')],
        [InlineKeyboardButton("📞 Контакты", callback_data='contacts')],
        [InlineKeyboardButton("⭐ Отзывы", callback_data='reviews')],
        [InlineKeyboardButton("ℹ️ Доп. информация", callback_data='info')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text(
        "Добро пожаловать в Bazzer Shop! 🛒\n"
        "Мы только открылись, поэтому у нас много скидок и промокодов 🎁\n"
        "Лучшие бусты для Brawl Stars по самым выгодным ценам!\n\n"
        "Выберите действие:",
        reply_markup=reply_markup
    )

# Обработчик кнопок
async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    if query.data == 'main_menu':
        keyboard = [
            [InlineKeyboardButton("🚀 Бусты", callback_data='boosts')],
            [InlineKeyboardButton("❓ Помощь", callback_data='help')],
            [InlineKeyboardButton("📞 Контакты", callback_data='contacts')],
            [InlineKeyboardButton("⭐ Отзывы", callback_data='reviews')],
            [InlineKeyboardButton("ℹ️ Доп. информация", callback_data='info')]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_text(
            "Добро пожаловать в Bazzer Shop! 🛒\n"
            "Мы только открылись, поэтому у нас много скидок и промокодов 🎁\n"
            "Лучшие бусты для Brawl Stars по самым выгодным ценам!\n\n"
            "Выберите действие:",
            reply_markup=reply_markup
        )

    elif query.data == 'boosts':
        keyboard = []
        for name, price in BOOSTS_LIST:
            keyboard.append([InlineKeyboardButton(f"{name} — {price}", callback_data='buy_info')])
        keyboard.append([InlineKeyboardButton("⬅️ Назад", callback_data='main_menu')])
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_text("Выберите буст:", reply_markup=reply_markup)

    elif query.data == 'help':
        keyboard = [
            [InlineKeyboardButton("👤 @b1zziks", url="https://t.me/b1zziks")],
            [InlineKeyboardButton("👤 @Veriw_ll", url="https://t.me/Veriw_ll")],
            [InlineKeyboardButton("🛒 Перейти к покупкам", callback_data='boosts')],
            [InlineKeyboardButton("⬅️ Назад", callback_data='main_menu')]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)

        help_text = (
            "❓ Нужна помощь?\n\n"
            "📞 Свяжитесь с нашими операторами:\n"
            "• @b1zziks\n"
            "• @Veriw_ll\n\n"
            "Или сразу перейдите к покупкам:"
        )

        await query.edit_message_text(help_text, reply_markup=reply_markup)

    elif query.data == 'contacts':
        keyboard = [
            [InlineKeyboardButton("👤 @b1zziks", url="https://t.me/b1zziks")],
            [InlineKeyboardButton("👤 @Veriw_ll", url="https://t.me/Veriw_ll")],
            [InlineKeyboardButton("⬅️ Назад", callback_data='main_menu')]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_text(
            "📞 Наши контакты:\n\n"
            "• @b1zziks\n"
            "• @Veriw_ll",
            reply_markup=reply_markup
        )

    elif query.data == 'reviews':
        keyboard = [
            [InlineKeyboardButton("⭐ Перейти к отзывам", url="https://t.me/otzevaba")],
            [InlineKeyboardButton("⬅️ Назад", callback_data='main_menu')]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_text(
            "💬 Все отзывы наших клиентов публикуются в официальном канале:\n\n"
            "👉 @otzevaba\n\n"
            "Подписывайтесь, чтобы убедиться в нашей надёжности!",
            reply_markup=reply_markup
        )

    elif query.data == 'info':
        keyboard = [
            [InlineKeyboardButton("🚀 Перейти к бустам", callback_data='boosts')],
            [InlineKeyboardButton("📞 Связаться с оператором", url="https://t.me/b1zziks")],
            [InlineKeyboardButton("⬅️ Назад", callback_data='main_menu')]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        
        info_text = (
            "ℹ️ Дополнительная информация:\n\n"
            "• Время и цена могут меняться\n"
            "• Стоимость варьируется в зависимости от:\n"
            "\t• Кубков на персонаже\n"
            "\t• Количества бойцов\n"
            "\t• Уровня силы\n\n"
            "💡 Для уточнения точной стоимости и сроков выполнения заказа,\n"
            "свяжитесь с нашими операторами!"
        )
        
        await query.edit_message_text(info_text, reply_markup=reply_markup)

    elif query.data == 'buy_info':
        keyboard = [
            [InlineKeyboardButton("👤 Связаться для покупки", url="https://t.me/b1zziks")],
            [InlineKeyboardButton("⬅️ Назад к бустам", callback_data='boosts')],
            [InlineKeyboardButton("🏠 Главное меню", callback_data='main_menu')]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_text(
            "💬 Чтобы купить буст, напишите оператору:\n\n"
            "👉 @b1zziks или @Veriw_ll\n\n"
            "Укажите:\n"
            "• Название буста\n"
            "• Вашу почту от Brawl Stars\n"
            "• Код, который пришёл на почту\n\n"
            "Оплата: СБП, USDT, карта РФ.",
            reply_markup=reply_markup
        )

# Запуск бота
def main():
    application = Application.builder().token(BOT_TOKEN).build()
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CallbackQueryHandler(button_handler))
    print("✅ Bazzer Shop запущен! Отправьте боту /start в Telegram.")
    application.run_polling()

if __name__ == '__main__':
    main()
