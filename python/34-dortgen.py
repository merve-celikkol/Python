def sag(adet):
	for a in range(int(adet)):
		print("/",end="")
def sol(adet):
	for a in range(int(adet)):
		print("\\",end="")
# 1 tane ters slash oluşturmak için iki tane \\ yapılmalı. 
def bosluk(adet):
	for a in range(int(adet)):
		print(" ",end="")
def atla(adet):
	for a in range(int(adet)):
		print()

# (çap/2)-1 ve range komutu 0 dan başlayarak çalışır.
def üst(çap):
	başlangıç = çap/2-1
	for a in range(int(çap/2)):
		bosluk(başlangıç-a)
		sag(1)
		bosluk(a*2)
		sol(1)
		atla(1)

def alt(çap):
	başlangıç = çap-2
	for a in range(int(çap/2)):
		bosluk(a)
		sol(1)
		bosluk(başlangıç - a*2)
		sag(1)
		atla(1)

def dortgen(çap):
	üst(çap)
	alt(çap)

dortgen(30)
