import discord
from discord import Webhook, AsyncWebhookAdapter
import asyncio
import sys
import aiohttp
import io
from seleniumwire import webdriver
import time
import json
import pickle
import eel
import threading
from threading import *
import re

from seleniumwire.webdriver import browser
asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

from tornado.platform.asyncio import AnyThreadEventLoopPolicy
asyncio.set_event_loop_policy(AnyThreadEventLoopPolicy())

eel.init('web')

options = {
	'mode': 'custom',
	'args': ['/usr/local/bin/electron', '.'],
	
}

global token
global numbers
numbers = ""

@eel.expose
def browserLogin():
    # eel.spawn(browserLogin_thread) 
    threading.Thread(target=browserLogin_thread, args=(), daemon=True).start()
    

def browserLogin_thread():
    # try:
        print("Opening Browser Window")
        eel.setSnackbar(f"Opening Browser Window")
        global token
        kill = False
        user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36"
        options = webdriver.ChromeOptions()
     
        # chromedriver options
        options.add_argument(f'user-agent={user_agent}')
        options.add_argument('--ignore-certificate-errors')
        options.add_argument('--allow-running-insecure-content')
        options.add_argument("--disable-extensions")
        options.add_argument("--window-size=750,500")
        options.add_argument("--window-position=540,265")
        options.add_argument("--proxy-server='direct://'")
        options.add_argument("--proxy-bypass-list=*")
        options.add_argument("--start-minimized")
        options.add_argument('--disable-gpu')
        options.add_argument('--disable-dev-shm-usage')
        options.add_argument('--no-sandbox')
        options.add_argument('ignore-certificate-errors')
        options.add_experimental_option("excludeSwitches", ['enable-automation'])
        options.add_argument("disable-infobars")
        options.add_argument("--mute-audio")
        options.add_argument("--app=http://discord.com/login")

        
        
        
        driver = webdriver.Chrome(executable_path="chromedriver.exe", options=options)
        eel.setSnackbar(f"Opened Browser Window")
        while True:
            try:
                driver.scopes = ["https://discord.com/api/v9/science"]
            
                cookies = pickle.load(open("cookies.pkl", "rb"))
                for cookie in cookies:       
                    driver.add_cookie(cookie)
                    
                    
                

                # driver.add_cookie({'': sessionStorage})
                print("Waiting For User Login")
                eel.setSnackbar(f"Waiting for User Login")
                time.sleep(7)
                break
                
            except:
                print("Browser Closed")
                eel.setConnection('Connecting to New User 🟡')
                # eel.spawn(ping) 
                threading.Thread(target=ping, args=(), daemon=True).start()
                sys.exit()

        
        while True:
            try:
                for request in driver.requests:
                    
                    token = request.headers['authorization']

                    if token == "undefined":
                        pass
                                    
                    else:
                        
                        safety = token
                        print(token)

                        try:
                            driver.find_element_by_class_name("name-uJV0GL")
                        except:
                            eel.setSnackbar("Browser Closed")
                            sys.exit() 

                        kill = True
                        sessionStorage = driver.get_cookies()


                        data = {}
                        data['appData'] = []
                        data['appData'].append({
                            'sessionStorage': sessionStorage,
                            'discordToken': safety,
                            'discordServers': "",
                            'discordServers_id': "",
                            "discordChannels": ""
                            

                        })
                        
                        with open('data.json', 'w') as outfile:
                            json.dump(data, outfile, indent=2)
                            
                        eel.setConnection('Connecting to New User 🟡')
                        # eel.spawn(ping) 
                        threading.Thread(target=ping, args=(), daemon=True).start()

                        
                        pickle.dump( driver.get_cookies() , open("cookies.pkl","wb"))
                        
                        break

            except:
                eel.setSnackbar("Browser Closed")
                sys.exit() 

            
            if kill == True:

                # monitor(token, 806959633674928168)
                # time.sleep(10)
                while True:
                    try: 
                        driver.find_element_by_xpath('//*[@id="private-channels-1"]/div/div[2]/div/div')

                    except:
                        print("Browser Closed")
                        eel.setConnection('Connecting to New User 🟡')
                        # eel.spawn(ping) 
                        check1 = threading.Thread(target=ping, args=(), daemon=True).start()
                        sys.exit()
        
    # except Exception as e:

    #     print(e)
    #     browserLogin()
        

@eel.expose
def schedule():
    time.sleep(2)
    eel.setConnection('Connecting 🟡')
    
    while True:
        
        time.sleep(3)
        # eel.spawn(ping)
        threading.Thread(target=ping, args=(), daemon=True).start()
        time.sleep(6400)

