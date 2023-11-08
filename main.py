from telegram.ext import *
from telegram import File, User
import os
from faceswapper import face_swap

first_photo_received = False
TOKEN = "YOUR TELEGRAM TOKEN HERE"


async def start(update, context):
    await update.message.reply_text("Welcome to the bot! Please send the first image")


async def handle_photo(update, conpyttext: CallbackContext):
    global first_photo_received
    user: User = update.message.from_user
    directory = str(user.id)

    if not os.path.exists(directory):
        os.mkdir(directory)

    photo_file: File = await update.message.photo[-1].get_file()

    if first_photo_received == False:
        await photo_file.download_to_drive(f"{directory}/user_photo.jpg")
        await update.message.reply_text("First photo received. Please send a second photo.")
        first_photo_received = True
    else:
        await photo_file.download_to_drive(f"{directory}/user_photo2.jpg")
        await update.message.reply_text("Second photo received. Please wait...")
        face_swap(directory)
        await context.bot.sendPhoto(
            chat_id=update.message['chat']['id'],
            photo=open(f"{directory}/image.jpeg", 'rb'),
            filename=f'{directory}/image.jpeg'
        )
        await update.message.reply_text("Thank you for using the bot! If you would like to continue using a bot, please send a photo")
        first_photo_received = False

if __name__ == "__main__":
    dp = Application.builder().token(TOKEN).build()
    dp.add_handler(CommandHandler("start", start))
    # dp.add_handler(MessageHandler("Load photo", handle_photo))
    dp.add_handler(MessageHandler(filters.PHOTO, handle_photo))
    dp.run_polling(poll_interval=3)
