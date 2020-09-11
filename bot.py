import requests


base_url = 'https://sjprojectsapi.herokuapp.com/torrent/?query='


async def magnet_link_s(client, message):
    search = message.text
    print(search)
    search = search.split(' ')
    if len(search) > 1:
        search.remove('/Magnet')
        def listToString(s):  
    
    # initialize an empty string 
            str1 = ""  
    
    # traverse in the string   
            for ele in s:  
                str1 += " "+ele   
    
    # return string   
            return str1
        link = (listToString(search))
        await message.reply_text("Searching Magnet..."+link, quote=True)
        r = requests.get(base_url+link).json()
        num = 0
        while num < 10:
            name = r[num]['name']
            size = r[num]['size']
            magnet = r[num]['magnet']
            await client.send_message(
                                      chat_id=update.chat.id,
                                      text="""{}
                                              {}
                                              <a href={}>Magnet</a>""".format(name,size,magnet),
                                      reply_to_message_id=update.message_id,
                                      parse_mode="html",
                                      disable_web_page_preview=True
                                      )
            num+=1
    else:
        pass