def ping():
    
    
    token = discord_id()

    if token == "undefined":
        eel.setSnackbar("Internal Error, Please Relogin To Discord")
        eel.setConnection("Internal Error 🔴")
        eel.sleep(3)
        sys.exit()

    client = discord.Client()
    @client.event
    
    async def on_ready():
        # await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="AMonitor"))
        
        eel.setConnection('Connected as {0.user} 🟢'.format(client))
        print('Logged in as {0.user}'.format(client))

        await asyncio.sleep(1)
        sys.exit()
        
    try:
        client.run(token)
        

    except Exception as e:
        print(f"failed connecting {e}")
        eel.setSnackbar(f"Disconnected from Discord")
        eel.setConnection('Disconnected 🔴')
        sys.exit()

def discord_id():
    try:
        f = open('data.json',)
        data = json.load(f)

        for i in data['appData']:
            token = i['discordToken']

        return token
    except Exception as e:
        eel.setSnackbar(f"Internal Error Reading Data {e}")
        print(f"Internal Error Reading Data {e}")

@eel.expose
def pullChannels():
    threading.Thread(target=pullChannels_thread, args=(), daemon=True).start()
    time.sleep(1)
    
def pullChannels_thread():
    eel.setSnackbar("Pulling Channels")

    token = discord_id()
   
    try:
        f = open('data.json',)
        data = json.load(f)

        for i in data['appData']:
            token = i['discordToken']
            sessionStorage = i['sessionStorage']
                
        client = discord.Client()

        @client.event
        async def on_ready():
            guilds = ""
            guilds_id = ""
            
            # pull servers
            async for guild in client.fetch_guilds(limit=150):
                guilds = guilds + guild.name + ","
                guilds_id = guilds_id + str(guild.id) + ","

            
            guilds_array = guilds.split(",")

            # send server list to gui
            for i in guilds_array:
                eel.updateChannel(i)

            eel.setSnackbar("Channels Pulled")

            # pull text channels
            text_channel_list = []
            for server in client.guilds:
                for channel in server.channels:
                    if str(channel.type) == 'text':
                        channel_str = str(channel)
                        channel_guild_str = str(channel.guild)
                        channel_id = str(channel.id)
                        text_channel_list.append(channel_str + ":" + channel_guild_str + "(" + channel_id + ")" + ",")
                    
            channels = ""
            for i in text_channel_list:
                channels = channels + i

            data = {}
            data['appData'] = []
            data['appData'].append({

                'sessionStorage': sessionStorage,
                'discordToken': token,
                'discordServers': guilds,
                'discordServers_id': guilds_id,
                "discordChannels": channels
                            

            })
            
            with open('data.json', 'w') as outfile:
                json.dump(data, outfile, indent=2)
 
            
        
        
        client.run(token)
        sys.exit()

    except Exception as e:
        eel.setSnackbar(e)
        sys.exit()

@eel.expose
def pullChannels_2():
    threading.Thread(target=pullChannels_thread_2, args=(), daemon=True).start()


@eel.expose
def pullChannels_thread_2():
    try:
        
        # pull data from json
        f = open('data.json',)
        data = json.load(f)

        for i in data['appData']:
            channels = i['discordChannels']

        channels = list(channels.split(","))

        # filteres list

        filtered = ""

        # fetch server name
        server = eel.getServer()()
    
        for i in channels:
            if server in i:
                filtered = filtered + i + ","

        filtered = list(filtered.split(","))

        # remove unneccesary data
        filtered = ''.join(map(str, filtered))

        channels = filtered.replace(server,"")
        channels_name = re.sub(r"\([^()]*\)", "", channels)
        channels_name = channels_name.replace(":", ",")
        channels_name = list(channels_name.split(","))

        

        # send channels to gui
        for i in channels_name:
            eel.updateChannels_2(i)
            
        
        return
        
    

    except Exception as e:
        print(e)
        eel.setSnackbar(e)

        return
        






@eel.expose

def mirror(channel_id):
    print(channel_id)
    token = discord_id()
    # eel.spawn(mirror_thread(token, channel_id)) 
    threading.Thread(target=mirror_thread, args=(token, channel_id), daemon=True).start()
    
def mirror_thread(token, channel_id):
    try:
        client = discord.Client()
        # "NzEzNDE4NzAyNzkxMzc3MDAy.YCW2pg.Sw4QVopfCOtHVWsBlUPrbtzswF4"
        token = token

        @client.event
        async def on_ready():
            print('Logged in as {0.user}'.format(client))
            await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="AMonitor"))



        @client.event
        async def on_message(message):
            if message.author == client.user:
                return

            if message.channel.id == channel_id:
                print(message.content)
                attach = message.attachments
                sentembed = message.embeds
                print(attach)
                print(sentembed)


                if attach:
                    for attachment in attach:
                        print (attachment)
                        fp = io.BytesIO()
                        await attachment.save(fp)
                        async with aiohttp.ClientSession() as session:
                            webhook = Webhook.from_url("https://discord.com/api/webhooks/842886865568661505/_EmwCSuRaow3mkI3Ek0xV47Lw83d18lXJz0PVRFhUX8OZZxZB_S399DeceGqmCmJv8DQ", adapter=AsyncWebhookAdapter(session))
                            await webhook.send(content=message.clean_content, file=discord.File(fp, filename=attachment.filename), embeds=sentembed)
                else:
                    async with aiohttp.ClientSession() as session:
                        webhook = Webhook.from_url("https://discord.com/api/webhooks/842886865568661505/_EmwCSuRaow3mkI3Ek0xV47Lw83d18lXJz0PVRFhUX8OZZxZB_S399DeceGqmCmJv8DQ", adapter=AsyncWebhookAdapter(session))
                        await webhook.send(content=message.clean_content, embeds=sentembed)


        client.run(token)

    except Exception as e:
        print(f"Unexpected Error Occured {e}")
        eel.setSnackbar(f"Unknown Error Occured {e}")

