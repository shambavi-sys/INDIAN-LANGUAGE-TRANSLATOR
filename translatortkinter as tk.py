
import tkinter as tk
from tkinter import ttk
from googletrans import Translator

# Define Indian languages and English
indian_languages = {
    "English": "en",
    "Hindi": "hi",
    "Bengali": "bn",
    "Telugu": "te",
    "Marathi": "mr",
    "Tamil": "ta",
    "Urdu": "ur",
    "Gujarati": "gu",
    "Malayalam": "ml",
    "Punjabi": "pa",
    "Kannada": "kn",
    "Odia": "or",
    "Assamese": "as",
}

# Create main window
root = tk.Tk()
root.title("INDIAN LANGUAGE TRANSLATOR")
root.geometry("800x600")
root.config(bg="black")

# =========================
# Welcome Screen
# =========================
def show_translator():
    welcome_frame.pack_forget()
    translator_frame.pack(fill=tk.BOTH, expand=True)

welcome_frame = tk.Frame(root, bg="black")
welcome_frame.pack(fill=tk.BOTH, expand=True)

welcome_label = tk.Label(welcome_frame, text="WELCOME TO", font=("Arial", 24, "bold"), bg="black", fg="white")
welcome_label.pack(pady=(100, 10))

app_name_label = tk.Label(welcome_frame, text="INDIAN LANGUAGE TRANSLATOR", font=("Arial", 28, "bold"), bg="black", fg="#4CAF50")
app_name_label.pack(pady=10)

continue_button = tk.Button(welcome_frame, text="Continue", font=("Arial", 14, "bold"), bg="#4CAF50", fg="white", padx=20, pady=10, command=show_translator)
continue_button.pack(pady=30)

# =========================
# Translator Screen
# =========================
translator_frame = tk.Frame(root, bg="white")

# Center main translator frame
main_frame = tk.Frame(translator_frame, bg="white", padx=20, pady=20, relief=tk.RIDGE, borderwidth=2)
main_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

# Title Label
title_label = tk.Label(main_frame, text="INDIAN LANGUAGE TRANSLATOR", font=("Arial", 18, "bold"), bg="white", fg="black")
title_label.grid(row=0, column=0, columnspan=2, pady=10)

# Language Selection
lang_frame = tk.Frame(main_frame, bg="white")
lang_frame.grid(row=1, column=0, columnspan=2, pady=10)

from_lang_label = tk.Label(lang_frame, text="From:", font=("Arial", 12, "bold"), bg="white", fg="black")
from_lang_label.grid(row=0, column=0, padx=5, pady=5)

from_language_combobox = ttk.Combobox(lang_frame, values=list(indian_languages.keys()), state="readonly", font=("Arial", 11))
from_language_combobox.set("English")
from_language_combobox.grid(row=0, column=1, padx=5, pady=5)

to_lang_label = tk.Label(lang_frame, text="To:", font=("Arial", 12, "bold"), bg="white", fg="black")
to_lang_label.grid(row=0, column=2, padx=5, pady=5)

to_language_combobox = ttk.Combobox(lang_frame, values=list(indian_languages.keys()), state="readonly", font=("Arial", 11))
to_language_combobox.set("Hindi")
to_language_combobox.grid(row=0, column=3, padx=5, pady=5)

# Input Area
input_label = tk.Label(main_frame, text="Enter Text to Translate:", font=("Arial", 12, "bold"), bg="white", fg="black")
input_label.grid(row=2, column=0, columnspan=2, pady=5)

input_text_area = tk.Text(main_frame, height=5, width=60, wrap=tk.WORD, font=("Arial", 11), relief=tk.GROOVE, borderwidth=2, bg="#f4f4f4", fg="black", insertbackground="black")
input_text_area.grid(row=3, column=0, columnspan=2, padx=10, pady=5)

# Translate Button
def on_enter(e):
    translate_button.config(bg="#45a049")

def on_leave(e):
    translate_button.config(bg="#4CAF50")

def translate_text():
    input_text = input_text_area.get("1.0", tk.END).strip()
    from_lang_name = from_language_combobox.get()
    to_lang_name = to_language_combobox.get()

    if input_text and from_lang_name in indian_languages and to_lang_name in indian_languages:
        from_lang = indian_languages[from_lang_name]
        to_lang = indian_languages[to_lang_name]

        try:
            translator = Translator()
            translated = translator.translate(input_text, src=from_lang, dest=to_lang)
            output_text_area.config(state=tk.NORMAL)
            output_text_area.delete(1.0, tk.END)
            output_text_area.tag_configure("center", justify='center')
            output_text_area.insert(tk.END, translated.text, "center")
            output_text_area.config(state=tk.DISABLED)
        except Exception as e:
            output_text_area.config(state=tk.NORMAL)
            output_text_area.delete(1.0, tk.END)
            output_text_area.tag_configure("center", justify='center')
            output_text_area.insert(tk.END, f"Translation Error: {str(e)}", "center")
            output_text_area.config(state=tk.DISABLED)

translate_button = tk.Button(main_frame, text="Translate", command=translate_text, font=("Arial", 12, "bold"), bg="#4CAF50", fg="white", padx=10, pady=5)
translate_button.grid(row=4, column=0, columnspan=2, pady=10)
translate_button.bind("<Enter>", on_enter)
translate_button.bind("<Leave>", on_leave)

# Output Area
output_label = tk.Label(main_frame, text="Translated Text:", font=("Arial", 12, "bold"), bg="white", fg="black")
output_label.grid(row=5, column=0, columnspan=2, pady=5)

output_text_area = tk.Text(main_frame, height=5, width=60, wrap=tk.WORD, font=("Arial", 11), relief=tk.FLAT, borderwidth=2, bg="#f4f4f4", fg="black", state=tk.DISABLED)
output_text_area.grid(row=6, column=0, columnspan=2, padx=10, pady=5)

# Run the app
root.mainloop()
