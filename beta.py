import simplejson as json
import requests

def return_list(url):
    r = requests.get(url)
    jsondata=json.loads(r.text)
    if 'data' not in jsondata:
        print(' Facebook is giving some Authentication Error')
        exit()
    h=jsondata['data']
    ind=0
    i1=0
    for j in h :
        if(len(j['to']['data'])!=2):
            i1+=1
            continue
        elif(len(j['to']['data'])==2):
            name=j['to']['data'][0]['name']+" and "+j['to']['data'][1]['name']
        #elif(len(j['to']['data'])==1):
            #name=j['to']['data'][0]['name']+" and Facebook User"
        else:
            name="Some unexpected error has occured"
        print(i1," for ",name)
        i1+=1
    print('enter the index of chat you want to read 1~22\nEnter 25 for next\n')
    ind=input()
    ind=int(ind)
    return ind;




def get_text_json(url,user_index):
    text2 = ""

    i=0
    while True:
        r = requests.get(url)
        jsondata = json.loads(r.text)
        if 'data' not in jsondata:
            print(' Facebook is giving some error while communicating with the server')
            break

        text=""

        if i==0:
            if 'id' not in jsondata['data'][user_index]:
                break
            url=jsondata['data'][user_index]['comments']['paging']['next']
            h=jsondata['data'][user_index]['comments']['data']
            for j in h :


                if 'message' in j:

                    text+=j['from']['name']+"-:"+j['message']+'\n'


                else:
                    text+=j['from']['name']+"- Sticker"+'\n'


        else:
            if 'paging' not in jsondata:
                break
            url=jsondata['paging']['next']
            h=jsondata['data']

            for j in h :
                if 'message' in j:
                    text+=j['from']['name']+"-:"+j['message']+'\n'

                else:
                    text+=j['from']['name']+"- Sticker"+'\n'

        #text+='\n*********BREAK***************'
        text2=text+text2
        i=i+1

    return text2;



def get_text_json2(url,user_index):
    text2 = ""

    i=0
    while True:
        r = requests.get(url)
        jsondata = json.loads(r.text)
        if 'data' not in jsondata:
            print(' Facebook is giving some error while communicating with the server')
            break

        text=""

        if i==0:
            if 'id' not in jsondata['data'][user_index]:
                break
            url=jsondata['data'][user_index]['comments']['paging']['next']
            h=jsondata['data'][user_index]['comments']['data']
            for j in h :


                if 'message' in j:

                    text+=j['from']['name']+"-:"+j['message']+'\n'


                else:
                    text+=j['from']['name']+"- Sticker"+'\n'


        else:
            if 'paging' not in jsondata:
                break
            url=jsondata['paging']['next']
            h=jsondata['data']

            for j in h :
                if 'message' in j:
                    text+=j['from']['name']+"-:"+j['message']+'\n'

                else:
                    text+=j['from']['name']+"- Sticker"+'\n'

        #text+='\n*********BREAK***************'
        text2=text+text2
        i=i+1

    return text2;



access_token='Your-Token-Here'
url1='https://graph.facebook.com/me/inbox?access_token='+access_token
a11=return_list(url1)



while(a11==25):
        #print('enter the index of chat you want to read 1~22\nEnter 25 for next\n')

        r = requests.get(url1)
        jsondata=json.loads(r.text)
        if 'paging' not in jsondata:
            print('Thats all! Please choose an option to proceed')
            ind=input()
            ind=int(ind)
            break
        url1=jsondata['paging']['next']
        a11=return_list(url1)

ind=a11
a=get_text_json(url1,ind)
#print(a)
r = requests.get(url1)
jsondata=json.loads(r.text)
if 'data' not in jsondata:
    print(' Facebook is giving some Authentication Error')
    exit()
h=jsondata['data']
filename=jsondata['data'][ind]['to']['data'][0]['name']+" and "+jsondata['data'][ind]['to']['data'][1]['name']+'.txt'
ye1=open(filename, 'w', encoding='utf-8')
ye1.write(a)
ye1.close()
#print(a, file = open(filename+'.txt','w'))
