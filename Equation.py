import time

import gspread
from oauth2client.service_account import ServiceAccountCredentials
scope = ['https://spreadsheets.google.com/feeds',
         'https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json', scope)
client = gspread.authorize(creds)
sheet = client.open('HelloThere').get_worksheet(2)
list_of_hashes = sheet.get_all_records()

def num(x,y,z,n):
    #n = going to
    #q = from
    k = 0
    writes = 1
    p = time.time()
    sleep = 0
    """p = n ** 2 squared
    q = n ** 3 cubed"""
    while z <= n:
        k = (x ** 3) - (y ** 3) - (z ** 3)
        while k>1000 or k<-1000:
            if x!=n:
                x+=1
            if x>=n:
                x=0
                y+=1
            if y==n:
                y=0
                z+=1
            if z==n:
                t = time.time() - p
                print("Took: ", t, "seconds")
                return "DONE"
            k = (x ** 3) - (y ** 3) - (z ** 3)
        if k <= -100 and k>=-1000 and x!=z and x!=y and y!=z:
            g = k * -1
            a = x * -1
            b = y * -1
            c = z * -1
            print(k)
            writes+=1
            sheet.append_row([g,a,b,c])
        elif k >= 100 and k<=1000 and x!=z and x!=y and y!=z:
            print(k)
            writes+=1
            sheet.append_row([k,x,y,z])
            
        x+=1
        if x==n:
            x=0
            y+=1
        if y==n:
            y=0
            z+=1
        if z>n:
            t = time.time() - p
            print("Took: ", t, "seconds")
        if writes >=98:
            while sleep<=102:
                time.sleep(1)
                sleep+=1
                print("Time until next run: ",sleep,end="\r")
            if sleep>102:
                writes = 1
                sleep = 0
                print("")
            print(k)
        
    
