import re
import tkinter as tk
from tkinter import messagebox

def remove_duplicates():
    text = input_text.get("1.0", tk.END).strip()

    if not text:
        messagebox.showwarning("Увага", "Введіть текст для обробки!")
        return

    words = re.findall(r'\b\w+\b', text, re.UNICODE)

    seen = set()
    unique_words = []
    removed_count = 0

    for word in words:
        word_lower = word.lower()
        if word_lower not in seen:
            seen.add(word_lower)
            unique_words.append(word)
        else:
            removed_count += 1


    result = ' '.join(unique_words)

    output_text.delete("1.0", tk.END)
    output_text.insert(tk.END, result)

    messagebox.showinfo("Результат", f"Видалено повторів: {removed_count}")

root = tk.Tk()
root.title("Лабораторна робота №3.3")
root.configure(bg="#E9F3F6")

tk.Label(root, text="Лабораторна робота №3.3", font=("Arial", 14, "bold"),
         bg="#005f66", fg="white", pady=6).grid(row=0, column=0, columnspan=2, sticky="we")

tk.Label(root, text="Введіть текст:", font=("Arial", 11, "bold"),
         bg="#E9F3F6").grid(row=1, column=0, sticky="w", padx=10, pady=5)

input_text = tk.Text(root, width=70, height=8, font=("Arial", 10))
input_text.grid(row=2, column=0, columnspan=2, padx=10, pady=5)

tk.Button(root, text="Видалити повторення слів", bg="#99e699", font=("Arial", 10, "bold"),
          command=remove_duplicates).grid(row=3, column=0, columnspan=2, pady=10)

tk.Label(root, text="Результат:", font=("Arial", 11, "bold"),
         bg="#E9F3F6").grid(row=4, column=0, sticky="w", padx=10, pady=5)

output_text = tk.Text(root, width=70, height=8, font=("Arial", 10))
output_text.grid(row=5, column=0, columnspan=2, padx=10, pady=5)

root.mainloop()
