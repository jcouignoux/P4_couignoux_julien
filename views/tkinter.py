from tkinter import *
from tkinter.messagebox import *


class TkinterView(Tk):

    def __init__(self, parent):
        self.window = Tk.__init__(self, parent)
        self.geometry('1000x800')
        self.bg = 'ivory'
        self.parent = parent
        self.initialize()
        # self.root()

    def run(self):
        self.mainloop()

    def initialize(self):
        self.title("ChessApp")
        menubar = Menu(self)
        menu1 = Menu(menubar, tearoff=0)
        menu1.add_command(label="Accueil",
                          command=self.root)
        # menu1.add_command(label="Créer un tournoi",
        #                   command=self.display_create_tournament)
        # menu1.add_command(label="Créer un joueur",
        #                   command=self.display_create_player)
        # menu1.add_command(label="Charger un tournoi", command=self.alert)
        menu1.add_separator()
        menu1.add_command(label="Quitter", command=self.quit)
        menubar.add_cascade(label="Fichier", menu=menu1)

        menu2 = Menu(menubar, tearoff=0)
        # menu2.add_command(label="Liste Tournois",
        #                   command=self.list_tournaments)
        # menu2.add_command(label="Liste Joueurs", command=self.liste_players)
        # menu2.add_command(label="Coller", command=self.alert)
        menubar.add_cascade(label="Editer", menu=menu2)

        menu3 = Menu(menubar, tearoff=0)
        # menu3.add_command(label="A propos", command=self.alert)
        menubar.add_cascade(label="Aide", menu=menu3)

        self.config(menu=menubar)

        self.frame = Frame(self, width=1000, height=800,
                           padx=5, pady=30, bg='ivory')
        self.frame.pack_propagate(False)
        self.frame.pack()

    def root(self):
        for widget in self.frame.winfo_children():
            widget.pack_forget()
        self.label = Label(self.frame, text="Bienvenue")
        self.label.pack()
        self.logo = PhotoImage(file="logo.png")
        self.canvas = Canvas(self.frame, width=1000, height=800, bg='ivory')
        self.canvas.create_image(500, 300, image=self.logo)
        self.canvas.pack(side=TOP, padx=5, pady=5)
