"""
 Does the equation x^3 +- y^3 +- z^3 = k
 Currently in -- mode and has to be manually changed
 -- mode seems to be the most efficient way to get greatest
 number of results compared to ++ or -- in terms of small numbers

 Smaller = <1000
"""

import time
import gspread

#Used to connect to spreadsheet
from oauth2client.service_account import ServiceAccountCredentials
scope = ['https://spreadsheets.google.com/feeds',
         'https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json', scope)
client = gspread.authorize(creds)
sheet = client.open('HelloThere').get_worksheet(2)
list_of_hashes = sheet.get_all_records()

def num(x,y,z,Limit): #x,y,z,Go to Ex: 0->1000
    k = 0
    writes = 1
    start_time = time.time()
    sleep = 0

    while z <= Limit:
        k = (x ** 3) - (y ** 3) - (z ** 3)
        #Bounds of what you're looking for; inbetween x,y
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
                elapsed_time = time.time() - start_time
                print("Took: ", elapsed_time, "seconds")
                return "DONE"
            k = (x ** 3) - (y ** 3) - (z ** 3)
        #Prints the -k as +k and -x,-y,-z instead
        if k <= -100 and k>=-1000 and x!=z and x!=y and y!=z:
            g = k * -1
            a = x * -1
            b = y * -1
            c = z * -1
            print(k)
            writes+=1
            sheet.append_row([g,a,b,c])
        #Prints k,x,y,z
        elif k >= 100 and k<=1000 and x!=z and x!=y and y!=z: #x!=z removes repeats 10^3-6^3-10^3...
            print(k)
            writes+=1
            sheet.append_row([k,x,y,z])
            
        x+=1
        if x==Limit:
            x=0
            y+=1
        if y==Limit:
            y=0
            z+=1
        if z>Limit:
            elapsed_time = time.time() - start_time
            print("Took: ", elapsed_time, "seconds")

        if writes >=98: #Prevents going over sheets api read/write limit
        #100 writes per 100 seconds
            while sleep<=102: #Sleeps 102 seconds to be sure
                time.sleep(1)
                sleep+=1
                print("Time until next run: ",sleep,end="\r")

            if sleep>102: #Resets counters
                writes = 1
                sleep = 0
                print("")
            print(k)