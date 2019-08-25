import json
import requests
import pdb
import coincap_quotes
import os
from datetime import datetime
import time
from prettytable import PrettyTable
from colorama import Fore,Back,Style
import smtplib
from email.message import EmailMessage
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
os.chdir(os.path.dirname(os.path.realpath(__file__)))
def sendmail (text):
	
	msg = MIMEMultipart()
	msg['From'] = 'python'
	msg['To'] = 'me'
	msg['Subject'] = 'crypto alert!'
	msg.attach(MIMEText(text, 'plain'))
	ms = msg.as_string()
	server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
	server.login("matanophir1@gmail.com", "Mm8166278")
	server.sendmail("matanophir1@gmail.com","matanophir1@gmail.com",ms)
	server.quit()
def getup(symb):

	url = 'https://sandbox-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest'
	headers = {
		'Accepts': 'application/json',
		'X-CMC_PRO_API_KEY': '7a67af9d-a4b9-4bcc-b483-c7b9011f5a7b',
		}
	parameters = {
		'symbol':symb,
		'convert':'ILS'
		}
	request = requests.Session()
	request.headers.update(headers)
	results = request.get(url,params=parameters).json()
	return results["data"][symb]["quote"]["ILS"]["percent_change_1h"]

por={}
with open("portfolio","r") as inp:
	for line in inp:
		psymb,pamount= line.split()
		por[psymb]={"coin":coincap_quotes.quote(psymb.upper()),"amount":pamount}


#pdb.set_trace()
table=PrettyTable()
table.field_names = ["#","Asset","Symbol","ID", "Amount Ownned", "ILS Value", "Price","1H","24H","7D"]
totalvalue=0
for i,idc in enumerate(por.values()):
	if idc["coin"].change1h>0:
		idc["coin"].change1h=Back.GREEN+str(idc["coin"].change1h)+'%'+Style.RESET_ALL
	else:
		idc["coin"].change1h=Back.RED+str(idc["coin"].change1h)+'%'+Style.RESET_ALL
	if idc["coin"].change24h>0:
		idc["coin"].change24h=Back.GREEN+str(idc["coin"].change24h)+'%'+Style.RESET_ALL
	else:
		idc["coin"].change24h=Back.RED+str(idc["coin"].change24h)+'%'+Style.RESET_ALL
	if idc["coin"].change7d>0:
		idc["coin"].change7d=Back.GREEN+str(idc["coin"].change7d)+'%'+Style.RESET_ALL
	else:
		idc["coin"].change7d=Back.RED+str(idc["coin"].change7d)+'%'+Style.RESET_ALL
	table.add_row([str(i),idc["coin"].name,idc["coin"].symbol,idc["coin"].id,idc["amount"],(float(idc["amount"])*idc["coin"].price),idc["coin"].price,idc["coin"].change1h,idc["coin"].change24h,idc["coin"].change7d])
	totalvalue+=(float(idc["amount"])*idc["coin"].price)
print ("\nMatan's portfolio")
print (table)
totalvalue="{:,}".format(round(totalvalue,2))
print (f"the total value is {Back.GREEN}{totalvalue} ILS{Style.RESET_ALL}")
print (f"last updated at- {datetime.now()}\n\n")

#start of P2
iftrack= input("Do you want to track the precent change according to 'upalerts.txt'?. y/n ")
if iftrack=='y':
	ifmail=input("do you want it sent to your mail? y/n ")
	print ("starts tracking...")
	trk={}
	score=[]
	while True:
		with open("upalerts","r") as inp:
			for line in inp:
				psymb,pamount= line.split()
				pamount=float(str(pamount))

			
				trk[psymb]={"1hchange":getup(psymb.upper()),"uplimit":pamount}
		mail=False
		for symb in trk.keys():
			#db.set_trace()
			if trk[symb]["1hchange"]>=trk[symb]["uplimit"] and symb not in score:
				print (f'{symb} just hit {trk[symb]["1hchange"]}')
				score.append(symb)
				mail=True
		if mail and ifmail=='y':
			msg=""
			with open("mail","w+") as mail:
				for sy in score:
					msg+=f"{sy.upper()} hit {trk[sy]['1hchange']} at {datetime.now()}\n"
					mail.write(f"{sy.upper()} hit {trk[sy]['1hchange']} at {datetime.now()}\n" )
			#print (msg) 
			sendmail(msg)
		print ('...')
		time.sleep(300)				

else:
	print ("see you next time")