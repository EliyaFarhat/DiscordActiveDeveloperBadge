import discord
from discord import app_commands
TOKEN = "<YOUR TOKEN>"

class MyClient(discord.Client):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    async def on_ready(self):
        await tree.sync()
        print("{0.user} is now online".format(client))



client = MyClient(intents=discord.Intents.default())
tree = app_commands.CommandTree(client)
@tree.command(name="badge", description="Get the badge.")
async def badge(interaction: discord.Interaction):
    embed = discord.Embed(
        title=":white_check_mark: You will be able to claim the badge from this link after 24 hours.",
        colour=discord.Colour.green(),
        url="https://discord.com/developers/active-developer"
    )
    await interaction.response.send_message(embed=embed)

client.run(TOKEN)