import discord
from discord.ext import commands
import time
import vgamepad as vg

bot = commands.Bot(command_prefix="dp!")
chatpad = vg.VX360Gamepad()
botChat = 'bot-spam'
token = 'Your Bot Token'

# removes help command
bot.remove_command("help")

# Login Confirmation
@bot.event
async def on_ready():
    print('We have logged in as {0.user}'.format(bot))
    await bot.change_presence(activity=discord.Game(name='dp!help'))

# Misc Commands
@bot.command()
async def help(ctx):
    helpMessage = discord.Embed(title="~Discord Plays Help~",
                                   description="Discord plays is a discord bot designed to emulate the 'Twitch Plays Pokemon' series of livestreams within discord!",
                                   color=discord.Colour.dark_blue())
    helpMessage.set_author(name="Azalea", icon_url='https://i.imgur.com/9ujzyPl.png')
    helpMessage.set_thumbnail(url='https://i.imgur.com/9ujzyPl.png')
    helpMessage.add_field(name="Getting started with Discord Plays", value="To get started you have access to all basic commands, up, down, left, right, start, select, A and B, to issue any command you just type it in #bot-spam and the command will be issued in the game, you can ***only*** type one command per message!"
                            , inline=False)
    helpMessage.set_footer(text='Created by Aurora (AquaChill) @2021')

    if ctx.channel.name == botChat:
        print(f'{ctx.message.author} has been helped. Yay!')
        await ctx.send(embed=helpMessage)
    else:
        print(f'{ctx.message.author} tried to get help in the wrong chat. Dummy!')

# Gamepad Controls
@bot.event
async def on_message(message):
    if message.content.lower().startswith('up') and message.channel.name == botChat:
        print('Up button')
        chatpad.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_UP)
        chatpad.update()
        time.sleep(.1)
        chatpad.release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_UP)
        chatpad.update()

    elif message.content.lower().startswith('down') and message.channel.name == botChat:
        print('Down button')
        chatpad.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_DOWN)
        chatpad.update()
        time.sleep(.1)
        chatpad.release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_DOWN)
        chatpad.update()

    elif message.content.lower().startswith('left') and message.channel.name == botChat:
        print('Left button')
        chatpad.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_LEFT)
        chatpad.update()
        time.sleep(.1)
        chatpad.release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_LEFT)
        chatpad.update()

    elif message.content.lower().startswith('right') and message.channel.name == botChat:
        print('Right button')
        chatpad.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_RIGHT)
        chatpad.update()
        time.sleep(.1)
        chatpad.release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_RIGHT)
        chatpad.update()

    elif message.content.lower().startswith('start') and message.channel.name == botChat:
        print('Start button')
        chatpad.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_START)
        chatpad.update()
        time.sleep(.1)
        chatpad.release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_START)
        chatpad.update()

    elif message.content.lower().startswith('select') and message.channel.name == botChat:
        print('Select button')
        chatpad.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_LEFT_THUMB)
        chatpad.update()
        time.sleep(.1)
        chatpad.release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_LEFT_THUMB)
        chatpad.update()

    elif message.content.lower().startswith('a') and message.channel.name == botChat:
        print('A button')
        chatpad.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_A)
        chatpad.update()
        time.sleep(.1)
        chatpad.release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_A)
        chatpad.update()

    elif message.content.lower().startswith('b') and message.channel.name == botChat:
        print('B button')
        chatpad.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_B)
        chatpad.update()
        time.sleep(.1)
        chatpad.release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_B)
        chatpad.update()

    await bot.process_commands(message)

bot.run(token)

# Discord Plays bot created by Aurora (AquaChill) @2021
