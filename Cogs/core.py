from os import name
import discord #1
from discord.ext import commands
from discord.ext.commands.core import command
from discord.utils import get
import os
import glob

class Core(commands.Cog): #2

    def __init__(self, bot): #3
        self.bot = bot #4

    @commands.command(name="핑")
    async def ping(self, ctx):
        embed=discord.Embed(title="지연율", description=f":ping_pong: {str(round(self.bot.latency*1000))}ms", color=0x800080)
        await ctx.send(embed=embed)
    
    @commands.command(name="작성")
    async def write(self, ctx, *, text):
        text = text.split("*")
        folder = "txts"
        files = os.listdir(folder)
        if f"{text[0]}.txt" in files:
            f = open(f"txts/{text[0]}.txt", 'w')
            f.write(text[1] + f"\n----------------------\n" + ctx.author.name + "#" + ctx.author.discriminator)
            embed=discord.Embed(title="작성되었습니다", description="당신이 주문과 당신의 이야기를 말하자 마법의책이 빛나더니 이전 이야기가 사라지고 당신의 이야기가 기록되었습니다", color=0x800800)
            await ctx.send(embed=embed)
        else:
            f = open(f"txts/{text[0]}.txt", 'w')
            f.write(text[1] + f"\n----------------------\n" + ctx.author.name + "#" + ctx.author.discriminator)
            embed=discord.Embed(title="작성되었습니다", description="당신이 주문과 당신의 이야기를 말하자 마법의책이 빛나더니 당신의 이야기가 기록되었습니다", color=0x800080)
            await ctx.send(embed=embed)
            f.close()

    @commands.command(name="목차")
    async def lists(self, ctx):
        targerdir = "txts"
        def getfiles(dirpath):
            filelist = [s for s in os.listdir(dirpath)
                if os.path.isfile(os.path.join(dirpath, s))]
            filelist.sort(key=lambda s: os.path.getmtime(os.path.join(dirpath, s)))
            return filelist

        texts = getfiles(targerdir)
        texts.reverse()        
        texts = texts[:3]
        embed=discord.Embed(title="목차", description="가장 최근에 작성된 이야기", color=0xff8008)
        await ctx.send(embed=embed)
        for i in texts :
            await ctx.send("```" + i + "```")

    @commands.command(name="독서")
    async def readdd(self, ctx, *, story):
        folder = "txts"
        files = os.listdir(folder)
        if f"{story}.txt" in files:
            f = open(f"txts/{story}.txt", "r")
            contents = f.read()
            embed=discord.Embed(title=f"{story}", description=contents, color=0x800080)
            await ctx.send(embed=embed)
            f.close()

def setup(bot): #5
    bot.add_cog(Core(bot))