@eel.expose
def printnow(something):
    print(something)

# main monitor script
@eel.expose
def monitor_start(data, row):

    threading.Thread(target=monitor_thread, args=(data, row), daemon=True).start()


    

@eel.expose
def monitor_thread(data, name):
    
    # get name and server from data
    

    data = data.split(',')
    
    channel = data[1]
    server = data[2]

    # connect to discord
    client = discord.Client()
    # get token
    token = discord_id()

    f = open('data.json',)
    data = json.load(f)

   

    for i in data['appData']:
        channels = i['discordChannels']


    # turn into array
    channel_array = channels.split(",")

    # format server and channel to serach through list
    search = channel + ':' + server
    for i in channel_array:
        if search in i: 
            id = i
    try:
        print(id)
    

        # get discord id in between paranthesis
        channel_id = id[id.find("(")+1:id.rfind(")")]
        channel_id = int(channel_id)

        @client.event
        async def on_ready():
            print('Logged in as {0.user}'.format(client))
            await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="AMonitor"))
            
    except UnboundLocalError:
        eel.setSnackbar("Refresh Channels")
        eel.setConnection('Refresh Channels 🔴')
        

    @client.event
    async def on_message(message):
        if message.author == client.user:
            return

        if message.channel.id == channel_id:
            sentembed = message.embeds
            print(sentembed)


            
            async with aiohttp.ClientSession() as session:
                start_time = time.time()

                # webhook = Webhook.from_url("https://discord.com/api/webhooks/842886865568661505/_EmwCSuRaow3mkI3Ek0xV47Lw83d18lXJz0PVRFhUX8OZZxZB_S399DeceGqmCmJv8DQ", adapter=AsyncWebhookAdapter(session))

                embeds = message.embeds # return list of embeds
                
                for embed in embeds:
                    message_use = (embed.to_dict())

                # await webhook.send(content=message.clean_content, embeds=sentembed)
                
                
                print(message_use)

                title = asyncio.create_task(searchDict(message_use, "title"))
                url = asyncio.create_task(searchDict(message_use, "url"))
                thumbnail = asyncio.create_task(searchDict(message_use, "thumbnail"))
                description = asyncio.create_task(searchDict(message_use, "description"))

                thumbnail = await thumbnail
                thumbnail_2 = asyncio.create_task(searchDict(thumbnail, "url"))
                
                title = await title
                url = await url
                
                description = await description
                thumbnail_2 = await thumbnail_2


                print(f"title is {title}")
                print(f"url is {url}")
                print(f"thumbnail is {thumbnail_2}")
                # print(f"price is {price}")
                # print(f"bot_actions is {bot_actions}")
        
                try:
                    description = description.replace("*", "")
                    description = list(description.split("\n"))
                except:
                    pass
                

                price = ""
                for item in description:
                    if "Price" in item:
                        price = item

                price = price.replace("Price", "").replace(":", "").replace(" ","")
                print(f"price is {price}")
                print(f"description is {description}")

                monitorData = title+","+url+","+thumbnail_2+","+price
                monitorData = list(monitorData.split(","))
                name_1 = re.sub("[\(\[].*?[\)\]]", "", name)
                name_1 = name_1.strip()
                print("python title" + name_1)
                eel.createItem(monitorData, name_1)

                print("--- %s seconds ---" % (time.time() - start_time))
                

    client.run(token)


async def searchDict(dict, kw):
    for name, value in dict.items():
        if name == kw:
            return value

def menu():
    threading.Thread(target=schedule, args=(), daemon=True).start()

    eel.browsers.set_path('electron', 'node_modules/electron/dist/electron')

    size = (1025, 525)

    # eel.start("index.html", mode='electron', port=8001,)
    # eel.browsers.open('index.html', mode="electron", port=8001)

@eel.expose
def auth(key):
    print(key)
    if key == "AMNTR-J6YD-AIMS-FLVO-46IH":
        time.sleep(1)
        eel.setButton("Key Validated")
        eel.create()
        menu()

        return
    else:
        time.sleep(1)
        eel.setButton("Invalid Key")

    

eel.browsers.set_path('electron', 'node_modules/electron/dist/electron')
eel.start("auth.html", mode='electron', port=8000)





