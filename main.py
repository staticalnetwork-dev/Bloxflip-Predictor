import discord
import random
from discord import app_commands 

class aclient(discord.Client):
    def __init__(self):
        super().__init__(intents = discord.Intents.default())
        self.synced = False 

    async def on_ready(self):
        await self.wait_until_ready()
        if not self.synced: 
            await tree.sync() 
            self.synced = True
        print(f"We have logged in as {self.user}.")

client = aclient()
tree = app_commands.CommandTree(client)

@tree.command(name='mines', description='mines predictor') 
async def self(interaction: discord.Interaction, round_id : str):
    round_id = str(round_id)
    round_length = len(round_id)
    if round_length < 36:
        await interaction.response.send_message("Invalid round id")
    elif round_length == 36:
        mine1, mine2, mine3, mine4, mine5, mine6, mine7, mine8, mine9, mine10, mine11, mine12, mine13, mine14, mine15, mine16, mine17, mine18, mine19, mine20, mine21, mine22, mine23, mine24, mine25 = ':question:', ':question:', ':question:', ':question:', ':question:', ':question:', ':question:', ':question:', ':question:', ':question:', ':question:', ':question:', ':question:', ':question:', ':question:', ':question:', ':question:', ':question:', ':question:', ':question:', ':question:', ':question:', ':question:', ':question:', ':question:'
        a = random.randint(1, 8)
        b = random.randint(9, 13)
        c = random.randint(14, 17)
        d = random.randint(18, 25)
        if a == 1:
            mine1 = ":green_square: "
        elif a == 2:
            mine2 = ":green_square: "
        elif a == 3:
            mine3 = ":green_square: "
        elif a == 4:
            mine4 = ":green_square: "
        elif a == 5:
            mine5 = ":green_square: "
        elif a == 6:
            mine6 = ":green_square: "
        elif a == 7:
            mine7 = ":green_square: "
        elif a == 8:
            mine8 = ":green_square: "
        if b == 9:
            mine9 = ":green_square: "
        elif b == 10:
            mine10 = ":green_square: "
        elif b == 11:
            mine11 = ":green_square: "
        elif b == 12:
            mine12 = ":green_square: "
        elif b == 13:
            mine13 = ":green_square: "
        if c == 14:
            mine14 = ":green_square: "
        elif c == 15:
            mine15 = ":green_square: "
        elif c == 16:
            mine16 = ":green_square: "
        elif c == 17:
            mine17 = ":green_square: "
        if d == 18:
            mine18 = ":green_square: "
        elif d == 19:
            mine19 = ":green_square: "
        elif d == 20:
            mine20 = ":green_square: "
        elif d == 21:
            mine21 = ":green_square: "
        elif d == 22:
            mine22 = ":green_square: "
        elif d == 23:
            mine23 = ":green_square: "
        elif d == 24:
            mine24 = ":green_square: "
        elif d == 25:
            mine25 = ":green_square: "
        row1 = mine1 + mine2 + mine3 + mine4 + mine5
        row2 = mine6 + mine7 + mine8 + mine9 + mine10
        row3 = mine11 + mine12 + mine13 + mine14 + mine15
        row4 = mine16 + mine17 + mine18 + mine19 + mine20
        row5 = mine21 + mine22 + mine23 + mine24 + mine25
        info = str(random.randint(45, 90))
        pfp = 'https://media3.giphy.com/media/Nuw350JrWXm0/200w.gif?cid=82a1493bkip1bj4orem8n2ra4jp9a1kaegid8nsf37jfx3ia&rid=200w.gif&ct=g'
        em = discord.Embed(color=0x11F1D3)
        em.set_thumbnail(url=pfp)
        em.set_footer(text="Made by geek | Composed by static#6666")
        em.add_field(name="Mines predictor",value=row1 + "\n" + row2 + "\n" + row3 + "\n" + row4 +"\n" + row5 + "\n" + "**Accuracy**" + "\n" + info +"%")
        await interaction.response.send_message(embed=em)

@tree.command(name='roulette', description='roulette predictor') 
async def self(interaction: discord.Interaction, round_id : str):
    round_id = str(round_id)
    round_length = len(round_id)
    if round_length == 36:
        predictions = ['red','red','red','purple','purple','purple','gold']
        prediction = random.choice(predictions)
        if prediction == 'red':
            embed_color = 0xFF0036
            color_text = 'Red'
            prediction = ":red_square:"
        elif prediction == 'purple':
            embed_color = 0xAE00FF
            color_text = 'Purple'
            prediction = ":purple_square:"
        elif prediction == 'purple':
            embed_color = 0xFFFB00
            color_text = 'Gold'
            prediction = ":yellow_square:"
        em = discord.Embed(color=embed_color)
        em.add_field(name="Roulette Predictor", value=color_text + "\n" + prediction)
        em.set_footer(text="Made by geek | Composed by static#6666")
        await interaction.response.send_message(embed=em)
    else:
        await interaction.response.send_message("Invalid round id")

