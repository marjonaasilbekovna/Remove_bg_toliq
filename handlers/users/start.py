from aiogram.types import Message
from loader import dp,db
from aiogram.filters import CommandStart
from keyboardbutton import menu


@dp.message(CommandStart())
async def start_command(message:Message):
    full_name = message.from_user.full_name
    telegram_id = message.from_user.id
    try:
        db.add_user(full_name=full_name,telegram_id=telegram_id) #foydalanuvchi bazaga qo'shildi
        await message.answer(text=f"Assalomu alaykum   {full_name}   hurmatli foydalanuvchi 'Background remove' botiga hush kelibsiz.\nBu bot sizga...\n\n- rasmlarning orqa fonini o'chirishga\n- orqa fonga rasm qo'yishga\n- orqa fonga rang qo'yishga imkon beradi\n\nSiz bajarmoqchi bo'lgan amalingizni tugmalardan tanlang.\nBu bot 'Sifatedu' o'quv markazi tomonidan yaratilgan.", reply_markup=menu)
    except:
        await message.answer(text=f"Assalomu alaykum   {full_name}   hurmatli foydalanuvchi 'Background remove' botiga hush kelibsiz.\nBu bot sizga...\n\n- rasmlarning orqa fonini o'chirishga\n- orqa fonga rasm qo'yishga\n- orqa fonga rang qo'yishga imkon beradi\n\nSiz bajarmoqchi bo'lgan amalingizni tugmalardan tanlang.\nBu bot 'Sifatedu' o'quv markazi tomonidan yaratilgan.", reply_markup=menu)

