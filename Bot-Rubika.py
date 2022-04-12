#coded by Mr.Exploit (ramtin Exploit)
from requests import get
from re import findall
from rubika import Bot
import time

bot = Bot("vdvzxeqtuwjkjabjzboocllzqwprajqb")
target = "g0B53KC0a46f892aac8e8337a25f95b2"
answered = [bot.getGroupAdmins]
retries = {}
sleeped = False
# delmess = ["دولی","کصکش","کون","کص","کیر" ,"خر","کستی","دول","گو","کس","کسکش","کوبص"]
plus= True

while True:
	try:
		admins = [i["member_guid"] for i in bot.getGroupAdmins(target)["data"]["in_chat_members"]]
		min_id = bot.getGroupInfo(target)["data"]["chat"]["last_message_id"]
		while True:
			try:
				messages = bot.getMessages(target,min_id)
				break
			except:
				continue
		
		open("id.db","w").write(str(messages[-1].get("message_id")))

		for msg in messages:
			if msg["type"]=="Text" and not msg.get("message_id") in answered:
				if not sleeped:
					if msg.get("text") == "/bot" and msg.get("author_object_guid") in admins :
						bot.sendMessage(target, "The bot is now active", message_id=msg.get("message_id"))

					if msg.get("text") == "/بات" and msg.get("author_object_guid") in admins :
						bot.sendMessage(target, "ربات در حال اضر فعال است", message_id=msg.get("message_id"))

					elif msg.get("text").startswith("!add") :
						bot.invite(target, [bot.getInfoByUsername(msg.get("text").split(" ")[1][1:])["data"]["chat"]["object_guid"]])
						bot.sendMessage(target, "کاربر به گپ اضافه شد ✅", message_id=msg.get("message_id"))

					elif msg.get("text") == "!info":
						bot.sendMessage(target, "لــیــست دســتــورات سـیــد پـوکــر هـوشــمـنـد 🤖:\n\n●🤖 !bot : فعال یا غیر فعال بودن بات\n\n●❎ !stop : غیر فعال سازی بات\n\n●✅ !start : فعال سازی بات\n\n●🕘 !time : ساعت\n\n●📅 !date : تاریخ\n\n●📋 !del : حذف پیام با ریپ بر روی ان\n\n●🔒 !lock : بستن چت در گروه\n\n●🔓 !unlock : باز کردن چت در گروه\n\n●❌ !ban : حذف کاربر با ریپ زدن\n\n●✉ !send : ارسال پیام با استفاده از ایدی\n\n●📌 !add : افزودن کاربر به گپ با ایدی\n\n●📜 !info : لیست دستورات ربات\n\n●🆑 !cal :ماشین حساب\n\n●🔴 !user : اطلاعات کاربر با ایدی\n\n●😂 !jok : ارسال جک\n\n●🔵 !font : ارسال فونت\n\n●🔴 !ping : گرفتن پینگ سایت\n\n●🔵 !tran : مترجم انگلیسی")
					elif msg.get("text").startswith("!cal"):
						msd = msg.get("text")
						if plus == True:
							try:
								call = [msd.split(" ")[1], msd.split(" ")[2], msd.split(" ")[3]]
								if call[1] == "+":
									am = float(call[0]) + float(call[2])
									bot.sendMessage(target, "حاصل :\n"+"".join(str(am)), message_id=msg.get("message_id"))
									plus = False
							
								elif call[1] == "-":
									am = float(call[0]) - float(call[2])
									bot.sendMessage(target, "حاصل :\n"+"".join(str(am)), message_id=msg.get("message_id"))
							
								elif call[1] == "*":
									am = float(call[0]) * float(call[2])
									bot.sendMessage(target, "حاصل :\n"+"".join(str(am)), message_id=msg.get("message_id"))
							
								elif call[1] == "/":
									am = float(call[0]) / float(call[2])
									bot.sendMessage(target, "حاصل :\n"+"".join(str(am)), message_id=msg.get("message_id"))
							except IndexError:
								bot.sendMessage(target, "لطفا دستور را به طور صحیح وارد کنید ❌" ,message_id=msg.get("message_id"))
						plus= True
					elif msg.get("text").startswith("!send") :
						bot.sendMessage(bot.getInfoByUsername(msg.get("text").split(" ")[1][1:])["data"]["chat"]["object_guid"], "شما یک پیام ناشناس دارید:\n"+" ".join(msg.get("text").split(" ")[2:]))
						bot.sendMessage(target, "پیام ارسال شد ✅", message_id=msg.get("message_id"))

					elif msg.get("text") == "سلام":
						bot.sendMessage(target, "سلام سید🗿👋", message_id=msg.get("message_id"))

					if  msg.get("text").startswith('!user @'):
						try:
							user_info = bot.getInfoByUsername( msg.get("text")[7:])
							if user_info['data']['exist'] == True:
								if user_info['data']['type'] == 'User':
									bot.sendMessage(target, 'Name User:\n ' + user_info['data']['user']['first_name'] + ' ' + user_info['data']['user']['last_name'] + '\n\nBio User:\n ' + user_info['data']['user']['bio'] + '\n\nGuid:\n ' + user_info['data']['user']['user_guid'] ,  msg.get('message_id'))
									print('sended response')
								else:
									bot.sendMessage(target, 'کانال است ❌' ,  msg.get('message_id'))
									print('sended response')
							else:
								bot.sendMessage(target, "کاربری وجود ندارد ❌" ,  msg.get('message_id'))
								print('sended response')
						except:
							print('server bug6')
							bot.sendMessage(target, "خطا در اجرای دستور مجددا سعی کنید ❌" ,message_id=msg.get("message_id"))
							

					elif msg.get("text") == "خاموش" and msg.get("author_object_guid") in admins :
						sleeped = True
						bot.sendMessage(target, "سید پوکر هوشمند خاموش شد🗿✅", message_id=msg.get("message_id"))

					elif msg.get("text").startswith("!ping"):
						
						try:
							responser = get(f"https://api.codebazan.ir/ping/?url={msg.get('text').split()[1]}").text
							bot.sendMessage(target, responser,message_id=msg["message_id"])
						except:
							bot.sendMessage(target, "دادا متاسفانه نت ندارم 😑", message_id=msg["message_id"])

					elif msg.get("text").startswith("!tran"):
						
						try:
							responser = get(f"https://api.codebazan.ir/translate/?type=json&from=en&to=fa&text={msg.get('text').split()[1:]}").json()
							al = [responser["result"]]
							bot.sendMessage(msg.get("author_object_guid"), "پاسخ به ترجمه:\n"+"".join(al)).text
							bot.sendMessage(target, " نتیجه به پیویتون ارسال شد😐", message_id=msg["message_id"])
						except:
							bot.sendMessage(target, "دادا متاسفانه نت ندارم 😑", message_id=msg["message_id"])

					elif msg.get("text").startswith("!font"):
						#print("\n".join(list(response["result"].values())))
						try:
							response = get(f"https://api.codebazan.ir/font/?text={msg.get('text').split()[1]}").json()
							bot.sendMessage(msg.get("author_object_guid"), "\n".join(list(response["result"].values())[:110])).text
							bot.sendMessage(target, "نتیجه به پیوی شما ارسال شد ✅", message_id=msg["message_id"])
						except:
							bot.sendMessage(target, "دادا متاسفانه نت ندارم 😑", message_id=msg["message_id"])
									
							
					elif msg.get("text") == "خب" and msg.get("author_object_guid") :
												bot.sendMessage(target, "خب که خب😐", message_id=msg.get("message_id"))
							
					elif msg.get("text") == "دک" and msg.get("author_object_guid") :
												bot.sendMessage(target, "اگه به ننت نگفتم یه آشی برات نپختم🗿", message_id=msg.get("message_id"))
							
					elif msg.get("text") == "😐😂" and msg.get("author_object_guid") :
												bot.sendMessage(target, "چرا میخندی سید؟", message_id=msg.get("message_id"))
							
					elif msg.get("text") == "مسابقه محله" and msg.get("author_object_guid") :
												bot.sendMessage(target, "یکو یکو یک دو دو دو سه سه سه حالا بازی شادی شیرین تر قنده 😐", message_id=msg.get("message_id"))
							
					elif msg.get("text") == "بای" and msg.get("author_object_guid") :
												bot.sendMessage(target, "بچه شیعه بای نمیدع میگه یا علی😟💔", message_id=msg.get("message_id"))
							
					
							
					elif msg.get("text") == "باشه" and msg.get("author_object_guid") :
												bot.sendMessage(target, " اوه🗿", message_id=msg.get("message_id"))
							
					elif msg.get("text") == "🗿" and msg.get("author_object_guid") :
												bot.sendMessage(target, " چه شاخی🗿", message_id=msg.get("message_id"))

					elif msg.get("text") == "عجب" and msg.get("author_object_guid") :
												bot.sendMessage(target, " مش رجب 🌚", message_id=msg.get("message_id"))
							
					elif msg.get("text") == "رایتل" and msg.get("author_object_guid") :
												bot.sendMessage(target, " یک روز مهمون ما باشید رایتل پر سرعت🗿💔", message_id=msg.get("message_id"))
							
					elif msg.get("text") == "ایرانسل" and msg.get("author_object_guid") :
												bot.sendMessage(target, "  ایرانسل پیشرو در کسب رضایت مشتری🗿", message_id=msg.get("message_id"))
							
					elif msg.get("text") == "همراه اول" and msg.get("author_object_guid") :
												bot.sendMessage(target, "  هیچکس تنها نیست همراه اول😐", message_id=msg.get("message_id"))
							
					elif msg.get("text") == "دیدن خری مثل تو صفا داره🗿" and msg.get("author_object_guid") :
												bot.sendMessage(target, "  گوه نخور سید😟", message_id=msg.get("message_id"))
							
					elif msg.get("text") == "خوبم" and msg.get("author_object_guid") :
												bot.sendMessage(target, "  شکر😐", message_id=msg.get("message_id"))
							
					elif msg.get("text") == "علیرضا" and msg.get("author_object_guid") :
												bot.sendMessage(target, "  یک بچه سال 🗿", message_id=msg.get("message_id"))
							
					elif msg.get("text") == "رامتین" and msg.get("author_object_guid") :
												bot.sendMessage(target, "  سازندم بمولا", message_id=msg.get("message_id"))
																
							
					elif msg.get("text") == "😐" and msg.get("author_object_guid") :
												bot.sendMessage(target, "    چیه نگاه داره😐", message_id=msg.get("message_id"))
							
					elif msg.get("text") == "سید" and msg.get("author_object_guid") :
												bot.sendMessage(target, "    جانم😐", message_id=msg.get("message_id"))
							
					elif msg.get("text") == "نشنیدم" and msg.get("author_object_guid") :
												bot.sendMessage(target, "    چون کری🗿", message_id=msg.get("message_id"))
							
					elif msg.get("text") == "ندیدم" and msg.get("author_object_guid") :
												bot.sendMessage(target, "    چون کوری🗿", message_id=msg.get("message_id"))
							
					elif msg.get("text") == "ربات" and msg.get("author_object_guid") :
												bot.sendMessage(target, "  بله؟😐", message_id=msg.get("message_id"))
							
					elif msg.get("text") == "بکیرم" and msg.get("author_object_guid") :
												bot.sendMessage(target, "  بکیرم که بکیرت🗿", message_id=msg.get("message_id"))
							
					elif msg.get("text") == "نخوندم" and msg.get("author_object_guid") :
												bot.sendMessage(target, "  چون سواد نداری🗿", message_id=msg.get("message_id"))
							
					elif msg.get("text") == "هری" and msg.get("author_object_guid") :
												bot.sendMessage(target, "  رئیسم😐", message_id=msg.get("message_id"))
							
					elif msg.get("text") == "امیر" and msg.get("author_object_guid") :
												bot.sendMessage(target, "  یک اسگل🗿🤝", message_id=msg.get("message_id"))
							
					elif msg.get("text") == "خوبی دادا" and msg.get("author_object_guid") :
												bot.sendMessage(target, "  اره سید تو خوبی؟🤙", message_id=msg.get("message_id"))


					elif msg.get("text").startswith("!jok"):
						
						try:
							response = get("https://api.codebazan.ir/jok/").text
							bot.sendMessage(target, response,message_id=msg.get("message_id"))
						except:
							bot.sendMessage(target, "دادا متاسفانه نت ندارم😑", message_id=msg["message_id"])

					elif msg.get("text") == "ساعت":
						bot.sendMessage(target, f"Time : {time.localtime().tm_hour} : {time.localtime().tm_min} : {time.localtime().tm_sec}", message_id=msg.get("message_id"))

					elif msg.get("text") == "تاریخ":
						bot.sendMessage(target, f"Date: {time.localtime().tm_year} / {time.localtime().tm_mon} / {time.localtime().tm_mday}", message_id=msg.get("message_id"))

					elif msg.get("text") == "!del" and msg.get("author_object_guid") in admins :
						bot.deleteMessages(target, [msg.get("reply_to_message_id")])
						bot.sendMessage(target, "پیام با موفقیت حذف شد🗿✅", message_id=msg.get("message_id"))

					# elif msg.get("text").split(" ")[0] in  delmess:
					# 	bot.deleteMessages(target, [msg.get("message_id")])
					# 	bot.sendMessage(target, "یک پیام مستهجن پاک شد ✅", message_id=msg.get("message_id"))


					elif msg.get("text") == "!lock" and msg.get("author_object_guid") in admins :
						print(bot.setMembersAccess(target, ["ViewMembers","ViewAdmins","AddMember"]).text)
						bot.sendMessage(target, "گپ با موفقیت بسته شد🗿✅", message_id=msg.get("message_id"))

					elif msg.get("text") == "!unlock" and msg.get("author_object_guid") in admins :
						bot.setMembersAccess(target, ["ViewMembers","ViewAdmins","SendMessages","AddMember"])
						bot.sendMessage(target, "گپ با موفقیت باز شد🗿✅", message_id=msg.get("message_id"))

					elif msg.get("text").startswith("!ban") and msg.get("author_object_guid") in admins :
						try:
							guid = bot.getInfoByUsername(msg.get("text").split(" ")[1][1:])["data"]["chat"]["abs_object"]["object_guid"]
							user = bot.getUserInfo(data['peer_objects'][0]['object_guid'])["data"]["user"]["first_name"]
							if not guid in admins :
								bot.banGroupMember(target, guid)
								bot.sendMessage(target, f"دلقک بای بده🗿👋", message_id=msg.get("message_id"))
							else :
								bot.sendMessage(target, f"لعنتی ادمینی😑🖕", message_id=msg.get("message_id"))
								
						except IndexError:
							a = bot.getMessagesInfo(target, [msg.get("reply_to_message_id")])[0]["author_object_guid"]
							if a in admins:
								bot.sendMessage(target, f"ادمینه داداش گلم🗿💔", message_id=msg.get("message_id"))
							else:
								bot.banGroupMember(target, bot.getMessagesInfo(target, [msg.get("reply_to_message_id")])[0]["author_object_guid"])
								bot.sendMessage(target, f"کاربر حذف شد ✅", message_id=msg.get("message_id"))

				else:
					if msg.get("text") == "روشن" and msg.get("author_object_guid") in admins :
						sleeped = False
						bot.sendMessage(target, "سید پوکر هوشمند روشن شد🗿✅", message_id=msg.get("message_id"))

			elif msg["type"]=="Event" and not msg.get("message_id") in answered and not sleeped:
				name = bot.getGroupInfo(target)["data"]["group"]["group_title"]
				data = msg['event_data']
				if data["type"]=="RemoveGroupMembers":
					user = bot.getUserInfo(data['peer_objects'][0]['object_guid'])["data"]["user"]["first_name"]
					bot.sendMessage(target, f"کاربر {user} سیک😐🖕", message_id=msg["message_id"])
				
				elif data["type"]=="AddedGroupMembers":
					user = bot.getUserInfo(data['peer_objects'][0]['object_guid'])["data"]["user"]["first_name"]
					bot.sendMessage(target, f"سلام {user} عزیز به گروه {name} خوش اومدی😐🖕", message_id=msg["message_id"])
				
				elif data["type"]=="LeaveGroup":
					user = bot.getUserInfo(data['performer_object']['object_guid'])["data"]["user"]["first_name"]
					bot.sendMessage(target, f"کاربر {user} بکیرم که لف دادی😐🤝", message_id=msg["message_id"])
					
				elif data["type"]=="JoinedGroupByLink":
					user = bot.getUserInfo(data['performer_object']['object_guid'])["data"]["user"]["first_name"]
					bot.sendMessage(target, f"سلام {user} عزیز به گروه {name} خوش اومدی😐🖕", message_id=msg["message_id"])

			answered.append(msg.get("message_id"))

	except KeyboardInterrupt:
		exit()

	except Exception as e:
		if type(e) in list(retries.keys()):
			if retries[type(e)] < 3:
				retries[type(e)] += 1
				continue
			else:
				retries.pop(type(e))
		else:
			retries[type(e)] = 1
			continue