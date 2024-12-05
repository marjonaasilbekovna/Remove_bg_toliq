from aiogram import Bot, Dispatcher,types
from aiogram.fsm.context import FSMContext
from aiogram import F
from aiogram.types import Message, CallbackQuery
from removebg import bg_add_pic, remove_bg, remove_bg_color
from keyboardbutton import menu
from state import BagPic, RemoveBg, BagColor
from inlinebutton import colors_button
from loader import dp, db, ADMINS, TOKEN, bot


@dp.message(F.text == "Fonga rasm qo'yish")
async def bag_pic(message:Message, state:FSMContext):
    await message.answer("Orqa fon qo'yish uchun rasm kiriting")
    await state.set_state(BagPic.background_pic)


@dp.message(F.photo, BagPic.background_pic)
async def bag_picture(message:Message, state:FSMContext):
    file_id = message.photo[-1].file_id

    file = await bot.get_file(file_id)
    file_path = file.file_path
    photos_url = f"https://api.telegram.org/file/bot{TOKEN}/{file_path}"
    await state.update_data(bg_url = photos_url)
    await state.set_state(BagPic.photo)
    await message.answer("Endi esa asosiy rasmni kiritng ;")

# Orqa fon rasmini tekshirish uchun kod
@dp.message(BagPic.background_pic)
async def remove_fon_rasm_del(message: Message, state: FSMContext):
    await message.delete()
    await message.answer(text="Iltimos fon rasmini kiriting ❗️")


@dp.message(F.photo, BagPic.photo)
async def picture(message:Message, state:FSMContext):
    data = await state.get_data()
 
    bg_url = data.get("bg_url")

    file_id = message.photo[-1].file_id
    
    file = await bot.get_file(file_id)
    file_path = file.file_path
    photos_url = f"https://api.telegram.org/file/bot{TOKEN}/{file_path}"

    rasm = bg_add_pic(bg_url, photos_url)
    if rasm:
        await message.answer_photo(photo=types.input_file.BufferedInputFile(rasm,filename="no-bg.png"))
        await message.answer_document(document=types.input_file.BufferedInputFile(rasm,filename="no-bg.png"))
        


# Asosiy rasmni tekshirish uchun kod
@dp.message(BagPic.photo)
async def remove_rasm_del(message: Message, state: FSMContext):
    await message.delete()
    await message.answer(text="Iltimos rasmni kiriting ❗️")

    await state.clear()

#-------------------
# finish Add bg fon 


# start remove bg  
#-------------------
@dp.message(F.text == "Fonni olib tashlash")
async def bag_pic(message:Message, state:FSMContext):
    await message.answer("Orq fonni olib tashlash uchun rasm kiriting")
    await state.set_state(RemoveBg.removebg)

@dp.message(F.photo, RemoveBg.removebg)
async def picture(message:Message, state:FSMContext):
    file_id = message.photo[-1].file_id
    
    file = await bot.get_file(file_id)
    file_path = file.file_path
    photos_url = f"https://api.telegram.org/file/bot{TOKEN}/{file_path}"
    rasm = remove_bg(photos_url)
    if rasm:
        await message.answer_photo(photo=types.input_file.BufferedInputFile(rasm,filename="no-bg.png"))
        await message.answer_document(document=types.input_file.BufferedInputFile(rasm,filename="no-bg.png"))
    

@dp.message(RemoveBg.removebg)
async def remove_photo_del(message: Message, state: FSMContext):
    await message.delete()
    await message.answer(text="Iltimos rasmni kiriting ❗️")

    await state.clear()
#-------------------
# finish remove bg 

# start add color bg
#-------------------

@dp.message(F.text == "Fonga rang berish")
async def bag_pic(message:Message, state:FSMContext):
    await message.answer("Orqa fonga rang kiritish uchun rasmni kiriting ;  ")
    await state.set_state(BagColor.bagcolor)

@dp.message(F.photo, BagColor.bagcolor)
async def photo(message:Message, state:FSMContext):
    file_id = message.photo[-1].file_id
    file = await bot.get_file(file_id)
    file_path = file.file_path
    photos_url = f"https://api.telegram.org/file/bot{TOKEN}/{file_path}"
    rasm = remove_bg_color(photos_url)
    text = "Rasmni orqa fonini qaysi ranga o'zgartirmoqchisiz tanlang !"
    if rasm:
        await message.answer_photo(photo=types.input_file.BufferedInputFile(rasm,filename="no-bg.png"),reply_markup=colors_button, caption=text)


# white
@dp.callback_query(F.data=="white")
async def white_handler(callback:CallbackQuery):
    file_id = callback.message.photo[-1].file_id
    file = await bot.get_file(file_id)
    file_path = file.file_path
    photos_url = f"https://api.telegram.org/file/bot{TOKEN}/{file_path}"
    rasm = remove_bg_color(photos_url, "white")
    text = "Rasmni orqa fonini qaysi ranga o'zgartirmoqchisiz tanlang !"
    await callback.message.answer_photo(photo=types.input_file.BufferedInputFile(rasm,filename="no-bg.png"),reply_markup=colors_button, caption=text)
    await callback.message.delete()

