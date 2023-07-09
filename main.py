from discord.ext import commands
import discord


class MyBot(commands.Bot):

    async def setup_hook(self) -> None:
        await self.load_extension("jishaku")
        await self.load_extension("cogs.dnsutils")

    async def on_ready(self) -> None:
        print("Ready")


bot = MyBot(command_prefix="t2!", intents=discord.Intents.all())


if __name__ == "__main__":
    from os import getenv
    bot.run(get_env("DISCORD_TOKEN"))
