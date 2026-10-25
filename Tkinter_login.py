import tkinter as tk
from tkinter import messagebox
import re
from datetime import datetime

class RegistrationWindow:
    def __init__(self, root):
        self.root = root
        self.root.title("Zdravko - Registracija")
        self.root.geometry("500x550")
        self.root.resizable(False, False)

        # Logo aplikacije
        try:
            self.logo = tk.PhotoImage(file="C:/Users/Alan/Desktop/Veleučulište u Rijeci/Drugi semestar/zdravko_log.png").subsample(15, 15)
            tk.Label(root, image=self.logo).pack(pady=10)
        except:
            tk.Label(root, text="Zdravko", font=("Helvetica", 24, "bold"), fg="blue").pack(pady=10)

        # Frame za formu, centriran i s paddingom
        form_frame = tk.Frame(root, bg="white", bd=2, relief="groove")
        form_frame.pack(padx=30, pady=10, fill="both", expand=True)

        # Polja za unos
        self.create_field(form_frame, "Ime:", 0)
        self.create_field(form_frame, "Prezime:", 1)
        self.create_mobile_field(form_frame, 2)
        self.create_field(form_frame, "Email:", 3)
        self.create_field(form_frame, "OIB:", 4)
        self.create_date_field(form_frame, 5)

        # Password polja
        self.password_var = tk.StringVar()
        self.confirm_password_var = tk.StringVar()
        self.show_password = False
        self.show_confirm_password = False

        # Prvo password polje
        tk.Label(form_frame, text="Lozinka:").grid(row=6, column=0, padx=5, pady=5, sticky="e")
        self.password_entry = tk.Entry(form_frame, textvariable=self.password_var, width=30, show="*")
        self.password_entry.grid(row=6, column=1, padx=5, pady=5, sticky="w")
        self.password_eye_btn = tk.Button(form_frame, text="👁️", command=self.toggle_password, relief="flat")
        self.password_eye_btn.grid(row=6, column=2, padx=2, pady=5, sticky="w")

        # Drugo password polje (potvrda)
        tk.Label(form_frame, text="Ponovi lozinku:").grid(row=7, column=0, padx=5, pady=5, sticky="e")
        self.confirm_password_entry = tk.Entry(form_frame, textvariable=self.confirm_password_var, width=30, show="*")
        self.confirm_password_entry.grid(row=7, column=1, padx=5, pady=5, sticky="w")
        self.confirm_password_eye_btn = tk.Button(form_frame, text="👁️", command=self.toggle_confirm_password, relief="flat")
        self.confirm_password_eye_btn.grid(row=7, column=2, padx=2, pady=5, sticky="w")

        # Gumbi
        button_frame = tk.Frame(root)
        button_frame.pack(pady=15)
        
        tk.Button(button_frame, text="Registriraj se", width=15, 
                 command=self.validate_registration).pack(side=tk.LEFT, padx=10)
        tk.Button(button_frame, text="Odustani", width=15, 
                 command=root.destroy).pack(side=tk.LEFT, padx=10)

        # Validacijske poruke
        self.validation_label = tk.Label(root, text="", fg="red")
        self.validation_label.pack(pady=5)

    def toggle_password(self):
        self.show_password = not self.show_password
        if self.show_password:
            self.password_entry.config(show="")
            self.password_eye_btn.config(text="🙈")
        else:
            self.password_entry.config(show="*")
            self.password_eye_btn.config(text="👁️")

    def toggle_confirm_password(self):
        self.show_confirm_password = not self.show_confirm_password
        if self.show_confirm_password:
            self.confirm_password_entry.config(show="")
            self.confirm_password_eye_btn.config(text="🙈")
        else:
            self.confirm_password_entry.config(show="*")
            self.confirm_password_eye_btn.config(text="👁️")

    def create_field(self, frame, label, row):
        tk.Label(frame, text=label).grid(row=row, column=0, padx=5, pady=5, sticky="e")
        entry = tk.Entry(frame, width=30)
        entry.grid(row=row, column=1, padx=5, pady=5, sticky="w")
        setattr(self, f"{label[:-1].lower()}_entry", entry)

    def create_mobile_field(self, frame, row):
        tk.Label(frame, text="Broj mobitela:").grid(row=row, column=0, padx=5, pady=5, sticky="e")
        self.mobile_entry = tk.Entry(frame, width=30)
        self.mobile_entry.insert(0, "+385")
        self.mobile_entry.grid(row=row, column=1, padx=5, pady=5, sticky="w")
        self.mobile_entry.bind("<KeyRelease>", self.validate_mobile_prefix)

    def create_date_field(self, frame, row):
        tk.Label(frame, text="Datum rođenja (DD.MM.YYYY):").grid(row=row, column=0, padx=5, pady=5, sticky="e")
        self.dob_entry = tk.Entry(frame, width=30)
        self.dob_entry.grid(row=row, column=1, padx=5, pady=5, sticky="w")

    def validate_mobile_prefix(self, event):
        current = self.mobile_entry.get()
        if not current.startswith("+385"):
            self.mobile_entry.delete(0, tk.END)
            self.mobile_entry.insert(0, "+385")
        else:
            if len(current) > 13:
                self.mobile_entry.delete(13, tk.END)
            if len(current) > 4 and not current[4:].isdigit():
                filtered = ''.join(filter(str.isdigit, current[4:]))
                self.mobile_entry.delete(4, tk.END)
                self.mobile_entry.insert(4, filtered)

    def validate_registration(self):
        errors = []
        ime = self.ime_entry.get().strip()
        prezime = self.prezime_entry.get().strip()
        mobitel = self.mobile_entry.get().strip()
        email = self.email_entry.get().strip()
        oib = self.oib_entry.get().strip()
        datum = self.dob_entry.get().strip()
        password = self.password_var.get()
        confirm_password = self.confirm_password_var.get()

        # Validacija imena
        if not re.match(r"^[a-zA-ZčćžšđČĆŽŠĐ\s-]{2,}$", ime):
            errors.append("Neispravno ime (dozvoljena samo slova, razmaci i crtice, minimalno 2 znaka)")

        # Validacija prezimena
        if not re.match(r"^[a-zA-ZčćžšđČĆŽŠĐ\s-]{2,}$", prezime):
            errors.append("Neispravno prezime (dozvoljena samo slova, razmaci i crtice, minimalno 2 znaka)")

        # Validacija emaila
        if not re.match(r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$", email):
            errors.append("Neispravan format email adrese")

        # Validacija OIB-a
        if not (len(oib) == 11 and oib.isdigit()):
            errors.append("Neispravan OIB (mora imati točno 11 znamenki)")

        # Validacija datuma
        try:
            datum_obj = datetime.strptime(datum, "%d.%m.%Y")
            if datum_obj > datetime.now():
                errors.append("Datum rođenja ne može biti u budućnosti")
        except ValueError:
            errors.append("Neispravan format datuma (DD.MM.YYYY)")

        # Validacija lozinke
        if len(password) < 6:
            errors.append("Lozinka mora imati najmanje 6 znakova")
        if password != confirm_password:
            errors.append("Lozinke se ne podudaraju")

        if errors:
            self.validation_label.config(text="\n".join(errors))
        else:
            # Spremanje podataka u datoteku prije potvrde
            self.save_to_file(ime, prezime, mobitel, email, oib, datum, password)
            self.show_confirmation()

    def save_to_file(self, ime, prezime, mobitel, email, oib, datum, password):
        # Otvara ili stvara datoteku korisnici.txt i dodaje novi zapis
        with open("korisnici.txt", "a", encoding="utf-8") as file:
            file.write(f"Ime: {ime}\n")
            file.write(f"Prezime: {prezime}\n")
            file.write(f"Mobitel: {mobitel}\n")
            file.write(f"Email: {email}\n")
            file.write(f"OIB: {oib}\n")
            file.write(f"Datum rođenja: {datum}\n")
            file.write(f"Lozinka: {password}\n")
            file.write("-" * 40 + "\n")

    def show_confirmation(self):
        messagebox.showinfo(
            "Uspješna registracija",
            "Korisnik je uspješno registriran!\n\nDetalji:\n"
            f"Ime: {self.ime_entry.get()}\n"
            f"Prezime: {self.prezime_entry.get()}\n"
            f"Mobitel: {self.mobile_entry.get()}\n"
            f"Email: {self.email_entry.get()}\n"
            f"OIB: {self.oib_entry.get()}\n"
            f"Datum rođenja: {self.dob_entry.get()}"
        )
        self.root.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = RegistrationWindow(root)
    root.mainloop()

