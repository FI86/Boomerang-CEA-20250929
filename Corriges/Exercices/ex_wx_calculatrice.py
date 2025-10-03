# Exercice WxPython : Faire l'apparence d'une calculatrice simple.

import wx

from math import sqrt

class Calculatrice(wx.Frame):
    LARGEUR = 400

    def __init__(self):
        super().__init__(parent=None, title="Calculatrice")
        panel = wx.Panel(self)
        self.SetMinSize((self.LARGEUR, 250))  # empêche la fenêtre d'être réduite plus petit que 400x250
        # Panel avec bordure pour creer un effet relief autour de l'afficheur.
        panel_afficheur = wx.Panel(panel, style=wx.BORDER_RAISED)

        # Champ texte statique pour afficher les entrees et les resultats.
        self.afficheur = wx.StaticText(panel_afficheur, style=wx.ALIGN_RIGHT)
        self.afficheur.SetFont(wx.Font(10, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD))
        # Fixe la largeur mini moins quelques pixels a cause des marges des panels etc..., -1 pour la hauteur signifie ne pas toucher a la hauteur.
        self.afficheur.SetMinSize((self.LARGEUR-30, -1))

        # Sizer pour l'afficheur avec un peu de marge.
        sizer_afficheur = wx.BoxSizer(wx.HORIZONTAL)
        sizer_afficheur.Add(self.afficheur, 1, wx.EXPAND | wx.ALL, 2)
        panel_afficheur.SetSizer(sizer_afficheur)

        # Sizer vertical principal.
        vbox = wx.BoxSizer(wx.VERTICAL)
        vbox.Add(panel_afficheur, 0, wx.EXPAND | wx.ALL, 2)

        # Grille pour les boutons.
        grid = wx.GridSizer(5, 4, 2, 2)

        # Liste des boutons.
        boutons = [
            "C", "CE", "x²", "√",
            "7", "8", "9", "*",
            "4", "5", "6", "-",
            "1", "2", "3", "+",
            "0", ".", "=", "/"]

        # Creation et liaison des boutons.
        for label in boutons:
            btn = wx.Button(panel, label=label)
            btn.SetCanFocus(False)
            btn.Bind(wx.EVT_BUTTON, self.on_clic)
            grid.Add(btn, 0, wx.EXPAND)

        # Ajout de la grille au sizer principal.
        vbox.Add(grid, 1, wx.EXPAND | wx.ALL, 2)
        panel.SetSizer(vbox)

        # Variable pour stocker l'expression.
        self.expression = ""

        # Focus sur l'afficheur au demarrage
        self.afficheur.SetFocus()

    def nettoyer_zeros(self, expr):
        # Operateurs a prendre en compte.
        operateurs: str = "+-*/"
        nettoyee: str = ""
        nombre: str = ""

        # Parcours des caracteres pour separer nombres et operateurs.
        for ch in expr:
            if ch in operateurs:
                if nombre != "":
                    # Suppression des zeros initiaux pour nombres decimaux.
                    if "." in nombre:
                        partie_entiere, partie_decimale = nombre.split(".", 1)
                        partie_entiere = partie_entiere.lstrip("0") or "0"
                        nombre = partie_entiere + "." + partie_decimale
                    else:
                        # Suppression des zeros initiaux pour entiers.
                        nombre = nombre.lstrip("0") or "0"

                    nettoyee += nombre
                    nombre = ""

                nettoyee += ch
            else:
                nombre += ch

        # Traitement du dernier nombre.
        if nombre != "":
            if "." in nombre:
                partie_entiere, partie_decimale = nombre.split(".", 1)
                partie_entiere = partie_entiere.lstrip("0") or "0"
                nombre = partie_entiere + "." + partie_decimale
            else:
                nombre = nombre.lstrip("0") or "0"

            nettoyee += nombre

        return nettoyee

    def format_resultat(self, valeur):
        # Convertit float en int si c'est un entier, sinon garde float
        if valeur == int(valeur):
            return str(int(valeur))
        else:
            return str(valeur)
        
    def on_clic(self, event):
        # Recuperation du texte du bouton clique.
        label = event.GetEventObject().GetLabel()

        match label:
            case "C":
                # Effacer toute l'expression.
                self.expression = ""
                self.afficheur.SetLabel("")
            case "CE":
                # Effacer le dernier caractere.
                self.expression = self.expression[:-1]
                self.afficheur.SetLabel(self.expression)
            case "x²":
                # Calculer le carre de la valeur affichee.
                try:
                    valeur = float(self.expression)
                    carre = valeur ** 2
                    self.expression = self.format_resultat(carre)
                    self.afficheur.SetLabel(self.expression)
                except:
                    self.afficheur.SetLabel("erreur")
                    self.expression = ""
            case "√":
                # Calculer la racine carree de la valeur affichee.
                try:
                    valeur = float(self.expression)
                    if valeur < 0:
                        raise ValueError("nombre negatif")
                    racine = sqrt(valeur)
                    self.expression = self.format_resultat(racine)
                    self.afficheur.SetLabel(self.expression)
                except:
                    self.afficheur.SetLabel("erreur")
                    self.expression = ""
            case "=":
                # Evaluer l'expression apres nettoyage des zeros initiaux.
                try:
                    expr = self.nettoyer_zeros(self.expression)
                    resultat = self.format_resultat(eval(expr))
                    self.afficheur.SetLabel(resultat)
                    self.expression = resultat
                except:
                    self.afficheur.SetLabel("erreur")
                    self.expression = ""
            case _:
                # Ajouter le texte du bouton a l'expression.
                self.expression += label
                self.afficheur.SetLabel(self.expression)
        
        # Redonne le focus a l'afficheur.
        wx.CallAfter(self.afficheur.SetFocus)

def main():
    # Lancer l'application wxPython.
    app = wx.App(False)
    fen = Calculatrice()
    fen.Show()
    app.MainLoop()

if __name__ == "__main__":
    main()
