import os
import tkinter
import string

number_of_logins = 0 # This shows the number of remebered logins
logins = {}

window = tkinter.Tk()
window.title("Network login")
window.geometry("400x250")

# This section handles putting the entires in login.txt into the logins dictionary
with open("login.txt", "r") as read:
	lines = read.readlines()
lines = list(map(lambda line: line.rstrip(), lines))
print (lines)
lines = list(map(lambda line: line.split(":"), lines))
print (lines)
for line in lines:
	logins[line[0]] = line[1]
print(logins)
number_of_logins = len(logins)

login_number = 0
for ssid in logins:
	login_number += 1
	exec("lbl_login" + str(login_number) + " = tkinter.Label(window, text = ssid)")

def exit(self):
	self.root.destroy()
	
def add_to_file(source, text):
    with open(source, "r") as read:
        lines = read.readlines()
    lines.append(text + "\n")
    with open(source, "w") as write:
        for line in lines:
            write.write(line)

lbl_welcome = tkinter.Label(window, text = "Welcome!", fg = "blue")
lbl_ssid = tkinter.Label(window, text = "Please enter the network SSID")
ent_ssid = tkinter.Entry(window)
lbl_password = tkinter.Label(window, text = "Please enter the network password")
ent_password = tkinter.Entry(window)
lbl_logins = tkinter.Label(window, text = "Remebered logins:")

def network_connect(ssid, password):
	os.system("networksetup -setairportnetwork en0 \"" + ssid + "\" " + password)
	lbl_welcome.configure(text = "Connecting...")

def add_login():
	
	addLogin = tkinter.Tk()
	addLogin.title("Add login details")
	
	lbl_info = tkinter.Label(addLogin, text = "Adding a login will save it so that you don't need to \n enter it every time you launch the program. \n Just click a button and you will be connected!")

	lbl_addLogin_ssid = tkinter.Label(addLogin, text = "SSID:")
	ent_addLogin_ssid = tkinter.Entry(addLogin)
	lbl_addLogin_password = tkinter.Label(addLogin, text = "Password: ")
	ent_addLogin_password = tkinter.Entry(addLogin)
	
	def addToLogins():
		global number_of_logins
		ssid = ent_addLogin_ssid.get()
		password = ent_addLogin_password.get()
		logins[ssid] = password
		add_to_file("login.txt", ssid + ":" + password)
		number_of_logins += 1 # Increment before execution for the name (login1, login2, etc.)
		#~ exec("lbl_login" + str(number_of_logins) + " = tkinter.Label(window, text = ssid)") # Initalises the button
		#~ exec("btn_login" + str(number_of_logins) + " = tkinter.Button(window, text = \"Connect\", command = lambda temp_ssid=ssid: network_connect(temp_ssid, password))")
		#~ exec("lbl_login" + str(number_of_logins) + ".pack()")
		#~ exec("btn_login" + str(number_of_logins) + ".pack()")
	
	btn_add = tkinter.Button(addLogin, text = "Add", command = addToLogins)
	
	lbl_info.pack()
	lbl_addLogin_ssid.pack()
	ent_addLogin_ssid.pack()
	lbl_addLogin_password.pack()
	ent_addLogin_password.pack()
	btn_add.pack()
	
	addLogin.mainloop()

# Initalisation of objects with pre-defined functions
btn_connect = tkinter.Button(window, text = "Connect", command = lambda ssid=ent_ssid.get(): network_connect(ssid, ent_password.get())) # I use a lambda function as if I don't, the function will run when the program runs.
btn_add_login = tkinter.Button(window, text = "Add login", command = add_login)

lbl_welcome.pack()
lbl_ssid.pack()
ent_ssid.pack()
lbl_password.pack()
ent_password.pack()
btn_connect.pack()
lbl_logins.pack()

for n in range(1, number_of_logins + 1):
	exec("lbl_login" + str(n) + ".pack()")

btn_add_login.pack()

tkinter.mainloop()

print(logins)
