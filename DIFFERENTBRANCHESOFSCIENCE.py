import tkinter as tk
from tkinter import ttk

def insert_data(tree):
    branches_data = [
        ("Aeronautics", "Science of flight of airplanes."),
        ("Astronomy", "Study of heavenly bodies."),
        ("Agronomy", "Science dealing with crop plant."),
        ("Angiology", "Deals with the study of blood vascular system."),
        ("Anthology", "Study of flower."),
        ("Anthropology", "Study of apes and man."),
        ("Apiculture", "Honey industries (Bee Keeping)."),
        ("Araneology", "Study of spiders."),
        ("Batracology", "Study of frogs."),
        ("Biochemistry", "Deals with the study of chemical reactions in relation to life activities."),
        ("Biotechnology", "Deals with the use of micro-organisms in commercial processes for producing fine chemicals such as drugs, vaccines, hormones etc. on a large scale."),
        ("Cardiology", "Study of heart."),
        ("Craniology", "Study of skulls."),
        ("Cryptography", "Study of secret writing."),
        ("Cryogenics", "Study concerning with the application and uses of very low temperature."),
        ("Cytology", "Study of cells."),
        ("Dermatology", "Study of skin."),
        ("Ecology", "The study of relationship between organisms and environment."),
        ("Entomology", "Study of insects."),
        ("Etiology", "Study of cause of insects."),
        ("Eugenics", "Study of improvement of human race by applying laws of heredity. it is related with future generations."),
        ("Evolution", "Deals with the study of origin of new from old."),
        ("Exbiology", "Deals with life or possibilities of life beyond the earth."),
        ("Floriculture", "Study of flower yielding plants."),
        ("Geology", "Study of condition and structure of the earth"),
        ("Genetics", "Study of heredity and variations."),
        ("Gerontology", "Study of growing old."),
        ("Gynaecology", "Study of female reproductive organs."),
        ("Horticulture", "Study of garden cultivation."),
        ("Haematology", "Study of blood."),
        ("Hepatology", "Study of liver."),
        ("Iconography", "Teachings by pictures and models."),
        ("Immunology", "Science which deals with the study of resistance of organisms against infection."),
        ("Jurisprudence", "Science of law."),
        ("Kalology", "Study of human beauty."),
        ("Lexicography", "Compiling of dictionary."),
        ("Mycology", "Study of fungi."),
        ("Myology", "Study of muscles."),
        ("Nephrology", "Study of kidneys."),
        ("Neurology", "Study of nervous system."),
        ("Numismatics", "Study of coins and medals."),
        ("Obstetrics", "Branch of medicine dealing with pregnancy."),
        ("Oneirology", "Study of dreams."),
        ("Ophthalmology", "Study of eyes ."),
        ("Omithology", "Study of birds."),
        ("Osteology", "Study of bones."),
        ("Palaeontology", "Study of fossils."),
        ("Philately", "Stamp collecting."),
        ("Philology", "Study of languages."),
        ("Phonetics", "Concerning the sounds of a language."),
        ("Physiography", "Natural phenomenon."),
        ("Pedology", "Study of soils."),
        ("Pathology", "Study of disease causing organisms."),
        ("Phycology", "Study of algae."),
        ("Physiology", "Science dealing with the study of functions of various parts of organisms."),
        ("Pisciculture", "Study of fish."),
        ("Pomology", "Study of fruits."),
        ("Seismology", "Study of earthquakes."),
        ("Sericulture", "Silk industry(culture of silk moth and pupa)."),
        ("Serpentology", "Study of snakes."),
        ("Telepathy", "Communication between two minds at a distance with the help of emotions, thoughts and feelings."),
        ("Taxonomy", "Study of classification of organisms."),
        ("Virology", "Study of virus."),
    ]

    for i, (branch, concerning_field) in enumerate(branches_data, start=1):
        tree.insert("", "end", iid=i, values=(branch, concerning_field))

def diff():
    root = tk.Tk()
    root.title("Branches and Concerning Fields Table")

    tree = ttk.Treeview(root)
    tree["columns"] = ("Branch", "Concerning Field")

    tree.column("Branch", anchor=tk.W, width=150)
    tree.column("Concerning Field", anchor=tk.W, width=300)

    tree.heading("Branch", text="Branch", anchor=tk.W)
    tree.heading("Concerning Field", text="Concerning Field", anchor=tk.W)

    insert_data(tree)

    tree.pack(expand=True, fill=tk.BOTH)

    root.resizable(width=True, height=True)
    root.mainloop()

if __name__ == "__main__":
    diff()
