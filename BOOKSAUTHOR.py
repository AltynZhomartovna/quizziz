import tkinter as tk
from tkinter import ttk

def insert_data(tree):
    books_data = [
        ("Vision of the Past", "Michel Madhusudan Dutta", ""),
        ("Captive Lady", "Michel Madhusudan Dutta", ""),
        ("A Nation is Making", "Surendra Nath Bandhopadhye", ""),
        ("War and Peace", "Tolstoy", ""),
        ("End and Means", "Huxlay", ""),
        ("Shadow of Ladakh", "Bhabani Bhattacharya", ""),
        ("Paradise Lost", "John Milton", ""),
        ("A week with Gandhi", "L. Fischer", ""),
        ("Myth of Independence", "Zulfikar Ali Bhutto", ""),
        ("Kidnapped", "Stevenson", ""),
        ("I Van Ho", "Walter Scot", ""),
        ("I follow the Mahatma", "K. M. Munshi", ""),
        ("Hindu View of Life", "S. Radhakrishnan", ""),
        ("Gathering Strom", "Churchill", ""),
        ("All the Prime Minister's Men", "Janardan Thakur", ""),
        ("Death of President", "W. Marchent", ""),
        ("Crisis of India", "Ronal Segal", ""),
        ("Urbashi", "R. D. Dinkar", ""),
        ("Adventures of Sherlock Homes", "Arther Canon Doel", ""),
        ("The Commedy of Errors", "William Shekhspeare", ""),
        ("Devine Comedi", "Dante", ""),
        ("A Pair of Blue Eyes", "Thomash Hardy", ""),
        ("Volga Se Ganga", "Rahul Sankrityayan", ""),
        ("Buddhacharit", "Asha Ghosh", ""),
        ("Astyadhaye", "Panini", ""),
        ("An Equal Music", "Vikram Seth", ""),
        ("Decamaren", "Bocachio", ""),
        ("Gaurdbaho", "Bakpatiraj", ""),
        ("Ferary Queen", "Edmond Spensar", ""),
        ("Three Marketiars", "Alexander Doma", ""),
        ("Kanterbary Tells", "Geofray Chosar", ""),
        ("Theory of Relativity", "Einstein", ""),
        ("Circle of the Region", "Amitav Ghosh", ""),
        ("City of Job Charnak", "Nisith Ranjan Roy", ""),
        ("India Divided", "Rajendra Prashad", ""),
        ("India Wins Freedom", "Abdul Kalam Azad", ""),
        ("Two Leaves and a Bud", "Mulkraj Anand", ""),
        ("Ramcharit", "S. K. Nandi", ""),
        ("A Tale of Two Cities", "Charls Dikens", ""),
        ("Indica", "Megasthenis", ""),
        ("Rajtarangini", "Kalhan", ""),
        ("Tahakak - E - Hind", "Albiruni", ""),
        ("The Satanic Verse", "Salman Rushdi", ""),
        ("Chidambara", "S. N. Panth", ""),
        ("Netaji Dead or Alive", "Samar Guha", ""),
        ("Apple Carte", "G. B. Shaw", ""),
        ("The Bandit Queen", "Mala Sen", ""),
        ("Bengali Zamindar", "Nilmoni Mukherjee", ""),
        ("The Silent Cry", "Kenjaburo Ue", ""),
        ("Allahabad Prasasti", "Harisen", ""),
    ]
    for i, (book_name, author, note) in enumerate(books_data, start=1):
        tree.insert("", "end", iid=i, values=(book_name, author, note))

def bookss():
    root = tk.Tk()
    root.title("Book Information Table")

    tree = ttk.Treeview(root)
    tree["columns"] = (
        "Book Name",
        "Author/Writer",
        "Note",
    )

    tree.column("Book Name", anchor=tk.W, width=150)
    tree.column("Author/Writer", anchor=tk.W, width=150)
    tree.column("Note", anchor=tk.W, width=200)

    tree.heading("Book Name", text="Book Name", anchor=tk.W)
    tree.heading("Author/Writer", text="Author/Writer", anchor=tk.W)
    tree.heading("Note", text="Note", anchor=tk.W)

    insert_data(tree)

    tree.pack(expand=True, fill=tk.BOTH)

    root.resizable(width=True, height=True)
    root.mainloop()

if __name__ == "__main__":
    bookss()
