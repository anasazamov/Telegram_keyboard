import requests
TOKEN="6058623152:AAGROkpnAa7tK6gXhGiE_F-DpMqqFuxK8ns"
BASE_URL='https://api.telegram.org/bot{}/'.format(TOKEN)
def Replay_Keyboard(chat_id,text):
    
    btn1={"text":"👑 Pro"}
    btn2={"text":"🤓 Mashqlar"}
    btn3={"text":"📚 So'zlar"}
    btn4={"text":"📊 Reyting"}
    btn5={"text":"⚔️ Bellashuv"}
    btn6={"text":"❓ Qo'llanma"}
    btn7={"text":"⚙️ Sozlanmalar"}
    
    ReplayKeyboard={'keyboard':[[btn1],[btn2, btn3, btn4],[btn5, btn6],[btn7]]}
    
    payload={"chat_id":chat_id,
              "text":text,
              "reply_markup":ReplayKeyboard}
    
    return requests.post(BASE_URL+"sendMessage",json=payload).json()


print(Replay_Keyboard(1698951222,"ok"))
