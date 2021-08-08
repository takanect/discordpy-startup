from discord.ext import commands
import os
import traceback

bot = commands.Bot(command_prefix='/')
token = os.environ['DISCORD_BOT_TOKEN']


@bot.event
async def on_command_error(ctx, error):
    orig_error = getattr(error, "original", error)
    error_msg = ''.join(traceback.TracebackException.from_exception(orig_error).format())
    await ctx.send(error_msg)


@bot.command()
async def ping(ctx):
    await ctx.send('pong')

@bot.command()
async def join(ctx):
  channel= ctx.author.voice.channel.id
  await channel.connect()
    
    
@client.event
async def on_message(message):
    if message.content == ".mute":
        if message.author.guild_permissions.administrator:
            bot_vc = message.guild.me.voice.channel # botのいるボイスチャンネルを取得
            for member in bot_vc.members:
                await member.edit(mute=True) # チャンネルの各参加者をミュートする
        else:
            await message.channel.send("実行できません。")


bot.run(token)
