# Liste des tâches
liste = []

#Fonctionnalité 1 : Afficher la liste des tâches
print("La liste est vide")

def add_task():
    tâche = input("Entrez une nouvelle tâche : ")
    liste.append({"task": tâche, "terminée": False})  # Ajouter la tâche sous forme de dictionnaire
    print("Tâche ajoutée !")

def show_tasks():
    if not liste:
        print("La liste est vide.")
    else:
        print("Liste des tâches :")
        for i, tâche in enumerate(liste):
            status = "✅" if tâche["terminée"] else "❌"  # Utilisation des emojis pour le statut
            print(f"{i + 1}. {tâche['task']} [{status}]")  # Affichage de chaque tâche

def mark_task_as_done():
    show_tasks()  # Afficher les tâches pour permettre le choix
    if not liste:
        return

    try:
        task_number = int(input("Entrez le numéro de la tâche à marquer comme terminée : "))
        if 1 <= task_number <= len(liste):
            liste[task_number - 1]["terminée"] = True  # Marquer la tâche comme terminée
            print(f"Tâche '{liste[task_number - 1]['task']}' marquée comme terminée !")
        else:
            print("Numéro de tâche invalide.")
    except ValueError:
        print("Veuillez entrer un numéro valide.")

# Boucle principale pour le menu
while True:
    print("\nChoisissez une action :")
    print("1. Afficher les tâches")
    print("2. Ajouter une tâche")
    print("3. Marquer une tâche comme terminée")
    print("4. Quitter")
    choice = input("> ")

    if choice == '1':
        show_tasks()
    elif choice == '2':
        add_task()
    elif choice == '3':
        mark_task_as_done()
    elif choice == '4':
        print("À bientôt !")
        break
    else:
        print("Choix invalide. Veuillez réessayer.")
