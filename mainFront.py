import tkinter as tk
from tkinter import filedialog, messagebox
import webbrowser
from Fiverr import DataScraping
from PIL import Image, ImageTk




def main_gui():
    def open_linkedin():
        webbrowser.open_new("https://www.linkedin.com/in/walid-benjdiya/")

    def display_image(image_path, width, height):
        # Ouvrir l'image avec Pillow
        img = Image.open(image_path)
        img = img.resize((width, height), Image.LANCZOS)
        return ImageTk.PhotoImage(img)  # Position en haut à gauche

    def save_function():
        repo_path = filedialog.askdirectory()
        if repo_path:
            repo_entry.config(state="normal")
            repo_entry.delete(0, tk.END)  # Supprime le texte précédent
            repo_entry.insert(0, repo_path)  # Insère le chemin choisi
            # Repasser le champ en mode "readonly"
            repo_entry.config(state="readonly")

    def search_function():
        title = entry.get()
        repo_path = repo_entry.get()

        if not title or not repo_path:
            messagebox.showerror("Erreur", "Please fill in the repository title and path.")
        else:
            DataScraping(title, repo_path)
            messagebox.showinfo("Confirmation", "The operation was performed successfully.")

    root = tk.Tk()
    #root.overrideredirect(True)

    root.title("Jobs Scrapers")
    root.geometry("850x470")
    root.resizable(False, False)
      # Ajustez la valeur ici pour l'espacement

    frame = tk.Frame(root)
    frame.pack(pady=(160, 0))
    background_image =display_image("../scraper1.png", 850, 470)
    background_label = tk.Label(root, image=background_image)
    background_label.place(x=0, y=0, relwidth=1, relheight=1)
    label = tk.Label(root, text="Enter Your Job Title :", font=("Arial", 12, "bold"), background="white")
    label.pack(pady=10)

    entry = tk.Entry(root, width=70)
    entry.pack(pady=0)

    save_ = tk.Button(root, text="Choose Your Repository", command=save_function)
    save_.pack(pady=10)

    repo_entry = tk.Entry(root, width=50,state="readonly")
    repo_entry.pack(pady=5)

    search = tk.Button(root,background="#f5ba4c", text="Generate Result", command=search_function)
    search.pack(pady=10)

    credit_text = tk.Label(root, text="Created by in/walid-benjdiya", fg="blue",cursor="hand2", bg="white")
    credit_text.place(relx=1.0, rely=1.0, anchor="se")  # Placer en bas à droite

    # Associer le label à l'ouverture du lien LinkedIn
    credit_text.bind("<Button-1>", lambda e: open_linkedin())
    root.mainloop()


if __name__ == '__main__':
    main_gui()
