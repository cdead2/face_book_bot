import subprocess
try:
    import fbchat
    from fbchat.models import *
except:
    subprocess.check_output('pip install --upgrade pip')
    subprocess.check_output('pip install fbchat')
    import fbchat
    from fbchat.models import *

def login():
    user = input('username : ')
    passs = input('your password : ')
    login = fbchat.Client(user, passs)
    if not login.isLoggedIn():
        login = fbchat.Client(user, passs)

    frind_name = input(" اسم الضحيه على الفيسبوك")
    frind_id = input('اي بي الضحية')
    msg=input('الرساله >')
    search = login.searchForUsers(frind_name)
    frinds = search[0]
    uid = frinds.uid
    num_of_msg=int(input('عدد الرسأل التي تريد ارسالها? : '))
    i=0
    while i<num_of_msg:

        login.send(Message(text=msg), thread_id=frind_id,thread_type=ThreadType.USER)
        i+=1
    print('sent successfully')
login()
