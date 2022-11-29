from dataclasses import InitVar
from tkinter import *
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
import ClassesMD as MD
import CreateFileMDArxml as CF
from tkinter import filedialog as fd
import ctypes


class GUI:
    
    def __init__ (self):
        self.root = Tk()
        self.root.title("BSWMD Wizard Tool") 
        # Set the resolution of window
        self.root.geometry("750x600")
        self.root.config (bg="#D0CECE")
        self.tree = None
        # Allow Window to be resizable
        self.root.resizable(width = False, height = False)
        self.listFrames = []
        self.listLabels = []
        self.listButt = []
        self.listEntry = []
        self.listText = []

    def windowDestroyElments(self):
        for each_frame in self.listFrames:
            each_frame.destroy ()
        
        for each_label in self.listLabels:
            each_label.destroy ()
        
        for each_but in  self.listButt:
            each_but.destroy()
        
        for each_ent in  self.listEntry:
            each_ent.destroy()
            
        for each_text in self.listText:
            each_text.destroy()
    

    def principalMenu (self):
        self.windowDestroyElments()


        # opens the image

        img_ModifyModule = PhotoImage(file='./immages/ModifyModule.png')
        img_DeleteModule = PhotoImage(file='./immages/DeleteModule.png')
        img_CloseModule = PhotoImage(file='./immages/CloseModule.png')
        

        #Buttons

        frame = Frame(master=self.root, width=400, height=70, bg="#D0CECE")
        frame.pack()
        self.listFrames.append (frame)

        frame1 = Frame(master=self.root, width=400, height=250, bg="#D0CECE")
        frame1.pack()
        self.listFrames.append (frame1)
        
        
        img_Welcome = PhotoImage(file='./immages/Welcome.png')
        label_Welcome = Label(master=frame1, image=img_Welcome, borderwidth=0)
        label_Welcome.pack(pady=20)
        self.listLabels.append (label_Welcome)
    
        img_CreateModule = PhotoImage(file='./immages/CreateModule.png')
        button_createModule = Button(master=self.root, command=self.windowCreateModule, image=img_CreateModule)
        button_createModule.pack(pady=10)
        self.listButt.append (button_createModule)

        button_modifyModule = Button(master=self.root, image=img_ModifyModule)
        button_modifyModule.pack(pady=10)
        self.listButt.append (button_modifyModule)
        
        button_deleteModule = Button(master=self.root, image=img_DeleteModule)
        button_deleteModule.pack(pady=10)
        self.listButt.append (button_deleteModule)

        button_closeModule = Button(master=self.root, image=img_CloseModule)
        button_closeModule.pack(pady=10)
        self.listButt.append (button_closeModule)

        self.root.mainloop()
    
    def TemplateFrame (self):
        ws =  Frame(master=self.root, width=500, height=550, bg="#D0CECE")
        ws.place (x=280, y=10)
        
        # Create A Main Frame
        main_frame = Frame(ws)
        main_frame.pack(fill=BOTH, expand=1)

        # Create A Canvas
        my_canvas = Canvas(main_frame, width=400, height=350,  bg="white", scrollregion=(0, 0, 1000, 1000))
        my_canvas.pack(side=LEFT, fill=BOTH, expand=1)

        # Add A Scrollbar To The Canvas
        my_scrollbar = ttk.Scrollbar(main_frame, orient=VERTICAL, command=my_canvas.yview)
        my_scrollbar.pack(side=RIGHT, fill=Y)

        # Configure The Canvas
        my_canvas.configure(yscrollcommand=my_scrollbar.set)
        my_canvas.bind('<Configure>', lambda e: my_canvas.configure(scrollregion = my_canvas.bbox("all")))

        # Create ANOTHER Frame INSIDE the Canvas
        frame = Frame(my_canvas, width=500, height=550, bg="white", borderwidth = 1, relief="solid")

        # Add that New frame To a Window In The Canvas
        my_canvas.create_window((0,0), window=frame, anchor="nw")
        
        label = Label(master=frame,
        text="Editor: ",
        foreground="black",  # Set the text color to white
        font=("Arial", 10),
        anchor = "w",
        width = 50
        )
        label.place(x=0, y=0)
        self.listLabels.append (label)        
               
    def LogFrame (self):
        #self.windowDestroyElments()
        
        frame = Frame(master=self.root, width=400, height=180, bg="#D0CECE", borderwidth = 2, relief='sunken')
        #frame.pack(pady=20, expand=True, side='left')
        frame.place (x=280, y=20+380)
        self.listFrames.append (frame)


    def windowCreateModule (self, NameModuleMod = "", VendorModuleMod = "", DescriptionModUleMpd = "", SipVersionModuleMod = "", SipPathModuleMod = "", LowerMultModuleMod = "", UpperMultModuleMod = ""):
        ws =  Frame(master=self.root, width=500, height=550, bg="#D0CECE")
        ws.place (x=280, y=10)
        
        # Create A Main Frame
        main_frame = Frame(ws)
        main_frame.pack(fill=BOTH, expand=1)

        # Create A Canvas
        my_canvas = Canvas(main_frame, width=400, height=350,  bg="white", scrollregion=(0, 0, 1000, 1000))
        my_canvas.pack(side=LEFT, fill=BOTH, expand=1)

        # Add A Scrollbar To The Canvas
        my_scrollbar = ttk.Scrollbar(main_frame, orient=VERTICAL, command=my_canvas.yview)
        my_scrollbar.pack(side=RIGHT, fill=Y)

        # Configure The Canvas
        my_canvas.configure(yscrollcommand=my_scrollbar.set)
        my_canvas.bind('<Configure>', lambda e: my_canvas.configure(scrollregion = my_canvas.bbox("all")))

        # Create ANOTHER Frame INSIDE the Canvas
        frame = Frame(my_canvas, width=500, height=550, bg="white", borderwidth = 1, relief="solid")

        # Add that New frame To a Window In The Canvas
        my_canvas.create_window((0,0), window=frame, anchor="nw")
        
        '''for each_thing in range(20):
            Button (second_frame, text=f'Button {each_thing} Yo').place(x=0, y= each_thing*40)'''

        '''frame =  Frame(master=self.root, width=400, height=300, bg="#D0CECE", borderwidth = 2, relief='sunken')
        #frame.pack(pady=20, expand=True, side='left')
        frame.place (x=280, y=10)  ''' 
        
        label = Label(master=frame,
        text="Editor: Creating Module",
        foreground="black",  # Set the text color to white
        font=("Arial", 10),
        anchor = "w",
        width = 50
        )
        label.place(x=0, y=0)
        self.listLabels.append (label)

        #Name of module
        NameModule = Label(master=frame,
        text="Name:",
        foreground="black",  # Set the text color to white
        font=("Arial", 10),
        anchor = "w",
        width = 8,
        bg="white"
        )
        NameModule.place(x=20, y=50)
        self.listLabels.append (NameModule)
        
        NameVariableInput = StringVar()
        NameInput = Entry(master=frame, 
        textvariable=NameVariableInput,
        font=("Arial", 10),
        width = 40,
        bd = 1,
        relief="solid",
        highlightthickness=1,
        highlightcolor="black",
        )
        NameInput.focus()
        NameInput.place(x=100, y=50)
        NameInput.insert(0, NameModuleMod)
        self.listEntry.append (NameInput)


        #Vendor of module
        VendorModule = Label(master=frame,
        text="Vendor:",
        foreground="black",  # Set the text color to white
        font=("Arial", 10),
        anchor = "w",
        width = 8,
        bg="white"
        )
        VendorModule.place(x=20, y=90) 
        self.listLabels.append (VendorModule)
        
        VendorVariableInput = StringVar()
        VendorInput = Entry(master=frame, 
        textvariable=VendorVariableInput,
        font=("Arial", 10),
        width = 40,
        bd = 1,
        relief="solid",
        highlightthickness=1,
        highlightcolor="black",
        )
        VendorInput.place(x=100, y=90)
        VendorInput.insert(0, VendorModuleMod)
        self.listEntry.append (VendorInput)
        
        
        #Description of module
        DescriptionModule = Label(master=frame,
        text="Description:",
        foreground="black",  # Set the text color to white
        font=("Arial", 10),
        anchor = "w",
        width = 8,
        bg="white"
        )
        DescriptionModule.place(x=20, y=130)
        self.listLabels.append (DescriptionModule)
        
        DescriptionInput = Text(master=frame, 
        font=("Arial", 10),
        width = 40,
        height = 3,
        bd = 1,
        relief="solid",
        highlightthickness=1,
        highlightcolor="black",
        )
        DescriptionInput.place(x=100, y=130)
        DescriptionInput.insert (INSERT, DescriptionModUleMpd)
        self.listText.append(DescriptionInput)


        #Sip
        SipVersion = Label(master=frame,
        text="Sip Version:",
        foreground="black",  # Set the text color to white
        font=("Arial", 10),
        anchor = "w",
        width = 8,
        bg="white"
        )
        SipVersion.place(x=20, y=200)
        self.listLabels.append (SipVersion)
        
        SipVariableInput = StringVar()
        SipInput = Entry(master=frame, 
        textvariable=SipVariableInput,
        font=("Arial", 10),
        width = 40,
        bd = 1,
        relief="solid",
        highlightthickness=1,
        highlightcolor="black",
        )
        SipInput.place(x=100, y=200)
        SipInput.insert(0, SipVersionModuleMod)
        self.listEntry.append (SipInput)



        #Sip Path
        SipPath = Label(master=frame,
        text="Path: ",
        foreground="black",  # Set the text color to white
        font=("Arial", 10),
        anchor = "w",
        width = 8,
        bg="white"
        )
        SipPath.place(x=20, y=240)
        self.listLabels.append (SipPath)

        SipPathVariableInput = StringVar()
        SipPathInput = Entry(master=frame, 
        textvariable=SipPathVariableInput,
        font=("Arial", 10),
        width = 40,
        bd = 1,
        relief="solid",
        highlightthickness=1,
        highlightcolor="black",
        )
        SipPathInput.place(x=100, y=240)
        SipPathInput.insert(0, SipPathModuleMod)
        self.listEntry.append (SipPathInput)

        #Lower Multiplicity
        LowerMultiplicity = Label(master=frame,
        text="Lower ",
        foreground="black",  # Set the text color to white
        font=("Arial", 10),
        anchor = "w",
        width = 8,
        bg="white"
        )
        LowerMultiplicity.place(x=20, y=280)
        self.listLabels.append (LowerMultiplicity)
        
        
        Multiplicity = Label(master=frame,
        text="Multiplicity: ",
        foreground="black",  # Set the text color to white
        font=("Arial", 10),
        anchor = "w",
        width = 8,
        bg="white"
        )
        Multiplicity.place(x=20, y=300)
        self.listLabels.append (Multiplicity)        
        

        LowerMultVariableInput = StringVar()
        LowerMultInput = Entry(master=frame, 
        textvariable=LowerMultVariableInput,
        font=("Arial", 10),
        width = 40,
        bd = 1,
        relief="solid",
        highlightthickness=1,
        highlightcolor="black",
        )
        LowerMultInput.place(x=100, y=300)
        LowerMultInput.insert(0, LowerMultModuleMod)
        self.listEntry.append (LowerMultInput)
        


        #Upper Multiplicity
        UpperMultiplicity = Label(master=frame,
        text="Upper ",
        foreground="black",  # Set the text color to white
        font=("Arial", 10),
        anchor = "w",
        width = 8,
        bg="white"
        )
        UpperMultiplicity.place(x=20, y=340)
        self.listLabels.append (UpperMultiplicity)
        
        
        MultiplicityUpp = Label(master=frame,
        text="Multiplicity: ",
        foreground="black",  # Set the text color to white
        font=("Arial", 10),
        anchor = "w",
        width = 8,
        bg="white"
        )
        MultiplicityUpp.place(x=20, y=360)
        self.listLabels.append (MultiplicityUpp)    


        UpperMultVariableInput = StringVar()
        UpperMultInput = Entry(master=frame, 
        textvariable=UpperMultVariableInput,
        font=("Arial", 10),
        width = 40,
        bd = 1,
        relief="solid",
        highlightthickness=1,
        highlightcolor="black",
        )
        UpperMultInput.place(x=100, y=360)
        UpperMultInput.insert(0, UpperMultModuleMod)
        self.listEntry.append (UpperMultInput)
 

        
        #Buttons

        button_right = Button(
        master=frame, 
        command = lambda: self.CheckCreateModuleParameters(NameInput, VendorInput, DescriptionInput, SipInput, SipPathInput, LowerMultInput, UpperMultInput), 
        text="Generate", 
        borderwidth=5,
        width=10)
        button_right.place(x=270, y=450)
        self.listButt.append (button_right)

        button_left = Button(
            master=frame, 
            command= self.TemplateFrame, 
            text="Close", 
            borderwidth=5, 
            width=10
            )
        button_left.place(x=50, y=450)  
        self.listButt.append (button_left)

    def windowCreateContainer (self):
        ws =  Frame(master=self.root, width=500, height=550, bg="#D0CECE")
        ws.place (x=280, y=10)
        
        # Create A Main Frame
        main_frame = Frame(ws)
        main_frame.pack(fill=BOTH, expand=1)

        # Create A Canvas
        my_canvas = Canvas(main_frame, width=400, height=350,  bg="white", scrollregion=(0, 0, 1000, 1000))
        my_canvas.pack(side=LEFT, fill=BOTH, expand=1)

        # Add A Scrollbar To The Canvas
        my_scrollbar = ttk.Scrollbar(main_frame, orient=VERTICAL, command=my_canvas.yview)
        my_scrollbar.pack(side=RIGHT, fill=Y)

        # Configure The Canvas
        my_canvas.configure(yscrollcommand=my_scrollbar.set)
        my_canvas.bind('<Configure>', lambda e: my_canvas.configure(scrollregion = my_canvas.bbox("all")))

        # Create ANOTHER Frame INSIDE the Canvas
        frame = Frame(my_canvas, width=500, height=550, bg="white", borderwidth = 1, relief="solid")

        # Add that New frame To a Window In The Canvas
        my_canvas.create_window((0,0), window=frame, anchor="nw")
        
        label = Label(master=frame,
        text="Editor: Creating Container",
        foreground="black",  # Set the text color to white
        font=("Arial", 10),
        anchor = "w",
        width = 50
        )
        label.place(x=0, y=0)
        self.listLabels.append (label)        
        
        
        #Name of Container
        NameContainer = Label(master=frame,
        text="Name:",
        foreground="black",  # Set the text color to white
        font=("Arial", 10),
        anchor = "w",
        width = 8,
        bg="white"
        )
        NameContainer.place(x=20, y=50)
        self.listLabels.append (NameContainer)
        
        NameVariableInput = StringVar()
        NameInput = Entry(master=frame, 
        textvariable=NameVariableInput,
        font=("Arial", 10),
        width = 40,
        bd = 1,
        relief="solid",
        highlightthickness=1,
        highlightcolor="black",
        )
        NameInput.focus()
        NameInput.place(x=100, y=50)
        self.listEntry.append (NameInput)
        
        
        #Description of Conyainer
        DescriptionContainer = Label(master=frame,
        text="Description:",
        foreground="black",  # Set the text color to white
        font=("Arial", 10),
        anchor = "w",
        width = 8,
        bg="white"
        )
        DescriptionContainer.place(x=20, y=90)
        self.listLabels.append (DescriptionContainer)
        
        DescriptionInput = Text(master=frame, 
        font=("Arial", 10),
        width = 40,
        height = 3,
        bd = 1,
        relief="solid",
        highlightthickness=1,
        highlightcolor="black",
        )
        DescriptionInput.place(x=100, y=90)
        self.listText.append(DescriptionInput)

        #Lower Multiplicity
        LowerMultiplicity = Label(master=frame,
        text="Lower ",
        foreground="black",  # Set the text color to white
        font=("Arial", 10),
        anchor = "w",
        width = 8,
        bg="white"
        )
        LowerMultiplicity.place(x=20, y=150)
        self.listLabels.append (LowerMultiplicity)
        
        
        Multiplicity = Label(master=frame,
        text="Multiplicity: ",
        foreground="black",  # Set the text color to white
        font=("Arial", 10),
        anchor = "w",
        width = 8,
        bg="white"
        )
        Multiplicity.place(x=20, y=170)
        self.listLabels.append (Multiplicity)        
        

        LowerMultVariableInput = StringVar()
        LowerMultInput = Entry(master=frame, 
        textvariable=LowerMultVariableInput,
        font=("Arial", 10),
        width = 40,
        bd = 1,
        relief="solid",
        highlightthickness=1,
        highlightcolor="black",
        )
        LowerMultInput.place(x=100, y=170)
        self.listEntry.append (LowerMultInput)
        


        #Upper Multiplicity
        UpperMultiplicity = Label(master=frame,
        text="Upper ",
        foreground="black",  # Set the text color to white
        font=("Arial", 10),
        anchor = "w",
        width = 8,
        bg="white"
        )
        UpperMultiplicity.place(x=20, y=210)
        self.listLabels.append (UpperMultiplicity)
        
        
        MultiplicityUpp = Label(master=frame,
        text="Multiplicity: ",
        foreground="black",  # Set the text color to white
        font=("Arial", 10),
        anchor = "w",
        width = 8,
        bg="white"
        )
        MultiplicityUpp.place(x=20, y=230)
        self.listLabels.append (MultiplicityUpp)    


        UpperMultVariableInput = StringVar()
        UpperMultInput = Entry(master=frame, 
        textvariable=UpperMultVariableInput,
        font=("Arial", 10),
        width = 40,
        bd = 1,
        relief="solid",
        highlightthickness=1,
        highlightcolor="black",
        )
        UpperMultInput.place(x=100, y=230)
        self.listEntry.append (UpperMultInput)


        #Buttons

        button_right = Button(
        master=frame, 
        command = lambda: self.CheckCreateContainer(NameInput, DescriptionInput, LowerMultInput, UpperMultInput), 
        text="Create", 
        borderwidth=5,
        width=10)
        button_right.place(x=270, y=300)
        self.listButt.append (button_right)

        button_left = Button(
            master=frame, 
            command= self.TemplateFrame, 
            text="Close", 
            borderwidth=5, 
            width=10
            )
        button_left.place(x=50, y=300)  
        self.listButt.append (button_left)
        

    def windowEditModule (self, NameModuleMod, VendorModuleMod, DescriptionModUleMpd, SipVersionModuleMod, SipPathModuleMod, LowerMultModuleMod, UpperMultModuleMod):
        ws =  Frame(master=self.root, width=500, height=550, bg="#D0CECE")
        ws.place (x=280, y=10)
        
        # Create A Main Frame
        main_frame = Frame(ws)
        main_frame.pack(fill=BOTH, expand=1)

        # Create A Canvas
        my_canvas = Canvas(main_frame, width=400, height=350,  bg="white", scrollregion=(0, 0, 1000, 1000))
        my_canvas.pack(side=LEFT, fill=BOTH, expand=1)

        # Add A Scrollbar To The Canvas
        my_scrollbar = ttk.Scrollbar(main_frame, orient=VERTICAL, command=my_canvas.yview)
        my_scrollbar.pack(side=RIGHT, fill=Y)

        # Configure The Canvas
        my_canvas.configure(yscrollcommand=my_scrollbar.set)
        my_canvas.bind('<Configure>', lambda e: my_canvas.configure(scrollregion = my_canvas.bbox("all")))

        # Create ANOTHER Frame INSIDE the Canvas
        frame = Frame(my_canvas, width=500, height=550, bg="white", borderwidth = 1, relief="solid")

        # Add that New frame To a Window In The Canvas
        my_canvas.create_window((0,0), window=frame, anchor="nw")
        
        label = Label(master=frame,
        text="Editor: Editing Module " + NameModuleMod,
        foreground="black",  # Set the text color to white
        font=("Arial", 10),
        anchor = "w",
        width = 50
        )
        label.place(x=0, y=0)
        self.listLabels.append (label)

        #Vendor of module
        VendorModule = Label(master=frame,
        text="Vendor:",
        foreground="black",  # Set the text color to white
        font=("Arial", 10),
        anchor = "w",
        width = 8,
        bg="white"
        )
        VendorModule.place(x=20, y=50) 
        self.listLabels.append (VendorModule)
        
        VendorVariableInput = StringVar()
        VendorInput = Entry(master=frame, 
        textvariable=VendorVariableInput,
        font=("Arial", 10),
        width = 40,
        bd = 1,
        relief="solid",
        highlightthickness=1,
        highlightcolor="black",
        )
        VendorInput.place(x=100, y=50)
        VendorInput.insert(0, VendorModuleMod)
        self.listEntry.append (VendorInput)
        
        
        #Description of module
        DescriptionModule = Label(master=frame,
        text="Description:",
        foreground="black",  # Set the text color to white
        font=("Arial", 10),
        anchor = "w",
        width = 8,
        bg="white"
        )
        DescriptionModule.place(x=20, y=90)
        self.listLabels.append (DescriptionModule)
        
        DescriptionInput = Text(master=frame, 
        font=("Arial", 10),
        width = 40,
        height = 3,
        bd = 1,
        relief="solid",
        highlightthickness=1,
        highlightcolor="black",
        )
        DescriptionInput.place(x=100, y=90)
        DescriptionInput.insert (INSERT, DescriptionModUleMpd)
        self.listText.append(DescriptionInput)


        #Sip
        SipVersion = Label(master=frame,
        text="Sip Version:",
        foreground="black",  # Set the text color to white
        font=("Arial", 10),
        anchor = "w",
        width = 8,
        bg="white"
        )
        SipVersion.place(x=20, y=160)
        self.listLabels.append (SipVersion)
        
        SipVariableInput = StringVar()
        SipInput = Entry(master=frame, 
        textvariable=SipVariableInput,
        font=("Arial", 10),
        width = 40,
        bd = 1,
        relief="solid",
        highlightthickness=1,
        highlightcolor="black",
        )
        SipInput.place(x=100, y=160)
        SipInput.insert(0, SipVersionModuleMod)
        self.listEntry.append (SipInput)



        #Sip Path
        SipPath = Label(master=frame,
        text="Path: ",
        foreground="black",  # Set the text color to white
        font=("Arial", 10),
        anchor = "w",
        width = 8,
        bg="white"
        )
        SipPath.place(x=20, y=200)
        self.listLabels.append (SipPath)

        SipPathVariableInput = StringVar()
        SipPathInput = Entry(master=frame, 
        textvariable=SipPathVariableInput,
        font=("Arial", 10),
        width = 40,
        bd = 1,
        relief="solid",
        highlightthickness=1,
        highlightcolor="black",
        )
        SipPathInput.place(x=100, y=200)
        SipPathInput.insert(0, SipPathModuleMod)
        self.listEntry.append (SipPathInput)

        #Lower Multiplicity
        LowerMultiplicity = Label(master=frame,
        text="Lower ",
        foreground="black",  # Set the text color to white
        font=("Arial", 10),
        anchor = "w",
        width = 8,
        bg="white"
        )
        LowerMultiplicity.place(x=20, y=240)
        self.listLabels.append (LowerMultiplicity)
        
        
        Multiplicity = Label(master=frame,
        text="Multiplicity: ",
        foreground="black",  # Set the text color to white
        font=("Arial", 10),
        anchor = "w",
        width = 8,
        bg="white"
        )
        Multiplicity.place(x=20, y=260)
        self.listLabels.append (Multiplicity)        
        

        LowerMultVariableInput = StringVar()
        LowerMultInput = Entry(master=frame, 
        textvariable=LowerMultVariableInput,
        font=("Arial", 10),
        width = 40,
        bd = 1,
        relief="solid",
        highlightthickness=1,
        highlightcolor="black",
        )
        LowerMultInput.place(x=100, y=260)
        LowerMultInput.insert(0, LowerMultModuleMod)
        self.listEntry.append (LowerMultInput)
        


        #Upper Multiplicity
        UpperMultiplicity = Label(master=frame,
        text="Upper ",
        foreground="black",  # Set the text color to white
        font=("Arial", 10),
        anchor = "w",
        width = 8,
        bg="white"
        )
        UpperMultiplicity.place(x=20, y=300)
        self.listLabels.append (UpperMultiplicity)
        
        
        MultiplicityUpp = Label(master=frame,
        text="Multiplicity: ",
        foreground="black",  # Set the text color to white
        font=("Arial", 10),
        anchor = "w",
        width = 8,
        bg="white"
        )
        MultiplicityUpp.place(x=20, y=320)
        self.listLabels.append (MultiplicityUpp)    


        UpperMultVariableInput = StringVar()
        UpperMultInput = Entry(master=frame, 
        textvariable=UpperMultVariableInput,
        font=("Arial", 10),
        width = 40,
        bd = 1,
        relief="solid",
        highlightthickness=1,
        highlightcolor="black",
        )
        UpperMultInput.place(x=100, y=320)
        UpperMultInput.insert(0, UpperMultModuleMod)
        self.listEntry.append (UpperMultInput)
 

        
        #Buttons

        button_right = Button(
        master=frame, 
        command = lambda: self.CheckEditModuleParameters(NameModuleMod, VendorInput, DescriptionInput, SipInput, SipPathInput, LowerMultInput, UpperMultInput), 
        text="Modify", 
        borderwidth=5,
        width=10)
        button_right.place(x=270, y=450)
        self.listButt.append (button_right)

        button_left = Button(
            master=frame, 
            command= self.TemplateFrame, 
            text="Close", 
            borderwidth=5, 
            width=10
            )
        button_left.place(x=50, y=450)  
        self.listButt.append (button_left)


    def windowEditContainer (self, NameContainerMod, DescriptionContainerMod, LowerMultContainerMod, UpperMultContainerMod, Module_obj):
        ws =  Frame(master=self.root, width=500, height=550, bg="#D0CECE")
        ws.place (x=280, y=10)
        
        # Create A Main Frame
        main_frame = Frame(ws)
        main_frame.pack(fill=BOTH, expand=1)

        # Create A Canvas
        my_canvas = Canvas(main_frame, width=400, height=350,  bg="white", scrollregion=(0, 0, 1000, 1000))
        my_canvas.pack(side=LEFT, fill=BOTH, expand=1)

        # Add A Scrollbar To The Canvas
        my_scrollbar = ttk.Scrollbar(main_frame, orient=VERTICAL, command=my_canvas.yview)
        my_scrollbar.pack(side=RIGHT, fill=Y)

        # Configure The Canvas
        my_canvas.configure(yscrollcommand=my_scrollbar.set)
        my_canvas.bind('<Configure>', lambda e: my_canvas.configure(scrollregion = my_canvas.bbox("all")))

        # Create ANOTHER Frame INSIDE the Canvas
        frame = Frame(my_canvas, width=500, height=550, bg="white", borderwidth = 1, relief="solid")

        # Add that New frame To a Window In The Canvas
        my_canvas.create_window((0,0), window=frame, anchor="nw")
        
        label = Label(master=frame,
        text="Editor: Editing Container " + NameContainerMod,
        foreground="black",  # Set the text color to white
        font=("Arial", 10),
        anchor = "w",
        width = 50
        )
        label.place(x=0, y=0)
        self.listLabels.append (label)
        
        #Description of module
        DescriptionModule = Label(master=frame,
        text="Description:",
        foreground="black",  # Set the text color to white
        font=("Arial", 10),
        anchor = "w",
        width = 8,
        bg="white"
        )
        DescriptionModule.place(x=20, y=50)
        self.listLabels.append (DescriptionModule)
        
        DescriptionInput = Text(master=frame, 
        font=("Arial", 10),
        width = 40,
        height = 3,
        bd = 1,
        relief="solid",
        highlightthickness=1,
        highlightcolor="black",
        )
        DescriptionInput.place(x=100, y=50)
        DescriptionInput.insert (INSERT, DescriptionContainerMod)
        self.listText.append(DescriptionInput)

        #Lower Multiplicity
        LowerMultiplicity = Label(master=frame,
        text="Lower ",
        foreground="black",  # Set the text color to white
        font=("Arial", 10),
        anchor = "w",
        width = 8,
        bg="white"
        )
        LowerMultiplicity.place(x=20, y=120)
        self.listLabels.append (LowerMultiplicity)
        
        
        Multiplicity = Label(master=frame,
        text="Multiplicity: ",
        foreground="black",  # Set the text color to white
        font=("Arial", 10),
        anchor = "w",
        width = 8,
        bg="white"
        )
        Multiplicity.place(x=20, y=140)
        self.listLabels.append (Multiplicity)        
        

        LowerMultVariableInput = StringVar()
        LowerMultInput = Entry(master=frame, 
        textvariable=LowerMultVariableInput,
        font=("Arial", 10),
        width = 40,
        bd = 1,
        relief="solid",
        highlightthickness=1,
        highlightcolor="black",
        )
        LowerMultInput.place(x=100, y=140)
        LowerMultInput.insert(0, LowerMultContainerMod)
        self.listEntry.append (LowerMultInput)
        


        #Upper Multiplicity
        UpperMultiplicity = Label(master=frame,
        text="Upper ",
        foreground="black",  # Set the text color to white
        font=("Arial", 10),
        anchor = "w",
        width = 8,
        bg="white"
        )
        UpperMultiplicity.place(x=20, y=180)
        self.listLabels.append (UpperMultiplicity)
        
        
        MultiplicityUpp = Label(master=frame,
        text="Multiplicity: ",
        foreground="black",  # Set the text color to white
        font=("Arial", 10),
        anchor = "w",
        width = 8,
        bg="white"
        )
        MultiplicityUpp.place(x=20, y=200)
        self.listLabels.append (MultiplicityUpp)    


        UpperMultVariableInput = StringVar()
        UpperMultInput = Entry(master=frame, 
        textvariable=UpperMultVariableInput,
        font=("Arial", 10),
        width = 40,
        bd = 1,
        relief="solid",
        highlightthickness=1,
        highlightcolor="black",
        )
        UpperMultInput.place(x=100, y=200)
        UpperMultInput.insert(0, UpperMultContainerMod)
        self.listEntry.append (UpperMultInput)
 

        
        #Buttons

        button_right = Button(
        master=frame, 
        command = lambda: self.CheckEditContainerParameters(NameContainerMod, DescriptionInput, LowerMultInput, UpperMultInput, Module_obj), 
        text="Modify", 
        borderwidth=5,
        width=10)
        button_right.place(x=270, y=250)
        self.listButt.append (button_right)

        button_left = Button(
            master=frame, 
            command= self.TemplateFrame, 
            text="Close", 
            borderwidth=5, 
            width=10
            )
        button_left.place(x=50, y=250)  
        self.listButt.append (button_left)

    def windowEditReference (self, Reference_Obj , Container_Obj):
        ws =  Frame(master=self.root, width=500, height=550, bg="#D0CECE")
        ws.place (x=280, y=10)
        
        # Create A Main Frame
        main_frame = Frame(ws)
        main_frame.pack(fill=BOTH, expand=1)

        # Create A Canvas
        my_canvas = Canvas(main_frame, width=400, height=350,  bg="white", scrollregion=(0, 0, 1000, 1000))
        my_canvas.pack(side=LEFT, fill=BOTH, expand=1)

        # Add A Scrollbar To The Canvas
        my_scrollbar = ttk.Scrollbar(main_frame, orient=VERTICAL, command=my_canvas.yview)
        my_scrollbar.pack(side=RIGHT, fill=Y)

        # Configure The Canvas
        my_canvas.configure(yscrollcommand=my_scrollbar.set)
        my_canvas.bind('<Configure>', lambda e: my_canvas.configure(scrollregion = my_canvas.bbox("all")))

        # Create ANOTHER Frame INSIDE the Canvas
        frame = Frame(my_canvas, width=500, height=550, bg="white", borderwidth = 1, relief="solid")

        # Add that New frame To a Window In The Canvas
        my_canvas.create_window((0,0), window=frame, anchor="nw")
        
        label = Label(master=frame,
        text="Editor: Editing Reference " + Reference_Obj.Name,
        foreground="black",  # Set the text color to white
        font=("Arial", 10),
        anchor = "w",
        width = 50
        )
        label.place(x=0, y=0)
        
        #Description of module
        DescriptionModule = Label(master=frame,
        text="Description:",
        foreground="black",  # Set the text color to white
        font=("Arial", 10),
        anchor = "w",
        width = 8,
        bg="white"
        )
        DescriptionModule.place(x=20, y=50)
        
        DescriptionInput = Text(master=frame, 
        font=("Arial", 10),
        width = 40,
        height = 3,
        bd = 1,
        relief="solid",
        highlightthickness=1,
        highlightcolor="black",
        )
        DescriptionInput.place(x=100, y=50)
        DescriptionInput.insert (INSERT, Reference_Obj.Description)

        #Lower Multiplicity
        LowerMultiplicity = Label(master=frame,
        text="Lower ",
        foreground="black",  # Set the text color to white
        font=("Arial", 10),
        anchor = "w",
        width = 8,
        bg="white"
        )
        LowerMultiplicity.place(x=20, y=120)
        
        
        Multiplicity = Label(master=frame,
        text="Multiplicity: ",
        foreground="black",  # Set the text color to white
        font=("Arial", 10),
        anchor = "w",
        width = 8,
        bg="white"
        )
        Multiplicity.place(x=20, y=140)
        

        LowerMultVariableInput = StringVar()
        LowerMultInput = Entry(master=frame, 
        textvariable=LowerMultVariableInput,
        font=("Arial", 10),
        width = 40,
        bd = 1,
        relief="solid",
        highlightthickness=1,
        highlightcolor="black",
        )
        LowerMultInput.place(x=100, y=140)
        LowerMultInput.insert(0, Reference_Obj.lowMultiplicity)
        


        #Upper Multiplicity
        UpperMultiplicity = Label(master=frame,
        text="Upper ",
        foreground="black",  # Set the text color to white
        font=("Arial", 10),
        anchor = "w",
        width = 8,
        bg="white"
        )
        UpperMultiplicity.place(x=20, y=180)
        
        
        MultiplicityUpp = Label(master=frame,
        text="Multiplicity: ",
        foreground="black",  # Set the text color to white
        font=("Arial", 10),
        anchor = "w",
        width = 8,
        bg="white"
        )
        MultiplicityUpp.place(x=20, y=200)


        UpperMultVariableInput = StringVar()
        UpperMultInput = Entry(master=frame, 
        textvariable=UpperMultVariableInput,
        font=("Arial", 10),
        width = 40,
        bd = 1,
        relief="solid",
        highlightthickness=1,
        highlightcolor="black",
        )
        UpperMultInput.place(x=100, y=200)
        UpperMultInput.insert(0, Reference_Obj.uppMultiplicity)
 
        #Origin
        OriginLabel = Label(master=frame,
        text="Origin: ",
        foreground="black",  # Set the text color to white
        font=("Arial", 10),
        anchor = "w",
        width = 8,
        bg="white"
        )
        OriginLabel.place(x=20, y=230)

        
        OriginVariableInput = StringVar()
        OriginInput = Entry(master=frame, 
        textvariable=OriginVariableInput,
        font=("Arial", 10),
        width = 40,
        bd = 1,
        relief="solid",
        highlightthickness=1,
        highlightcolor="black",
        )
        OriginInput.place(x=100, y=230)

        #Destination
        DestinationLabel = Label(master=frame,
        text="Destination: ",
        foreground="black",  # Set the text color to white
        font=("Arial", 10),
        anchor = "w",
        width = 8,
        bg="white"
        )
        DestinationLabel.place(x=20, y=260)

        
        DestinationVariableInput = StringVar()
        DestinationInput = Entry(master=frame, 
        textvariable=DestinationVariableInput,
        font=("Arial", 10),
        width = 40,
        bd = 1,
        relief="solid",
        highlightthickness=1,
        highlightcolor="black",
        )
        DestinationInput.place(x=100, y=260)

        
        #Buttons

        button_right = Button(
        master=frame, 
        command = lambda: self.CheckEditReference(Reference_Obj.Name, DescriptionInput, LowerMultInput, UpperMultInput, Container_Obj), 
        text="Modify", 
        borderwidth=5,
        width=10)
        button_right.place(x=270, y=290)
        self.listButt.append (button_right)

        button_left = Button(
            master=frame, 
            command= self.TemplateFrame, 
            text="Close", 
            borderwidth=5, 
            width=10
            )
        button_left.place(x=50, y=290)  
        self.listButt.append (button_left)

    
    def windowEditParameters (self, Parameter_Obj , Container_Obj):
        
        
        NameParameterMod = Parameter_Obj.Name
        TypeParameterMod = Parameter_Obj.Parameter
        DescriptionParameterMod = Parameter_Obj.Description
        LowerMultParameterMod = Parameter_Obj.minMultiplicity
        UpperMultParameterMod = Parameter_Obj.maxMultiplicity
        IndexParameterMod = Parameter_Obj.Index
        SymbolicParameterMod = Parameter_Obj.Symbolic
        DefaultValueParameterMod = Parameter_Obj.DefaultValue
        MaxValueParameterMod = Parameter_Obj.MaxValue
        MinValueParameterMod = Parameter_Obj.MinValue
        EnumListParameterMod = Parameter_Obj.EnumListName
        
        
        ws =  Frame(master=self.root, width=500, height=550, bg="#D0CECE")
        ws.place (x=280, y=10)
        
        # Create A Main Frame
        main_frame = Frame(ws)
        main_frame.pack(fill=BOTH, expand=1)

        # Create A Canvas
        my_canvas = Canvas(main_frame, width=400, height=350,  bg="white", scrollregion=(0, 0, 1000, 1000))
        my_canvas.pack(side=LEFT, fill=BOTH, expand=1)

        # Add A Scrollbar To The Canvas
        my_scrollbar = ttk.Scrollbar(main_frame, orient=VERTICAL, command=my_canvas.yview)
        my_scrollbar.pack(side=RIGHT, fill=Y)

        # Configure The Canvas
        my_canvas.configure(yscrollcommand=my_scrollbar.set)
        my_canvas.bind('<Configure>', lambda e: my_canvas.configure(scrollregion = my_canvas.bbox("all")))

        # Create ANOTHER Frame INSIDE the Canvas
        frame = Frame(my_canvas, width=500, height=700, bg="white", borderwidth = 1, relief="solid")

        # Add that New frame To a Window In The Canvas
        my_canvas.create_window((0,0), window=frame, anchor="nw")
        
        label = Label(master=frame,
        text="Editor: Editing Parameter - " + NameParameterMod,
        foreground="black",  # Set the text color to white
        font=("Arial", 10),
        anchor = "w",
        width = 50
        )
        label.place(x=0, y=0)
        self.listLabels.append (label)

        var = 50
        
        #Type Parameter
        TypeparameterLabel = Label(master=frame,
        text="Type: ",
        foreground="black",  # Set the text color to white
        font=("Arial", 10),
        anchor = "w",
        width = 8,
        bg="white"
        )
        TypeparameterLabel.place(x=20, y=var)


        TypeParameterVariableInput = StringVar()
        TypeParameterInput = Entry(master=frame, 
        textvariable=TypeParameterVariableInput,
        font=("Arial", 10),
        width = 40,
        bd = 1,
        relief="solid",
        highlightthickness=1,
        highlightcolor="black",
        )
        TypeParameterInput.place(x=100, y=var)
        TypeParameterInput.insert(0, TypeParameterMod)

        TypeParameterInput["state"] = "disabled"
        
        var = var + 40

        #Description of module
        DescriptionModule = Label(master=frame,
        text="Description:",
        foreground="black",  # Set the text color to white
        font=("Arial", 10),
        anchor = "w",
        width = 8,
        bg="white"
        )
        DescriptionModule.place(x=20, y=var)
        self.listLabels.append (DescriptionModule)
        
        DescriptionInput = Text(master=frame, 
        font=("Arial", 10),
        width = 40,
        height = 3,
        bd = 1,
        relief="solid",
        highlightthickness=1,
        highlightcolor="black",
        )
        DescriptionInput.place(x=100, y=var)
        DescriptionInput.insert (INSERT, DescriptionParameterMod)
        self.listText.append(DescriptionInput)
        
        var = var + 60
        
        #Lower Multiplicity
        LowerMultiplicity = Label(master=frame,
        text="Lower \nMultiplicity:",
        foreground="black",  # Set the text color to white
        font=("Arial", 10),
        anchor = "w",
        width = 15,
        bg="white",
        justify = LEFT
        )
        LowerMultiplicity.place(x=20, y=var)
        self.listLabels.append (LowerMultiplicity)
        
        var = var + 20

        LowerMultVariableInput = StringVar()
        LowerMultInput = Entry(master=frame, 
        textvariable=LowerMultVariableInput,
        font=("Arial", 10),
        width = 40,
        bd = 1,
        relief="solid",
        highlightthickness=1,
        highlightcolor="black",
        )
        LowerMultInput.place(x=100, y=var)
        LowerMultInput.insert(0, LowerMultParameterMod)
        self.listEntry.append (LowerMultInput)
        
        var = var + 40

        #Upper Multiplicity
        UpperMultiplicity = Label(master=frame,
        text="Upper \nMultiplicity:",
        foreground="black",  # Set the text color to white
        font=("Arial", 10),
        anchor = "w",
        width = 15,
        bg="white",
        justify = LEFT
        )
        UpperMultiplicity.place(x=20, y=var)
        
        
        var = var + 20   


        UpperMultVariableInput = StringVar()
        UpperMultInput = Entry(master=frame, 
        textvariable=UpperMultVariableInput,
        font=("Arial", 10),
        width = 40,
        bd = 1,
        relief="solid",
        highlightthickness=1,
        highlightcolor="black",
        )
        UpperMultInput.place(x=100, y=var)
        UpperMultInput.insert(0, UpperMultParameterMod)

        var = var + 40 
        
        #index
        IndexParameter = Label(master=frame,
        text="Index: ",
        foreground="black",  # Set the text color to white
        font=("Arial", 10),
        anchor = "w",
        width = 8,
        bg="white"
        )
        IndexParameter.place(x=20, y=var)
        self.listLabels.append (IndexParameter) 

        
        IndexVariableInput = StringVar()
        IndexInput = Entry(master=frame, 
        textvariable=IndexVariableInput,
        font=("Arial", 10),
        width = 40,
        bd = 1,
        relief="solid",
        highlightthickness=1,
        highlightcolor="black",
        )
        IndexInput.place(x=100, y=var)
        IndexInput.insert(0, IndexParameterMod)
        var = var + 40 


        SymbolicParameter = Label(master=frame,
        text="Symbolic \nName: ",
        foreground="black",  # Set the text color to white
        font=("Arial", 10),
        anchor = "w",
        width = 7,
        bg="white",
        justify = LEFT
        )
        SymbolicParameter.place(x=20, y= var)

        var = var + 10 


        SymbolicVariableInput = StringVar()
        SymbolicInput = Entry(master=frame, 
        textvariable=SymbolicVariableInput,
        font=("Arial", 10),
        width = 40,
        bd = 1,
        relief="solid",
        highlightthickness=1,
        highlightcolor="black",
        )
        SymbolicInput.place(x=100, y=var)
        SymbolicInput.insert(0, SymbolicParameterMod)


        var = var + 60
        
        #Default Value - Min and Max - Enums


        enumframe =  Frame(master=frame, width=360, height=140, bg="white", borderwidth = 1, relief="groove")
        enumframe.place (x=20, y=var)


        # Create A Canvas
        my_canvas_enum = Canvas(enumframe, width=340, height=140,  bg="white", scrollregion=(0, 0, 1000, 1000))
        my_canvas_enum.pack(side=LEFT, fill=BOTH, expand=1)

        # Add A Scrollbar To The Canvas
        my_scrollbar = ttk.Scrollbar(enumframe, orient=VERTICAL, command=my_canvas_enum.yview)
        my_scrollbar.pack(side=RIGHT, fill=Y)

        # Configure The Canvas
        my_canvas_enum.configure(yscrollcommand=my_scrollbar.set)
        my_canvas_enum.bind('<Configure>', lambda e: my_canvas_enum.configure(scrollregion = my_canvas_enum.bbox("all")))

        size_frame_enum = 140
        if len (EnumListParameterMod) > 3:
            size_frame_enum = size_frame_enum + (30 * (len (EnumListParameterMod) - 3))


        # Create ANOTHER Frame INSIDE the Canvas
        frame_enum = Frame(my_canvas_enum, width=360, height=size_frame_enum, bg="white", borderwidth = 1, relief="solid")

        # Add that New frame To a Window In The Canvas
        my_canvas_enum.create_window((0,0), window=frame_enum, anchor="nw")   


        enumframeLabel = Label(master=frame_enum,
        text="Parameter Values: ",
        foreground="black",  # Set the text color to white
        font=("Arial", 10),
        anchor = "w",
        width = 20,
        bg="white",
        justify = LEFT,
        )
        enumframeLabel.place(x=0, y=0)

        var2= 40
        EnumListNameMod = []
        if TypeParameterMod != "ENUMERATION":
            #Default Value
            DefaultValueLabel = Label(master=frame_enum,
            text="Default Value:",
            foreground="black",  # Set the text color to white
            font=("Arial", 10),
            anchor = "w",
            width = 15,
            bg="white",
            justify = LEFT
            )
            DefaultValueLabel.place(x=20, y=var2)
            

            DefaultValuetVariableInput = StringVar()
            DefaultValueInput = Entry(master=frame_enum, 
            textvariable=DefaultValuetVariableInput,
            font=("Arial", 10),
            width = 30,
            bd = 1,
            relief="solid",
            highlightthickness=1,
            highlightcolor="black",
            )
            DefaultValueInput.place(x=110, y=var2)
            DefaultValueInput.insert(0, DefaultValueParameterMod)

            var2 = var2 + 30
            
            MinValueInput = None
            MaxValueInput = None
            
            if TypeParameterMod == "INTEGER" or TypeParameterMod == "FLOAT":

                #Min Value
                MinValueLabel = Label(master=frame_enum,
                text="Min Value:",
                foreground="black",  # Set the text color to white
                font=("Arial", 10),
                anchor = "w",
                width = 15,
                bg="white",
                justify = LEFT
                )
                MinValueLabel.place(x=20, y=var2)
                

                MinValueVariableInput = StringVar()
                MinValueInput = Entry(master=frame_enum, 
                textvariable=MinValueVariableInput,
                font=("Arial", 10),
                width = 30,
                bd = 1,
                relief="solid",
                highlightthickness=1,
                highlightcolor="black",
                )
                MinValueInput.place(x=110, y=var2)
                MinValueInput.insert(0, MinValueParameterMod)

                var2 = var2 + 30

                #Max Value
                MaxValueLabel = Label(master=frame_enum,
                text="Max Value:",
                foreground="black",  # Set the text color to white
                font=("Arial", 10),
                anchor = "w",
                width = 15,
                bg="white",
                justify = LEFT
                )
                MaxValueLabel.place(x=20, y=var2)
                

                MaxValueVariableInput = StringVar()
                MaxValueInput = Entry(master=frame_enum, 
                textvariable=MaxValueVariableInput,
                font=("Arial", 10),
                width = 30,
                bd = 1,
                relief="solid",
                highlightthickness=1,
                highlightcolor="black",
                )
                MaxValueInput.place(x=110, y=var2)
                MaxValueInput.insert(0, MaxValueParameterMod)

            else:
                pass

        else:
            
            idx = 0
            pos_y = 30
            DefaultValueInput = None
            MaxValueInput = None
            MinValueInput = None
            for each_enum in EnumListParameterMod:

                #Default Value
                EnumLabelName = Label(master=frame_enum,
                text="Enum " + str(idx) + ":",
                foreground="black",  # Set the text color to white
                font=("Arial", 10),
                anchor = "w",
                width = 8,
                bg="white",
                )
                EnumLabelName.place(x=20, y=pos_y)

                EnumVariableInput = StringVar()
                EnumInput = Entry(master=frame_enum, 
                textvariable=EnumVariableInput,
                font=("Arial", 10),
                width = 30,
                bd = 1,
                relief="solid",
                highlightthickness=1,
                highlightcolor="black",
                )
                EnumInput.place(x=120, y=pos_y)           
                EnumInput.insert(0, each_enum)

                EnumListNameMod.append (EnumInput)
                idx = idx + 1
                pos_y = pos_y + 30



