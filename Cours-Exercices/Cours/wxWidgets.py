# Cours wxPython


        # definie une taille et un titre a la fentre principale.

        # Creation d'une barre de statut (en bas de la fenetre principale).


        # Menu
        # Creation d'un objet Menu vide qui sera le menu deroulant nommé Fichier.

        # Ajoute un element au Menu (ID_EXIT est un identifiant wx standard pour un element de sortie)
        # Affectation a une variable quitter pour associer a un evenement.

        # Creation d'une barre de menu qui contiendra le menu Fichier.

        # Ajout du menu Fichier a la barre de menu (& permet de faire Alt + lettre suivant le &)

        # Association de la barre de menu a la fenetre.

        # Connection d'un evenement a l'element Quitter du menu Fichier.
        # wx.EVT_MENU est l’événement déclenché quand on clique sur un item de menu.
        # self.on_exit est la méthode appelée lorsque l’item quitter est sélectionné.
        # quitter est la source de l’événement (le menu item "Quitter").


        # Onglets


        # Onglet 1 : texte multiline
        # Creer un panel enfant de onglet

        # Creer un sizer (layout) enfant de panel1 (ne peut contenir des widgets directement, ne sert qu'a la mise en forme)

        # Creer un widget enfant de panel1

        # Mise en forme du widget

        # Attribution du sizer a panel1

        # Ajoute panel1 a l'onglet "Onglet 1"


        # Onglet 2 : d'autres widgets


        # StaticText (label)
 

        # TextCtrl (zone de saisie)


        # Bouton simple


        # CheckBox


        # RadioButton (choix exclusif)


        # ComboBox (liste déroulante)


        # Barre de progression


        # Bouton pour lancer la progression


        # Sizers pour mise en page verticale avec marges
        # wx.ALL = wx.LEFT + wx.RIGHT + wx.TOP + wx.BOTTOM, permet de savoir où appliquer le padding
        # wx.EXPAND = le widget prendra toute la place disponible dans le sizer.
        # si le sizer est vertical, le wdget prendra l'espace horizontale disponible, et vice-versa.

        # Association de la mise en forme (sizer / layout) a panel2


        # Association de panel2 a l'onglet Formulaire.


        # Layout global

        # Ajout des onglets au sizer principale.

        # ajout du sizer principal a la fenetre principale.
 

    # Sortie de l'application
    # (event est obligatoire meme si on ne l'utilise pas car wxPython retourne un event).


    # Fonction d'affichage des valeurs des widgets.
    # (event est obligatoire meme si on ne l'utilise pas car wxPython retourne un event).

        # Recuperation des valeurs des widgets

        # Composition du message selon les valeurs recuperes

        # Affichage du message.


    # Fonction de la barre de progression.
    # (event est obligatoire meme si on ne l'utilise pas car wxPython retourne un event)

        # Simple simulation de progression.

            # wx.Yield() une fonction qui permet à la boucle principale de l’interface graphique
            # de traiter les événements en attente pendant qu’un autre traitement long est en cours.



# Programme principal.

    # Creation de l'application.

    # Creation de la fenetre principale.

    # Affichage de la fenetre principale.

    # Boucle principale permettant d'attendre les evenements.


# Execution du programme principal.
