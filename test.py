import tkinter as tk
from tkinter import messagebox
from gtts import gTTS
import pygame
import os
from dictionary import tanglish_to_english  # Import dictionary

# Function to translate Tanglish to English
def translate_tanglish_to_english(text):
    words = text.lower().split()
    translated_words = [tanglish_to_english.get(word, word) for word in words]
    return " ".join(translated_words)

# Function to convert text to speech
def text_to_speech(text, language='en'):
    tts = gTTS(text=text, lang=language, slow=False)
    filename = "output.mp3"
    tts.save(filename)
    
    pygame.mixer.init()
    pygame.mixer.music.load(filename)
    pygame.mixer.music.play()

    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)
    
    pygame.mixer.quit()
    os.remove(filename)

# Function to handle "Translate and Speak" button click
def on_translate_click():
    tanglish_text = input_text.get("1.0", tk.END).strip()
    if not tanglish_text:
        messagebox.showwarning("Input Error", "Please enter some Tanglish text!")
        return
    
    english_text = translate_tanglish_to_english(tanglish_text)
    output_text.delete("1.0", tk.END)
    output_text.insert(tk.END, english_text)

    text_to_speech(english_text)

# Function to handle "Exit" button click
def on_exit_click():
    root.destroy()

# GUI Application
root = tk.Tk()
root.title("Tanglish to English Translator")
root.geometry("500x400")

input_label = tk.Label(root, text="Enter Tanglish Text:", font=("Arial", 12))
input_label.pack(pady=10)

input_text = tk.Text(root, height=5, width=50, font=("Arial", 12))
input_text.pack(pady=10)

translate_button = tk.Button(root, text="Translate and Speak", command=on_translate_click, font=("Arial", 12))
translate_button.pack(pady=10)

output_label = tk.Label(root, text="Translated English Text:", font=("Arial", 12))
output_label.pack(pady=10)

output_text = tk.Text(root, height=5, width=50, font=("Arial", 12))
output_text.pack(pady=10)

exit_button = tk.Button(root, text="Exit", command=on_exit_click, font=("Arial", 12))
exit_button.pack(pady=10)

root.mainloop()
