import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import BackEnd
# from tkinter import messagebox

# name=None, email=None, userid=None, model=None, role=None, sf_role=None, country=None, manager=None, service=False

def set_background(image_path, canvas, root):
    global img, img_id
    img = Image.open(image_path)
    img = img.resize((root.winfo_width(), root.winfo_height()), Image.ANTIALIAS)
    img = ImageTk.PhotoImage(img)

    # Scale the image to fit the window size
    #img = img.subsample(int(img.width() / window_width), int(img.height() / window_height))

    # Configure canvas size to match the window
    canvas.config(width=root.winfo_width(), height=root.winfo_height())

    # Set the scaled image as the background
    img_id = canvas.create_image(0, 0, anchor=tk.NW, image=img)


def runGUI():   
    def submit():       
        
        name = name_entry.get()
        email = email_entry.get()
        userid = id_entry.get()
        model = model_entry.get()
        role = role_entry.get()
        sf_role = sf_role_entry.get()
        country = dropdown.get()
        manager = manager_entry.get()
        service = true_var.get()
        """
        print(name)
        print(email)
        print(userid)
        print(model)
        print(role)
        print(sf_role)
        print(country)
        print(manager)
        print(service)
        """
        user = BackEnd.Person(name, email, userid, model, role, sf_role, country, manager, service)
        BackEnd.write_to_notebook(user)
        root.destroy()
    
    def toggle_entry_state():
        entry_state = 'normal' if toggle_var.get() else 'disabled'
        model_entry.config(state=entry_state)
    # Create the main window
    root = tk.Tk()
    root.title('New User Info')
    
    image_path = "logoDanfoss.png"
    """ 
    canvas = tk.Canvas(root)
    canvas.grid(row=0, column=0, sticky=tk.NSEW)

    # Set the image as the background
    set_background(image_path, canvas, root)

    """
    pil_image = Image.open(image_path)
    img = ImageTk.PhotoImage(pil_image)

    # Create a label to display the image
    label = tk.Label(root, image=img)
    label.grid(row=0, column=0, padx=10, pady=0, sticky='w')
       
    
    # Create and place widgets
    empty_space = tk.Label(root, text="")
    empty_space.grid(row=1, column=0, padx=10, pady=0, sticky='w')
    
    # Name start
    label = tk.Label(root, text='Name: ')
    label.grid(row=2, column=0, padx=10, pady=0, sticky='w')    
    name_entry = tk.Entry(root, width=70)
    name_entry.grid(row=3, column=0, padx=10, pady=0, sticky='w')
    # Name end
    
    # Email start
    label1 = tk.Label(root, text='Email: ')
    label1.grid(row=4, column=0, padx=10, pady=0, sticky='w')    
    email_entry = tk.Entry(root, width=70)
    email_entry.grid(row=5, column=0, padx=10, pady=0, sticky='w')
    # Email end
    
    # ID start
    label2 = tk.Label(root, text='UserID: ')
    label2.grid(row=6, column=0, padx=10, pady=0, sticky='w')    
    id_entry = tk.Entry(root, width=70)
    id_entry.grid(row=7, column=0, padx=10, pady=0, sticky='w')
    # ID end
    
    #empty_space1 = tk.Label(root, text="")
    #empty_space1.grid(row=8, column=0, padx=10, pady=0, sticky='w')
    
    # Role start
    label5 = tk.Label(root, text='Role: ')
    label5.grid(row=8, column=0, padx=10, pady=0, sticky='w')    
    role_entry = tk.Entry(root, width=70)
    role_entry.grid(row=9, column=0, padx=10, pady=0, sticky='w')
    # Role end
    
    # SF Role start
    label5 = tk.Label(root, text='Salesforce Role: ')
    label5.grid(row=10, column=0, padx=10, pady=0, sticky='w')    
    sf_role_entry = tk.Entry(root, width=70)
    sf_role_entry.grid(row=11, column=0, padx=10, pady=0, sticky='w')
    # SF Role end
    
    # Manager start
    label4 = tk.Label(root, text='Manager: ')
    label4.grid(row=12, column=0, padx=10, pady=0, sticky='w')    
    manager_entry = tk.Entry(root, width=70)
    manager_entry.grid(row=13, column=0, padx=10, pady=0, sticky='w')
    # Manager end
    
    # Country start
    label3 = tk.Label(root, text='Country: ')
    label3.grid(row=14, column=0, padx=10, pady=0, sticky='w')    
    options = ["Brasil", "Mexico", "Colombia", "Chile", "Argentina"]
    dropdown = ttk.Combobox(root, values=options)
    dropdown.set(options[0])  # Set the default selected option
    dropdown.grid(row=15, column=0, padx=10, pady=0, sticky='w')
    # Country end
    
    # Service start
    true_var = tk.BooleanVar()
    true_checkbox = tk.Checkbutton(root, text='Is Service? ', variable=true_var)
    true_checkbox.grid(row=19, column=0, padx=10, pady=10, sticky='w')
    # Service end
    
    # Model start
    toggle_var = tk.BooleanVar()
    toggle_var.set(True)
    toggle_checkbox = tk.Checkbutton(root, text='Has Model User: ', variable=toggle_var, command=toggle_entry_state)
    toggle_checkbox.grid(row=20, column=0, padx=10, pady=0, sticky='w')    
    model_entry = tk.Entry(root, width=70)
    model_entry.grid(row=21, column=0, padx=10, pady=0, sticky='w')
    # Model end 
    
    submit_button = tk.Button(root, text='Submit', command=submit)
    submit_button.grid(row=100, column=0, padx=20, pady=10, sticky='w')
    
    # Set window size
    root.geometry('470x655')
    
    # Start the main loop
    root.mainloop()