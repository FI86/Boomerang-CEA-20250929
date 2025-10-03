# Cours wxPython

import wx

class ExempleFrame(wx.Frame):
    def __init__(self):
        # definie une taille et un titre a la fentre principale.
        super().__init__(None, title="Exemple complet wxPython", size=(450, 400))
        # Creation d'une barre de statut (en bas de la fenetre principale).
        self.CreateStatusBar()

        # Menu
        # Creation d'un objet Menu vide qui sera le menu deroulant nommé Fichier.
        menu_fichier = wx.Menu()
        # Ajoute un element au Menu (ID_EXIT est un identifiant wx standard pour un element de sortie)
        # Affectation a une variable quitter pour associer a un evenement.
        quitter = menu_fichier.Append(wx.ID_EXIT, "Quitter\tCtrl+Q")
        # Creation d'une barre de menu qui contiendra le menu Fichier.
        menu_bar = wx.MenuBar()
        # Ajout du menu Fichier a la barre de menu (& permet de faire Alt + lettre suivant le &)
        menu_bar.Append(menu_fichier, "&Fichier")
        # Association de la barre de menu a la fenetre.
        self.SetMenuBar(menu_bar)
        # Connection d'un evenement a l'element Quitter du menu Fichier.
        # wx.EVT_MENU est l’événement déclenché quand on clique sur un item de menu.
        # self.on_exit est la méthode appelée lorsque l’item quitter est sélectionné.
        # quitter est la source de l’événement (le menu item "Quitter").
        self.Bind(wx.EVT_MENU, self.on_exit, quitter)

        # Onglets
        onglet = wx.Notebook(self)

        # Onglet 1 : texte multiline
        # Creer un panel enfant de onglet
        panel1 = wx.Panel(onglet)
        # Creer un sizer (layout) enfant de panel1 (ne peut contenir des widgets directement, ne sert qu'a la mise en forme)
        vbox1 = wx.BoxSizer(wx.VERTICAL)
        # Creer un widget enfant de panel1
        text = wx.TextCtrl(panel1, style=wx.TE_MULTILINE)
        # Mise en forme du widget
        vbox1.Add(text, 1, wx.EXPAND | wx.ALL, 10)
        # Attribution du sizer a panel1
        panel1.SetSizer(vbox1)
        # Ajoute panel1 a l'onglet "Onglet 1"
        onglet.AddPage(panel1, "Onglet 1")

        # Onglet 2 : d'autres widgets
        panel2 = wx.Panel(onglet)

        # StaticText (label)
        self.label = wx.StaticText(panel2, label="Entrez votre nom:")

        # TextCtrl (zone de saisie)
        self.text_ctrl = wx.TextCtrl(panel2)

        # Bouton simple
        self.bouton_saluer = wx.Button(panel2, label="Saluer")
        self.bouton_saluer.Bind(wx.EVT_BUTTON, self.on_saluer)

        # CheckBox
        self.checkbox_important = wx.CheckBox(panel2, label="Important ?")

        # RadioButton (choix exclusif)
        self.radio1 = wx.RadioButton(panel2, label="Option 1", style=wx.RB_GROUP)
        self.radio2 = wx.RadioButton(panel2, label="Option 2")

        # ComboBox (liste déroulante)
        self.combo = wx.ComboBox(panel2, choices=["elem 1", "elem 2", "elem 3"], style=wx.CB_READONLY)
        self.combo.SetSelection(0)

        # Barre de progression
        self.gauge = wx.Gauge(panel2, range=100, size=(250, 25))

        # Bouton pour lancer la progression
        self.bouton_progression = wx.Button(panel2, label="Lancer progression")
        self.bouton_progression.Bind(wx.EVT_BUTTON, self.on_progression)

        # Sizers pour mise en page verticale avec marges
        # wx.ALL = wx.LEFT + wx.RIGHT + wx.TOP + wx.BOTTOM, permet de savoir où appliquer le padding
        # wx.EXPAND = le widget prendra toute la place disponible dans le sizer.
        # si le sizer est vertical, le wdget prendra l'espace horizontale disponible, et vice-versa.
        vbox2 = wx.BoxSizer(wx.VERTICAL)
        vbox2.Add(self.label, 0, wx.ALL, 5)
        vbox2.Add(self.text_ctrl, 0, wx.EXPAND | wx.LEFT | wx.RIGHT, 5)
        vbox2.Add(self.bouton_saluer, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL, 10)
        vbox2.Add(self.checkbox_important, 0, wx.ALL, 5)
        vbox2.Add(self.radio1, 0, wx.ALL, 5)
        vbox2.Add(self.radio2, 0, wx.ALL, 5)
        vbox2.Add(self.combo, 0, wx.ALL | wx.EXPAND, 5)
        vbox2.Add(self.gauge, 0, wx.ALL | wx.EXPAND, 5)
        vbox2.Add(self.bouton_progression, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL, 10)
        # Association de la mise en forme (sizer / layout) a panel2
        panel2.SetSizer(vbox2)

        # Association de panel2 a l'onglet Formulaire.
        onglet.AddPage(panel2, "Formulaire")

        # Layout global
        sizer = wx.BoxSizer(wx.VERTICAL)
        # Ajout des onglets au sizer principale.
        sizer.Add(onglet, 1, wx.EXPAND)
        # ajout du sizer principal a la fenetre principale.
        self.SetSizer(sizer)

    # Sortie de l'application
    # (event est obligatoire meme si on ne l'utilise pas car wxPython retourne un event).
    def on_exit(self, event):
        self.Close(True)

    # Fonction d'affichage des valeurs des widgets.
    # (event est obligatoire meme si on ne l'utilise pas car wxPython retourne un event).
    def on_saluer(self, event):
        # Recuperation des valeurs des widgets
        nom = self.text_ctrl.GetValue()
        important = self.checkbox_important.GetValue()
        option = "Option 1" if self.radio1.GetValue() else "Option 2"
        elem = self.combo.GetStringSelection()
        # Composition du message selon les valeurs recuperes
        message = f"Bonjour {nom}!\n"
        message += f"Important : {'Oui' if important else 'Non'}\n"
        message += f"Option choisie : {option}\n"
        message += f"Element choisi : {elem}"
        # Affichage du message.
        wx.MessageBox(message, "Salutation", wx.OK | wx.ICON_INFORMATION)

    # Fonction de la barre de progression.
    # (event est obligatoire meme si on ne l'utilise pas car wxPython retourne un event)
    def on_progression(self, event):
        # Simple simulation de progression.
        for i in range(101):
            wx.MilliSleep(10)
            self.gauge.SetValue(i)
            # wx.Yield() une fonction qui permet à la boucle principale de l’interface graphique
            # de traiter les événements en attente pendant qu’un autre traitement long est en cours.
            wx.Yield()


# Programme principal.
def main():
    # Creation de l'application.
    app = wx.App(False)
    # Creation de la fenetre principale.
    frame = ExempleFrame()
    # Affichage de la fenetre principale.
    frame.Show()
    # Boucle principale permettant d'attendre les evenements.
    app.MainLoop()

# Execution du programme principal.
if __name__ == "__main__":
    main()