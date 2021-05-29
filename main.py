import discord
import asyncio
from discord.ext import commands
import openpyxl
import os
from keep_alive import keep_alive

keep_alive()

intents = discord.Intents().all()
bot = commands.Bot(command_prefix='=', intents=intents)
bot.remove_command('help')

def heoji(ctx):
    return ctx.message.author.id == 789436022181855242

for filename in os.listdir("Cogs"):
    if filename.endswith(".py"):
        bot.load_extension(f"Cogs.{filename[:-3]}")


@bot.command(name="로드")
@commands.check(heoji)
async def load_commands(ctx, extension):
    bot.load_extension(f"Cogs.{extension}")
    await ctx.send(f":white_check_mark: {extension}을(를) 로드했습니다!")


@bot.command(name="언로드")
@commands.check(heoji)
async def unload_commands(ctx, extension):
    bot.unload_extension(f"Cogs.{extension}")
    await ctx.send(f":white_check_mark: {extension}을(를) 언로드했습니다!")


@bot.command(name="리로드")
@commands.check(heoji)
async def reload_commands(ctx, extension=None):
    if extension is None:
        for filename in os.listdir("Cogs"):
            if filename.endswith(".py"):
                bot.unload_extension(f"Cogs.{filename[:-3]}")
                bot.load_extension(f"Cogs.{filename[:-3]}")
                await ctx.send(":white_check_mark: 모든 명령어를 다시 불러왔습니다!")
    else:
        bot.unload_extension(f"Cogs.{extension}")
        bot.load_extension(f"Cogs.{extension}")
        await ctx.send(f":white_check_mark: {extension}을(를) 다시 불러왔습니다!")

@bot.event
async def on_ready():
    print(f"We have logged in as {bot.user}")
    await bot.change_presence(activity=discord.Activity(
        type=discord.ActivityType.watching, name=f"=도움말"))
    print(discord.__version__)

@bot.event
async def on_message(message):
    await bot.process_commands(message)

    if message.author == bot.user:
        return

    if message.content in ["=도움말","=도움","=help"]:
        embed = discord.Embed(title=" [마법의책] 목차 ",
                              description="글쓴이 허지#0435 / 주문 =",
                              color=0x800080)
        embed.add_field(name="작성", value="`=작성 (글제목)*(내용)\n글제목이나 내용엔 *가 들어가서는 안 된다`", inline=False)
        embed.add_field(name="독서", value="`=독서 (글제목)`", inline=False)
        embed.add_field(name="목차", value="`=목차`", inline=False)
        embed.add_field(name="편지", value="`마법의책 개인메세지에 무언가를 쓰면 그대로 누군가에게 전해진다`", inline=False)
        embed.set_footer(text="독서 주문의 경우에는 장문 도배가 될 수 있으니 주의해야 한다")

        await message.channel.send(embed=embed)

    if not message.content.startswith("="):
      if isinstance(message.channel, discord.abc.PrivateChannel) and message.author.id != "826743049307684895":
        await bot.get_user(789436022181855242).send(message.author.name + "(" + str(message.author.id) + "): " + message.content)
        embed = discord.Embed(title=" 전송되었습니다 ", description=" 당신이 페이지 한장을 뜯어 무언가를 쓰니 페이지가 종이비행기로 변해 어딘가로 날아갑니다", color=0x800008)
        await message.channel.send(embed=embed)
bot.run(os.getenv("TOKEN"))