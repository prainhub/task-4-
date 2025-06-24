from cryptography.fernet import Fernet
from cryptography.fernet import Fernet
import os
import tkinter as tk
from tkinter import filedialog, messagebox

# Step 1: Generate key


def generate_key():
    key = Fernet.generate_key()
    with open("secret.key", "wb") as key_file:
        key_file.write(key)

# Step 2: Load key


def load_key():
    return open("secret.key", "rb").read()

# Step 3: Encrypt file


def encrypt_file(filename, key):
    fernet = Fernet(key)
    with open(filename, "rb") as file:
        original = file.read()
    encrypted = fernet.encrypt(original)
    with open(filename, "wb") as encrypted_file:
        encrypted_file.write(encrypted)

# Step 4: Decrypt file


def decrypt_file(filename, key):
    fernet = Fernet(key)
    with open(filename, "rb") as enc_file:
        encrypted = enc_file.read()
    decrypted = fernet.decrypt(encrypted)
    with open(filename, "wb") as dec_file:
        dec_file.write(decrypted)

# ===== GUI Starts Here =====


def select_file():
    file_path.set(filedialog.askopenfilename())


def encrypt_action():
    if not os.path.exists("secret.key"):
        generate_key()
    key = load_key()
    try:
        encrypt_file(file_path.get(), key)
        messagebox.showinfo("Success", "File encrypted successfully!")
    except Exception as e:
        messagebox.showerror("Error", f"Encryption failed:\n{str(e)}")


def decrypt_action():
    if not os.path.exists("secret.key"):
        messagebox.showerror("Error", "Key not found. Please encrypt first.")
        return
    key = load_key()
    try:
        decrypt_file(file_path.get(), key)
        messagebox.showinfo("Success", "File decrypted successfully!")
    except Exception as e:
        messagebox.showerror("Error", f"Decryption failed:\n{str(e)}")


# GUI Window
app = tk.Tk()
app.title("AES-256 File Encryption Tool")
app.geometry("400x250")

file_path = tk.StringVar()

tk.Label(app, text="Select a file to encrypt/decrypt").pack(pady=10)
tk.Entry(app, textvariable=file_path, width=40).pack(pady=5)
tk.Button(app, text="Browse", command=select_file).pack(pady=5)
tk.Button(app, text="Encrypt", command=encrypt_action,
          bg="green", fg="white").pack(pady=5)
tk.Button(app, text="Decrypt", command=decrypt_action,
          bg="blue", fg="white").pack(pady=5)

app.mainloop()
