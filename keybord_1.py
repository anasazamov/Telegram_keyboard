import requests
TOKEN="6058623152:AAGROkpnAa7tK6gXhGiE_F-DpMqqFuxK8ns"
BASE_URL='https://api.telegram.org/bot{}/'.format(TOKEN)
def Replay_Keyboard(chat_id,text):
    
    btn1={"text":"👫 Play With Friends"}
    btn2={"text":"🔥 Trending Games"}
    btn3={"text":"🕔 Last Played Games"}
    btn4={"text":"🎮 Catigories"}
    btn5={"text":"🚀 Join GAMEE Token Chanel"}
    btn6={"text":"💰 Get App & Win Cash"}
    
    ReplayKeyboard={'keyboard':[[btn1, btn2],[btn3, btn4],[btn5, btn6]]}
    
    payload={"chat_id":chat_id,
              "text":text,
              "reply_markup":ReplayKeyboard}
    
    return requests.post(BASE_URL+"sendMessage",json=payload).json()


print(Replay_Keyboard(1698951222,"ok"))
