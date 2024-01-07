import tkinter as tk
from tkinter import ttk
import keyboard
import pandas as pd
import subprocess

def speak(text):
    try:
        subprocess.run(["espeak", text])
    except Exception as e:
        print(f"Error while speaking: {e}")

df = pd.read_csv('app.csv')
def process_scanned_barcode(scanned_barcode):
  
    if scanned_barcode in df['Barcode'].astype(str).values:
    
        card_data = df[df['Barcode'].astype(str) == scanned_barcode].to_dict(orient='records')[0]
        display_result(f"Scanned Barcode: {scanned_barcode}\nCard Data:\n" + "\n".join([f"{key}: {value}" for key, value in card_data.items()]))
        speak("present")
    else:
        display_result(f"Scanned Barcode: {scanned_barcode}\nCard not found.")
        speak("invalid card")
def on_scan(event):
    if event.event_type == keyboard.KEY_DOWN:
        key = event.name
        if key and key.isnumeric():
       
            current_barcode.append(key)
        elif key == 'enter' and current_barcode:
           
            scanned_barcode = ''.join(current_barcode)
            process_scanned_barcode(scanned_barcode)
            current_barcode.clear()

def display_result(result_text):
    result_label.config(text=result_text)

current_barcode = []

def main():
    app = tk.Tk()
    app.title("Continuous Barcode Scanner App")

    label = ttk.Label(app, text="Scanning for Barcode:")
    label.grid(row=0, column=0, padx=10, pady=10)

    global result_label
    result_label = ttk.Label(app, text="")
    result_label.grid(row=1, column=0, padx=10, pady=10)
    keyboard.hook(on_scan)

    app.mainloop()

if __name__ == "__main__":
    main()
