import gspread
from oauth2client.service_account import ServiceAccountCredentials

scope = ['https://spreadsheets.google.com/feeds',
         'https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json', scope)
client = gspread.authorize(creds)

sheet = client.open('HelloThere').sheet1

list_of_hashes = sheet.get_all_records()

#print(list_of_hashes)
#sheet.append_row
#sheet.delete_row

#print(sheet.acell('A2'))
#print(sheet.cell(2,1).value)
#sheet.update_acell('B2','browner')
