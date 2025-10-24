import re
import tkinter as tk
from tkinter import messagebox, scrolledtext

IP_REGEX = r'\b(?:25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)(?:\.(?:25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)){3}\b'


def find_ips():
    text = input_text.get("1.0", tk.END)
    ips = re.findall(IP_REGEX, text)
    display_results(ips)

def delete_ip():
    text = input_text.get("1.0", tk.END)
    ip_to_delete = delete_var.get().strip()

    if not ip_to_delete:
        messagebox.showwarning("Попередження", "Введіть IP-адресу для видалення.")
        return

    new_text = text.replace(ip_to_delete, "")
    input_text.delete("1.0", tk.END)
    input_text.insert(tk.END, new_text)
    messagebox.showinfo("Видалено", f"IP {ip_to_delete} видалено з тексту.")


def replace_ip():
    old_ip = replace_old_var.get().strip()
    new_ip = replace_new_var.get().strip()
    text = input_text.get("1.0", tk.END)

    if not old_ip or not new_ip:
        messagebox.showwarning("Увага", "Введіть обидві IP-адреси!")
        return

    if old_ip not in text:
        messagebox.showerror("Помилка", f"IP {old_ip} не знайдено у тексті.")
        return

    new_text = text.replace(old_ip, new_ip)
    input_text.delete("1.0", tk.END)
    input_text.insert(tk.END, new_text)
    messagebox.showinfo("Заміна виконана", f"IP {old_ip} замінено на {new_ip}.")


def display_results(ips):
    output_text.config(state="normal")
    output_text.delete("1.0", tk.END)
    if ips:
        output_text.insert(tk.END, f"🔹 Знайдені IP-адреси ({len(ips)}):\n\n")
        for ip in ips:
            output_text.insert(tk.END, f"{ip}\n")
    else:
        output_text.insert(tk.END, "❌ У тексті не знайдено жодної IP-адреси.")
    output_text.config(state="disabled")


root = tk.Tk()
root.title("Лабораторна №3.3")
root.geometry("800x600")
root.configure(bg="#edf6f9")

root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=1)
root.columnconfigure(2, weight=1)

tk.Label(
    root,
    text="Лабораторна робота №3.2",
    bg="#006d77",
    fg="white",
    font=("Arial", 13, "bold"),
    pady=10
).grid(row=0, column=0, columnspan=3, sticky="ew", pady=(0, 10))

tk.Label(root, text="Введіть текст:", bg="#edf6f9", font=("Arial", 11, "bold")).grid(
    row=1, column=0, padx=20, pady=(5, 0)
)
input_text = scrolledtext.ScrolledText(root, width=90, height=8, wrap=tk.WORD, font=("Consolas", 10))
input_text.grid(row=2, column=0, columnspan=3, padx=20, pady=5)

tk.Button(root, text="Знайти IP-адреси", command=find_ips, width=20, bg="#b3e6b3").grid(row=3, column=0, pady=10)
tk.Button(root, text="Видалити IP", command=delete_ip, width=20, bg="#ffb3b3").grid(row=3, column=1, pady=10)
tk.Button(root, text="Замінити IP", command=replace_ip, width=20, bg="#b3d1ff").grid(row=3, column=2, pady=10)

tk.Label(root, text="Результати:", bg="#edf6f9", font=("Arial", 11, "bold")).grid(row=4, column=0, padx=20, pady=(5, 0))
output_text = scrolledtext.ScrolledText(root, width=90, height=8, wrap=tk.WORD, font=("Consolas", 10), state="disabled")
output_text.grid(row=5, column=0, columnspan=3, padx=20, pady=5)

tk.Label(root, text="Видалити IP:", bg="#edf6f9").grid(row=6, column=0, sticky="e", padx=10, pady=5)
delete_var = tk.StringVar()
tk.Entry(root, textvariable=delete_var, width=30).grid(row=6, column=1, sticky="w", pady=5)

tk.Label(root, text="Заміна IP:", bg="#edf6f9").grid(row=7, column=0, sticky="e", padx=10, pady=5)
replace_old_var = tk.StringVar()
replace_new_var = tk.StringVar()
tk.Entry(root, textvariable=replace_old_var, width=25).grid(row=7, column=1, sticky="w", pady=5)
tk.Label(root, text="->", bg="#edf6f9", font=("Arial", 11, "bold")).grid(row=7, column=1, sticky="e", padx=60)
tk.Entry(root, textvariable=replace_new_var, width=25).grid(row=7, column=2, sticky="w", pady=5)


root.mainloop()