# black
@dp.callback_query(F.data=="black")
async def black_handler(callback:CallbackQuery):
    file_id = callback.message.photo[-1].file_id
    file = await bot.get_file(file_id)
    file_path = file.file_path
    photos_url = f"https://api.telegram.org/file/bot{TOKEN}/{file_path}"
    rasm = remove_bg_color(photos_url, "black")
    text = "Rasmni orqa fonini qaysi ranga o'zgartirmoqchisiz tanlang !"
    await callback.message.answer_photo(photo=types.input_file.BufferedInputFile(rasm,filename="no-bg.png"),reply_markup=colors_button, caption=text)
    await callback.message.delete()

# yellow
@dp.callback_query(F.data=="yellow")
async def yellow_handler(callback:CallbackQuery):
    file_id = callback.message.photo[-1].file_id
    file = await bot.get_file(file_id)
    file_path = file.file_path
    photos_url = f"https://api.telegram.org/file/bot{TOKEN}/{file_path}"
    rasm = remove_bg_color(photos_url, "yellow")
    text = "Rasmni orqa fonini qaysi ranga o'zgartirmoqchisiz tanlang !"
    await callback.message.answer_photo(photo=types.input_file.BufferedInputFile(rasm,filename="no-bg.png"),reply_markup=colors_button, caption=text)
    await callback.message.delete()

# orange
@dp.callback_query(F.data=="orange")
async def orange_handler(callback:CallbackQuery):
    file_id = callback.message.photo[-1].file_id
    file = await bot.get_file(file_id)
    file_path = file.file_path
    photos_url = f"https://api.telegram.org/file/bot{TOKEN}/{file_path}"
    rasm = remove_bg_color(photos_url, "orange")
    text = "Rasmni orqa fonini qaysi ranga o'zgartirmoqchisiz tanlang !"
    await callback.message.answer_photo(photo=types.input_file.BufferedInputFile(rasm,filename="no-bg.png"),reply_markup=colors_button, caption=text)
    await callback.message.delete()

# blue
@dp.callback_query(F.data=="blue")
async def blue_handler(callback:CallbackQuery):
    file_id = callback.message.photo[-1].file_id
    file = await bot.get_file(file_id)
    file_path = file.file_path
    photos_url = f"https://api.telegram.org/file/bot{TOKEN}/{file_path}"
    rasm = remove_bg_color(photos_url, "blue")
    text = "Rasmni orqa fonini qaysi ranga o'zgartirmoqchisiz tanlang !"
    await callback.message.answer_photo(photo=types.input_file.BufferedInputFile(rasm,filename="no-bg.png"),reply_markup=colors_button, caption=text)
    await callback.message.delete()


# pink
@dp.callback_query(F.data=="pink")
async def pink_handler(callback:CallbackQuery):
    file_id = callback.message.photo[-1].file_id
    file = await bot.get_file(file_id)
    file_path = file.file_path
    photos_url = f"https://api.telegram.org/file/bot{TOKEN}/{file_path}"
    rasm = remove_bg_color(photos_url, "pink")
    text = "Rasmni orqa fonini qaysi ranga o'zgartirmoqchisiz tanlang !"
    await callback.message.answer_photo(photo=types.input_file.BufferedInputFile(rasm,filename="no-bg.png"),reply_markup=colors_button, caption=text)
    await callback.message.delete()

# red
@dp.callback_query(F.data=="red")
async def red_handler(callback:CallbackQuery):
    file_id = callback.message.photo[-1].file_id
    file = await bot.get_file(file_id)
    file_path = file.file_path
    photos_url = f"https://api.telegram.org/file/bot{TOKEN}/{file_path}"
    rasm = remove_bg_color(photos_url, "red")
    text = "Rasmni orqa fonini qaysi ranga o'zgartirmoqchisiz tanlang !"
    await callback.message.answer_photo(photo=types.input_file.BufferedInputFile(rasm,filename="no-bg.png"),reply_markup=colors_button, caption=text)
    await callback.message.delete()

# green
@dp.callback_query(F.data=="green")
async def green_handler(callback:CallbackQuery):
    file_id = callback.message.photo[-1].file_id
    file = await bot.get_file(file_id)
    file_path = file.file_path
    photos_url = f"https://api.telegram.org/file/bot{TOKEN}/{file_path}"
    rasm = remove_bg_color(photos_url, "green")
    text = "Rasmni orqa fonini qaysi ranga o'zgartirmoqchisiz tanlang !"
    await callback.message.answer_photo(photo=types.input_file.BufferedInputFile(rasm,filename="no-bg.png"),reply_markup=colors_button, caption=text)
    await callback.message.delete()

@dp.message(BagColor.bagcolor)
async def remove_photo_del(message: Message, state: FSMContext):
    await message.delete()
    await message.answer(text="Iltimos rasmni kiriting ❗️")