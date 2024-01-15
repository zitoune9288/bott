import os
import time
import random
import webbrowser

# Changer le titre de la fenêtre CMD
os.system("title zit-bot by zit_zitoune")

# Définir le motif dans une variable
motif = '''


███████╗██╗████████╗   ██████╗  ██████╗ ████████╗
╚══███╔╝██║╚══██╔══╝   ██╔══██╗██╔═══██╗╚══██╔══╝
  ███╔╝ ██║   ██║█████╗██████╔╝██║   ██║   ██║   
 ███╔╝  ██║   ██║╚════╝██╔══██╗██║   ██║   ██║   
███████╗██║   ██║      ██████╔╝╚██████╔╝   ██║   
╚══════╝╚═╝   ╚═╝      ╚═════╝  ╚═════╝    ╚═╝   
                                                 


                By zit_zitoune
                                                         
[1] Lancer le bot              [2] Tiktok          
[3] Instagram                  [4] Quitter       
'''

# Afficher le motif
print(motif)

# Demander à l'utilisateur de choisir
choix_utilisateur = input("Veuillez choisir: ")

# Traitement en fonction du choix
if choix_utilisateur == "1":
    print("Vous avez choisi 1. Exécution du bot...")
    time.sleep(3)
    phrase = input("Veuillez entrer L'url (lien) de votre musique sporify: ")
    print()
    print()

    print("Veuillez patientez quelque secondes...")
    time.sleep(10)
    print("Connection...")
    time.sleep(2)
    print("Préparation...")
    time.sleep(2)
    print("Connexion au 12 Machines via Cloud")
    time.sleep(2)
    print("Ecoute sur spotify sur 24 naviguateur Chrome donc 345 onglets")
    canal = random.randint(101, 135)
   # print(f"{canal} canal type = CC droper")
    time.sleep(1)
    print("Ecoute...")
    time.sleep(8000000)
elif choix_utilisateur == "2":
    webbrowser.open('https://www.tiktok.com/@zit_zitoune0')
elif choix_utilisateur == "3":
    webbrowser.open('https://www.instagram.com/zit_zitoune9999/')

elif choix_utilisateur == "4":
    print("exiting..")
    time.sleep(2)
    os.system("exit")

else:
    print("Choix non valide. Le programme se termine.")
