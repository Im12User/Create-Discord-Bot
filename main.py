import discord
from discord.ext import commands
import config
from asyncio import sleep
import datetime
import random
import time

intents = discord.Intents.all()
client = commands.Bot(command_prefix=config.prefix, intents=intents)

#>————==== Status & Activity ====————<#

async def status():
    while True:
        try:
            await client.wait_until_ready()
            await client.change_presence(status=discord.Status.online, activity=discord.Game(name=f"Bot prefix: {config.prefix}"))
            await sleep(5)
            await client.change_presence(status=discord.Status.dnd, activity=discord.Activity(type=discord.ActivityType.watching, name=config.activity1))
            await sleep(5)
            await client.change_presence(status=discord.Status.idle, activity=discord.Activity(type=discord.ActivityType.listening, name=config.activity2))
            await sleep(5)
        except:
            print("Status error")




#>————==== Avatar ====————<#

@client.command()
async def avatar(ctx, member: discord.Member=None):
    if member == None:
        member = ctx.author
        icon_url = member.avatar
        avatarEmbed = discord.Embed(title = f" ", color = config.embed_color)
        avatarEmbed.set_author(name=f"{member.name}'s Avatar", icon_url=icon_url)
        avatarEmbed.set_image(url = f"{icon_url}")
        avatarEmbed.set_footer(text=f"{ctx.author.name}", icon_url=f"{ctx.author.avatar}")
        avatarEmbed.timestamp = ctx.message.created_at
        await ctx.reply(embed = avatarEmbed)
    else:
        icon_url = member.avatar
        avatarEmbed = discord.Embed(title = f" ", color = config.embed_color)
        avatarEmbed.set_author(name=f"{member.name}'s Avatar", icon_url=icon_url)
        avatarEmbed.set_image(url = f"{icon_url}")
        avatarEmbed.set_footer(text=f"{ctx.author.name}", icon_url=f"{ctx.author.avatar}")
        avatarEmbed.timestamp = ctx.message.created_at
        await ctx.reply(embed = avatarEmbed)




#>————==== User Info ====————<#

@client.command()
async def user(ctx, member: discord.Member=None):
    if member == None:
        member = ctx.author
        img = member.display_avatar
        status = str(member.status).replace("dnd", "⛔ Do Not Disturb").replace("online", "🟢 Online").replace("idle", "🌙 Idle").replace("offline", "⚫ Offline")
        roles = [role for role in member.roles[1:]]
        embed = discord.Embed(
        color = discord.Color(config.embed_color),
        title = f"{member.name} info")
        embed.add_field(name="**👤 Name:**", value=f"{member}", inline=False)
        embed.add_field(name="**🆔 ID:**", value=f"{member.id}", inline=False)
        embed.add_field(name="**✨ Status:**", value=f"{status}", inline=False)
        embed.add_field(name=f"**🎈 Roles ({len(member.roles) - 1})**", value='• '.join([role.mention for role in roles]), inline=False)
        embed.add_field(name="**📅 Account Created At:**", value=f"{member.created_at.date()}".replace("-", "/"), inline=True)
        embed.add_field(name="**⌛ Joined Server At:**", value=f"{member.joined_at.date()}".replace("-", "/"), inline = True)
        embed.set_footer(icon_url = f"{ctx.author.avatar}", text = f"Requested by {ctx.author}")
        embed.timestamp = datetime.datetime.utcnow()
        embed.set_thumbnail(url=f"{img}")
        await ctx.reply(embed=embed)
    else:
        img = member.display_avatar
        status = str(member.status).replace("dnd", "⛔ Do Not Disturb").replace("online", "🟢 Online").replace("idle", "🌙 Idle").replace("offline", "⚫ Offline")
        roles = [role for role in member.roles[1:]]
        embed = discord.Embed(
        color = discord.Color(config.embed_color),
        title = f"{member.name} info")
        embed.add_field(name="**👤 Name:**", value=f"{member}", inline=False)
        embed.add_field(name="**🆔 ID:**", value=f"{member.id}", inline=False)
        embed.add_field(name="**✨ Status:**", value=f"{status}", inline=False)
        embed.add_field(name=f"**🎈 Roles ({len(member.roles) - 1})**", value='• '.join([role.mention for role in roles]), inline=False)
        embed.add_field(name="**📅 Account Created At:**", value=f"{member.created_at.date()}".replace("-", "/"), inline=True)
        embed.add_field(name="**⌛ Joined Server At:**", value=f"{member.joined_at.date()}".replace("-", "/"), inline = True)
        embed.set_footer(icon_url = f"{ctx.author.avatar}", text = f"Requested by {ctx.author}")
        embed.timestamp = datetime.datetime.utcnow()
        embed.set_thumbnail(url=f"{img}")
        await ctx.reply(embed=embed)