#---------------------------------------------------------#
        var = var + 200

        
        #Buttons

        button_right = Button(
        master=frame, 
        command = lambda: self.CheckEditParameters (NameParameterMod, TypeParameterMod, DescriptionInput, LowerMultInput, UpperMultInput, IndexInput, SymbolicInput, DefaultValueInput, Parameter_Obj , Container_Obj,MinValueInput, MaxValueInput, EnumListNameMod), 
        text="Modify", 
        borderwidth=5,
        width=10)
        button_right.place(x=270, y=var)
        self.listButt.append (button_right)

        button_left = Button(
            master=frame, 
            command= self.TemplateFrame, 
            text="Close", 
            borderwidth=5, 
            width=10
            )
        button_left.place(x=50, y=var)  
        self.listButt.append (button_left)



    def CheckCreateModuleParameters (self, NameInput, VendorInput, DescriptionInput, SipInput, SipPathInput, LowerMultInput, UpperMultInput, NumContInput = 0):
        #Name
        ModuleName = NameInput.get()
        if ModuleName == "":
            messagebox.showinfo(message='Fill name field')
            return
        else:
            for each_ch in ModuleName:
                asci_ch = ord (each_ch)
                if (asci_ch ==32):
                    messagebox.showinfo(message='name field must not contain spaces')
                    return
        
        #Vendor
        VendorName = VendorInput.get()
        if VendorName == "":
            messagebox.showinfo(message='Fill vendor field')
            return
        else:
            for each_ch in VendorName:
                asci_ch = ord (each_ch)
                if (asci_ch ==32):
                    messagebox.showinfo(message='vendor field must not contain spaces')
                    return
                        
        #Description
        ModuleDescription = DescriptionInput.get("1.0",'end-1c')
        if ModuleDescription == "":
            messagebox.showinfo(message='Fill description field')
            return
        
        #Sip Name
        SipVersion = SipInput.get()
        if SipVersion == "":
            messagebox.showinfo(message='Fill sip field')
            return
        
        #Sip Path
        SipPath = SipPathInput.get ()
        if SipPath == "":
            messagebox.showinfo(message='Fill path of sip')
            return
        
        #Lower and Upper mutiplicity
        LowerMultiplicity = LowerMultInput.get()
        if LowerMultiplicity == "":
            messagebox.showinfo(message='Fill lower multiplicity')
            return        
        else:
            try:
                LowerMultiplicity = int (LowerMultiplicity)
            except:
                messagebox.showinfo(message='lower multiplicity must be a number')
                return
            
        UpperMultiplicity = UpperMultInput.get()
        if UpperMultiplicity == "":
            messagebox.showinfo(message='Fill upper multiplicity')
            return        
        else:
            try:
                UpperMultiplicity = int (UpperMultiplicity)
            except:
                messagebox.showinfo(message='upper multiplicity must be a number')
                return

        NumContainers2Create = NumContInput
        
        ReturnVal = CF.CreateFileMDArxml(self.tree, ModuleName, VendorName, ModuleDescription, SipVersion, SipPath, LowerMultiplicity, UpperMultiplicity, NumContainers2Create)
        if ReturnVal == "MS_OK":
            self.TemplateFrame()


    def CheckCreateSubcontainer (self, NameInput, DescriptionInput, LowerMultInput, UpperMultInput, Container_Obj):

        #Name
        ContainerName = NameInput.get()
        if ContainerName == "":
            messagebox.showinfo(message='Fill name field')
            return
        else:
            for each_ch in ContainerName:
                asci_ch = ord (each_ch)
                if (asci_ch ==32):
                    messagebox.showinfo(message='name field must not contain spaces')
                    return
                                
        #Description
        ContainerDescription = DescriptionInput.get("1.0",'end-1c')
        if ContainerDescription == "":
            messagebox.showinfo(message='Fill description field')
            return
        
        #Lower and Upper mutiplicity
        LowerMultiplicity = LowerMultInput.get()
        if LowerMultiplicity == "":
            messagebox.showinfo(message='Fill lower multiplicity')
            return        
        else:
            try:
                LowerMultiplicity = int (LowerMultiplicity)
            except:
                messagebox.showinfo(message='lower multiplicity must be a number')
                return
            
        UpperMultiplicity = UpperMultInput.get()
        if UpperMultiplicity == "":
            messagebox.showinfo(message='Fill upper multiplicity')
            return        
        else:
            try:
                UpperMultiplicity = int (UpperMultiplicity)
            except:
                messagebox.showinfo(message='upper multiplicity must be a number')
                return
        
        Container_Obj.setSubcontainerInContainer (ContainerName, ContainerDescription, LowerMultiplicity, UpperMultiplicity)

        Module = Container_Obj.ModuleObj
        
        ReturnVal = CF.ModifileFileMDArxml(Module.ModuleName, 
                    Module.VendorName, 
                    Module.ModuleDescription, 
                    Module.SipVersion, 
                    Module.SipPath, 
                    Module.LowMultiplicity, 
                    Module.UppMultiplicity)


        subcontainer_obj = Container_Obj.dict_subcontainers [ContainerName]
        
        selected = self.tree.focus()
        item_container = self.tree.item (selected, "text")
        #Module_obj.printModule()

        item_container = self.tree.get_children(selected)[2]
            
        
        if ReturnVal == "MS_OK":
            item_subcontainer = self.tree.insert(item_container, 'end', subcontainer_obj.ObjContainer.Name, text=subcontainer_obj.ObjContainer.Name, values = (Container_Obj, subcontainer_obj))
            self.tree.insert(item_subcontainer, 'end', text="Parameters", values = (None, "Parameters"))
            self.tree.insert(item_subcontainer, 'end', text="References", values = (None, "References"))
            self.tree.insert(item_subcontainer, 'end', text="Subcontainers", values = (None, "Subcontainers"))

            self.TemplateFrame()

    def CheckCreateReference (self, NameInput, DescriptionInput, LowerMultInput, UpperMultInput, OriginInput, DestinationInput, Container_Obj):

        #Name
        Name = NameInput.get()
        if Name == "":
            messagebox.showinfo(message='Fill name field')
            return
        else:
            for each_ch in Name:
                asci_ch = ord (each_ch)
                if (asci_ch ==32):
                    messagebox.showinfo(message='name field must not contain spaces')
                    return
                                
        #Description
        Description = DescriptionInput.get("1.0",'end-1c')
        if Description == "":
            messagebox.showinfo(message='Fill description field')
            return
        
        #Lower and Upper mutiplicity
        LowerMultiplicity = LowerMultInput.get()
        if LowerMultiplicity == "":
            messagebox.showinfo(message='Fill lower multiplicity')
            return        
        else:
            try:
                LowerMultiplicity = int (LowerMultiplicity)
            except:
                messagebox.showinfo(message='lower multiplicity must be a number')
                return
            
        UpperMultiplicity = UpperMultInput.get()
        if UpperMultiplicity == "":
            messagebox.showinfo(message='Fill upper multiplicity')
            return        
        else:
            try:
                UpperMultiplicity = int (UpperMultiplicity)
            except:
                messagebox.showinfo(message='upper multiplicity must be a number')
                return
        

        #Origin
        Origin = OriginInput.get()
        if Origin == "":
            messagebox.showinfo(message='Fill origin field')
            return
        else:
            for each_ch in Origin:
                asci_ch = ord (each_ch)
                if (asci_ch ==32):
                    messagebox.showinfo(message='Origin field must not contain spaces')
                    return        
        #Destinatino
        Destination = DestinationInput.get()
        if Destination == "":
            messagebox.showinfo(message='Fill Destination field')
            return
        else:
            for each_ch in Destination:
                asci_ch = ord (each_ch)
                if (asci_ch ==32):
                    messagebox.showinfo(message='Destination field must not contain spaces')
                    return           
        
        
        Container_Obj.setReferenceInContainer (Name, Description, LowerMultiplicity, UpperMultiplicity, Origin, Destination)

        Module = Container_Obj.ModuleObj
        
        ReturnVal = CF.ModifileFileMDArxml(Module.ModuleName, 
                    Module.VendorName, 
                    Module.ModuleDescription, 
                    Module.SipVersion, 
                    Module.SipPath, 
                    Module.LowMultiplicity, 
                    Module.UppMultiplicity)


        reference_obj = Container_Obj.dict_reference [Name]
        
        selected = self.tree.focus()
        item_container = self.tree.item (selected, "text")
        #Module_obj.printModule()

        item_container = self.tree.get_children(selected)[1]
            
        
        if ReturnVal == "MS_OK":
            item_reference = self.tree.insert(item_container, 'end', text=reference_obj.Name, values = (Container_Obj, reference_obj))
            self.TemplateFrame()



    def CheckCreateContainer (self, NameInput, DescriptionInput, LowerMultInput, UpperMultInput):

        #Name
        ContainerName = NameInput.get()
        if ContainerName == "":
            messagebox.showinfo(message='Fill name field')
            return
        else:
            for each_ch in ContainerName:
                asci_ch = ord (each_ch)
                if (asci_ch ==32):
                    messagebox.showinfo(message='name field must not contain spaces')
                    return
                                
        #Description
        ContainerDescription = DescriptionInput.get("1.0",'end-1c')
        if ContainerDescription == "":
            messagebox.showinfo(message='Fill description field')
            return
        
        #Lower and Upper mutiplicity
        LowerMultiplicity = LowerMultInput.get()
        if LowerMultiplicity == "":
            messagebox.showinfo(message='Fill lower multiplicity')
            return        
        else:
            try:
                LowerMultiplicity = int (LowerMultiplicity)
            except:
                messagebox.showinfo(message='lower multiplicity must be a number')
                return
            
        UpperMultiplicity = UpperMultInput.get()
        if UpperMultiplicity == "":
            messagebox.showinfo(message='Fill upper multiplicity')
            return        
        else:
            try:
                UpperMultiplicity = int (UpperMultiplicity)
            except:
                messagebox.showinfo(message='upper multiplicity must be a number')
                return
        

        selected = self.tree.focus()
        print (selected)
        ModuleName = self.tree.item (selected, "text")
        Module_obj = MD.ModuleCollection.dict_Modules[ModuleName]
        
        NewContainer = MD.ContainerMD ()
        NewContainer.InitContainer (Module_obj, ContainerName, ContainerDescription, LowerMultiplicity, UpperMultiplicity)
        
        Module_obj.AddContainer (NewContainer)
        #Module_obj.printModule()

        ReturnVal = CF.ModifileFileMDArxml (Module_obj.ModuleName, Module_obj.VendorName, Module_obj.ModuleDescription, Module_obj.SipVersion, Module_obj.SipPath, Module_obj.LowMultiplicity , Module_obj.UppMultiplicity)
        
        if ReturnVal == "MS_OK":
            item_container = self.tree.insert (selected, 'end', text = ContainerName, values = (Module_obj, NewContainer))
            self.tree.insert(item_container, 'end', text="Parameters", values = (None, "Parameters"))
            self.tree.insert(item_container, 'end', text="References", values = (None, "References"))
            self.tree.insert(item_container, 'end', text="Subcontainers", values = (None, "Subcontainers"))

            self.TemplateFrame()

    def CheckEditModuleParameters (self, NameInput, VendorInput, DescriptionInput, SipInput, SipPathInput, LowerMultInput, UpperMultInput, NumContInput = 0):

        #Vendor
        VendorName = VendorInput.get()
        if VendorName == "":
            messagebox.showinfo(message='Fill vendor field')
            return
        else:
            for each_ch in VendorName:
                asci_ch = ord (each_ch)
                if (asci_ch ==32):
                    messagebox.showinfo(message='vendor field must not contain spaces')
                    return
                        
        #Description
        ModuleDescription = DescriptionInput.get("1.0",'end-1c')
        if ModuleDescription == "":
            messagebox.showinfo(message='Fill description field')
            return
        
        #Sip Name
        SipVersion = SipInput.get()
        if SipVersion == "":
            messagebox.showinfo(message='Fill sip field')
            return
        
        #Sip Path
        SipPath = SipPathInput.get ()
        if SipPath == "":
            messagebox.showinfo(message='Fill path of sip')
            return
        
        #Lower and Upper mutiplicity
        LowerMultiplicity = LowerMultInput.get()
        if LowerMultiplicity == "":
            messagebox.showinfo(message='Fill lower multiplicity')
            return        
        else:
            try:
                LowerMultiplicity = int (LowerMultiplicity)
            except:
                messagebox.showinfo(message='lower multiplicity must be a number')
                return
            
        UpperMultiplicity = UpperMultInput.get()
        if UpperMultiplicity == "":
            messagebox.showinfo(message='Fill upper multiplicity')
            return        
        else:
            try:
                UpperMultiplicity = int (UpperMultiplicity)
            except:
                messagebox.showinfo(message='upper multiplicity must be a number')
                return

        print (UpperMultiplicity)
        
        ReturnVal = CF.ModifileFileMDArxml(NameInput, VendorName, ModuleDescription, SipVersion, SipPath, LowerMultiplicity, UpperMultiplicity)

        if ReturnVal == "MS_OK":
            self.TemplateFrame()

    def CheckEditContainerParameters (self, NameInput, DescriptionInput, LowerMultInput, UpperMultInput, Module_Obj, NumContInput = 0):

        
        #Description
        ContainerDescription = DescriptionInput.get("1.0",'end-1c')
        if ContainerDescription == "":
            messagebox.showinfo(message='Fill description field')
            return
        
        #Lower and Upper mutiplicity
        LowerMultiplicity = LowerMultInput.get()
        if LowerMultiplicity == "":
            messagebox.showinfo(message='Fill lower multiplicity')
            return        
        else:
            try:
                LowerMultiplicity = int (LowerMultiplicity)
            except:
                messagebox.showinfo(message='lower multiplicity must be a number')
                return
            
        UpperMultiplicity = UpperMultInput.get()
        if UpperMultiplicity == "":
            messagebox.showinfo(message='Fill upper multiplicity')
            return        
        else:
            try:
                UpperMultiplicity = int (UpperMultiplicity)
            except:
                messagebox.showinfo(message='upper multiplicity must be a number')
                return

        Module_Obj.dict_Containers[NameInput].Description = ContainerDescription
        Module_Obj.dict_Containers[NameInput].minMultiplicity = LowerMultiplicity
        Module_Obj.dict_Containers[NameInput].maxMultiplicity = UpperMultiplicity
        
        
        ReturnVal = CF.ModifileFileMDArxml(Module_Obj.ModuleName, 
                    Module_Obj.VendorName, 
                    Module_Obj.ModuleDescription, 
                    Module_Obj.SipVersion, 
                    Module_Obj.SipPath, 
                    Module_Obj.LowMultiplicity, 
                    Module_Obj.UppMultiplicity)

        if ReturnVal == "MS_OK":
            self.TemplateFrame()

    def CheckEditReference (self, Name, DescriptionInput, LowerMultInput, UpperMultInput, OriginInput, DestinationInput, Container_Obj):
               
        #Description
        Description = DescriptionInput.get("1.0",'end-1c')
        if Description == "":
            messagebox.showinfo(message='Fill description field')
            return
        
        #Lower and Upper mutiplicity
        LowerMultiplicity = LowerMultInput.get()
        if LowerMultiplicity == "":
            messagebox.showinfo(message='Fill lower multiplicity')
            return        
        else:
            try:
                LowerMultiplicity = int (LowerMultiplicity)
            except:
                messagebox.showinfo(message='lower multiplicity must be a number')
                return
            
        UpperMultiplicity = UpperMultInput.get()
        if UpperMultiplicity == "":
            messagebox.showinfo(message='Fill upper multiplicity')
            return        
        else:
            try:
                UpperMultiplicity = int (UpperMultiplicity)
            except:
                messagebox.showinfo(message='upper multiplicity must be a number')
                return
        

        #Origin
        Origin = OriginInput.get()
        if Origin == "":
            messagebox.showinfo(message='Fill origin field')
            return
        else:
            for each_ch in Origin:
                asci_ch = ord (each_ch)
                if (asci_ch ==32):
                    messagebox.showinfo(message='Origin field must not contain spaces')
                    return        
        #Destinatino
        Destination = DestinationInput.get()
        if Destination == "":
            messagebox.showinfo(message='Fill Destination field')
            return
        else:
            for each_ch in Destination:
                asci_ch = ord (each_ch)
                if (asci_ch ==32):
                    messagebox.showinfo(message='Destination field must not contain spaces')
                    return           
        
        
        Container_Obj.setReferenceInContainer (Name, Description, LowerMultiplicity, UpperMultiplicity, Origin, Destination)

        Module = Container_Obj.ModuleObj
        
        ReturnVal = CF.ModifileFileMDArxml(Module.ModuleName, 
                    Module.VendorName, 
                    Module.ModuleDescription, 
                    Module.SipVersion, 
                    Module.SipPath, 
                    Module.LowMultiplicity, 
                    Module.UppMultiplicity)


        reference_obj = Container_Obj.dict_reference [Name]
        
        selected = self.tree.focus()
        item_container = self.tree.item (selected, "text")
        #Module_obj.printModule()

        item_container = self.tree.get_children(selected)[2]
            
        
        if ReturnVal == "MS_OK":
            item_reference = self.tree.insert(item_container, 'end', text=reference_obj.Name, values = (Container_Obj, reference_obj))
            self.TemplateFrame()


    def CheckEditParameters (self, NameParameterMod, TypeParameterMod, DescriptionInput, LowerMultInput, UpperMultInput, IndexInput, SymbolicInput, DefaultValueInput, Parameter_Obj, Container_Obj, MinValueInput = None, MaxValueInput = None, EnumListParameterMod = []):
        #Description
        Description = DescriptionInput.get("1.0",'end-1c')
        if Description == "":
            messagebox.showinfo(message='Fill description field')
            return
        
        #Lower and Upper mutiplicity
        LowerMultiplicity = LowerMultInput.get()
        if LowerMultiplicity == "":
            messagebox.showinfo(message='Fill lower multiplicity')
            return        
        else:
            try:
                LowerMultiplicity = int (LowerMultiplicity)
            except:
                messagebox.showinfo(message='lower multiplicity must be a number')
                return
            
        UpperMultiplicity = UpperMultInput.get()
        if UpperMultiplicity == "":
            messagebox.showinfo(message='Fill upper multiplicity')
            return        
        else:
            try:
                UpperMultiplicity = int (UpperMultiplicity)
            except:
                messagebox.showinfo(message='upper multiplicity must be a number')
                return
            

        Index = IndexInput.get()
        if Index == "":
            messagebox.showinfo(message='Fill Index field')
            return        
        else:
            if Index != "false" and Index != "true":
                messagebox.showinfo(message='Index field must be false or true')
                return


        Symbolic = SymbolicInput.get()
        if Symbolic == "":
            messagebox.showinfo(message='Fill Symbolic Name field')
            return        
        else:
            if Symbolic != "false" and Symbolic != "true":
                messagebox.showinfo(message='Symbolic Name field must be false or true')
                return            

        Enum_Names = []
        MinValue = None
        MaxValue = None
        if TypeParameterMod == "BOOLEAN":
            DefaultValue = DefaultValueInput.get()
            if DefaultValue == "":
                messagebox.showinfo(message='Fill default value field')
                return        
            else:
                if DefaultValue != "false" and DefaultValue != "true":
                    messagebox.showinfo(message='default value must be false or true')
                    return                
            
        elif TypeParameterMod == "STRING" or TypeParameterMod == "FUNCTION":
            DefaultValue = DefaultValueInput.get()
            if DefaultValue == "":
                messagebox.showinfo(message='Fill default value field')
                return        
            else:
                for each_ch in DefaultValue:
                    asci_ch = ord (each_ch)
                    if (asci_ch ==32):
                        messagebox.showinfo(message='vendor field must not contain spaces')
                        return  

        elif TypeParameterMod == "INTEGER" or TypeParameterMod == "FLOAT":

            DefaultValue = DefaultValueInput.get()
            if DefaultValue == "":
                messagebox.showinfo(message='Fill default value field')
                return        
            else:
                try:
                    DefaultValue = int (DefaultValue)
                except:
                    messagebox.showinfo(message='default value must be a number')
                    return
                

            MinValue = MinValueInput.get()
            if MinValue == "":
                messagebox.showinfo(message='Fill min value field')
                return        
            else:
                try:
                    MinValue = int (MinValue)
                except:
                    messagebox.showinfo(message='min value must be a number')
                    return

            MaxValue = MaxValueInput.get()
            if MaxValue == "":
                messagebox.showinfo(message='Fill max value field')
                return        
            else:
                try:
                    MaxValue = int (MaxValue)
                except:
                    messagebox.showinfo(message='max value must be a number')
                    return



        elif TypeParameterMod == "ENUMERATION":

            idx = 0
            DefaultValue = None
            for each_enum in EnumListParameterMod:

                each_enumValue = each_enum.get()
                if each_enumValue == "":
                    messagebox.showinfo(message='Fill enum ' + str(idx) + ' field')
                    return 
                else:
                    for each_ch in each_enumValue:
                        asci_ch = ord (each_ch)
                        if (asci_ch ==32):
                            messagebox.showinfo(message='Enum ' + str(idx) + ' field must not contain spaces')
                            return                

                idx += 1
                Enum_Names.append(each_enumValue)
                
        Parameter_Obj.Description = Description
        Parameter_Obj.minMultiplicity = str (LowerMultiplicity)
        Parameter_Obj.maxMultiplicity = str (UpperMultiplicity)
        Parameter_Obj.Index = Index
        Parameter_Obj.Symbolic = Symbolic
        Parameter_Obj.DefaultValue = str (DefaultValue)
        Parameter_Obj.MaxValue = str (MaxValue)
        Parameter_Obj.MinValue = str (MinValue)
        Parameter_Obj.EnumListName = Enum_Names
        
        Module_Obj = Container_Obj.ModuleObj
        
        ReturnVal = CF.ModifileFileMDArxml(Module_Obj.ModuleName, 
                    Module_Obj.VendorName, 
                    Module_Obj.ModuleDescription, 
                    Module_Obj.SipVersion, 
                    Module_Obj.SipPath, 
                    Module_Obj.LowMultiplicity, 
                    Module_Obj.UppMultiplicity)

        if ReturnVal == "MS_OK":
            self.TemplateFrame()
         
    def windowCreateSubcontainer (self, Container):
        
        ws =  Frame(master=self.root, width=500, height=550, bg="#D0CECE")
        ws.place (x=280, y=10)
        
        # Create A Main Frame
        main_frame = Frame(ws)
        main_frame.pack(fill=BOTH, expand=1)

        # Create A Canvas
        my_canvas = Canvas(main_frame, width=400, height=350,  bg="white", scrollregion=(0, 0, 1000, 1000))
        my_canvas.pack(side=LEFT, fill=BOTH, expand=1)

        # Add A Scrollbar To The Canvas
        my_scrollbar = ttk.Scrollbar(main_frame, orient=VERTICAL, command=my_canvas.yview)
        my_scrollbar.pack(side=RIGHT, fill=Y)

        # Configure The Canvas
        my_canvas.configure(yscrollcommand=my_scrollbar.set)
        my_canvas.bind('<Configure>', lambda e: my_canvas.configure(scrollregion = my_canvas.bbox("all")))

        # Create ANOTHER Frame INSIDE the Canvas
        frame = Frame(my_canvas, width=500, height=550, bg="white", borderwidth = 1, relief="solid")

        # Add that New frame To a Window In The Canvas
        my_canvas.create_window((0,0), window=frame, anchor="nw")
        
        label = Label(master=frame,
        text="Editor: Creating Subcontainer",
        foreground="black",  # Set the text color to white
        font=("Arial", 10),
        anchor = "w",
        width = 50
        )
        label.place(x=0, y=0)
        self.listLabels.append (label)        
        
        
        #Name of SubContainer
        NameContainer = Label(master=frame,
        text="Name:",
        foreground="black",  # Set the text color to white
        font=("Arial", 10),
        anchor = "w",
        width = 8,
        bg="white"
        )
        NameContainer.place(x=20, y=50)
        self.listLabels.append (NameContainer)
        
        NameVariableInput = StringVar()
        NameInput = Entry(master=frame, 
        textvariable=NameVariableInput,
        font=("Arial", 10),
        width = 40,
        bd = 1,
        relief="solid",
        highlightthickness=1,
        highlightcolor="black",
        )
        NameInput.focus()
        NameInput.place(x=100, y=50)
        self.listEntry.append (NameInput)
        
        
        #Description of SubContainer
        DescriptionContainer = Label(master=frame,
        text="Description:",
        foreground="black",  # Set the text color to white
        font=("Arial", 10),
        anchor = "w",
        width = 8,
        bg="white"
        )
        DescriptionContainer.place(x=20, y=90)
        self.listLabels.append (DescriptionContainer)
        
        DescriptionInput = Text(master=frame, 
        font=("Arial", 10),
        width = 40,
        height = 3,
        bd = 1,
        relief="solid",
        highlightthickness=1,
        highlightcolor="black",
        )
        DescriptionInput.place(x=100, y=90)
        self.listText.append(DescriptionInput)

        #Lower Multiplicity
        LowerMultiplicity = Label(master=frame,
        text="Lower ",
        foreground="black",  # Set the text color to white
        font=("Arial", 10),
        anchor = "w",
        width = 8,
        bg="white"
        )
        LowerMultiplicity.place(x=20, y=150)
        self.listLabels.append (LowerMultiplicity)
        
        
        Multiplicity = Label(master=frame,
        text="Multiplicity: ",
        foreground="black",  # Set the text color to white
        font=("Arial", 10),
        anchor = "w",
        width = 8,
        bg="white"
        )
        Multiplicity.place(x=20, y=170)
        self.listLabels.append (Multiplicity)        
        

        LowerMultVariableInput = StringVar()
        LowerMultInput = Entry(master=frame, 
        textvariable=LowerMultVariableInput,
        font=("Arial", 10),
        width = 40,
        bd = 1,
        relief="solid",
        highlightthickness=1,
        highlightcolor="black",
        )
        LowerMultInput.place(x=100, y=170)
        self.listEntry.append (LowerMultInput)
        


        #Upper Multiplicity
        UpperMultiplicity = Label(master=frame,
        text="Upper ",
        foreground="black",  # Set the text color to white
        font=("Arial", 10),
        anchor = "w",
        width = 8,
        bg="white"
        )
        UpperMultiplicity.place(x=20, y=210)
        self.listLabels.append (UpperMultiplicity)
        
        
        MultiplicityUpp = Label(master=frame,
        text="Multiplicity: ",
        foreground="black",  # Set the text color to white
        font=("Arial", 10),
        anchor = "w",
        width = 8,
        bg="white"
        )
        MultiplicityUpp.place(x=20, y=230)
        self.listLabels.append (MultiplicityUpp)    


        UpperMultVariableInput = StringVar()
        UpperMultInput = Entry(master=frame, 
        textvariable=UpperMultVariableInput,
        font=("Arial", 10),
        width = 40,
        bd = 1,
        relief="solid",
        highlightthickness=1,
        highlightcolor="black",
        )
        UpperMultInput.place(x=100, y=230)
        self.listEntry.append (UpperMultInput)


        #Buttons

        button_right = Button(
        master=frame, 
        command = lambda: self.CheckCreateSubcontainer(NameInput, DescriptionInput, LowerMultInput, UpperMultInput, Container), 
        text="Create", 
        borderwidth=5,
        width=10)
        button_right.place(x=270, y=300)
        self.listButt.append (button_right)

        button_left = Button(
            master=frame, 
            command= self.TemplateFrame, 
            text="Close", 
            borderwidth=5, 
            width=10
            )
        button_left.place(x=50, y=300)  
        self.listButt.append (button_left)

    def callbackFunc (self, event, box_value, NumberOfEnumLabel, NumberOfEnum):
        if box_value.get() == "Enumeration":
            NumberOfEnumLabel["state"] = "normal"
            NumberOfEnum ["state"] = "normal"
        
        else:
            NumberOfEnumLabel["state"] = "disabled"
            NumberOfEnum ["state"] = "disabled"

    def windowCreateParameter (self, Module, Container, InpNameParameter = "", InpTypeParameter = 2, InpDescParameter = "", InpMinMultParameter = "", InpMaxMultParameter = "", InpIndexParameter = 0, InpSymbolicParameter = 0):
        
        ws =  Frame(master=self.root, width=500, height=550, bg="#D0CECE")
        ws.place (x=280, y=10)
        
        # Create A Main Frame
        main_frame = Frame(ws)
        main_frame.pack(fill=BOTH, expand=1)

        # Create A Canvas
        my_canvas = Canvas(main_frame, width=400, height=350,  bg="white", scrollregion=(0, 0, 1000, 1000))
        my_canvas.pack(side=LEFT, fill=BOTH, expand=1)

        # Add A Scrollbar To The Canvas
        my_scrollbar = ttk.Scrollbar(main_frame, orient=VERTICAL, command=my_canvas.yview)
        my_scrollbar.pack(side=RIGHT, fill=Y)

        # Configure The Canvas
        my_canvas.configure(yscrollcommand=my_scrollbar.set)
        my_canvas.bind('<Configure>', lambda e: my_canvas.configure(scrollregion = my_canvas.bbox("all")))

        # Create ANOTHER Frame INSIDE the Canvas
        frame = Frame(my_canvas, width=500, height=550, bg="white", borderwidth = 1, relief="solid")

        # Add that New frame To a Window In The Canvas
        my_canvas.create_window((0,0), window=frame, anchor="nw")
        
        label = Label(master=frame,
        text="Editor: Creating Parameter",
        foreground="black",  # Set the text color to white
        font=("Arial", 10),
        anchor = "w",
        width = 50
        )
        label.place(x=0, y=0)
        self.listLabels.append (label)        
        
        var = 50
        
        #Name of Parameter
        Name = Label(master=frame,
        text="Name:",
        foreground="black",  # Set the text color to white
        font=("Arial", 10),
        anchor = "w",
        width = 8,
        bg="white"
        )
        Name.place(x=20, y=var)
        self.listLabels.append (Name)
        
        NameVariableInput = StringVar()
        NameInput = Entry(master=frame, 
        textvariable=NameVariableInput,
        font=("Arial", 10),
        width = 40,
        bd = 1,
        relief="solid",
        highlightthickness=1,
        highlightcolor="black",
        )
        NameInput.focus()
        NameInput.place(x=100, y=var)
        NameInput.insert(0, InpNameParameter)
        self.listEntry.append (NameInput)
    
    
        #Type Parameter

        TypeParameter = Label(master=frame,
        text="Type:",
        foreground="black",  # Set the text color to white
        font=("Arial", 10),
        anchor = "w",
        width = 8,
        bg="white"
        )
        TypeParameter.place(x=20, y=var + 40)
        self.listLabels.append (TypeParameter)        

        box_value=StringVar()
              
        TypeParameterInput = ttk.Combobox(frame,
                            textvariable=box_value
                            )
        
        TypeParameterInput['values'] = ["Boolean", "Enumeration", 
                                        "Integer", "Float", "String"]

        TypeParameterInput.place(x=100, y=var + 40)
        
        
        
        #Num of enums
        EnableNumOfEnum = "disabled"            
        
        
        NumberOfEnumLabel = Label(master=frame,
        text="N. Enums:",
        foreground="black",  # Set the text color to white
        font=("Arial", 10),
        anchor = "w",
        width = 8,
        bg="white",
        state = EnableNumOfEnum
        )
        NumberOfEnumLabel.place(x=250, y=var + 40)


        NumberOfEnumInput = StringVar()
        NumberOfEnum = Entry(master=frame, 
        textvariable=NumberOfEnumInput,
        font=("Arial", 10),
        width = 8,
        bd = 1,
        relief="solid",
        highlightthickness=1,
        highlightcolor="black",
        state = EnableNumOfEnum
        )
        NumberOfEnum.place(x=330, y=var + 40)
        
        
        TypeParameterInput.bind("<<ComboboxSelected>>", lambda event: self.callbackFunc(event, box_value, NumberOfEnumLabel, NumberOfEnum))

    
        #Description of Parameter
        Description = Label(master=frame,
        text="Description:",
        foreground="black",  # Set the text color to white
        font=("Arial", 10),
        anchor = "w",
        width = 8,
        bg="white"
        )

        Description.place(x=20, y=var + 80)
        self.listLabels.append (Description)
        
        DescriptionInput = Text(master=frame, 
        font=("Arial", 10),
        width = 40,
        height = 3,
        bd = 1,
        relief="solid",
        highlightthickness=1,
        highlightcolor="black",
        )
        DescriptionInput.insert (INSERT, InpDescParameter)

        DescriptionInput.place(x=100, y=var + 80)
        self.listText.append(DescriptionInput)

        #Lower Multiplicity
        LowerMultiplicity = Label(master=frame,
        text="Lower ",
        foreground="black",  # Set the text color to white
        font=("Arial", 10),
        anchor = "w",
        width = 8,
        bg="white"
        )
        LowerMultiplicity.place(x=20, y=var + 140)
        self.listLabels.append (LowerMultiplicity)
        
        
        Multiplicity = Label(master=frame,
        text="Multiplicity: ",
        foreground="black",  # Set the text color to white
        font=("Arial", 10),
        anchor = "w",
        width = 8,
        bg="white"
        )
        Multiplicity.place(x=20, y=var + 160)
        self.listLabels.append (Multiplicity)        
        

        LowerMultVariableInput = StringVar()
        LowerMultInput = Entry(master=frame, 
        textvariable=LowerMultVariableInput,
        font=("Arial", 10),
        width = 40,
        bd = 1,
        relief="solid",
        highlightthickness=1,
        highlightcolor="black",
        )
        LowerMultInput.place(x=100, y=var + 160)
        self.listEntry.append (LowerMultInput)
        LowerMultInput.insert(0, InpMinMultParameter)



        #Upper Multiplicity
        UpperMultiplicity = Label(master=frame,
        text="Upper ",
        foreground="black",  # Set the text color to white
        font=("Arial", 10),
        anchor = "w",
        width = 8,
        bg="white"
        )
        UpperMultiplicity.place(x=20, y=var + 200)
        self.listLabels.append (UpperMultiplicity)
        
        
        MultiplicityUpp = Label(master=frame,
        text="Multiplicity: ",
        foreground="black",  # Set the text color to white
        font=("Arial", 10),
        anchor = "w",
        width = 8,
        bg="white"
        )
        MultiplicityUpp.place(x=20, y=var + 220)
        self.listLabels.append (MultiplicityUpp)    


        UpperMultVariableInput = StringVar()
        UpperMultInput = Entry(master=frame, 
        textvariable=UpperMultVariableInput,
        font=("Arial", 10),
        width = 40,
        bd = 1,
        relief="solid",
        highlightthickness=1,
        highlightcolor="black",
        )
        UpperMultInput.place(x=100, y=var + 220)
        self.listEntry.append (UpperMultInput)
        UpperMultInput.insert(0, InpMaxMultParameter)

        
        #index
        IndexParameter = Label(master=frame,
        text="Index: ",
        foreground="black",  # Set the text color to white
        font=("Arial", 10),
        anchor = "w",
        width = 8,
        bg="white"
        )
        IndexParameter.place(x=20, y=var + 260)
        self.listLabels.append (IndexParameter) 

        Index = IntVar(value = InpIndexParameter)
        IndexInput = Checkbutton(master=frame, 
            variable=Index,
            onvalue=1, 
            offvalue=0,
            bg="white"
            )
        IndexInput.place(x=100, y=var + 260)


        SymbolicParameter = Label(master=frame,
        text="Symbolic \nName: ",
        foreground="black",  # Set the text color to white
        font=("Arial", 10),
        anchor = "w",
        width = 7,
        bg="white",
        justify = LEFT
        )
        SymbolicParameter.place(x=20, y=var + 300)
        self.listLabels.append (IndexParameter) 

        SymbolicName = IntVar(value = InpSymbolicParameter)
        SymbolicNameInput = Checkbutton(master=frame, 
            variable=SymbolicName,
            onvalue=1, 
            offvalue=0,
            bg="white"
            )
        SymbolicNameInput.place(x=100, y=var + 310)

        #Buttons

        button_right = Button(
        master=frame, 
        command = lambda: self.CheckCreateParameters(Module, Container, NameInput, TypeParameterInput, DescriptionInput, LowerMultInput, UpperMultInput, Index, SymbolicName, NumberOfEnum), 
        text="Next", 
        borderwidth=5,
        width=10)
        button_right.place(x=270, y=420)
        self.listButt.append (button_right)

        button_left = Button(
            master=frame, 
            command= self.TemplateFrame, 
            text="Close", 
            borderwidth=5, 
            width=10
            )
        button_left.place(x=50, y=420)  
        self.listButt.append (button_left)


    def windowCreateReference (self, Container):
        
        ws =  Frame(master=self.root, width=500, height=550, bg="#D0CECE")
        ws.place (x=280, y=10)
        
        # Create A Main Frame
        main_frame = Frame(ws)
        main_frame.pack(fill=BOTH, expand=1)

        # Create A Canvas
        my_canvas = Canvas(main_frame, width=400, height=350,  bg="white", scrollregion=(0, 0, 1000, 1000))
        my_canvas.pack(side=LEFT, fill=BOTH, expand=1)

        # Add A Scrollbar To The Canvas
        my_scrollbar = ttk.Scrollbar(main_frame, orient=VERTICAL, command=my_canvas.yview)
        my_scrollbar.pack(side=RIGHT, fill=Y)

        # Configure The Canvas
        my_canvas.configure(yscrollcommand=my_scrollbar.set)
        my_canvas.bind('<Configure>', lambda e: my_canvas.configure(scrollregion = my_canvas.bbox("all")))

        # Create ANOTHER Frame INSIDE the Canvas
        frame = Frame(my_canvas, width=500, height=550, bg="white", borderwidth = 1, relief="solid")

        # Add that New frame To a Window In The Canvas
        my_canvas.create_window((0,0), window=frame, anchor="nw")
        
        label = Label(master=frame,
        text="Editor: Creating Reference",
        foreground="black",  # Set the text color to white
        font=("Arial", 10),
        anchor = "w",
        width = 50
        )
        label.place(x=0, y=0)
        
        
        #Name
        NameContainer = Label(master=frame,
        text="Name:",
        foreground="black",  # Set the text color to white
        font=("Arial", 10),
        anchor = "w",
        width = 8,
        bg="white"
        )
        NameContainer.place(x=20, y=50)
        
        NameVariableInput = StringVar()
        NameInput = Entry(master=frame, 
        textvariable=NameVariableInput,
        font=("Arial", 10),
        width = 40,
        bd = 1,
        relief="solid",
        highlightthickness=1,
        highlightcolor="black",
        )
        NameInput.place(x=100, y=50)
        
        
        #Description
        DescriptionContainer = Label(master=frame,
        text="Description:",
        foreground="black",  # Set the text color to white
        font=("Arial", 10),
        anchor = "w",
        width = 8,
        bg="white"
        )
        DescriptionContainer.place(x=20, y=90)
        self.listLabels.append (DescriptionContainer)
        
        DescriptionInput = Text(master=frame, 
        font=("Arial", 10),
        width = 40,
        height = 3,
        bd = 1,
        relief="solid",
        highlightthickness=1,
        highlightcolor="black",
        )
        DescriptionInput.place(x=100, y=90)
        self.listText.append(DescriptionInput)

        #Lower Multiplicity
        LowerMultiplicity = Label(master=frame,
        text="Lower ",
        foreground="black",  # Set the text color to white
        font=("Arial", 10),
        anchor = "w",
        width = 8,
        bg="white"
        )
        LowerMultiplicity.place(x=20, y=150)
        self.listLabels.append (LowerMultiplicity)
        
        
        Multiplicity = Label(master=frame,
        text="Multiplicity: ",
        foreground="black",  # Set the text color to white
        font=("Arial", 10),
        anchor = "w",
        width = 8,
        bg="white"
        )
        Multiplicity.place(x=20, y=170)
        self.listLabels.append (Multiplicity)        
        

        LowerMultVariableInput = StringVar()
        LowerMultInput = Entry(master=frame, 
        textvariable=LowerMultVariableInput,
        font=("Arial", 10),
        width = 40,
        bd = 1,
        relief="solid",
        highlightthickness=1,
        highlightcolor="black",
        )
        LowerMultInput.place(x=100, y=170)
        self.listEntry.append (LowerMultInput)
        


        #Upper Multiplicity
        UpperMultiplicity = Label(master=frame,
        text="Upper ",
        foreground="black",  # Set the text color to white
        font=("Arial", 10),
        anchor = "w",
        width = 8,
        bg="white"
        )
        UpperMultiplicity.place(x=20, y=210)
        self.listLabels.append (UpperMultiplicity)
        
        
        MultiplicityUpp = Label(master=frame,
        text="Multiplicity: ",
        foreground="black",  # Set the text color to white
        font=("Arial", 10),
        anchor = "w",
        width = 8,
        bg="white"
        )
        MultiplicityUpp.place(x=20, y=230)
        self.listLabels.append (MultiplicityUpp)    


        UpperMultVariableInput = StringVar()
        UpperMultInput = Entry(master=frame, 
        textvariable=UpperMultVariableInput,
        font=("Arial", 10),
        width = 40,
        bd = 1,
        relief="solid",
        highlightthickness=1,
        highlightcolor="black",
        )
        UpperMultInput.place(x=100, y=230)
        self.listEntry.append (UpperMultInput)


        #Origin
        OriginLabel = Label(master=frame,
        text="Origin:",
        foreground="black",  # Set the text color to white
        font=("Arial", 10),
        anchor = "w",
        width = 8,
        bg="white"
        )
        OriginLabel.place(x=20, y=260)
        
        OriginVariableInput = StringVar()
        OriginInput = Entry(master=frame, 
        textvariable=OriginVariableInput,
        font=("Arial", 10),
        width = 40,
        bd = 1,
        relief="solid",
        highlightthickness=1,
        highlightcolor="black",
        )
        OriginInput.place(x=100, y=260)



        #Destination
        DestinationLabel = Label(master=frame,
        text="Destination:",
        foreground="black",  # Set the text color to white
        font=("Arial", 10),
        anchor = "w",
        width = 8,
        bg="white"
        )
        DestinationLabel.place(x=20, y=290)
        
        DestinationVariableInput = StringVar()
        DestinationInput = Entry(master=frame, 
        textvariable=DestinationVariableInput,
        font=("Arial", 10),
        width = 40,
        bd = 1,
        relief="solid",
        highlightthickness=1,
        highlightcolor="black",
        )
        DestinationInput.place(x=100, y=290)

        #Buttons

        button_right = Button(
        master=frame, 
        command = lambda: self.CheckCreateReference(NameInput, DescriptionInput, LowerMultInput, UpperMultInput, OriginInput, DestinationInput, Container), 
        text="Create", 
        borderwidth=5,
        width=10)
        button_right.place(x=270, y=330)
        self.listButt.append (button_right)

        button_left = Button(
            master=frame, 
            command= self.TemplateFrame, 
            text="Close", 
            borderwidth=5, 
            width=10
            )
        button_left.place(x=50, y=330)  
        self.listButt.append (button_left)




 

    def CheckCreateParameters (self, Module, Container, NameInput, TypeParameterInput, DescriptionInput, LowerMultInput, UpperMultInput, IndexInput, SymbolicNameInput, NumberOfEnum):
        
        #Name
        ParameterName = NameInput.get()
        if ParameterName == "":
            messagebox.showinfo(message='Fill name field')
            return
        else:
            for each_ch in ParameterName:
                asci_ch = ord (each_ch)
                if (asci_ch ==32):
                    messagebox.showinfo(message='name field must not contain spaces')
                    return
        
        #Type
        ParameterType = TypeParameterInput.get()
        if ParameterType == "":
            messagebox.showinfo(message='Choose a type')
            return

        if ParameterType == "Enumeration":
            Num_Enum = NumberOfEnum.get()
            if Num_Enum == "":
                messagebox.showinfo(message='Fill Number of Enums')
                return        
            else:
                try:
                    Num_Enum = int (Num_Enum)
                    if Num_Enum <= 0:
                        messagebox.showinfo(message='Enum must be greter than 0')
                        return
                except:
                    messagebox.showinfo(message='Enum Number must be a number')
                    return
        else:
            Num_Enum = ""         
        #Description
        ParameterDescription = DescriptionInput.get("1.0",'end-1c')
        if ParameterDescription == "":
            messagebox.showinfo(message='Fill description field')
            return
        
        #Lower and Upper mutiplicity
        LowerMultiplicity = LowerMultInput.get()
        if LowerMultiplicity == "":
            messagebox.showinfo(message='Fill lower multiplicity')
            return        
        else:
            try:
                LowerMultiplicity = int (LowerMultiplicity)
            except:
                messagebox.showinfo(message='lower multiplicity must be a number')
                return
            
        UpperMultiplicity = UpperMultInput.get()
        if UpperMultiplicity == "":
            messagebox.showinfo(message='Fill upper multiplicity')
            return        
        else:
            try:
                UpperMultiplicity = int (UpperMultiplicity)
            except:
                messagebox.showinfo(message='upper multiplicity must be a number')
                return
        
        
        if IndexInput.get() == 0:
            IndexInput = "false"
        else:
            IndexInput = "true"

        if SymbolicNameInput.get() == 0:
            SymbolicNameInput = "false"
        else:
            SymbolicNameInput = "true"
        
        
        self.definingTypeParameter (Module, Container, ParameterName, ParameterType, ParameterDescription, LowerMultiplicity, UpperMultiplicity, IndexInput, SymbolicNameInput, Num_Enum)
    
    def definingTypeParameter (self, Module, Container, NameInput, TypeParameterInput, DescriptionInput, LowerMultInput, UpperMultInput, IndexInput, SymbolicNameInput, Num_Enum):
        ws =  Frame(master=self.root, width=500, height=550, bg="#D0CECE")
        ws.place (x=280, y=10)
        
        # Create A Main Frame
        main_frame = Frame(ws)
        main_frame.pack(fill=BOTH, expand=1)

        # Create A Canvas
        my_canvas = Canvas(main_frame, width=400, height=350,  bg="white", scrollregion=(0, 0, 1000, 1000))
        my_canvas.pack(side=LEFT, fill=BOTH, expand=1)

        # Add A Scrollbar To The Canvas
        my_scrollbar = ttk.Scrollbar(main_frame, orient=VERTICAL, command=my_canvas.yview)
        my_scrollbar.pack(side=RIGHT, fill=Y)

        # Configure The Canvas
        my_canvas.configure(yscrollcommand=my_scrollbar.set)
        my_canvas.bind('<Configure>', lambda e: my_canvas.configure(scrollregion = my_canvas.bbox("all")))

        # Create ANOTHER Frame INSIDE the Canvas
        frame = Frame(my_canvas, width=500, height=600, bg="white", borderwidth = 1, relief="solid")

        # Add that New frame To a Window In The Canvas
        my_canvas.create_window((0,0), window=frame, anchor="nw")        
        

        var = 50
        
        bool_statetype = "disabled"
        bool_boxstatetype = "disabled"
        integerfloat_statetype = "disabled"
        string_statetype = "disabled"
        enum_statetype = "disabled"
        
        
        
        if TypeParameterInput == "Boolean":
            bool_statetype ="normal"
            bool_boxstatetype = "readonly"

        elif TypeParameterInput == "Integer" or TypeParameterInput == "Float":
            integerfloat_statetype ="normal"
 
        elif TypeParameterInput == "String":
            string_statetype ="normal"
        
        elif TypeParameterInput == "Enumeration":
            enum_statetype ="normal" 
        #----------------- boolean ---------------- #
        
        boolframe =  Frame(master=frame, width=360, height=80, bg="white", borderwidth = 1, relief="groove")
        boolframe.place (x=20, y=20)
        
        boolframeLabel = Label(master=boolframe,
        text="Boolean Parameters: ",
        foreground="black",  # Set the text color to white
        font=("Arial", 10),
        anchor = "w",
        width = 20,
        bg="white",
        justify = LEFT,
        state= bool_statetype
        )
        boolframeLabel.place(x=0, y=0)


        #Default Value
        DefaultValueBool = Label(master=boolframe,
        text="Default Value:",
        foreground="black",  # Set the text color to white
        font=("Arial", 10),
        anchor = "w",
        width = 15,
        bg="white",
        state= bool_statetype
        )
        DefaultValueBool.place(x=20, y=30)


        DefaultValueBoolVariableInput=StringVar()
        vlist = ["false", "true"]
        
        DefaultValueBoolInput = ttk.Combobox(boolframe, 
                            values = vlist,
                            textvariable=DefaultValueBoolVariableInput,
                            state=bool_boxstatetype
                            )
        
        DefaultValueBoolInput.place(x=140, y=30)

        #-------------- Integer or Float ------------- #
        integerfloatframe =  Frame(master=frame, width=360, height=140, bg="white", borderwidth = 1, relief="groove")
        integerfloatframe.place (x=20, y=120)

        integerfloatframeLabel = Label(master=integerfloatframe,
        text="Integer and float Parameters: ",
        foreground="black",  # Set the text color to white
        font=("Arial", 10),
        anchor = "w",
        width = 30,
        bg="white",
        justify = LEFT,
        state= integerfloat_statetype
        )
        integerfloatframeLabel.place(x=0, y=0)


        #Default Value
        DefaultValueIntegerFloat = Label(master=integerfloatframe,
        text="Default Value:",
        foreground="black",  # Set the text color to white
        font=("Arial", 10),
        anchor = "w",
        width = 15,
        bg="white",
        state= integerfloat_statetype
        )
        DefaultValueIntegerFloat.place(x=20, y=30)

        DefaultValueVariableIntegerFloatInput = StringVar()
        DefaultValueIntegerFloatInput = Entry(master=integerfloatframe, 
        textvariable=DefaultValueVariableIntegerFloatInput,
        font=("Arial", 10),
        width = 30,
        bd = 1,
        relief="solid",
        highlightthickness=1,
        highlightcolor="black",
        state= integerfloat_statetype
        )
        DefaultValueIntegerFloatInput.place(x=120, y=30)

        #Min Value
        MintValue = Label(master=integerfloatframe,
        text="Min Value:",
        foreground="black",  # Set the text color to white
        font=("Arial", 10),
        anchor = "w",
        width = 8,
        bg="white",
        state= integerfloat_statetype
        )
        MintValue.place(x=20, y=60)

        MintValueVariableInput = StringVar()
        MintValueInput = Entry(master=integerfloatframe, 
        textvariable=MintValueVariableInput,
        font=("Arial", 10),
        width = 30,
        bd = 1,
        relief="solid",
        highlightthickness=1,
        highlightcolor="black",
        state= integerfloat_statetype
        )
        MintValueInput.place(x=120, y=60)
        

        #Max Value
        MaxtValue = Label(master=integerfloatframe,
        text="Max Value:",
        foreground="black",  # Set the text color to white
        font=("Arial", 10),
        anchor = "w",
        width = 8,
        bg="white",
        state= integerfloat_statetype
        )
        MaxtValue.place(x=20, y=90)

        MaxtValueVariableInput = StringVar()
        MaxtValueInput = Entry(master=integerfloatframe, 
        textvariable=MaxtValueVariableInput,
        font=("Arial", 10),
        width = 30,
        bd = 1,
        relief="solid",
        highlightthickness=1,
        highlightcolor="black",
        state= integerfloat_statetype
        )
        MaxtValueInput.focus()
        MaxtValueInput.place(x=120, y=90)


        #----------------- String ---------------- #
        
        stringframe =  Frame(master=frame, width=360, height=80, bg="white", borderwidth = 1, relief="groove")
        stringframe.place (x=20, y=280)
        
        stringframeLabel = Label(master=stringframe,
        text="String Parameters: ",
        foreground="black",  # Set the text color to white
        font=("Arial", 10),
        anchor = "w",
        width = 20,
        bg="white",
        justify = LEFT,
        state= string_statetype
        )
        stringframeLabel.place(x=0, y=0)


        #Default Value
        DefaultValueStr = Label(master=stringframe,
        text="Default Value:",
        foreground="black",  # Set the text color to white
        font=("Arial", 10),
        anchor = "w",
        width = 15,
        bg="white",
        state= string_statetype
        )
        DefaultValueStr.place(x=20, y=30)

        DefaultValueVariableStrInput = StringVar()
        DefaultValueStrInput = Entry(master=stringframe, 
        textvariable=DefaultValueVariableStrInput,
        font=("Arial", 10),
        width = 30,
        bd = 1,
        relief="solid",
        highlightthickness=1,
        highlightcolor="black",
        state= string_statetype
        )
        DefaultValueStrInput.place(x=120, y=30)


        #----------------- Enums ---------------- #
        if Num_Enum == "" or Num_Enum == None:
            Num_Enum = 0
        
        Num_Enum = int (Num_Enum)
        
        enumframe =  Frame(master=frame, width=360, height=140, bg="white", borderwidth = 1, relief="groove")
        enumframe.place (x=20, y=380)


        # Create A Canvas
        my_canvas_enum = Canvas(enumframe, width=340, height=140,  bg="white", scrollregion=(0, 0, 1000, 1000))
        my_canvas_enum.pack(side=LEFT, fill=BOTH, expand=1)

        # Add A Scrollbar To The Canvas
        my_scrollbar = ttk.Scrollbar(enumframe, orient=VERTICAL, command=my_canvas_enum.yview)
        my_scrollbar.pack(side=RIGHT, fill=Y)

        # Configure The Canvas
        my_canvas_enum.configure(yscrollcommand=my_scrollbar.set)
        my_canvas_enum.bind('<Configure>', lambda e: my_canvas_enum.configure(scrollregion = my_canvas_enum.bbox("all")))

        size_frame_enum = 140
        if Num_Enum > 3:
            size_frame_enum = size_frame_enum + (30 * (Num_Enum - 3))


        # Create ANOTHER Frame INSIDE the Canvas
        frame_enum = Frame(my_canvas_enum, width=360, height=size_frame_enum, bg="white", borderwidth = 1, relief="solid")

        # Add that New frame To a Window In The Canvas
        my_canvas_enum.create_window((0,0), window=frame_enum, anchor="nw")   


        enumframeLabel = Label(master=frame_enum,
        text="Enum Parameters: ",
        foreground="black",  # Set the text color to white
        font=("Arial", 10),
        anchor = "w",
        width = 20,
        bg="white",
        justify = LEFT,
        state= enum_statetype
        )
        enumframeLabel.place(x=0, y=0)

        
        enum_list = []


            
        pos_y = 30
        for each_enum in range(0,int(Num_Enum)):

            #Default Value
            EnumLabelName = Label(master=frame_enum,
            text="Enum " + str(each_enum) + ":",
            foreground="black",  # Set the text color to white
            font=("Arial", 10),
            anchor = "w",
            width = 8,
            bg="white",
            state= enum_statetype
            )
            EnumLabelName.place(x=20, y=pos_y)

            EnumVariableInput = StringVar()
            EnumInput = Entry(master=frame_enum, 
            textvariable=EnumVariableInput,
            font=("Arial", 10),
            width = 30,
            bd = 1,
            relief="solid",
            highlightthickness=1,
            highlightcolor="black",
            state= enum_statetype
            )
            EnumInput.place(x=120, y=pos_y)           
            enum_list.append (EnumInput)
            pos_y = pos_y + 30
        #Buttons

        button_right = Button(
        master=frame,
        command = lambda: self.checkParameterInputs(Module, Container, NameInput, TypeParameterInput, DescriptionInput, LowerMultInput, UpperMultInput, IndexInput, SymbolicNameInput, DefaultValueBoolInput,DefaultValueIntegerFloatInput, MaxtValueInput, MintValueInput, DefaultValueStrInput, enum_list), 
        text="Generate", 
        borderwidth=5,
        width=10)
        button_right.place(x=270, y=500+40)
        self.listButt.append (button_right)

        button_left = Button(
            master=frame, 
            command= lambda: self.windowCreateParameter (Module, Container, NameInput, TypeParameterInput, DescriptionInput, LowerMultInput, UpperMultInput, IndexInput, SymbolicNameInput), 
            text="Back", 
            borderwidth=5, 
            width=10
            )
        button_left.place(x=50, y=500+40)  
        self.listButt.append (button_left)


    
    def checkParameterInputs(self, Module, Container, ParameterName, TypeParameterInput, ParameterDescription, ParameterMinMultiplicity, ParameterMaxMultiplicity, IndexInput, SymbolicNameInput, DefaultValueBoolInput, DefaultValueIntegerFloatInput, MaxtValueInput, MintValueInput, DefaultValueStrInput, enum_list):
        
        
        Enum_Names = []
        if TypeParameterInput == "Boolean":
            
            DefaultValueBool = DefaultValueBoolInput.get()
            if DefaultValueBool == "":
                messagebox.showinfo(message='Choose a Default Value')
                return

            DefaultValueInput = DefaultValueBool
            MinValue = None
            MaxValue = None

        elif TypeParameterInput == "Integer" or TypeParameterInput == "Float":
            DefaultValueIntegerFloat = DefaultValueIntegerFloatInput.get()
            
            if DefaultValueIntegerFloat == "":
                messagebox.showinfo(message='Fill the Default Value')
                return        
            else:
                try:
                    DefaultValueIntegerFloat = int (DefaultValueIntegerFloat)
                except:
                    messagebox.showinfo(message='Default value must be a number')
                    return

            DefaultValueInput = DefaultValueIntegerFloat
            
            MinValue = MintValueInput.get()
            if MinValue == "":
                messagebox.showinfo(message='Fill the Min Value')
                return        
            else:
                try:
                    MinValue = int (MinValue)
                except:
                    messagebox.showinfo(message='Min value must be a number')
                    return
                

            MaxValue = MaxtValueInput.get()
            if MaxValue == "":
                messagebox.showinfo(message='Fill the Max Value')
                return        
            else:
                try:
                    MaxValue = int (MaxValue)
                except:
                    messagebox.showinfo(message='Max value must be a number')
                    return



        elif TypeParameterInput == "String":
            
            DefaultValueStr = DefaultValueStrInput.get()
            if DefaultValueStr == "":
                messagebox.showinfo(message='Fill Default Value')
                return 
            else:
                for each_ch in DefaultValueStr:
                    asci_ch = ord (each_ch)
                    if (asci_ch ==32):
                        messagebox.showinfo(message='name field must not contain spaces')
                        return

            DefaultValueInput = DefaultValueStr
            MinValue = None
            MaxValue = None
        elif TypeParameterInput == "Enumeration":
            idx = 0 
            for each_enum in enum_list:

                each_enumValue = each_enum.get()
                if each_enumValue == "":
                    messagebox.showinfo(message='Fill enum ' + str(idx) + ' field')
                    return 
                else:
                    for each_ch in each_enumValue:
                        asci_ch = ord (each_ch)
                        if (asci_ch ==32):
                            messagebox.showinfo(message='Enum ' + str(idx) + ' field must not contain spaces')
                            return                

                idx += 1
                Enum_Names.append(each_enumValue)
            DefaultValueInput = None
            MinValue = None
            MaxValue = None 
                
        Container.setParameterInContainer (ParameterName, ParameterDescription, ParameterMinMultiplicity, ParameterMaxMultiplicity, TypeParameterInput, IndexInput, SymbolicNameInput, DefaultValueInput, MaxValue, MinValue, Enum_Names)
        ReturnVal = CF.ModifileFileMDArxml(Module.ModuleName, 
                    Module.VendorName, 
                    Module.ModuleDescription, 
                    Module.SipVersion, 
                    Module.SipPath, 
                    Module.LowMultiplicity, 
                    Module.UppMultiplicity)


        parameter_obj = Container.dict_Parameters [ParameterName]
        
        selected = self.tree.focus()
        item_container = self.tree.item (selected, "text")
        #Module_obj.printModule()

        item_parameters = self.tree.get_children(selected)[0]
            
        
        if ReturnVal == "MS_OK":
            self.tree.insert(item_parameters, 'end', text=parameter_obj.Name, values = (Container, parameter_obj))
            self.TemplateFrame()

        
    def menuBar (self):
        
        menubar = Menu(self.root)
        self.root.config(menu=menubar)

        file_menu = Menu(menubar)
        file_menu = Menu(menubar, tearoff=False)


        # add menu items to the File menu
        file_menu.add_command(
            label='New',
            command=self.windowCreateModule
        )
        
        file_menu.add_command(
            label='Load...',
            command=self.select_file
        )
        
        file_menu.add_separator()

        # add Exit menu item
        file_menu.add_command(
            label='Exit',
            command=self.root.destroy
        )

        # add the File menu to the menubar
        menubar.add_cascade(
            label="File",
            menu=file_menu
        )
        # create the Help menu
        help_menu = Menu(
            menubar,
            tearoff=0
        )

        help_menu.add_command(label='Welcome')
        help_menu.add_command(label='About...')

        # add the Help menu to the menubar
        menubar.add_cascade(
            label="Help",
            menu=help_menu
        )


    def treeView (self):


        frame = Frame(master=self.root, width=250, height=550, bg="white", borderwidth = 4, relief='sunken')
        frame.place (x=10, y=20)
        self.listFrames.append (frame)
        
        self.tree = ttk.Treeview(frame, height=27)
        self.tree.heading ("#0",text="Modules",anchor=W, )
        # Inserted at the root, program chooses id:
        #self.tree.insert('', 'end', 'widgets', text='Widget Tour')
        #self.tree.insert('', 'end', 'Container', text='Container1')    
        '''tree.insert('Container', 'end', text='Container2') 
        tree.insert('Container', 'end', text='Container3')
        tree.insert('Container', 'end', text='Container4')        
        # Same thing, but inserted as first child:
        tree.insert('', 0, 'gallery', text='Applications')
        tree.insert("gallery","end",text ="HelloWorld")
        # Treeview chooses the id:
        id = tree.insert('', 'end', text='Tutorial')

        # Inserted underneath an existing node:
        tree.insert('widgets', 'end', text='Canvas')
        tree.insert(id, 'end', text='Tree')
        tree.insert(id, 'end', text='Juan')'''
        self.tree.place(x=10, y=10,  height=470, width = 200)


        s = ttk.Scrollbar(frame, orient=VERTICAL, command=self.tree.yview)
        s.place(x=215, y=10,  height=470)
        self.tree['yscrollcommand'] = s.set


        h = ttk.Scrollbar(frame, orient= HORIZONTAL, command=self.tree.xview)
        h.place(x=10, y=480, width = 200)
        self.tree['xscrollcommand'] = h.set

        
        NewButton = Button (
            frame, 
            text = "New Module",
            command = self.windowCreateModule
            )
        NewButton.place (x= 20, y= 500)
 
        DeleteButton = Button (
            frame, 
            text = "Delete Module",
            command = self.delete_module
            )
        DeleteButton.place (x= 120, y= 500) 
        
        self.tree.bind ("<<TreeviewSelect>>", self.select_module)
        
        
        
    def windowShowModule (self, Module):
        ws =  Frame(master=self.root, width=400, height=350, bg="#D0CECE")
        ws.place (x=280, y=10)
        
        # Create A Main Frame
        main_frame = Frame(ws)
        main_frame.pack(fill=BOTH, expand=1)

        # Create A Canvas
        my_canvas = Canvas(main_frame, width=400, height=350,  bg="white", scrollregion=(0, 0, 0, 0))
        my_canvas.pack(side=LEFT, fill=BOTH, expand=1)

        # Add A Scrollbar To The Canvas
        my_scrollbar = ttk.Scrollbar(main_frame, orient=VERTICAL, command=my_canvas.yview)
        my_scrollbar.pack(side=RIGHT, fill=Y)

        # Configure The Canvas
        my_canvas.configure(yscrollcommand=my_scrollbar.set)
        my_canvas.bind('<Configure>', lambda e: my_canvas.configure(scrollregion = my_canvas.bbox("all")))

        # Create ANOTHER Frame INSIDE the Canvas
        frame = Frame(my_canvas, width=500, height=550, bg="white", borderwidth = 1, relief="solid")

        # Add that New frame To a Window In The Canvas
        my_canvas.create_window((0,0), window=frame, anchor="nw")

        
        label = Label(master=frame,
        text="Editor: Module - " + Module.ModuleName,
        foreground="black",  # Set the text color to white
        font=("Arial", 10),
        anchor = "w",
        width = 50
        )
        label.place(x=0, y=0)
        self.listLabels.append (label)

        ver = 50
        
        #Name of module
        NameModule = Label(master=frame,
        text="Name: "+ Module.ModuleName,
        foreground="black",  # Set the text color to white
        font=("Arial", 10),
        anchor = "w",
        width = 40,
        bg="white"
        )
        NameModule.place(x=20, y=ver)

        #Vendor of module
        VendorModule = Label(master=frame,
        text="Vendor: "+ Module.VendorName,
        foreground="black",  # Set the text color to white
        font=("Arial", 10),
        anchor = "w",
        width = 40,
        bg="white"
        )
        VendorModule.place(x=20, y=ver+20)

        #Description of module
        DescriptionModule = Label(master=frame,
        text="Description: "+ Module.ModuleDescription,
        foreground="black",  # Set the text color to white
        font=("Arial", 10),
        anchor = "w",
        width = 40,
        bg="white"
        )
        DescriptionModule.place(x=20, y=ver+40)

        #Sip Version
        SipModule = Label(master=frame,
        text="Sip Version: "+ Module.SipVersion,
        foreground="black",  # Set the text color to white
        font=("Arial", 10),
        anchor = "w",
        width = 40,
        bg="white"
        )
        SipModule.place(x=20, y=ver+60)

        #Sip path
        SipPathModule = Label(master=frame,
        text="Sip path: "+ Module.SipPath,
        foreground="black",  # Set the text color to white
        font=("Arial", 10),
        anchor = "w",
        width = 40,
        bg="white"
        )
        SipPathModule.place(x=20, y=ver+80)

        #Lower Multiplicity
        LowerMultModule = Label(master=frame,
        text="Lower Multiplicity: " + str(Module.LowMultiplicity),
        foreground="black",  # Set the text color to white
        font=("Arial", 10),
        anchor = "w",
        width = 40,
        bg="white"
        )
        LowerMultModule.place(x=20, y=ver+100)
            
        #Upper Multiplicity
        UpperMultModule = Label(master=frame,
        text="Upper Multiplicity: "+ str(Module.UppMultiplicity),
        foreground="black",  # Set the text color to white
        font=("Arial", 10),
        anchor = "w",
        width = 40,
        bg="white"
        )
        UpperMultModule.place(x=20, y=ver+120)     
           
        #Num Containers
        NumContModule = Label(master=frame,
        text="Number of Containers: "+ str(Module.NumContainers),
        foreground="black",  # Set the text color to white
        font=("Arial", 10),
        anchor = "w",
        width = 40,
        bg="white"
        )
        NumContModule.place(x=20, y=ver+140)
        
        button_right = Button(
            master=frame, 
            command = self.windowCreateContainer, 
            text="Create Container", 
            borderwidth=5,
            width=13
            )
        button_right.place(x=250, y=ver + 200)
        self.listButt.append (button_right)

        button_left = Button(
            master=frame,   
            command= lambda: self.windowEditModule(
                Module.ModuleName,
                Module.VendorName,
                Module.ModuleDescription,
                Module.SipVersion,
                Module.SipPath,
                Module.LowMultiplicity,
                Module.UppMultiplicity
                ), 
            text="Edit Module", 
            borderwidth=5, 
            width=13
            )
        button_left.place(x=50, y=ver + 200) 

    def windowShowContainer (self, Module, Container):
        ws =  Frame(master=self.root, width=400, height=350, bg="#D0CECE")
        ws.place (x=280, y=10)
        
        # Create A Main Frame
        main_frame = Frame(ws)
        main_frame.pack(fill=BOTH, expand=1)

        # Create A Canvas
        my_canvas = Canvas(main_frame, width=400, height=350,  bg="white", scrollregion=(0, 0, 0, 0))
        my_canvas.pack(side=LEFT, fill=BOTH, expand=1)

        # Add A Scrollbar To The Canvas
        my_scrollbar = ttk.Scrollbar(main_frame, orient=VERTICAL, command=my_canvas.yview)
        my_scrollbar.pack(side=RIGHT, fill=Y)

        # Configure The Canvas
        my_canvas.configure(yscrollcommand=my_scrollbar.set)
        my_canvas.bind('<Configure>', lambda e: my_canvas.configure(scrollregion = my_canvas.bbox("all")))

        # Create ANOTHER Frame INSIDE the Canvas
        frame = Frame(my_canvas, width=500, height=550, bg="white", borderwidth = 1, relief="solid")

        # Add that New frame To a Window In The Canvas
        my_canvas.create_window((0,0), window=frame, anchor="nw")

        
        label = Label(master=frame,
        text="Editor: Container - " + Container.Name + " - Module - " + Module.ModuleName,
        foreground="black",  # Set the text color to white
        font=("Arial", 10),
        anchor = "w",
        width = 50
        )
        label.place(x=0, y=0)
        self.listLabels.append (label)

        ver = 50
        
        #Name of module
        NameModule = Label(master=frame,
        text="Name: "+ Container.Name,
        foreground="black",  # Set the text color to white
        font=("Arial", 10),
        anchor = "w",
        width = 40,
        bg="white"
        )
        NameModule.place(x=20, y=ver)


        #Description of module
        DescriptionModule = Label(master=frame,
        text="Description: "+ Container.Description,
        foreground="black",  # Set the text color to white
        font=("Arial", 10),
        anchor = "w",
        width = 40,
        bg="white"
        )
        DescriptionModule.place(x=20, y=ver+20)

        #Lower Multiplicity
        LowerMultModule = Label(master=frame,
        text="Lower Multiplicity: " + str(Container.minMultiplicity),
        foreground="black",  # Set the text color to white
        font=("Arial", 10),
        anchor = "w",
        width = 40,
        bg="white"
        )
        LowerMultModule.place(x=20, y=ver+40)
            
        #Upper Multiplicity
        UpperMultModule = Label(master=frame,
        text="Upper Multiplicity: "+ str(Container.maxMultiplicity),
        foreground="black",  # Set the text color to white
        font=("Arial", 10),
        anchor = "w",
        width = 40,
        bg="white"
        )
        UpperMultModule.place(x=20, y=ver+60)     
           
        #Num SubContainers
        NumSubContainers = Label(master=frame,
        text="Number of Subcontainers: "+ str(Container.NumSubContainer),
        foreground="black",  # Set the text color to white
        font=("Arial", 10),
        anchor = "w",
        width = 40,
        bg="white"
        )
        NumSubContainers.place(x=20, y=ver+80)

        #Num parameters
        NumParameters = Label(master=frame,
        text="Number of Parameters: "+ str(Container.NumParameters),
        foreground="black",  # Set the text color to white
        font=("Arial", 10),
        anchor = "w",
        width = 40,
        bg="white"
        )
        NumParameters.place(x=20, y=ver+100)
        
        buttonR_CreateSubCont = Button(
            master=frame,
            command = lambda: self.windowCreateSubcontainer(Container),
            text="Create Subcontainer", 
            borderwidth=5,
            width=15
            )
        buttonR_CreateSubCont.place(x=250, y=ver + 160)
        self.listButt.append (buttonR_CreateSubCont)


        buttonL_CreateParameter = Button(
            master=frame, 
            command = lambda: self.windowCreateParameter(Module, Container),
            text="Create Parameter", 
            borderwidth=5,
            width=15
            )
        buttonL_CreateParameter.place(x=50, y=ver + 160)
        self.listButt.append (buttonL_CreateParameter)


        button_CreateReference = Button(
            master=frame, 
            command = lambda: self.windowCreateReference(Container),
            text="Create Reference", 
            borderwidth=5,
            width=15
            )
        button_CreateReference.place(x=50, y=ver + 270)



        buttonR_ModifyContainer = Button(
            master=frame, 
            command= lambda: self.windowEditContainer(
                Container.Name,
                Container.Description,
                Container.minMultiplicity,
                Container.maxMultiplicity,
                Module
                ),             
            text="Modify Container", 
            borderwidth=5,
            width=15
            )
        buttonR_ModifyContainer.place(x=250, y=ver + 220)
        self.listButt.append (buttonR_ModifyContainer)


        buttonL_DeleteContainer = Button(
            master=frame, 
            command = self.delete_container,
            text="Delete Container", 
            borderwidth=5,
            width=15
            )
        buttonL_DeleteContainer.place(x=50, y=ver + 220)
        self.listButt.append (buttonL_DeleteContainer)

    def windowShowParameterContainer (self, Container, Parameter):
        ws =  Frame(master=self.root, width=400, height=350, bg="#D0CECE")
        ws.place (x=280, y=10)
        
        # Create A Main Frame
        main_frame = Frame(ws)
        main_frame.pack(fill=BOTH, expand=1)

        # Create A Canvas
        my_canvas = Canvas(main_frame, width=400, height=350,  bg="white", scrollregion=(0, 0, 0, 0))
        my_canvas.pack(side=LEFT, fill=BOTH, expand=1)

        # Add A Scrollbar To The Canvas
        my_scrollbar = ttk.Scrollbar(main_frame, orient=VERTICAL, command=my_canvas.yview)
        my_scrollbar.pack(side=RIGHT, fill=Y)

        # Configure The Canvas
        my_canvas.configure(yscrollcommand=my_scrollbar.set)
        my_canvas.bind('<Configure>', lambda e: my_canvas.configure(scrollregion = my_canvas.bbox("all")))

        # Create ANOTHER Frame INSIDE the Canvas
        frame = Frame(my_canvas, width=500, height=550, bg="white", borderwidth = 1, relief="solid")

        # Add that New frame To a Window In The Canvas
        my_canvas.create_window((0,0), window=frame, anchor="nw")        

        label = Label(master=frame,
        text="Editor: Parameter - " + Parameter.Name + " - Container - " + Container.Name,
        foreground="black",  # Set the text color to white
        font=("Arial", 10),
        anchor = "w",
        width = 50
        )
        label.place(x=0, y=0)
        
        var = 50
        
        #Name of Parameter
        Name = Label(master=frame,
        text="Name:" + Parameter.Name,
        foreground="black",  # Set the text color to white
        font=("Arial", 10),
        anchor = "w",
        width = 40,
        bg="white"
        )
        Name.place(x=20, y=var)

        var += 20
        
        #Type of Parameter
        TypeParameter = Label(master=frame,
        text="Type Parameter:" + Parameter.Parameter,
        foreground="black",  # Set the text color to white
        font=("Arial", 10),
        anchor = "w",
        width = 40,
        bg="white"
        )
        TypeParameter.place(x=20, y=var)

        var += 20
        
        #Description
        Description = Label(master=frame,
        text="Description: "+ Parameter.Description,
        foreground="black",  # Set the text color to white
        font=("Arial", 10),
        anchor = "w",
        width = 40,
        bg="white"
        )
        Description.place(x=20, y=var)

        var += 20

        #Lower Multiplicity
        LowerMult = Label(master=frame,
        text="Lower Multiplicity: " + str(Parameter.minMultiplicity),
        foreground="black",  # Set the text color to white
        font=("Arial", 10),
        anchor = "w",
        width = 40,
        bg="white"
        )
        LowerMult.place(x=20, y=var)

        var += 20

        #Upper Multiplicity
        UpperMult = Label(master=frame,
        text="Upper Multiplicity: "+ str(Parameter.maxMultiplicity),
        foreground="black",  # Set the text color to white
        font=("Arial", 10),
        anchor = "w",
        width = 40,
        bg="white"
        )
        UpperMult.place(x=20, y=var)  
        
        var += 20

        #Index
        Index = Label(master=frame,
        text="Index: "+ str(Parameter.Index),
        foreground="black",  # Set the text color to white
        font=("Arial", 10),
        anchor = "w",
        width = 40,
        bg="white"
        )
        Index.place(x=20, y=var)  

        var += 20

        
        #Symbolic
        Symbolic = Label(master=frame,
        text="Symbolic Name: "+ str(Parameter.Symbolic),
        foreground="black",  # Set the text color to white
        font=("Arial", 10),
        anchor = "w",
        width = 40,
        bg="white"
        )
        Symbolic.place(x=20, y=var)         
        
        var += 20
        #Values

        if Parameter.Parameter != "ENUMERATION":

            DefaultValue = Label(master=frame,
                text="Default Value: "+ str(Parameter.DefaultValue),
                foreground="black",  # Set the text color to white
                font=("Arial", 10),
                anchor = "w",
                width = 40,
                bg="white"
                )
            DefaultValue.place(x=20, y=var)              

            var += 20



            if Parameter.Parameter == "INTEGER" or Parameter.Parameter == "FLOAT":
                MinValue = Label(master=frame,
                text="Min Value: "+ str(Parameter.MinValue),
                foreground="black",  # Set the text color to white
                font=("Arial", 10),
                anchor = "w",
                width = 40,
                bg="white"
                )
                MinValue.place(x=20, y=var)
                  
                var += 20
                
                MaxValue = Label(master=frame,
                text="Min Value: "+ str(Parameter.MaxValue),
                foreground="black",  # Set the text color to white
                font=("Arial", 10),
                anchor = "w",
                width = 40,
                bg="white"
                )
                MaxValue.place(x=20, y=var)  
                var += 20
            else:
                pass
            
        else:
            index = 0
            for each_enum in Parameter.EnumListName:
                EnumValue = Label(master=frame,
                text="Enum " + str(index) + ":" + each_enum,
                foreground="black",  # Set the text color to white
                font=("Arial", 10),
                anchor = "w",
                width = 40,
                bg="white"
                )
                EnumValue.place(x=20, y=var)
                index = index + 1
                var += 20               

        buttonR_ModifyParameter = Button(
            master=frame,
            command = lambda: self.windowEditParameters (Parameter, Container),     
            text="Modify Parameter", 
            borderwidth=5,
            width=15
            )
        buttonR_ModifyParameter.place(x=250, y=var + 50)


        buttonL_DeleteParameter = Button(
            master=frame, 
            text="Delete Parameter",
            command = self.delete_parameter,
            borderwidth=5,
            width=15
            )
        buttonL_DeleteParameter.place(x=50, y=var + 50)


    def windowShowReference (self, Container, Reference):
        ws =  Frame(master=self.root, width=400, height=350, bg="#D0CECE")
        ws.place (x=280, y=10)
        
        # Create A Main Frame
        main_frame = Frame(ws)
        main_frame.pack(fill=BOTH, expand=1)

        # Create A Canvas
        my_canvas = Canvas(main_frame, width=400, height=350,  bg="white", scrollregion=(0, 0, 0, 0))
        my_canvas.pack(side=LEFT, fill=BOTH, expand=1)

        # Add A Scrollbar To The Canvas
        my_scrollbar = ttk.Scrollbar(main_frame, orient=VERTICAL, command=my_canvas.yview)
        my_scrollbar.pack(side=RIGHT, fill=Y)

        # Configure The Canvas
        my_canvas.configure(yscrollcommand=my_scrollbar.set)
        my_canvas.bind('<Configure>', lambda e: my_canvas.configure(scrollregion = my_canvas.bbox("all")))

        # Create ANOTHER Frame INSIDE the Canvas
        frame = Frame(my_canvas, width=500, height=550, bg="white", borderwidth = 1, relief="solid")

        # Add that New frame To a Window In The Canvas
        my_canvas.create_window((0,0), window=frame, anchor="nw")

        
        label = Label(master=frame,
        text="Editor: Container - " + Container.Name + " - Reference - " + Reference.Name,
        foreground="black",  # Set the text color to white
        font=("Arial", 10),
        anchor = "w",
        width = 50
        )
        label.place(x=0, y=0)
        self.listLabels.append (label)

        ver = 50
        
        #Name
        NameModule = Label(master=frame,
        text="Name: "+ Reference.Name,
        foreground="black",  # Set the text color to white
        font=("Arial", 10),
        anchor = "w",
        width = 40,
        bg="white"
        )
        NameModule.place(x=20, y=ver)


        #Description
        DescriptionModule = Label(master=frame,
        text="Description: "+ Reference.Description,
        foreground="black",  # Set the text color to white
        font=("Arial", 10),
        anchor = "w",
        width = 40,
        bg="white"
        )
        DescriptionModule.place(x=20, y=ver+20)

        #Lower Multiplicity
        LowerMultModule = Label(master=frame,
        text="Lower Multiplicity: " + str(Reference.lowMultiplicity),
        foreground="black",  # Set the text color to white
        font=("Arial", 10),
        anchor = "w",
        width = 40,
        bg="white"
        )
        LowerMultModule.place(x=20, y=ver+40)
            
        #Upper Multiplicity
        UpperMultModule = Label(master=frame,
        text="Upper Multiplicity: "+ str(Reference.uppMultiplicity),
        foreground="black",  # Set the text color to white
        font=("Arial", 10),
        anchor = "w",
        width = 40,
        bg="white"
        )
        UpperMultModule.place(x=20, y=ver+60)     

        #Origin
        OriginReference = Label(master=frame,
        text="Origin: "+ str(Reference.Origin),
        foreground="black",  # Set the text color to white
        font=("Arial", 10),
        anchor = "w",
        width = 40,
        bg="white"
        )
        OriginReference.place(x=20, y=ver+80)              
        
        #Destination
        DestinationReference = Label(master=frame,
        text="Destination: "+ str(Reference.Destination),
        foreground="black",  # Set the text color to white
        font=("Arial", 10),
        anchor = "w",
        width = 40,
        bg="white"
        )
        DestinationReference.place(x=20, y=ver+100)
         
        buttonR_ModifyReference = Button(
            master=frame,
            command = lambda: self.windowEditReference (Reference, Container),     
            text="Modify Reference", 
            borderwidth=5,
            width=15
            )
        buttonR_ModifyReference.place(x=250, y=ver + 150)


        buttonL_DeleteReference = Button(
            master=frame, 
            text="Delete reference",
            #command = self.delete_parameter,
            borderwidth=5,
            width=15
            )
        buttonL_DeleteReference.place(x=50, y=ver + 150)




    def building_treeviewSubcontainers (self, item_parent, container, subcontainer):
            
        item_container = self.tree.insert(item_parent, 'end', text=subcontainer.ObjContainer.Name, values = (container, subcontainer)) 
            
        item_parameters = self.tree.insert(item_container, 'end', text="Parameters", values = (None, "Parameters"))
        item_reference = self.tree.insert(item_container, 'end', text="References", values = (None, "References"))
        item_subcontainer = self.tree.insert(item_container, 'end', text="Subcontainers", values = (None, "Subcontainers"))

        if len (subcontainer.ObjContainer.dict_Parameters.values()) > 0:
            for each_parameter in subcontainer.ObjContainer.dict_Parameters.values():
                self.tree.insert(item_parameters, 'end', text=each_parameter.Name, values = (subcontainer, each_parameter))

        if len (subcontainer.ObjContainer.dict_reference.values()) > 0:
            for each_reference in subcontainer.ObjContainer.dict_reference.values():
                self.tree.insert(item_reference, 'end', text=each_reference.Name, values = (subcontainer, each_reference))

        if len (subcontainer.ObjContainer.dict_subcontainers.values()) > 0:
            for each_subcontainer in subcontainer.ObjContainer.dict_subcontainers.values():
                self.building_treeviewSubcontainers (item_subcontainer, subcontainer.ObjContainer, each_subcontainer)
    
    def select_file(self):
        filetypes = (
            ('arxml files', '*.arxml'),
        )

        filename = fd.askopenfilename(
            title='Open a file',
            initialdir='/',
            filetypes=filetypes)

        Mudule_obj = MD.ModuleMD()
        Mudule_obj.SetFileXml (filename)
        Mudule_obj.ReadArxmlStructure()
        MD.ModuleCollection.AddModule (Mudule_obj)
        
        print("Holaaaa")
        MD.ModuleCollection.PrintModules()
        try:
            item_tree = self.tree.insert('', 'end', Mudule_obj.ModuleName, text=Mudule_obj.ModuleName, values = (None, Mudule_obj))
            
            for each_container in Mudule_obj.dict_Containers.values():
                
                item_container = self.tree.insert(item_tree, 'end', text=each_container.Name, values = (Mudule_obj, each_container)) 
                
                item_parameters = self.tree.insert(item_container, 'end', text="Parameters", values = (None, "Parameters"))
                item_reference = self.tree.insert(item_container, 'end', text="References", values = (None, "References"))
                item_subcontainers = self.tree.insert(item_container, 'end', text="Subcontainers", values = (None, "Subcontainers"))

                if len (each_container.dict_Parameters.values()) > 0:
                    for each_parameter in each_container.dict_Parameters.values():
                        self.tree.insert(item_parameters, 'end', text=each_parameter.Name, values = (each_container, each_parameter))

                if len (each_container.dict_reference.values()) > 0:
                    for each_reference in each_container.dict_reference.values():
                        self.tree.insert(item_reference, 'end', text=each_reference.Name, values = (each_container, each_reference))


                if len (each_container.dict_subcontainers.values()) > 0:
                    for each_subcontainer in each_container.dict_subcontainers.values():
                        self.building_treeviewSubcontainers (item_subcontainers, each_container, each_subcontainer)
    
    

        except:
            messagebox.showinfo(message='The Module is already exist')   
           


        
    def select_module (self, event):
        selected = self.tree.focus()
        item_tree = self.tree.item (selected, "text")

        p_id = self.tree.selection() # collect selected row id
       
        try:
            (val1, val2) = self.tree.item(p_id)['values'] # List of values        
        

            try:
                val1 = ((val1.split("at ")[1]).replace(">",""))
                val1 =  (int(val1, base=16))
                valuetree1 = ctypes.cast(val1, ctypes.py_object).value

            except:
                valuetree1 = val1
            
            try: 
                val2 = ((val2.split("at ")[1]).replace(">",""))
                val2 =  (int(val2, base=16))
                valuetree2 = ctypes.cast(val2, ctypes.py_object).value

            except:
                valuetree2 = val2
                    
            print (valuetree1, valuetree2)
            print (isinstance (valuetree2, MD.ModuleMD))
            
            if valuetree1 == "None" and isinstance (valuetree2, MD.ModuleMD) == True:
                Module_obj = valuetree2
                self.windowShowModule(Module_obj)        
            
            elif isinstance (valuetree1, MD.ModuleMD) == True and isinstance (valuetree2, MD.ContainerMD) == True:
                Module_obj = valuetree1
                Container_obj = valuetree2
                self.windowShowContainer (Module_obj, Container_obj)
                
            elif isinstance (valuetree1, MD.ContainerMD) == True and isinstance (valuetree2, MD.ParameterMD) == True:
                Container_obj = valuetree1
                Parameter_obj = valuetree2            
            
                self.windowShowParameterContainer (Container_obj, Parameter_obj)

            elif isinstance (valuetree1, MD.ContainerMD) == True and isinstance (valuetree2, MD.ReferencesMD) == True:

                Container_obj = valuetree1
                reference_obj = valuetree2           
                self.windowShowReference (Container_obj, reference_obj)

            elif isinstance (valuetree1, MD.ContainerMD) == True and isinstance (valuetree2, MD.SubContainerMD) == True:
                Module_obj = valuetree1.ModuleObj
                Subcontainer_obj = valuetree2.ObjContainer
                self.windowShowContainer (Module_obj, Subcontainer_obj)

            elif isinstance (valuetree1, MD.SubContainerMD) == True and isinstance (valuetree2, MD.SubContainerMD) == True:
                Module_obj = valuetree1.ObjContainer.ModuleObj
                Subcontainer_obj = valuetree2.ObjContainer
                self.windowShowContainer (Module_obj, Subcontainer_obj)

            elif isinstance (valuetree1, MD.SubContainerMD) == True and isinstance (valuetree2, MD.ParameterMD) == True:
                Container_obj = valuetree1.ObjContainer
                Parameter_obj = valuetree2            
            
                self.windowShowParameterContainer (Container_obj, Parameter_obj)

            elif isinstance (valuetree1, MD.SubContainerMD) == True and isinstance (valuetree2, MD.ReferencesMD) == True:

                Container_obj = valuetree1.ObjContainer
                reference_obj = valuetree2           
                self.windowShowReference (Container_obj, reference_obj)
            
                            
            else:
                self.TemplateFrame()
        
        except:
            pass
            
    def delete_module (self):

        selected_item = self.tree.selection()[0] ## get selected item
        self.tree.delete(selected_item)
        module_obj = MD.ModuleMD ()
        module_obj = MD.ModuleCollection.dict_Modules[selected_item]
        del MD.ModuleCollection.dict_Modules[selected_item]
        self.TemplateFrame()
        MsgBox = messagebox.askquestion ('Delete Module: ','Do you want to delete the module also inside the SIP',icon = 'warning')
        if MsgBox == 'yes':
            module_obj.DeleteModule_Sip()
        else:
            pass
        
    def delete_container (self):
        selected_item = self.tree.selection()[0] ## get selected item
        parent_iid = self.tree.parent(selected_item)
        Module_obj = MD.ModuleCollection.dict_Modules[parent_iid]
        Container_Obj = Module_obj.dict_Containers[selected_item]
        Module_obj.DelContainer (Container_Obj)
        #Module_obj.printModule()

        ReturnVal = CF.ModifileFileMDArxml (Module_obj.ModuleName, Module_obj.VendorName, Module_obj.ModuleDescription, Module_obj.SipVersion, Module_obj.SipPath, Module_obj.LowMultiplicity , Module_obj.UppMultiplicity)
        
        if ReturnVal == "MS_OK":
            self.tree.delete(selected_item)
            self.TemplateFrame()
        
    def delete_parameter (self):
        p_id = self.tree.selection() # collect selected row id
        (ContainerAdd, ParameterAdd) = self.tree.item(p_id)['values'] # List of values
 
        ContainerAdd = ((ContainerAdd.split("at ")[1]).replace(">",""))
        ContainerAdd = (int(ContainerAdd, base=16))
        ContainerObj = ctypes.cast(ContainerAdd, ctypes.py_object).value

        ParameterAdd = ((ParameterAdd.split("at ")[1]).replace(">",""))
        ParameterAdd = (int(ParameterAdd, base=16))
        ParameterObj = ctypes.cast(ParameterAdd, ctypes.py_object).value

        ContainerObj.delParameterInContainer (ParameterObj.Name)
        ContainerObj.PrintContainer()
        Module = ContainerObj.ModuleObj
        Module.printModule()

        ReturnVal = CF.ModifileFileMDArxml(Module.ModuleName, 
                    Module.VendorName, 
                    Module.ModuleDescription, 
                    Module.SipVersion, 
                    Module.SipPath, 
                    Module.LowMultiplicity, 
                    Module.UppMultiplicity)
                
        if ReturnVal == "MS_OK":
            self.tree.delete(p_id)
            self.TemplateFrame()
        


def __main__():
    gui_obj = GUI ()
    gui_obj.treeView()
    gui_obj.TemplateFrame()
    gui_obj.LogFrame()
    gui_obj.menuBar()
    gui_obj.root.mainloop()

__main__()