import discord
client = discord.client
@client.event:
       async def on_ready():
              print('Barter Bot is online'.format(client))
class MyClient(discord.Client):
    async def on_message(self, message):
        if message.author == self.user:
            return

        if message.content.startswith('$hello'):
            await message.channel.send('Hello World!')

client.logging()
