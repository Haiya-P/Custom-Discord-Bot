import discord
from discord.ext import commands

bot = commands.Bot(command_prefix=".", intents= discord.Intents.all())
'''allows the bot to see
events()'''

@bot.event
async def on_ready():
    print("Here I am!")

@bot.hybrid_command(name='sync', with_app_command=True)
@commands.is_owner()
async def sync(ctx):
    """Synchronizes the command tree."""
    print("Command tree synced")

    await bot.tree.sync()
    await ctx.send("Sync successful")

'''End of sync command'''

'''The Zodiac Command: The portion below represents the zodiac / command, put in your zodiac, and it returns a description
of the zodiac sign you entered'''

@bot.hybrid_command(name='zodiac', with_app_command=True)
async def zodiac(ctx, sign: str):
    """put in your zodiac sign to get a description, ex: capricorn, pisces"""
    if sign.lower() in ["capricorn", "aquarius", "pisces", "aries", "taurus", "gemini", "cancer", "leo", "virgo", "libra", "scorpio", "sagittarius"]:
        match sign.lower():
            case "capricorn":
                await ctx.send("""Capricorn :capricorn: (December 22 - January 19)
Element: Earth
Ruling Planet: Saturn
Symbol: The Goat
Characteristics: Capricorns are known for their discipline, ambition, and practicality. They are hardworking, responsible, and often goal-oriented. Capricorns value tradition and have a strong sense of duty. However, they can also be pessimistic, stubborn, and sometimes overly serious.
""")
            case "aquarius":
                await ctx.send("""Aquarius :aquarius: (January 20 - February 18)
Element: Air
Ruling Planet: Uranus (and Saturn in traditional astrology)
Symbol: The Water Bearer
Characteristics: Aquarius individuals are known for their originality, independence, and humanitarian spirit. They are often innovative, progressive, and have a strong sense of social justice. Aquarians value intellectual stimulation and are usually open-minded. However, they can also be aloof, unpredictable, and sometimes emotionally detached.
""")

            case "pisces":
                await ctx.send("""Pisces :pisces: (February 19 - March 19)
Element: Water
Ruling Planet: Neptune (and Jupiter in traditional astrology)
Symbol: The Fish
Characteristics: Pisces are known for their empathy, intuition, and artistic nature. They are often compassionate, gentle, and have a deep emotional understanding. Pisces individuals are imaginative and can be quite spiritual. However, they can also be overly idealistic, escapist, and sometimes overly sensitive.
""")
            case "aries":
                await ctx.send("""Aries :aries: (March 20 - April 18)
Element: Fire
Ruling Planet: Mars
Symbol: The Ram
Characteristics: Aries are known for their fiery energy, enthusiasm, and leadership qualities. They are often seen as courageous, determined, and confident. Aries individuals are pioneers who love to take initiative and are not afraid of challenges. However, they can also be impatient, impulsive, and sometimes overly aggressive.
""")
            case "taurus":
                await ctx.send("""Taurus :taurus: (April 19 - May 19)
Element: Earth
Ruling Planet: Venus
Symbol: The Bull
Characteristics: Taurus individuals are known for their practicality, reliability, and strong determination. They value stability and comfort, often seeking security in their surroundings. They have a strong appreciation for beauty and luxury. However, they can also be stubborn, possessive, and resistant to change.
""")
            case "gemini":
                await ctx.send("""Gemini :gemini: (May 20 - June 19)
Element: Air
Ruling Planet: Mercury
Symbol: The Twins
Characteristics: Gemini are known for their adaptability, communication skills, and intellectual curiosity. They are often social, witty, and enjoy learning new things. Geminis are versatile and can easily handle multiple tasks. However, they can also be indecisive, inconsistent, and superficial at times.
""")
            case "cancer":
                await ctx.send("""Cancer :cancer: (June 20 - July 21)
Element: Water
Ruling Planet: Moon
Symbol: The Crab
Characteristics: Cancer individuals are known for their emotional depth, sensitivity, and nurturing nature. They value family and home, often creating a comfortable and loving environment. Cancers are intuitive and empathetic, but they can also be moody, overly cautious, and prone to holding grudges.
""")
            case "leo":
                await ctx.send("""Leo :leo: (July 22 - August 21)
Element: Fire
Ruling Planet: Sun
Symbol: The Lion
Characteristics: Leos are known for their charisma, confidence, and leadership qualities. They enjoy being in the spotlight and have a natural ability to inspire others. Leos are generous, creative, and passionate. However, they can also be arrogant, stubborn, and sometimes overly dramatic.
""")
            case "virgo":
                await ctx.send("""Virgo :virgo: (August 22 - September 21)
Element: Earth
Ruling Planet: Mercury
Symbol: The Virgin
Characteristics: Virgos are known for their attention to detail, practicality, and analytical minds. They are hardworking, reliable, and often perfectionists. Virgos have a strong sense of duty and are excellent at organizing and planning. However, they can also be overly critical, worry-prone, and sometimes too focused on flaws.
""")
            case "libra":
                await ctx.send("""Libra :libra: (September 22 - October 21)
Element: Air
Ruling Planet: Venus
Symbol: The Scales
Characteristics: Libras are known for their sense of balance, diplomacy, and love for harmony. They value relationships and are often charming and sociable. Libras have a strong sense of justice and fairness, often seeking to resolve conflicts peacefully. However, they can also be indecisive, avoid confrontations, and sometimes overly dependent on others.
""")
            case "scorpio":
                await ctx.send("""Scorpio :scorpio: (October 22 - November 20)
Element: Water
Ruling Planet: Pluto (and Mars in traditional astrology)
Symbol: The Scorpion
Characteristics: Scorpios are known for their intensity, passion, and determination. They are often mysterious and have a strong sense of intuition. Scorpios are loyal and protective, with a deep emotional depth. However, they can also be secretive, jealous, and sometimes overly controlling.
""")
            case "sagittarius":
                await ctx.send("""Sagittarius :sagittarius: (November 21 - December 20)
Element: Fire
Ruling Planet: Jupiter
Symbol: The Archer
Characteristics: Sagittarius individuals are known for their adventurous spirit, optimism, and love for freedom. They enjoy exploring new ideas, cultures, and places. Sagittarians are honest, enthusiastic, and have a great sense of humor. However, they can also be reckless, impatient, and sometimes tactless.
""")
            case _:
                await ctx.send("NOT A VALID SIGN")

'''Zodiac Command ends here'''

'''The Hello Command: this is a test command, check if the bot says hello back!'''
@bot.hybrid_command(name='hello', with_app_command=True)
async def hello(ctx):
    await ctx.send(f"How are ya, {ctx.author.mention}?")

'''The Hello command ends here'''

'''The Helpme Command: lists the commands that can be used'''

@bot.hybrid_command(name='helpme', with_app_command=True)
async def helpme(ctx):
    await ctx.send("My Commands: helpme, hello, zodiac")
    
'''The Helpme command ends here.'''

bot.run("Custom Discord Bot's Token Goes Here")

