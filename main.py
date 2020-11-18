import requests
import discord
import time
from discord.ext import tasks, commands
import json
from datetime import date
from discord.utils import get
from discord.ext.commands import check, MissingRole, CommandError
bot_config = json.loads(open("config.json", "r").read())
client = commands.Bot(command_prefix=bot_config["bot_prefix"])
client.remove_command("help")
channeltopost = bot_config["channel_id_to_send_boblox_updates"]

@client.event
async def on_ready():
	await client.change_presence(activity=discord.Game(name="Looking for boblox update :eyes:"))
	print("Bot is ready!")
	await my_loop.start()

@client.command(pass_context=True)
async def ping(ctx):
	await ctx.send("> `Pong! " + str(round(client.latency * 1000)) + "ms`")

@client.command(pass_context=True)
@commands.has_role("Friends")
async def cum(ctx):
	await ctx.send("Onii-Chan Don't Cum Inside Kyaa~😊")

@tasks.loop(seconds=1.0)
async def my_loop():
	a = requests.get('http://setup.roblox.com/version')
	time.sleep(10)
	b = requests.get('http://setup.roblox.com/version')
	if b.text not in a.text:
		channel = client.get_channel(channeltopost)
		embed = discord.Embed(title="Roblox updated their client:", description= "", color=0x00ff00)
		embed.add_field(name="Roblox Version", value="``"+b.text+"``", inline=True)
		embed.add_field(name="Last Version", value="``"+a.text+"``", inline=True)
		await channel.send(embed=embed)

@my_loop.before_loop
async def before_some_task():
  await client.wait_until_ready()



client.run(bot_config["bot_token"])