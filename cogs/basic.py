import discord
import datetime
from discord.ext import commands
from discord.ext.commands import BadArgument
from discord import utils

class basic(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        
    @commands.command(name='hug', aliases=['huh','hugh'])
    @commands.guild_only()
    async def hug(self, ctx: commands.Context, friend: discord.Member):
        """Hugs a person."""
        if friend == ctx.author:
            await ctx.send("You must be really lonely if you need to hug yourself, have one from me instead!")
        elif friend == self.bot.user:
            await ctx.send("Thanks for the hug! :heart:")
        else:
            await ctx.send(f"{friend.mention}, you have recieved a big, big hug from {ctx.author.name}!")

    @commands.command(name='fight', aliases=['fite'])
    @commands.guild_only()
    async def fight(self, ctx: commands.Context, friend: discord.Member):
        """Fights a person."""
        if friend == ctx.author:
            await ctx.send("Why are you trying to fight yourself?")
        elif friend == self.bot.user:
            await ctx.send("Whoa, whoa. Why are you fighting me? :frowning:")
        else:
            await ctx.send(f"{ctx.author.name} is fighting {friend.mention}!")
    
    @commands.command(hidden=True)
    async def restart(self, ctx):
        """Restarts the bot"""
        Ghoul = [298618155281154058]
        if ctx.author.id not in Ghoul:
            return await ctx.send("Sorry, I'm afraid that you don't have the permission to use this secret command.")
        await ctx.send("Restarting...")
        await self.bot.logout()
        await self.bot.close()

def setup(bot):
    bot.add_cog(basic(bot))
