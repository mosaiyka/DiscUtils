import requests
from datetime import datetime, timezone
import threading
import websocket
import websockets
import asyncio
import json
import time
from functools import wraps
import sys
import random
import colorama
from collections import namedtuple

class client:
    def __init__(self, token, onlyone=True, prefix=" ", dict=False):
        self.dict = dict
        self.token = token
        self.theard = True
        self.headers = {'Authorization': f'{self.token}', 'User-Agent': "Mozilla/5.0 (iPhone; CPU iPhone OS 11_4_1 like Mac OS X) AppleWebKit/604.3.5 (KHTML, like Gecko) Version/11.0 MQQBrowser/8.7.1 Mobile/15B87 Safari/604.1 MttCustomUA/2 QBWebViewType/1 WKType/1NULL"}
        self.headersjson = {'Authorization': f'{self.token}', 'User-Agent': "Mozilla/5.0 (iPhone; CPU iPhone OS 11_4_1 like Mac OS X) AppleWebKit/604.3.5 (KHTML, like Gecko) Version/11.0 MQQBrowser/8.7.1 Mobile/15B87 Safari/604.1 MttCustomUA/2 QBWebViewType/1 WKType/1NULL", "Content-Type": "application/json"}
        self.session = requests.Session()
        self.dm_listeners = []
        self.onlyone = onlyone
        self.bot_id = None
        self.message_listeners = []
        self.ready_listener = None
        self.dmg_listeners = []
        self.msg_listeners = []
        self.events_listeners = []
        self.events_gatewayls = []
        self.message_m = []
        self.nuller = "⠀"
        self.letters = ['А', 'а', 'Б', 'б', 'В', 'в', 'Г', 'г', 'Д', 'д', 'Е', 'е', 'Ё', 'ё', 'Ж', 'ж', 'З', 'з', 'И', 'и', 'Й', 'й', 'К', 'к', 'Л', 'л', 'М', 'м', 'Н', 'н', 'О', 'о', 'П', 'п', 'Р', 'р', 'С', 'с', 'Т', 'т', 'У', 'у', 'Ф', 'ф', 'Х', 'х', 'Ц', 'ц', 'Ч', 'ч', 'Ш', 'ш', 'Щ', 'щ', 'Ъ', 'ъ', 'Ы', 'ы', 'Ь', 'ь', 'Э', 'э', 'Ю', 'ю', 'Я', 'я', 'A', 'a', 'B', 'b', 'C', 'c', 'D', 'd', 'E', 'e', 'F', 'f', 'G', 'g', 'H', 'h', 'I', 'i', 'J', 'j', 'K', 'k', 'L', 'l', 'M', 'm', 'N', 'n', 'O', 'o', 'P', 'p', 'Q', 'q', 'R', 'r', 'S', 's', 'T', 't', 'U', 'u', 'V', 'v', 'W', 'w', 'X', 'x', 'Y', 'y', 'Z', 'z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        self.zaglushka = True
        self.ws = websocket.WebSocketApp('wss://gateway.discord.gg/?v=9&encoding=json', on_message=self.check_message, on_error=self.on_error, on_close=self.on_close)
        self.prefix = prefix
        self.command_registry = {}

    ###USER_DATA###
    
    def change_hypesquad_status(self, hypesquad_house):
	    headers = self.headers
	    data = {
	        "house_id": hypesquad_house
	    }
	    response = requests.post("https://discord.com/api/v9/hypesquad/online", headers=headers, json=data)
	    data = {"Name": "ChangeName", "RespCode": f"{response.status_code}", "RespText": f"{response.text}"}
	    
	    if response.status_code == 204:
	        self.dispatch("on_event", data)
	    else:
	        self.dispatch("on_event", data)
    
    def change_name(password, new_display_name):
	    headers = self.headersjson
	    
	    payload = {
	        'username': new_display_name,
	        "password": password
	    }
	
	    response = self.session.patch('https://discord.com/api/v9/users/@me', json=payload, headers=headers)
	    data = {"Name": "ChangeName", "RespCode": f"{response.status_code}", "RespText": f"{response.text}"}
	
	    if response.status_code == 200:
	    	self.dispatch("on_event", data)
	    else:
	    	self.dispatch("on_event", data)
    
    ###USER_DATA###
    
    ###UTILS###
    
    def split_args(self, text, splittor='"'):
	    n = text.split(splittor)
	    for i in list(n):
	        if i == "" or i == " ":
	            n.remove(i)
	    return n
    
    def _run_mber(self, guild_id, letters, count):
        asyncio.run(self._mber(guild_id, letters, count))
    
    def member_fetcher(self, guild_id, letters=None, count=43):
        if letters is None:
        	letters = self.letters
        t = threading.Thread(target=self._run_mber, args=(guild_id, letters, count))
        t.start()
    
    def create_channel(self, guild_id, name="Discutils", type=0):
	    url = f"https://discord.com/api/guilds/{guild_id}/channels"
	    headers = self.headersjson
	    data = {
	        "name": f"{name}",
	        "type": type
	    }
	    resp = requests.post(url, headers=headers, json=data)
	    data = {"Name": "CreateChannrl", "RespCode": f"{resp.status_code}", "RespText": f"{resp.json()}"}
	    self.dispatch("on_event", data)
    
    async def _mber(self, guild_id, letters, count=43):
	    users_ids = []
	    nb = 0
	    async with websockets.connect('wss://gateway.discord.gg') as websocket:
	        payload = {
	                  "op": 8,
	                  "d": {
	                    "guild_id": guild_id,
	                    "query": "",
	                    "limit": 1000
	                  }}
	        data = {
	            "op": 2,
	            "d": {
	                "token": self.token,
	                "intents": 513,
	                "properties": {
	                        "$os": "Mac os",
	                        "$browser": "Crome",
	                        "$device": "Macbook pro"
	                    }
	            }
	        }
	        await websocket.send(json.dumps(data))
	        nn = False
	        C = True
	        
	        while C:
	                
	                response = await websocket.recv()
	                response_data = json.loads(response)
	                resp = json.loads(response)
	                if nn == True:
	                    for l in letters:
	                        payload["d"]["query"] = l
	                        await websocket.send(json.dumps(payload))
	                        while True:
	                            response = await websocket.recv()
	                            response_data = json.loads(response)
	                            resp = json.loads(response)
	                            
	                            if response_data['t'] == "GUILD_MEMBERS_CHUNK":
	                                for u in resp['d']['members']:
	                                    
	                                    if u['user']['id'] not in users_ids:
	                                        users_ids.append(u['user']['id'])	
	                                break
	                    if count >= 1:
		                    for i in range(count):
		                        q = f"{random.choice(letters)}{random.choice(letters)}"
		                        payload["d"]["query"] = q
		                        await websocket.send(json.dumps(payload))
		                        while True:
		                            response = await websocket.recv()
		                            response_data = json.loads(response)
		                            resp = json.loads(response)
		                            
		                            if response_data['t'] == "GUILD_MEMBERS_CHUNK":
		                                for u in resp['d']['members']:
		                                    
		                                    if u['user']['id'] not in users_ids:
		                                        users_ids.append(u['user']['id'])
		                                break
		                        nb += 1
	                    C = False
	                    break
	                if response_data['t'] == 'READY':
	                    nn = True
	                    continue
	                
	        data = {"Name": "MemberChunk", "RespCode": "200", "RespText": users_ids}
	        self.dispatch("on_event", data)
    
    def change_bio(self, new_bio):
	    payload = {'bio': new_bio}
	    response = self.session.patch('https://discord.com/api/v9/users/@me', json=payload, headers=self.headers)
	    data = {"Name": "ChangeBio", "RespCode": f"{response.status_code}", "RespText": f"{response.text}"}
	    self.dispatch("on_event", data)
	    return response.ok

    def get_friends(self):
	    response = self.session.get('https://discord.com/api/v9/users/@me/relationships', headers=self.headers)
	    return response.json() if response.ok else []
    
    def get_profile(self, user_id):
    	response = self.session.get(f'https://discord.com/api/v9/users/{user_id}/profile?with_mutual_guilds=true&with_mutual_fr_count=true', headers=self.headers)
    	return response.json()
    
    def get_mutualguilds(self, user_id):
    	response = self.session.get(f'https://discord.com/api/v9/users/{user_id}/profile?with_mutual_guilds=true&with_mutual_fr_count=true', headers=self.headers)
    	return response.json()['mutual_guils'] 
    
    def get_guilds(self):
    	guilds = self.session.get('https://discord.com/api/v9/users/@me/guilds', headers=self.headers).json()
    	return guilds
    
    def add_embed(self, text, embed):
    	if text is None:
    		text = " "
    	n = self.nuller
    	spaces = [i for i, char in enumerate(text) if char == ' ']
    	if not spaces:
	        text = f'[{n}]({embed}) ' + text if random.choice((True, False)) else text + f'[{n}]({embed})'
    	else:
	        space_index = random.choice(spaces)
	        text = text[:space_index] + f'[{n}]({embed})' + text[space_index + 1:]
	    
    	return text
    
    def convert(self, d):
        return namedtuple('Data', d.keys())(*d.values())
    
    def print01(self, text, speed=0.015, code=">", color="CYAN"):
    	 cc = colorama.Fore.WHITE
    	 if color == "CYAN":
    	 	cc = colorama.Fore.CYAN
    	 elif color == "GREEN":
    	 	cc = colorama.Fore.GREEN
    	 elif color == "BLUE":
    	 	cc = cc = colorama.Fore.BLUE
    	 sys.stdout.write(cc + f"{code} " + colorama.Fore.WHITE)
    	 for c in text:
	        sys.stdout.write(c)
	        sys.stdout.flush()
        	time.sleep(speed)
    	 print("")
    
    ###UTILS###
    
    ###COMMANDS###
    
    def command(self, data):
	    def decorator(func):
	        def wrapper(message, args=None):
	            return func(message, args)
	        self.command_registry[data] = wrapper
	        return wrapper
	    return decorator

    def execute_command(self, name, message, args=None):
	    if name in self.command_registry:
	        self.command_registry[name](message, args)
	    else:
	        self.print01(f"Command {name} not found")
    
    def _command(self, message):
    	comma = message['content'].split(" ")
    	s = comma[0].replace(self.prefix, "")
    	if s in str(self.command_registry):
    		for command, method in self.command_registry.items():
    			if s == str(command):
    				css = message
    				args = message['content'].replace(f"{self.prefix}{command}", "")
    				self.execute_command(s, css, args)
    
    ###COMMANDS###
    
    def call(self, channel_id, guild_id=None, second=5, mute=False, deaf=False):
        t = threading.Thread(target=self._run_call, args=(channel_id, guild_id, second, mute, deaf))
        t.start()
    
    def _run_call(self, channel_id, guild_id, second, mute, deaf):
        asyncio.run(self._call(channel_id, guild_id, second, mute, deaf))
    
    async def _call(self, channel_id, guild_id=None, second=5, mute=False, deaf=False):
        async with websockets.connect('wss://gateway.discord.gg/?v=9&encoding=json') as ws:
            auth_payload = {
                "op": 2,
                "d": {
                    "token": self.token,
                    "intents": 0,
                    "properties": {
                        "$os": "linux",
                        "$browser": "Chrome",
                        "$device": "Macbook pro"
                    }
                }
            }
            await ws.send(json.dumps(auth_payload))
            voice_state_payload = {
                "op": 4,
                "d": {
                    "guild_id": guild_id,  
                    "channel_id": channel_id,
                    "self_mute": False,
                    "self_deaf": False
                }
            }
            await ws.send(json.dumps(voice_state_payload))
            data = {"Name": "Calling", "RespCode": f"None", "RespText": f"Sendned"}
            self.dispatch("on_event", data)
            await asyncio.sleep(second)
            leave_voice_state_payload = {
                "op": 4,
                "d": {
                    "guild_id": guild_id,
                    "channel_id": None,  
                    "self_mute": False,
                    "self_deaf": False
                }
            }
            await ws.send(json.dumps(leave_voice_state_payload))
    
    def typing(self, channel_id):
        typing_endpoint = f"https://discord.com/api/v9/channels/{channel_id}/typing"
        headers = self.headersjson
        response = self.session.post(typing_endpoint, headers=headers)
        if response.status_code == 204:
            data = {"Name": "IsTyping", "RespCode": f"{response.status_code}", "RespText": f"{response.text}"}
            self.dispatch("on_event", data)
        else:
            pass
            #print(f"ошибка: {response.text}")
    
    ###MESSAGES###
    
    def add_reaction(self, channel_id, message_id, emoji):
	    url = f"https://discord.com/api/channels/{channel_id}/messages/{message_id}/reactions/{emoji}/@me"
	    headers = self.headers
	    response = self.session.put(url, headers=headers)
    
    def edit_message(self, channel_id, message_id, new_content):
	    url = f"https://discord.com/api/channels/{channel_id}/messages/{message_id}"
	    headers = self.headersjson
	    data = {
	        "content": new_content
	    }
	    response = self.session.patch(url, headers=headers, json=data)
    
    def delete_message(self, channel_id, message_id):
	    url = f"https://discord.com/api/channels/{channel_id}/messages/{message_id}"
	    headers = self.headers
	    response = self.session.delete(url, headers=headers)
    
    def send_file(self, channel_id, message=None, path_to_file=""):
        url = f"https://discord.com/api/v10/channels/{channel_id}/messages"
        headers = self.headers
        payload = {
            "content": message
        }
        files = {
            "file": open(path_to_file, 'rb')
        }
        response = requests.post(url, headers=headers, data=payload, files=files)
        print(response)
    
    def send_message(self, channel_id=None, message=None, embed=None):
        url = f"https://discord.com/api/v10/channels/{channel_id}/messages"
        if embed is None:
	        data = {"content": message}
        else:
        	data = {"content": self.add_embed(message, embed)}
        response = self.session.post(url, headers=self.headers, json=data)
    
    ###MESSAGES###
    
    ###USERS###
    def get_user(self, user_id):
        headers = self.headers
        response = requests.get(f"https://discord.com/api/v9/users/{user_id}", headers=headers)
        if response.status_code == 200:
            user_info = response.json()
            username = user_info.get('username')
            display_name = user_info.get('global_name')
            avatar_url = f"https://cdn.discordapp.com/avatars/{user_id}/{user_info.get('avatar')}.png"
            return {
                    "username": username,
                    "display_name": display_name,
                    "avatar_url": avatar_url}
        else:
            return None
    
    ###USERS###
    
    def get_guild_channels(self, guild_id):
        response = self.session.get(f'https://discord.com/api/v9/guilds/{guild_id}/channels', headers=self.headers)
        return response.json() if response.ok else []

    def get_id(self):
        return self.bot_id
    

    def get_messages(self, channel_id, limit=1):
        response = self.session.get(f'https://discord.com/api/v9/channels/{channel_id}/messages', headers=self.headers, params={'limit': limit})
        return response.json() if response.ok else []

    def login(self):
        user = self._login()
        if self.ready_listener and user:
            self.ready_listener(user)

    def _login(self):
        url = "https://discord.com/api/v9/users/@me"
        response = self.session.get(url, headers=self.headers)
        if response.ok:
            data = response.json()
            user_id = data['id']
            self.bot_id = user_id  
            username = data['username'] + '#' + data['discriminator']
            avatar_url = data['avatar']
            if avatar_url:
                avatar = f"https://cdn.discordapp.com/avatars/{user_id}/{avatar_url}.png"
            else:
                avatar = None 
            creation_date = user_id  
    
            if self.dict == True:
                return data
            else:
                return self.convert(data)
        else:
            raise Exception(f"Ошибка авторизации: {response.status_code}")

    ###READY###
    
    def ready(self, func):
        self.ready_listener = func
        return func

    ###READY###
    
    ###MSG_GATEWAY###
    
    def on_open(self, ws):
        ws.send(json.dumps({
            'op': 2,
            'd': {
                'token': f'{self.token}',
                'properties': {
                    '$os': 'linux',
                    '$browser': 'Chrome',
                    "$device": "Macbook pro"
                }
            }
        }))
    
    def glushilka(self):
        while True:
            if self.zaglushka == False:
                break
    
    def on_close(self, ws, close_status_code, close_msg):
        self.theard = False
        self.the_rm()
        pass
    
    def on_error(self, ws, error):
        print(error)
        pass
    
    def check_message(self, ws, message):
        data = json.loads(message)
        if data.get('t') == 'MESSAGE_CREATE':
            content = data['d']['content']
            if self.onlyone == True and self.prefix not in content:
            	self.dispatch('on_message', data["d"])
            elif self.prefix in content:
            	self._command(data['d'])
            elif data['d'].get('guild_id') is None and self.onlyone != True:
                self.dispatch('dm_gateway', data['d'])
            else:
                self.dispatch('message_gateway', data['d'])
        if data.get('t') != 'MESSAGE_CREATE':
            self.dispatch('on_event_gateway', data)
        if 'op' in data and data['op'] == 10:
            heartbeat_interval = data['d']['heartbeat_interval'] / 1000
            ws.send(json.dumps({
                'op': 1,
                'd': None
            }))
    
    def the_rm2(self):
        loop = asyncio.get_event_loop()
        loop.create_task(self.retrieve_message())
        loop.run_forever()
    
    def the_rm(self):
        self.theard = True
        t = threading.Thread(target=self.the_rm2())
        t.start()
        
    
    async def retrieve_message(self):
        websocket.enableTrace(False)
        ws = websocket.WebSocketApp('wss://gateway.discord.gg/?v=9&encoding=json', on_message=self.check_message, on_error=self.on_error, on_close=self.on_close)
        ws.on_open = self.on_open
        self.login()
        ws.run_forever()

    def dispatch(self, event_name, *args):
        if event_name == 'dm_gateway':
            for listener in self.dmg_listeners:
                listener(*args)
        elif event_name == 'message_gateway':
                for listener in self.msg_listeners:
                        listener(*args)
        elif event_name == 'on_event':
                for listener in self.events_listeners:
                        listener(*args)
        elif event_name == 'on_message':
                for listener in self.message_m:
                        listener(*args)
        elif event_name == 'on_event_gateway':
                for listener in self.events_gatewayls:
                        listener(*args)
                        
    def message(self, func):
        self.message_m.append(func)
        return func
    
    def on_message_gateway(self, func):
        self.msg_listeners.append(func)
        return func
    
    def on_dm_gateway(self, func):
        self.dmg_listeners.append(func)
        return func
    
    ###MSG_GATEWAY###
    
    ###EVENTS###
    
    def on_event_gateway(self, func):
        self.events_gatewayls.append(func)
        return func
    
    def on_event(self, func):
        self.events_listeners.append(func)
        return func
    
    ###EVENTS###
    
    def on_dm(self, func):
        self.dm_listeners.append(func)

    def on_message(self, func):
        self.message_listeners.append(func)

    def check_new_messages(self, channel_id, start_time, is_dm_channel):
        last_message_id = None
        while True:
            try:
                messages = self.get_messages(channel_id)
                if messages:
                    message = messages[0]
                    message_time = datetime.strptime(message['timestamp'], '%Y-%m-%dT%H:%M:%S.%f%z')
                    if message_time > start_time and (last_message_id is None or message['id'] != last_message_id):
                        last_message_id = message['id']
                        listeners = self.dm_listeners if is_dm_channel else self.message_listeners
                        for listener in listeners:
                            listener(message)
                asyncio.run(asyncio.sleep(0.01))
            except Exception as e:
                print(f"Error: {e}")
    
    def run(self):
        start_time = datetime.now(timezone.utc)
        self.the_rm()

class gateway:
    def gateway():
        print("gatet")

class embeds:
    def get_embed(provider_name="", provider_url="", author_name="", author_url="", title="", color="30C291", media_type="none", media_url="", thumbnail_url="none", description=""):
	    url = 'https://embedl.ink/api/create'
	    data = {"url":f"?deg&provider={provider_name}&providerurl={provider_url}&author={author_name}&authorurl={author_url}&title={title}&color=%23{color}&media={media_type}&mediaurl={media_url}&desc={description}","providerName":"","providerUrl":"","authorName":"","authorUrl":"","title":title,"mediaType":"none","mediaUrl":"","mediaThumb":"none","description":description}
	    response = requests.post(url, json=data)
	    if response.status_code == 200:
	        embed_url = response.json()
	        return f"https://embedl.ink/e/{embed_url['code']}"
	    else:
	        print(response.text)
	        return None 