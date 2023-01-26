# Rexa!


import os
import random
from telethon.tl.types import InputMessagesFilterPhotos
from telethon.tl.types import InputMessagesFilterVideo
from Hikari.events import register
from Hikari import telethn as tbot, ubot2                 


@register(pattern="^/asupan ?(.*)")
async def _(event):
    memeks = await event.reply("**Mencari Video Asupan...🔍**") 
    try:
        asupannya = [
            asupan
            async for asupan in ubot2.iter_messages(
            "@Database_TonicUbot", filter=InputMessagesFilterVideo
            )
        ]
        kontols = random.choice(asupannya)
        pantek = await ubot2.download_media(kontols)
        await tbot.send_file(
            event.chat.id, 
            caption="Nih Asupan nya Kak 🥵", 
            file=pantek
            )
        await memeks.delete()
    except Exception:
        await memeks.edit("Asupannya gaada komsol")  


@register(pattern="^/ppanime ?(.*)")
async def _(event):
    memeks = await event.reply("**Mencari PP Anime...🔍**") 
    try:
        asupannya = [
            asupan
            async for asupan in ubot2.iter_messages(
            "@animehikarixa", filter=InputMessagesFilterPhotos
            )
        ]
        kontols = random.choice(asupannya)
        pantek = await ubot2.download_media(kontols)
        await tbot.send_file(
            event.chat.id, 
            caption="Nih pp animenya ", 
            file=pantek
            )
        await memeks.delete()
    except Exception:
        await memeks.edit("PP animenya ga ada ")
        
        
@register(pattern="^/ppcp ?(.*)")
async def _(event):
    memeks = await event.reply("**Mencari PPCP...🔍**") 
    try:
        asupannya = [
            asupan
            async for asupan in ubot2.iter_messages(
            "@ppcpcilik", filter=InputMessagesFilterPhotos
            )
        ]
        kontols = random.choice(asupannya)
        pantek = await ubot2.download_media(kontols)
        await tbot.send_file(
            event.chat.id, 
            caption="Nih ppcp ", 
            file=pantek
            )
        await memeks.delete()
    except Exception:
        await memeks.edit("PP ga ada ")  
        
        
@register(pattern="^/ayang ?(.*)")
async def _(event):
    memeks = await event.reply("**Mencari Ayang...🔍**") 
    try:
        asupannya = [
            asupan
            async for asupan in ubot2.iter_messages(
            "@CeweLogoPack", filter=InputMessagesFilterPhotos
            )
        ]
        kontols = random.choice(asupannya)
        pantek = await ubot2.download_media(kontols)
        await tbot.send_file(
            event.chat.id, 
            caption="Nih ayang siapa ?", 
            file=pantek
            )
        await memeks.delete()
    except Exception:
        await memeks.edit("Ayang nya ga ada ")  


@register(pattern="^/wallanime ?(.*)")
async def _(event):
    memeks = await event.reply("**Mencari Wallpaper Anime...🔍**") 
    try:
        asupannya = [
            asupan
            async for asupan in ubot2.iter_messages(
            "@Anime_WallpapersHD", filter=InputMessagesFilterPhotos
            )
        ]
        kontols = random.choice(asupannya)
        pantek = await ubot2.download_media(kontols)
        await tbot.send_file(
            event.chat.id, 
            caption="Nih Wallpaper Animenya ", 
            file=pantek
            )
        await memeks.delete()
    except Exception:
        await memeks.edit("Wallpaper Animenya Kosong ")  
        
        
@register(pattern="^/bokep ?(.*)")
async def _(event):
    memeks = await event.reply("**Mencari Bokep...🔍**") 
    try:
        asupannya = [
            asupan
            async for asupan in ubot2.iter_messages(
            "@bahaninimah", filter=InputMessagesFilterPhotos
            )
        ]
        kontols = random.choice(asupannya)
        pantek = await ubot2.download_media(kontols)
        await tbot.send_file(
            event.chat.id, 
            caption="Nih Buat Coli ", 
            file=pantek
            )
        await memeks.delete()
    except Exception:
        await memeks.edit("Coli Mulu Lu ")  






















  




