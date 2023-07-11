import time
import random
import tkinter as tk
from tkinter import messagebox
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import undetected_chromedriver as uc
from fake_useragent import UserAgent
from playsound import playsound

window = tk.Tk()
window.iconphoto(False,tk.PhotoImage(file="favicon.png"))
window.title("PASTEURIZE")
window.minsize(300,180)
window.resizable(False,False)

info = tk.Label(text="Floods Tellonym boards rendering them useless.")
firstname_label = tk.Label(text="Tellonym Full link plz :-)")
firstname_entry = tk.Entry()
rounds_label = tk.Label(text="# of iterations")
rounds_entry = tk.Entry()
length_label = tk.Label(text="Length of text")
length_entry = tk.Entry()
def spam():
    playsound('freshmeat.mp3')
    if firstname_entry.get() == "":
        tk.messagebox.showerror(title="Don't forget your URL!",message="You forgot to input a Tellonym URL! Please restart this app.")
        pass
    rounds = 5
    length = 50
    if rounds_entry.get() != "":
        rounds = int(rounds_entry.get())
    if length_entry.get() != "":
        length = int(length_entry.get())
    wait_time = 1
    random.seed(random.randint(0,999))
    abc = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ12345567890!@#$%^&*()`~-_=+[]\{}|"
    fake_pass = ""

    options = Options()
    ua = UserAgent()
    user_agent = ua.random
    print("User agent: " + str(user_agent))
    
    driver = uc.Chrome(chrome_options=options,headless=False)
    driver.get(firstname_entry.get())
    
    for i in range(rounds):
        fake_pass = ""
        time.sleep(.75)
        for _ in range(length):
            fake_pass = ''.join((fake_pass,abc[random.randint(0,len(abc)-1)]))
        driver.find_element(By.NAME,"tell").send_keys(fake_pass)
        driver.find_element(By.XPATH,'/html/body/div[1]/div/div/div[5]/div/div/div[1]/div[2]/div/div[2]/div[2]/div[2]/div/div/div[2]/form/button').click()
        time.sleep(4)
        driver.get(firstname_entry.get())
    
begin_button = tk.Button(text="Start burying",command=spam)

info.pack()
firstname_label.pack()
firstname_entry.pack()
rounds_label.pack()
rounds_entry.pack()
length_label.pack()
length_entry.pack()
begin_button.pack()
window.mainloop()

