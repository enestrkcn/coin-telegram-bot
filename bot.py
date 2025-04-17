from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import requests

# Token'ı buraya ekle
TOKEN = "8150124732:AAE8yExD8umWHj4b03aGfs0lBWURZ-1S7_I"

# Coin fiyatını getiren fonksiyon
def get_coin_price(coin_id):
    url = f"https://api.coingecko.com/api/v3/simple/price?ids={coin_id}&vs_currencies=usd"
    response = requests.get(url)
    data = response.json()
    if coin_id in data:
        return data[coin_id]['usd']
    else:
        return "Coin bulunamadı."

# /start komutu işlevi
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Bot çalışıyor! 🎉")

# /price komutu işlevi
async def price(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if context.args:
        coin_id = context.args[0].lower()  # Coin adını al
        price = get_coin_price(coin_id)
        await update.message.reply_text(f"{coin_id.capitalize()} fiyatı: ${price}")
    else:
        await update.message.reply_text("Lütfen bir coin adı girin. Örneğin: /price bitcoin")

# Uygulama ve komutlar
app = ApplicationBuilder().token(TOKEN).build()

# Komutları ekleyelim
app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("price", price))

# Botu başlat
app.run_polling()
