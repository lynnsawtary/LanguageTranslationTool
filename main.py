import tkinter as tk
from tkinter import ttk, messagebox
from deep_translator import GoogleTranslator
import pyperclip
import pyttsx3


LANGUAGES = {
    "Auto Detect": "auto",
    "English": "en",
    "Arabic": "ar",
    "French": "fr",
    "Spanish": "es",
    "German": "de",
    "Italian": "it",
    "Turkish": "tr",
    "Chinese": "zh-CN",
    "Japanese": "ja",
    "Korean": "ko",
}


def translate_text():
    input_text = input_box.get("1.0", tk.END).strip()

    if not input_text:
        messagebox.showwarning("Missing Text", "Please enter text to translate.")
        return

    source_language = LANGUAGES[source_combo.get()]
    target_language = LANGUAGES[target_combo.get()]

    if target_language == "auto":
        messagebox.showwarning("Invalid Target", "Please select a valid target language.")
        return

    try:
        translated = GoogleTranslator(
            source=source_language,
            target=target_language
        ).translate(input_text)

        output_box.delete("1.0", tk.END)
        output_box.insert(tk.END, translated)

    except Exception as e:
        messagebox.showerror("Translation Error", f"Something went wrong:\n{e}")


def copy_translation():
    translated_text = output_box.get("1.0", tk.END).strip()

    if not translated_text:
        messagebox.showwarning("Nothing to Copy", "There is no translated text to copy.")
        return

    pyperclip.copy(translated_text)
    messagebox.showinfo("Copied", "Translated text copied to clipboard.")


def speak_translation():
    translated_text = output_box.get("1.0", tk.END).strip()

    if not translated_text:
        messagebox.showwarning("Nothing to Speak", "There is no translated text to speak.")
        return

    try:
        engine = pyttsx3.init()
        engine.say(translated_text)
        engine.runAndWait()
    except Exception as e:
        messagebox.showerror("Speech Error", f"Could not speak text:\n{e}")


def clear_text():
    input_box.delete("1.0", tk.END)
    output_box.delete("1.0", tk.END)


# -----------------------------
# Main Window
# -----------------------------
root = tk.Tk()
root.title("Language Translation Tool")
root.geometry("850x600")
root.resizable(False, False)
root.configure(bg="#0f172a")

# -----------------------------
# Title
# -----------------------------
title_label = tk.Label(
    root,
    text="Language Translation Tool",
    font=("Arial", 24, "bold"),
    bg="#0f172a",
    fg="white"
)
title_label.pack(pady=20)

subtitle_label = tk.Label(
    root,
    text="Translate text between multiple languages using AI-powered translation",
    font=("Arial", 11),
    bg="#0f172a",
    fg="#cbd5e1"
)
subtitle_label.pack(pady=5)

# -----------------------------
# Language Selection Frame
# -----------------------------
language_frame = tk.Frame(root, bg="#0f172a")
language_frame.pack(pady=20)

source_label = tk.Label(
    language_frame,
    text="Source Language",
    font=("Arial", 11, "bold"),
    bg="#0f172a",
    fg="white"
)
source_label.grid(row=0, column=0, padx=20, pady=5)

target_label = tk.Label(
    language_frame,
    text="Target Language",
    font=("Arial", 11, "bold"),
    bg="#0f172a",
    fg="white"
)
target_label.grid(row=0, column=1, padx=20, pady=5)

source_combo = ttk.Combobox(
    language_frame,
    values=list(LANGUAGES.keys()),
    state="readonly",
    width=25
)
source_combo.current(0)
source_combo.grid(row=1, column=0, padx=20)

target_combo = ttk.Combobox(
    language_frame,
    values=list(LANGUAGES.keys())[1:],
    state="readonly",
    width=25
)
target_combo.current(0)
target_combo.grid(row=1, column=1, padx=20)

# -----------------------------
# Text Boxes Frame
# -----------------------------
text_frame = tk.Frame(root, bg="#0f172a")
text_frame.pack(pady=15)

input_label = tk.Label(
    text_frame,
    text="Enter Text",
    font=("Arial", 12, "bold"),
    bg="#0f172a",
    fg="white"
)
input_label.grid(row=0, column=0, padx=15, sticky="w")

output_label = tk.Label(
    text_frame,
    text="Translated Text",
    font=("Arial", 12, "bold"),
    bg="#0f172a",
    fg="white"
)
output_label.grid(row=0, column=1, padx=15, sticky="w")

input_box = tk.Text(
    text_frame,
    height=10,
    width=45,
    font=("Arial", 11),
    wrap=tk.WORD
)
input_box.grid(row=1, column=0, padx=15, pady=10)

output_box = tk.Text(
    text_frame,
    height=10,
    width=45,
    font=("Arial", 11),
    wrap=tk.WORD
)
output_box.grid(row=1, column=1, padx=15, pady=10)

# -----------------------------
# Buttons Frame
# -----------------------------
button_frame = tk.Frame(root, bg="#0f172a")
button_frame.pack(pady=15)

translate_button = tk.Button(
    button_frame,
    text="Translate",
    command=translate_text,
    font=("Arial", 11, "bold"),
    bg="#2563eb",
    fg="white",
    width=15,
    cursor="hand2"
)
translate_button.grid(row=0, column=0, padx=10)

copy_button = tk.Button(
    button_frame,
    text="Copy",
    command=copy_translation,
    font=("Arial", 11, "bold"),
    bg="#16a34a",
    fg="white",
    width=15,
    cursor="hand2"
)
copy_button.grid(row=0, column=1, padx=10)

speak_button = tk.Button(
    button_frame,
    text="Speak",
    command=speak_translation,
    font=("Arial", 11, "bold"),
    bg="#9333ea",
    fg="white",
    width=15,
    cursor="hand2"
)
speak_button.grid(row=0, column=2, padx=10)

clear_button = tk.Button(
    button_frame,
    text="Clear",
    command=clear_text,
    font=("Arial", 11, "bold"),
    bg="#dc2626",
    fg="white",
    width=15,
    cursor="hand2"
)
clear_button.grid(row=0, column=3, padx=10)

# -----------------------------
# Footer
# -----------------------------
footer_label = tk.Label(
    root,
    text="CodeAlpha Internship Project",
    font=("Arial", 10),
    bg="#0f172a",
    fg="#94a3b8"
)
footer_label.pack(pady=10)

root.mainloop()