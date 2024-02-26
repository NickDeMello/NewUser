# -*- coding: utf-8 -*-
"""
Created on Mon Dec 11 16:39:33 2023

@author: U429604
"""
import tkinter as tk
from tkinter import messagebox


def runGUI():
    def submit():
        name = entry.get()
        is_true = true_var.get()
    
        print(name)
        print(is_true)
        
    def toggle_entry_state():
        entry_state = 'normal' if toggle_var.get() else 'disabled'
        entry1.config(state=entry_state)
    # Create the main window
    root = tk.Tk()
    root.title('New User Info')
    
    # Create and place widgets
    empty_space = tk.Label(root, text="")
    empty_space.grid(row=0, column=0, padx=10, pady=0, sticky='w')
    
    label = tk.Label(root, text='Name: ')
    label.grid(row=1, column=0, padx=10, pady=0, sticky='w')
    
    entry = tk.Entry(root, width=30)
    entry.grid(row=2, column=0, padx=10, pady=0, sticky='w')
    
    empty_space = tk.Label(root, text="")
    empty_space.grid(row=3, column=0, padx=10, pady=0, sticky='w')
    
    toggle_var = tk.BooleanVar()
    toggle_var.set(True)
    toggle_checkbox = tk.Checkbutton(root, text='Has Model User: ', variable=toggle_var, command=toggle_entry_state)
    toggle_checkbox.grid(row=4, column=0, padx=10, pady=0, sticky='w')
    
    entry1 = tk.Entry(root, width=30)
    entry1.grid(row=6, column=0, padx=10, pady=0, sticky='w')
    
    true_var = tk.BooleanVar()
    true_checkbox = tk.Checkbutton(root, text='True?', variable=true_var)
    true_checkbox.grid(row=8, column=0, padx=10, pady=10, sticky='w')
    
    submit_button = tk.Button(root, text='Submit', command=submit)
    submit_button.grid(row=10, column=0, padx=10, pady=10, sticky='w')
    
    # Set window size
    root.geometry('600x600')
    
    # Start the main loop
    root.mainloop()