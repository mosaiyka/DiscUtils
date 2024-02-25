## DiscordUtils
[![DiscUtils  - 1.8.0](https://img.shields.io/badge/DiscUtils_-1.8.0-2ea44f)](https://)


![](/data/DiscUtils.png "")

### О библиотеке

 **DiscordUtils - библиотека является полным переосмыслением Discum, discord.py-self без лишнего функционала, более легкая**

### Функциональность:

* Не асинхронная библиотека
* Поддержка embeds
* Легкий gateway
* ~~Поддержка обхода капч~~


### Быстрый старт

```python
from DiscUtils import embeds, client

bot = client("TOKEN", prefix="!", onlyone=True)

@bot.ready
def ready(data):
	print(f"Logged in as: {data.username}")

@bot.command("oldping")
def oldping(m, args=None):
	bot.send_message(m['channel_id'], "pong!")

@bot.command("ping")
def ping(m, args=None):
	embed = embeds.get_embed(provider_name="Pong", description="PONG", color="2A8B55")
	bot.send_message(m['channel_id'], embed=embed)

@bot.message
def message(m):
	print(f"{m['author']['username']} > {m['content']}")
	
bot.run()
```

### Подробнее
[вся документация тута](docs/readme.md)

### ⚠️ Отказ от ответственности ⚠️
  Пользовательские боты нарушают условия использования Discord
  Библиотека создана лишь для демонстрации того, что пользовательские боты возможны