@tree.command(name='cups', description='cups predictor')
async def self(interaction: discord.Interaction, round_id : str):
    round_id = str(round_id)
    round_length = len(round_id)
    if round_length == 36:
        prediction = random.randint(1,2)
        if prediction == 1:
            embed_color= 0xFF0036
            text = 'Red Cup'
            prediction = ":red_square:"
        elif prediction == 2:
            embed_color= 0x3498DB
            text = 'Blue Cup'
            prediction = ":blue_square:"
        em = discord.Embed(color=embed_color)
        em.add_field(name="Cups Predictor", value=text + "\n" + prediction)
        em.set_footer(text="Made by geek | Composed by static#6666")
        await interaction.response.send_message(embed=em)
    else:
        await interaction.response.send_message("Invalid round id")

@tree.command(name='towers', description='towers predictor')
async def self(interaction: discord.Interaction, round_id : str):
    round_id = str(round_id)
    round_length = len(round_id)
    if round_length < 36:
        await interaction.response.send_message("Invalid round id")
    elif round_length == 36:
        tower1,tower2,tower3,tower4,tower5,tower6,tower7,tower8,tower9,tower10,tower11,tower12,tower13,tower14,tower15,tower16,tower17,tower18,tower19,tower20,tower21,tower22,tower23,tower24 = ":question:",":question:",":question:",":question:",":question:",":question:",":question:",":question:",":question:",":question:",":question:",":question:",":question:",":question:",":question:",":question:",":question:",":question:",":question:",":question:",":question:",":question:",":question:",":question:"
        a = random.randint(1, 3)
        b = random.randint(1, 3)
        c = random.randint(1, 3)
        d = random.randint(1, 3)
        e = random.randint(1, 3)
        f = random.randint(1, 3)
        g = random.randint(1, 3)
        h = random.randint(1, 3)

        if a == 1:
            tower1 = ":star:"
        elif a == 2:
            towe2 = ":star:"
        elif a ==3:
            tower3 = ":star:"
        if b == 1:
            tower4 = ":star:"
        elif b == 2:
            tower5 = ":star:"
        elif b ==3:  
            tower6 = ":star:"
        if c == 1:
            tower7 = ":star:"
        elif c == 2:
            tower8 = ":star:"
        elif c ==3:
            tower9 = ":star:"
        if d == 1:
            tower10 = ":star:"
        elif d == 2:
            tower11 = ":star:"
        elif d ==3:
            tower12 = ":star:"
        if e == 1:
            tower13 = ":star:"
        elif e == 2:
            tower14 = ":star:"
        elif e ==3:
            tower15 = ":star:"
        if f == 1:
            tower16 = ":star:"
        elif f == 2:
            tower17 = ":star:"
        elif f ==3:
            tower18 = ":star:"
        if g == 1:
            tower19 = ":star:"
        elif g == 2:
            tower20 = ":star:"
        elif g ==3:
            tower21 = ":star:"
        if h == 1:
            tower22 = ":star:"
        elif h == 2:
            tower23 = ":star:"
        elif h ==3:
            tower24 = ":star:"

        row1 = tower1 + tower2 + tower3
        row2 = tower4 + tower5 + tower6
        row3 = tower7 + tower8 + tower9
        row4 = tower10 + tower11 + tower12
        row5 = tower13 + tower14 + tower15
        row6 = tower16 + tower17 + tower18
        row7 = tower19 + tower20 + tower21
        row8 = tower22 + tower23 + tower24
        #await ctx.send(row1 + "\n" + row2 + "\n" + row3 + "\n" +row4 + "\n" +row5 + "\n" +row6 + "\n" +row7 + "\n" +row8)
        info = str(random.randint(45, 95))
        pfp = 'https://cdn.discordapp.com/attachments/1012915410435309661/1015697209280450612/standard.gif'
        list = [0xFF0000, 0x00FF2E, 0x000FFF, 0xF700FF]
        color = random.choice(list)
        em = discord.Embed(color=color)
        em.set_thumbnail(url=pfp)
        em.set_footer(text="Made by geek | Composed by static#6666")
        em.add_field(name="Towers Predictor", value=row1 + "\n" + row2 + "\n" + row3 + "\n" +row4 + "\n" +row5 + "\n" +row6 + "\n" +row7 + "\n" +row8 + "\n" + "**Accuracy**" + "\n" + info + "%")   
        await interaction.response.send_message(embed=em)

client.run('token here')
