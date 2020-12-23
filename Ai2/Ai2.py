import discord
from discord.ext import commands
import os
from chatterbot.trainers import ListTrainer
from chatterbot import ChatBot
from time import sleep

intents = discord.Intents.default()
intents.members = True

bot = commands.Bot(command_prefix='-', description="Powered by Ai-Engine", intents=intents)
bot.remove_command('help')

# Listen
@bot.listen()
async def on_message(message):
    chatbot = ChatBot("Ai2")
    conversation = [
        "Hello, my name is Ai2",
        "What’s your nationality?",
        "Everybody can be my friend.",
        "So we’ve met again,eh?",
        "What have you been doing?",
        "I like jazz music",
        "Training",
        "Who is your favourite singer?",
        "Pai",
        "Nice to meet you",
        "How are you?",
        "My favourite sport is batminton",
        "My favourite sport is chairball",
        "When is your birthday?",
        "Hello",
        "23th Dec 2020",
        "Do you have a mobile phone?",
        "Yes, I do",
        "No, I don't",
        "How long have you been here for? ",
        "What kind of music do you like?",
        "I like pop music",
        "Fine thanks, and you?",
        "I’m okay, thank you",
        "Where are you from?",
        "How much is it?",
        "Can you give me a discount?",
        "This is a special price for you",
        "I’m from Thailand",
        "How old are you?",
        "I’m 0 years old",
        "I like hip-hop music",
        "I like rock music",
        "I like electronic music",
        "What’s your favorite food?",
        "Thank you",
        "Thanks for everything",
        "My favourite food is noodle",
        "What’s your favorite movie?",
        "My favourite movie is Avenger",
        "My favourite movie is Interstellar",
        "Yes",
        "Do you deliver?",
        "Does it have a warranty?",
	    "I am good",
	    "That is good to hear",
        "That’s not fair",
	    "You are welcome"
        "My favourite movie is Avatar",
        "What’s your favorite sport?",
        "My favourite sport is football",
        "My favourite sport is basketball",
        "My favourite sport is tennis",
        "What animals do you like?",
        "I like dogs",
        "I like cats",
        "What kind of fruit do you like?",
        "Do you like bananas?",
        "I like watching TV",
        "I really like gardening",
        "I love the cinema",
        "I enjoy travelling",
        "I’m interested in photography",
        "I read a lot",
        "How many languages can you speak?",
        "Can you sing?",
        "Can I try it on?",
        "I’ll take this one",
        "I like it very much",
        "I’ll take it",
        "This is the last piece!",
        "That seems expensive",
        "Do you have a less expensive one?",
        "It’s just right",
        
        "No",
        "I’ll pay",
        "What do you want to eat?",
        "What are you looking for?",
        "I’m looking for shoes",
        "I’m just looking",
        
        
    ]

    trainer = ListTrainer(chatbot)
    trainer.train(conversation)
    textttt = message.content.lower()

    response = chatbot.get_response(textttt)
    output = str(response) + "\n"

    if message.author.id == bot.user.id:
	    return
    await message.channel.send(output)
    sleep(1)

# Events
@bot.event
async def on_ready():
	await bot.change_presence(activity=discord.Game(name="Training"))
	print('Ai2 is Running !!')

Token = os.environ["Ai2Token"]
bot.run(Token)