#>————==== Server Info ====————<#

@client.command()
async def server(ctx):
    serverOwner = ctx.guild.owner_id
    server_info_Embed = discord.Embed(color= config.embed_color)
    server_info_Embed.set_author(name=f"{ctx.guild.name} info", icon_url=f"{ctx.guild.icon}")
    server_info_Embed.add_field(name="**🏁 Server Name: **", value=ctx.guild.name, inline=False)
    server_info_Embed.add_field(name="**🆔 Server Id: **", value=ctx.guild.id, inline=False)
    server_info_Embed.add_field(name="**👑 Server Owner: **", value=f"<@{serverOwner}>", inline=False)
    server_info_Embed.add_field(name="**🗨 Text Channels: **", value=len(ctx.message.guild.text_channels), inline=False)
    server_info_Embed.add_field(name="**🔊 Voice Channels: **", value=len(ctx.message.guild.voice_channels), inline=False)
    server_info_Embed.add_field(name="**✨ Roles: **", value=len(ctx.message.guild.roles), inline=False)
    server_info_Embed.add_field(name="**📅 Create at: **", value=ctx.guild.created_at.__format__("%A , %d. %B %Y | %H:%M.%S"), inline=True)
    server_info_Embed.add_field(name="**🌍 Region: **", value=ctx.guild.region, inline=True)
    server_info_Embed.set_thumbnail(url=f"{ctx.guild.icon}")
    server_info_Embed.set_footer(text=f"Request by {ctx.author.name}", icon_url=f"{ctx.author.avatar}")
    await ctx.reply(embed=server_info_Embed)




#>————==== Ping ====————<#

@client.command()
async def ping(ctx):
    embed=discord.Embed(title="Pong", color=config.embed_color)
    embed.add_field(name="**🛰 Bot ping:**", value=f"__**{round(client.latency *1000)}ms**__", inline=False)
    uptime = str(datetime.timedelta(seconds=int(round(time.time()-time.time()))))
    embed.add_field(name="**⏳ Uptime:**", value=uptime, inline=False)
    embed.set_footer(text=f"Request by {ctx.author.name}", icon_url=f"{ctx.author.avatar}")
    await ctx.reply(embed=embed)




#>————==== Rainbow Role ====————<#

colours = [discord.Color.dark_orange(),discord.Color.orange(),discord.Color.dark_gold(),discord.Color.gold(),discord.Color.dark_magenta(),discord.Color.magenta(),discord.Color.red(),discord.Color.dark_red(),discord.Color.blue(),discord.Color.dark_blue(),discord.Color.teal(),discord.Color.dark_teal(),discord.Color.green(),discord.Color.dark_green(),discord.Color.purple(),discord.Color.dark_purple()]
async def rainbowrole():
    if config.rrstatus == "on":
        delay = config.delay
        rainbowrolename = config.rgbRoleName
        serverid = config.serverId
        for role in client.get_guild(serverid).roles:
            if str(role) == str(rainbowrolename):
                print("detected role")
                while not client.is_closed():
                    try:
                        await role.edit(color=random.choice(colours))
                    except Exception:
                        print("can't edit role, make sure the bot role is above the rainbow role and that is have the perms to edit roles")
                        pass
                    await sleep(delay)
        print('role with the name "' + rainbowrolename +'" not found')
        print("creating the role...")
        try:
            await client.get_guild(serverid).create_role(reason="Created rainbow role", name=rainbowrolename)
            print("role created!")
            await sleep(2)
        except Exception as e:
            print("couldn't create the role. Make sure the bot have the perms to edit roles")
            print(e)
            pass
            await sleep(10)
    if config.rrstatus == "off":
        pass

@client.event
async def on_ready():
    client.loop.create_task(status())
    client.loop.create_task(rainbowrole())
    print(f'Log : {client.user}')




    #>————==== Connect voice ====————<#
    
    chi = config.voiceChannelId
    channel = client.get_channel(chi)
    await channel.connect()

client.run(config.token)
