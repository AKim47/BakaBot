
# bot.py
import discord

# create discord client
client = discord.Client()
token = '51385695d559b432c91d8e96beb1380cd835052136721420a48dcdc22bd40152'

idiot_tracker = {}

# bot is ready
@client.event
async def on_ready():
    try:
        print(client.user.name)
        print(client.user.id)

    except Exception as e:
        print(e)


# on new message
@client.event
async def on_message(message):

    # if the message is from the bot itself ignore it
    if message.author == client.user:
        pass
    else:

        # try to evaluate with the command handler
        if message.content.startswith('!baka'):
            args = message.content.split(' ')
            if args[0] == '!baka':
                args.pop(0)

            if args[0] in idiot_tracker:
                idiot_tracker[args[0]] +=1
            else:
                idiot_tracker[args[0]] = 1
            x = 'BAKA '
            baka = x*idiot_tracker[args[0]]

            try:
                await message.channel.send(str(baka) + ' ' + args[0] + '!')

        # message doesn't contain a command trigger
            except TypeError as e:
                pass

        # generic python error
            except Exception as e:
                print(e)
        else:
            pass

# start bot
client.run(token)
