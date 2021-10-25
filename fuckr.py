#!/usr/bin/env python3

import os

os.system("clear")
os.system("pkg install toilet")
os.system("clear")
os.system("toilet -f mono12 -F metal Fuckr")
print("Tool Maked By @yusiqo")
print("Version: 1.0.0)
print(""" 

(1) Paketleri Indir
(2) Toollar
(3) Toolu Güncelle
(Q) Exit
""")

giris=input("Seçim: ")

if giris=="1":
	os.system("clear")
	os.system("pkg install nano")
	os.system("pkg install python2")
	os.system("pkg install toilet")
	os.system("pkg install figlet")
	os.system("pkg install cmatrix")
	os.system("clear")
	os.system("python3 fuckr.py")
	
if giris=="Q":
	os.system("exit")
	
if giris=="3":
	os.system("apt update -y")
	os.system("pkg update -y")
	os.system("apt upgrade -y")
	os.system("pkg upgrade -y")
	
if giris=="2":
	os.system("clear")
	os.system("toilet -f mono12 -F metal Tools")
	print("""
	
	(1) Cupp (wordlist)
	(2) Zphisher (phishing)
	(3) Hulk (Ddos)
	(4) Cam Hackers
	(5) XerXes (Ddos)
	
	""")
tool=input("Seçim: ")
	
if tool=="1":
	os.system("clear")
	print("Başlıyor......")
	os.system("cd")
	os.system("clear")
	os.system("git clone https://github.com/Mebus/cupp")
	os.system("clear")
	os.system("figlet Kuruldu")
	print("Bitti.....")
	
if tool=="2":
	os.system("clear")
	print("Başlıyor......")
	os.system("cd")
	os.system("clear")
	os.system("git clone https://github.com/htr-tech/zphisher")
	os.system("clear")
	os.system("figlet Kuruldu")
	print("Bitti.....")
	
if tool=="3":
	os.system("clear")
	print("Başlıyor......")
	os.system("cd")
	os.system("clear")
	os.system("git clone https://github.com/Mr4FX/HULK")
	os.system("clear")
	os.system("figlet Kuruldu")
	print("Bitti.....")
	
if tool=="4":
	os.system("clear")
	print("Başlıyor......")
	os.system("cd")
	os.system("clear")
	os.system("git clone https://github.com/AngelSecurityTeam/Cam-Hackers")
	os.system("clear")
	os.system("figlet Kuruldu")
	print("Bitti.....")
	
if tool=="5":
	os.system("clear")
	print("Başlıyor......")
	os.system("cd")
	os.system("clear")
	os.system("git clone https://github.com/CyberXCodder/XerXes")
	os.system("clear")
	os.system("figlet Kuruldu")
	print("Bitti.....")
