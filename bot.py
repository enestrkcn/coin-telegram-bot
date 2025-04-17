from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import requests

# Token'ı buraya ekle
TOKEN = "7887984646 : AAFuu5cE2YDXk8YHjwiUxM1-DeiDnd8FD6w"

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
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import requests

# Pi Coin fiyatını OKX'ten çekiyoruz
def get_pi_price():
    url = "https://www.okx.com/api/v5/market/ticker?instId=PI-USDT"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        price = data['data'][0]['last']
        return f"Pi Coin fiyatı: ${price}"
    else:
        return "Pi Coin fiyatı alınamadı."

# /start komutu
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Merhaba! Komutlara hazırım. /pi yazarak Pi Coin fiyatını alabilirsin.")

# /pi komutu
async def pi_price(update: Update, context: ContextTypes.DEFAULT_TYPE):
    price = get_pi_price()
    await update.message.reply_text(price)

# Botu çalıştır
app = ApplicationBuilder().token("BOT_TOKEN").build()
app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("pi", pi_price))
app.run_polling()
import requests

def get_okx_pi_klines():
    url = "https://www.okx.com/api/v5/market/candles"
    params = {
        "instId": "PI-USDT",
        "bar": "1m",  # 1 dakikalık veri
        "limit": 10   # Son 10 mum verisi
    }
    response = requests.get(url, params=params)
    if response.status_code == 200:
        data = response.json()["data"]
        for candle in data:
            print(f"Zaman: {candle[0]}, Açılış: {candle[1]}, Kapanış: {candle[4]}")
    else:
        print("Veri alınamadı:", response.text)

get_okx_pi_klines()