def exportacion(bot):
    @bot.event
    async def on_message(message):
        if not message.content == "hola":
            return
        await message.channel.send("holi")