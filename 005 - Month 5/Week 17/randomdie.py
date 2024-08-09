import random
import discord
from discord.ext import commands
from apikeys import BOTTOKEN



class Dice:
    @staticmethod
    def roll_dice():
        return random.randint(1, 6), random.randint(1, 20)



class RollButton(discord.ui.Button ):
    def __init__(self):
        super().__init__(label="Roll Dice", style=discord.ButtonStyle.primary)

    async def callback(self, interaction: discord.Interaction):
        six_sided_die, twenty_sided_die = Dice.roll_dice()
        await interaction.response.send_message(f"6-sided die roll: {six_sided_die}\n20-sided die roll: {twenty_sided_die}")



class RollView(discord.ui.View):
    def __init__(self, timeout=5):
        super().__init__(timeout=timeout)
        self.add_item(RollButton())



class MyClient(commands.Bot):
    def __init__(self, command_prefix, intents):
        super().__init__(command_prefix=command_prefix, intents=intents)

    async def on_ready(self):
        print(f'Logged on as {self.user}!')
        activity = discord.Game(name="on R4ins.xyz")
        await self.change_presence(status=discord.Status.online, activity=activity)

    async def on_message(self, message):
        if message.author == self.user:
            return

        if message.content.startswith('!roll'):
            view = RollView()
            await message.channel.send("Press the button to roll the dice!", view=view)

def on_run():
    intents = discord.Intents.default()
    intents.message_content = True
    client = MyClient(command_prefix="!", intents=intents)
    client.run(BOTTOKEN)

if __name__ == "__main__":
    on_run()
