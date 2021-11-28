from pypresence import Presence

from time import time

RPC = Presence("914587711522897963")

btns = [

	{		"label": "YouTube",

		"url": "https://youtube.com/channel/UCsjPhdUbdSDOkEbmm4wiY0w"

	},

	{

		"label": "GitHub",

		"url": "https://github.com/KrikerGaming"

	}

]

RPC.connect()

RPC.update(

	state="Мне 14 лет, изучаю NodeJs & Python",

	details="Меня зовут Дима",

	start=time(),

	buttons=btns,

	large_image="new",

	small_image="old",

        large_text="Geometry Dash icon",

	small_text="Old ава"

)

input()  
