import discord
import config

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')

    if message.channel.id in config.channel_relay:
        channel = client.get_channel(config.channel_relay[message.channel.id])
        msg = "`" + message.author.nick + "` from `" +  message.channel.name + "` in `" + message.guild.name + '`\n' + message.content
        await channel.send(msg)



client.run(config.bot_token)


