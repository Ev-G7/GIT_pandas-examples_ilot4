# Ecrivez votre programme ci-dessous.
# Bouton Fullscreen pour passer en plein ecran
# Ensuite Save + Run puis Save + Evaluate
# Pour des raisons techniques, laissez une ligne blanche avant de commencer votre programme.


def tarif_carte(carte):
    if carte == "Jeune":
        return 50
    elif carte == "Senior":
        return 60 
    else:
        print("carte inconue")
        return None
        
        
def plein_tarif(ville_depart, ville_arrivee):
    prix_trajet = {
        ("Grenoble" , "Paris"): 100, ("Grenoble" , "Lyon"): 20, ("Lyon" , "Paris"): 80, ("Paris" , "Grenoble"): 100, ("Lyon" , "Grenoble"): 20, ("Paris" , "Lyon"): 80
    }
    if (ville_depart , ville_arrivee) in prix_trajet:
        return prix_trajet[(ville_depart, ville_arrivee)]
    
    else:
        print("trajet inconnu")
        return None 
      
        
def tarif_billet(ville_depart, ville_arrivee, modifiable=True, carte=None, periode=None):
    prix_trajet = {
        ("Grenoble" , "Paris"): 100, ("Grenoble" , "Lyon"): 20, ("Lyon" , "Paris"): 80, ("Paris" , "Grenoble"): 100, ("Lyon" , "Grenoble"): 20, ("Paris" , "Lyon"): 80
    }
    
    tarif = prix_trajet[(ville_depart , ville_arrivee)]
    
    if carte == "Jeune":
        if periode == "bleue":
             tarif *= 0.5
        elif periode == "blanche":
            tarif*=0.70
        else:
            print("erreur")
            return None
            
    elif carte == "Senior":
            if periode == "bleue":
                tarif *=0.5
            elif periode == "blanche":
                tarif*=0.75
            else:
                print("erreur")
                return None 
    
    elif not modifiable:
        tarif *= 0.9
    
    return tarif
     
if __name__=="__main__": # NE PAS SUPPRIMER CETTE LIGNE
    # Votre programme principal ne sera pas évalué.
    # Utilisez-le pour tester votre programme en faisant
    # les appels de votre choix.
    # Respectez bien ce niveau d'identation.
    print("Debut du prog. principal")
    print(tarif_carte("Jeune"))
    print(tarif_billet("Paris" , "Lyon"))
    print(tarif_billet("Paris , Lyon" ,False, "Jeune" , "bleue"))
    