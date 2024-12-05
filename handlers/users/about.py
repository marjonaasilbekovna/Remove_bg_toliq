from aiogram.types import Message
from loader import dp
from aiogram.filters import Command

#about commands
@dp.message(Command("about"))
async def about_commands(message:Message):
    await message.answer("Bu bot orqali siz:\n - rasmlarning orqa fonini o'chirish\n - orqa fonni o'zgartirish\n - orqa fonga rasm qo'yish\n\n\nkabi amallarni bajarishingiz mumkin .Bizning botimizda afzalliklar va qulayliklar ko'p. Bizni tanlaganingizdan xursandmiz.")

