import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, MessageHandler, CommandHandler, filters

# إعداد السجلات الأساسية
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

# بيانات التشغيل المدمجة بأمان لتعمل فوراً على بوتك
TELEGRAM_BOT_TOKEN = "9020513918:AAGEPKIxO2TA5c5tvpj2Fv4GWUOUzlH8dbQ"
ADMIN_CHAT_ID = 8547046828

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """رسالة الترحيب التلقائية لجذب المشتركين وتفعيل البوت"""
    user = update.effective_user
    welcome_message = (
        f"مرحباً بك يا {user.first_name} في بوت الخدمات والتحميل الذكي! 🤖🔥\n\n"
        "قم بإرسال أي رابط فيديو أو طلب وسأقوم بمساعدتك فوراً.\n"
        "شارك البوت مع أصدقائك لتعم الفائدة ويقتمع المشتركون!"
    )
    await update.message.reply_text(welcome_message)

async def handle_user_messages(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """معالجة رسائل المشتركين والروابط المرسلة"""
    text = update.message.text.strip()
    
    if "http" in text:
        await update.message.reply_text(
            "📥 تم استلام الرابط بنجاح!\n"
            "🔄 جاري معالجة الطلب وإعداده..."
        )
    else:
        await update.message.reply_text("أهلاً بك! يرجى إرسال رابط صالح لنتمكن من خدمتك وتوفير طلبك.")

def main():
    # تشغيل البوت وربطه بتوكنك الخاص
    app = ApplicationBuilder().token(TELEGRAM_BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & (~filters.COMMAND), handle_user_messages))

    print("[+] البوت يعمل الآن بنجاح ومستعد لاستقبال المشتركين...")
    app.run_polling()

if __name__ == "__main__":
    main()
