import tkinter as tk
from tkinter import ttk

def insert_data(tree):
    inventions_data = [
         ("Acetylene Gas", "Berthelot", "1862", "France"),
        ("Adding Machine", "Pascal", "1642", "France"),
        ("Adhesive Tape, Scotch", "Richard Drew", "1930", "U.S.A."),
        ("Aeroplane", "Orville & Wilbur Wright", "1903", "U.S.A."),
        ("Aerosol Spray", "Erik Rotheim", "1926", "Norway"),
        ("Air Conditioning", "Carrier", "1902", "U.S.A."),
        ("Airplane, Jet Engine", "Ohain", "1939", "Germany"),
        ("Airship (non-rigid)", "Henri Giffard", "1852", "France"),
        ("Artificial Heart", "Willem Kolff", "1957", "Netherlands"),
        ("Atomic Bomb", "J. Robert Oppenheimer", "1945", "U.S.A."),
        ("Atomic Numbers", "Moseley", "1913", "Britain"),
        ("Atomic Theory", "Dalton", "1803", "Britain"),
        ("Automatic Rifle", "John Browning", "1918", "U.S.A."),
        ("Bakelite", "Leo H. Baekeland", "1907", "Belgium"),
        ("Ball-Point Pen", "John J. Loud", "1888", "U.S.A."),
        ("Ballistic Missile", "Wemher von Braun", "1944", "Germany"),
        ("Balloon", "Jacques & Joseph Montgolfier", "1783", "France"),
        ("Barometer", "Evangelista Torricelli", "1644", "Italy"),
        ("Battery (Electric)", "Alessandro Volta", "1800", "Italy"),
        ("Bicycle", "Kirkpatrick Macmillan", "1839-40", "Britain"),
        ("Bicycle Tyres (Pneumatic)", "John Boyd Dunlop", "1888", "Britain"),
        ("Bifocal Lens", "Benjamin Franklin", "1780", "U.S.A."),
        ("Bleaching Powder", "Tennant", "1798", "Britain"),
        ("Bunsen Burner", "R.Willhelm von Bunsen", "1855", "Germany"),
        ("Burglar Alarm", "Edwin T. Holmes", "1858", "U.S.A."),
    ]

    for i, (invention, inventor, year, country) in enumerate(inventions_data, start=1):
        tree.insert("", "end", iid=i, values=(invention, inventor, year, country))

def invention():
    root = tk.Tk()
    root.title("Inventions Table")

    tree = ttk.Treeview(root)
    tree["columns"] = ("Invention", "Inventor", "Year", "Country")

    tree.column("Invention", anchor=tk.W, width=150)
    tree.column("Inventor", anchor=tk.W, width=150)
    tree.column("Year", anchor=tk.W, width=100)
    tree.column("Country", anchor=tk.W, width=100)

    tree.heading("Invention", text="Invention", anchor=tk.W)
    tree.heading("Inventor", text="Inventor", anchor=tk.W)
    tree.heading("Year", text="Year", anchor=tk.W)
    tree.heading("Country", text="Country", anchor=tk.W)

    insert_data(tree)

    tree.pack(expand=True, fill=tk.BOTH)

    root.resizable(width=True, height=True)
    root.mainloop()

if __name__ == "__main__":
    invention()
