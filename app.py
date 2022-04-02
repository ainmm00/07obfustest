from tkinter import *
import tkinter as tk
from PIL import Image, ImageTk
from tkinter.filedialog import askopenfile
from obfuscapk.main import perform_obfuscation, check_external_tool_dependencies
from obfuscapk.obfuscator_manager import ObfuscatorManager


root = tk.Tk()							#Start of GUI

canvas = tk.Canvas(root, width=600, height=300)
canvas.grid(columnspan=3, rowspan=3)

#Logo
logo = Image.open('logo.png') 			#logo.png must be in same directory as app
logo = ImageTk.PhotoImage(logo)
logo_label = tk.Label(image=logo)
logo_label.image = logo
logo_label.grid(column=1, row=0)

#instructions
instructions = tk.Label(root, text="Select PDF", font="Arial")
instructions.grid(columnspan=3, column=0, row=1)

#select obfuscation method
OBF = ['AdvancedReflection','ArithmeticBranch','CallIndirection','DebugRemoval',
				'Goto','MethodOverload','Nop',	'Reflection', 'Reorder', 'AssetEncryption',
                        'ConstStringEncryption', 'LibEncryption', 'ResStringEncryption', 'VirusTotal', 'ClassRename',
                        'FieldRename', 'MethodRename', 'RandomManifest', 'NewAlignment', 'NewSignature', 'Rebuild']
data = {} # dictionary to store all the IntVars

# mb = Menubutton (root, text="Obfuscation Method", relief=RAISED )
# mb.menu  =  Menu ( mb, tearoff = 0 )
# mb["menu"]  =  mb.menu



# for obMethod in OBF:
#     var = IntVar()
#     mb.menu.add_checkbutton(label=obMethod, variable=var)
#     data[obMethod] = var # add IntVar to the dictionary

# mb.grid(column=1, row=2)
# values = [(obMethod, var.get()) for obMethod, var in data.items()]

lb = Listbox(root, selectmode = "multiple")
lb.grid(column=1,row=2)
for item in range(len(OBF)): 
	lb.insert(END, OBF[item]) 
	lb.itemconfig(item, bg="#bdc1d6")

val = []
values = lb.curselection()
for i in values:
	op = lb.get(i)
	val.append(op)

# def showSelected():
#     countries = []
#     cname = lb.curselection()
#     for i in cname:
#         op = lb.get(i)
#         countries.append(op)
#     for val in countries:
#         print(val)

def open_file():
	browse_text.set("Open")
	file = askopenfile(parent=root, mode='rb', title="Choose a file", filetype=[("APK file","*apk")])
	if file:
		print("File successfully loaded")
		# obfuscators = ObfuscatorManager().get_obfuscators_names()
		check_external_tool_dependencies()
		
		perform_obfuscation(file.name,val)
		
		#add obfuscator

		
#def savefile():
#   filename = filedialog.asksaveasfile(mode='w', defaultextension=".apk")
#    if not filename:
#        return
#    edge.save(filename)

#Browse Button
browse_text = tk.StringVar()
browse_btn = tk.Button(root, textvariable=browse_text, command=lambda:open_file(), font="Arial", bg="#20bebe", fg="white", height=2, width=15)
browse_text.set("Browse")
browse_btn.grid(column=1, row=3)



root.mainloop()					#End of GUI