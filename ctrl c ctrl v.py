dp.message.register(_handler, F.text=='')
bot = Bot(token=settings.bot_token, parse_mode='HTML')



async def audio_handler(message: types.Message, msg: Message, bot: Bot):
    tts = gTTS(message.text, lang='ru')
    tts.save(f'{message.from_user.id}.mp3')
    await msg.answer(text='Ты зашел во вкладку "Аудио-перевод"\nЧто это такое? Наверняка задал ты вопрос, так вот:\nЗайдя в эту вкладку ты можешь написать любой текст, а бот запишет голосовое с этим текстом.\nДо сих пор не понял? напиши что-нибудь в чат и увидишь!')
    await message.answer_voice(open(f'{message.from_user.id}.mp3', 'rb'))


f"Приветствую, {html.bold(html.quote(message.from_user.full_name))}! <b>я - ваш бот ассистент</b>.\nМоя задача помочь вам и хоть немного облегчить вашу жизнь"

Приветствую, ! <b>я - ваш бот ассистент</b>.\nМоя задача помочь вам и хоть немного облегчить вашу жизнь

#<del></del> ЗАЧЕРКНУТЫЙ




async def vkmp_apk(chat_id, bot: Bot, msg: Message):
    file_path='VKMP.apk'
    with open(file_path, 'rb') as file:
        await msg.answer_document(chat_id, file)
async def vkmp_apk_issue(message: types.Message, bot: Bot):
    chat_id = message.chat.id
    await vkmp_apk(chat_id)


    # Отправка файла из файловой системы
    vk_apk_from_pc = FSInputFile("image_from_pc.jpg")
    result = await message.answer_document(
        vk_apk_from_pc,
        caption="Загрузчик VKMP"
    )
    file_ids.append(result.document[-1].file_id)