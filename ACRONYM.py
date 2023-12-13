import tkinter as tk
from tkinter import ttk
def insert_data(tree):
    acronyms_data = [
        ("3G", "Third Generation", ""),
        ("4G", "Fourth Generation", ""),
        ("A.M.", "Ante Meridiem (before noon)", ""),
        ("AAA", "Asian Athletics Association", ""),
        ("AAF", "Amateur Athletics Federation of India", ""),
        ("AAG", "Afro-Asian Games", ""),
        ("AAI", "Airport Authority of India", ""),
        ("AAIB", "Aircraft Accident Investigation Bureau", ""),
        ("AAOU", "Asian Association for Open University", ""),
        ("AAPSO", "Afro-Asian Peoples Solidarity Organisation", ""),
        ("AASU", "All-Assam Students' Union", ""),
        ("ABC", "Audit Bureau of Circulations", "American Broadcasting Company"),
        ("ABM", "Anti Ballistic Missile", ""),
        ("ABSU", "All Bodo Student' Union", ""),
        ("ABU", "Asian Broadcasting Union", ""),
        ("AC", "Air Conditioner", "Ante Christum (Before Christ)"),
        ("Ashok Chakra", "", ""),
        ("ACAS", "Airborne Collision Avoidance System", ""),
        ("ACB", "Anti-Corruption Bureau", ""),
        ("ACC", "Auxiliary Cadet Corps", "Air Coordinating Committee"),
        ("ACD", "Asian Co-operation Dialogue", "Anti Collision Device"),
        ("ACEEE", "American Council for an Energy-Efficient Economy", ""),
        ("ACHR", "Asian Centre for Human Rights", ""),
        ("ACL", "Access Control List", ""),
        ("ACU", "Asian Clearing Union", ""),
        ("AD", "Anno Domini (After Christ)", ""),
        ("ADB", "Asian Development Bank", ""),
        ("ADF", "Asian Development Fund", ""),
        ("ADRs", "American Depository Receipts", ""),
        ("ADS", "Air Defence Ship", ""),
        ("AEC", "Atomic Energy Commission", ""),
        ("AEOI", "Automatic Exchange of Information", ""),
        ("AERB", "Atomic Energy Regulation Board", ""),
        ("AF", "Audio Frequency", ""),
        ("AFC", "Asian Football Confederation", ""),
        ("AFI", "Athletics Federation of India", ""),
        ("AFMC", "Armed Forces Medical College", ""),
        ("AFNET", "Air Force Network", ""),
        ("AFP", "Australian Federal Police", ""),
        ("AFSPA", "Armed Forces Special Powers Act", ""),
        ("AFTC", "Asia Foundation for Thermonuclear Studies", ""),
        ("AG", "Accountant General", "Attorney General"),
        ("AGM", "Annual General Meeting", ""),
        ("AGP", "Accelerated Graphics Port", ""),
        ("AI", "Artificial Intelligence", ""),
        ("AIADMK", "All India Anna Dravida Munnetra Kazhagam", ""),
        ("AIBEA", "All India Bank Employees Association", ""),
    ]

    for i, (acronym, abbreviation, full_form) in enumerate(acronyms_data, start=1):
        tree.insert("", "end", iid=i, values=(acronym, abbreviation, full_form))

def acro():
    root = tk.Tk()
    root.title("Acronyms and Abbreviations Table")
    tree = ttk.Treeview(root)
    tree["columns"] = ("Acronym", "Abbreviation", "Full Form")
    tree.column("Acronym", anchor=tk.W, width=100)
    tree.column("Abbreviation", anchor=tk.W, width=150)
    tree.column("Full Form", anchor=tk.W, width=300)
    tree.heading("Acronym", text="Acronym", anchor=tk.W)
    tree.heading("Abbreviation", text="Abbreviation", anchor=tk.W)
    tree.heading("Full Form", text="Full Form", anchor=tk.W)
    insert_data(tree)
    tree.pack(expand=True, fill=tk.BOTH)

    root.resizable(width=True, height=True)
    root.mainloop()

if __name__ == "__main__":
    acro()
