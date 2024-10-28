import asyncio
import datetime
import logging
import os
import re
import sys

from asyncio import sleep
from random import choice
from pyrogram import Client, filters
from pyrogram.types import Message
from pytgcalls import StreamType

from BADMUSIC.utils.queues import QUEUE, add_to_queue, get_queue, clear_queue
from BADMUSIC.misc import SUDOERS as SUDO_USER


logging.basicConfig(level=logging.INFO)

aud_list = [
    "./BADMUSIC/audio/AUDIO1",
    "./BADMUSIC/audio/AUDIO2",
    "./BADMUSIC/audio/AUDIO3",
    "./BADMUSIC/audio/AUDIO4",
    "./BADMUSIC/audio/AUDIO5",
    "./BADMUSIC/audio/AUDIO6",
    "./BADMUSIC/audio/AUDIO7",
    "./BADMUSIC/audio/AUDIO8",
]



@Client.on_message(filters.command("vcraid", prefixes=".") & SUDO_USER)
async def vcraid(_, e: Message):
    gid = e.chat.id
    uid = e.from_user.id
    inp = e.text.split(None, 2)[1]
    chat = await Client.get_chat(inp)
    chat_id = chat.id
    aud = choice(aud_list) 

    if inp:
        Client = await e.reply_text("**Starting Raid**")
        link = f"https://zaid-robot.github.io/{aud[1:]}"
        dl = aud
        songname = aud[18:]
        if chat_id in QUEUE:
            pos = add_to_queue(chat_id, songname, dl, link, "Audio", 0)
            await Client.delete()
            await e.reply_text(f"**> Raiding in:** {chat.title} \n\n**> Audio:** {songname} \n**> Position:** #{pos}")
        else:
            if Client:
                await Client.join_group_call(chat_id, AudioPiped(dl), stream_type=StreamType().pulse_stream)
            if Client:
                await Client.join_group_call(chat_id, AudioPiped(dl), stream_type=StreamType().pulse_stream)
            if Client:
                await Client.join_group_call(chat_id, AudioPiped(dl), stream_type=StreamType().pulse_stream)
            if Client:
                await Client.join_group_call(chat_id, AudioPiped(dl), stream_type=StreamType().pulse_stream)
            if Client:
                await Client.join_group_call(chat_id, AudioPiped(dl), stream_type=StreamType().pulse_stream)
            add_to_queue(chat_id, songname, dl, link, "Audio", 0)
            await Client.delete()
            await e.reply_text(f"**> Raiding in:** {chat.title} \n\n**> Audio:** {songname} \n**> Position:** Ongoing Raid")


@Client.on_message(filters.command("vraid", prefixes=".") & SUDO_USER)
async def vraid(_, e: Message):
    gid = e.chat.id
    uid = e.from_user.id
    replied = e.reply_to_message
    inp = e.text.split(None, 2)[1]
    chat = await Client.get_chat(inp)
    chat_id = chat.id
    aud = choice(aud_list) 
    if replied:
        if replied.video or replied.document:
            suhu = await replied.reply("📥 **Downloading Your Replied File...**")
            dl = await replied.download()
    if inp:
        Client = await e.reply_text("**Starting Raid**")
        link = f"https://zaid-robot.github.io/{aud[1:]}"
        songname = aud[18:]
        if chat_id in QUEUE:
            pos = add_to_queue(chat_id, songname, dl, link, "Audio", 0)
            await Client.delete()
            await e.reply_text(f"**> Raiding in:** {chat.title} \n\n**> Audio:** {songname} \n**> Position:** #{pos}")
        else:
            if Client:
               await Client.join_group_call(chat_id, AudioVideoPiped(dl), stream_type=StreamType().pulse_stream)
            if Client:
               await Client.join_group_call(chat_id, AudioVideoPiped(dl), stream_type=StreamType().pulse_stream)
            if Client:
               await Client.join_group_call(chat_id, AudioVideoPiped(dl), stream_type=StreamType().pulse_stream)
            if Client:
               await Client.join_group_call(chat_id, AudioVideoPiped(dl), stream_type=StreamType().pulse_stream)
            if Client:
               await Client.join_group_call(chat_id, AudioVideoPiped(dl), stream_type=StreamType().pulse_stream)
            add_to_queue(chat_id, songname, dl, link, "Audio", 0)
            await Client.delete()
            await e.reply_text(f"**> Raiding in:** {chat.title} \n\n**> Video:** {songname} \n**> Position:** Ongoing Raid")


@Client.on_message(filters.command("raidend", prefixes=".") & SUDO_USER)
async def ping(_, e: Message):
    gid = e.chat.id
    uid = e.from_user.id
    if gid == uid:
        inp = e.text.split(None, 2)[1]
        chat_ = await Client.get_chat(inp)
        chat_id = chat_.id
    else:
         chat_id = gid
    if chat_id in QUEUE:
        try:
            if Client:
                await Client.leave_group_call(chat_id)
            if Client:
                await Client.leave_group_call(chat_id)
            if Client:
                await Client.leave_group_call(chat_id)
            if Client:
                await Client.leave_group_call(chat_id)
            if Client:
                await Client.leave_group_call(chat_id)
            await e.reply_text("**VC Raid Ended!**")
        except Exception as ex:
            await e.reply_text(f"**ERROR** \n`{ex}`")
    else:
        await e.reply_text("**No ongoing raid!**")



@Client.on_message(filters.command("raidpause", prefixes=".") & SUDO_USER)
async def ping(_, e: Message):
    gid = e.chat.id
    uid = e.from_user.id
    if gid == uid:
        inp = e.text.split(None, 2)[1]
        chat_ = await Client.get_chat(inp)
        chat_id = chat_.id
    else:
         chat_id = gid
    if chat_id in QUEUE:
        try:
            if Client:
                await Client.pause_stream(chat_id)
            if Client:
                await Client.pause_stream(chat_id)
            if Client:
                await Client.pause_stream(chat_id)
            if Client:
                await Client.pause_stream(chat_id)
            if Client:
                await Client.pause_stream(chat_id)
            await e.reply_text(f"**VC Raid Paued In:** {chat_.title}")
        except Exception as e:
            await e.reply_text(f"**ERROR** \n`{e}`")
    else:
        await e.reply_text("**No ongoing raid!**")


@Client.on_message(filters.command("raidrausme", prefixes=".") & SUDO_USER)
async def ping(_, e: Message):
    gid = e.chat.id
    uid = e.from_user.id
    if gid == uid:
        inp = e.text.split(None, 2)[1]
        chat_ = await Client.get_chat(inp)
        chat_id = chat_.id
    else:
         chat_id = gid
    if chat_id in QUEUE:
        try:
            if Client:
                await Client.resume_stream(chat_id)
            if Client:
                await Client.resume_stream(chat_id)
            if Client:
                await Client.resume_stream(chat_id)
            if Client:
                await Client.resume_stream(chat_id)
            if Client:
                await Client.resume_stream(chat_id)
            await e.reply_text(f"**VC Raid Resumed In {chat_.title}**")
        except Exception as e:
            await e.reply_text(f"**ERROR** \n`{e}`")
    else:
        await e.reply_text("**No raid is currently paused!**")
        
