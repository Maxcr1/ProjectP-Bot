from discord.ext import commands

from src import active_guild_id
from src.EmojiRegistration.EmojiRegistrationCog import EmojiRegistrationCog
from src.PinSystem.PinCog import PinCog
from src.PinSystem.TimestampGenerator import TimestampGenerator
from src.Translation.TranslationCog import TranslationCog

ts = TimestampGenerator("BANE")


class Bot(commands.Bot):

    def __init__(self, *args, **kwargs):
        self.guild = None
        self.channelDict = {}
        super().__init__(*args, **kwargs)

    async def on_ready(self):
        # Find guild that matches active_guild_id
        self.guild = [guild for guild in self.guilds if guild.id == active_guild_id][0]
        print(ts.get_time_stamp(), "Found Active Guild: " + self.guild.name)

        # Populate channelDict for future convenience
        for a in self.guild.text_channels:
            self.channelDict[a.name] = a

        # Start cogs
        print(ts.get_time_stamp(), 'Starting Cogs')
        self.add_cog(PinCog(bot, self))
        self.add_cog(TranslationCog(bot))
        self.add_cog(EmojiRegistrationCog(bot, self))


# Read API key from file
f = open("data/test_key.txt", "r")
key = f.read()

# Create and start Bane Bot
bot = Bot()
bot.run(key)
