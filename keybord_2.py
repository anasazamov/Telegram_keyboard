import requests
TOKEN="6058623152:AAGROkpnAa7tK6gXhGiE_F-DpMqqFuxK8ns"
BASE_URL='https://api.telegram.org/bot{}/'.format(TOKEN)
def Replay_Keyboard(chat_id,text):
    
    btn1={"text":"🏣 Catalog"}
    btn2={"text":"📦 Orders"}
    btn3={"text":"👤 User Info"}
    btn4={"text":"🛒 Cart"}
    btn5={"text":"🎛 Administration demo"}
    
    
    ReplayKeyboard={'keyboard':[[btn1, btn2],[btn3, btn4],[btn5]]}
    
    payload={"chat_id":chat_id,
              "text":text,
              "reply_markup":ReplayKeyboard}
    
    return requests.post(BASE_URL+"sendMessage",json=payload).json()


print(Replay_Keyboard(1698951222,"ok"))
