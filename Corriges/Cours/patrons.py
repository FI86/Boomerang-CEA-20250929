# Fichier d'exemple de patrons de conception

# Singleton pattern
class Singleton:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

# Utilisation
a = Singleton()
b = Singleton()
print(a is b)  # True



# Factory pattern
class Chien:
    def parler(self):
        return "Wouf!"


class Chat:
    def parler(self):
        return "Miaou!"

def animal_factory(animal_type):
    match (animal_type):
        case "chien": return Chien()
        case "chat":  return Chat()

# Utilisation
animal = animal_factory("chien")
print(animal.parler())  # Wouf!



# Observer pattern
class Sujet:
    def __init__(self):
        self._observateurs = []

    def attache(self, observateur):
        self._observateurs.append(observateur)

    def notification(self, message):
        for observateur in self._observateurs:
            observateur.maj(message)


class Observateur:
    def maj(self, message):
        print("Reçu:", message)

# Utilisation
sujet = Sujet()
observateur1 = Observateur()
observateur2 = Observateur()
sujet.attache(observateur1)
sujet.attache(observateur2)

sujet.notification("Changement d'état")  # Tous les observateurs seront notifiés



# Strategy pattern
class Context:
    def __init__(self, strategy):
        self.strategy = strategy

    def execute(self, data):
        return self.strategy(data)

def strategy_upper(text :str):
    return text.upper()

def strategy_lower(text :str):
    return text.lower()

# Utilisation
ctx = Context(strategy_upper)
print(ctx.execute("Hello"))  # HELLO

ctx.strategy = strategy_lower
print(ctx.execute("Hello"))  # hello
