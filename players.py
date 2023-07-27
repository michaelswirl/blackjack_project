
class Player:
    POSSIBLE_FIRST_NAMES = [
        "John", "Sarah", "Emily", "Michael", "Jessica", 
        "Jacob", "Emma", "Daniel", "Olivia", "David", 
        "Sophia", "Joseph", "Ava", "Benjamin", "Isabella", 
        "Samuel", "Mia", "Matthew", "Charlotte", "Luke",
        "Amelia", "James", "Harper", "Andrew", "Evelyn",
        "Alexander", "Abigail", "Ryan", "Ella", "Joshua", 
        "Scarlett", "Ethan", "Grace", "William", "Madison", 
        "Jack", "Elizabeth", "Owen", "Avery", "Gabriel", 
        "Sofia", "Zachary", "Chloe", "Justin", "Lily",
        "Nathan", "Addison", "Caleb", "Lucy", "Adam", 
        "Audrey", "Aiden", "Bella", "Henry", "Nora", 
        "Isaac", "Zoe", "Liam", "Paisley", "Mason", 
        "Brooklyn", "Thomas", "Hannah", "Noah", "Natalie", 
        "Jackson", "Layla", "Logan", "Alexa", "Robert", 
        "Violet", "Lucas", "Stella", "Max", "Mila", 
        "Oliver", "Piper", "Charlie", "Ruby", "Elijah", 
        "Sadie", "Carter", "Penelope", "Hunter", "Riley", 
        "Jaxon", "Leah", "Connor", "Hazel", "Levi", 
        "Victoria", "Julian", "Aria", "Aaron", "Ellie", 
        "Adrian", "Alice", "Austin", "Gabriella", "Evan", 
        "Madelyn", "Angel", "Cora", "Dominic", "Peyton", 
        "Cooper", "Julia", "Jonathan", "Isla", "Nicholas", 
        "Claire", "Jordan", "Annabelle", "Gavin", "Aubrey"
        ]
    POSSIBLE_LAST_NAMES = [
        "Smith", "Johnson", "Williams", "Jones", "Brown", 
        "Davis", "Miller", "Wilson", "Moore", "Taylor", 
        "Anderson", "Thomas", "Jackson", "White", "Harris",
        "Martin", "Thompson", "Garcia", "Martinez", "Robinson", 
        "Clark", "Rodriguez", "Lewis", "Lee", "Walker",
        "Hall", "Allen", "Young", "Hernandez", "King", 
        "Wright", "Lopez", "Hill", "Scott", "Green",
        "Adams", "Baker", "Gonzalez", "Nelson", "Carter",
        "Mitchell", "Perez", "Roberts", "Turner", "Phillips", 
        "Campbell", "Parker", "Evans", "Edwards", "Collins",
        "Stewart", "Sanchez", "Morris", "Rogers", "Reed",
        "Cook", "Morgan", "Bell", "Murphy", "Bailey", 
        "Rivera", "Cooper", "Richardson", "Cox", "Howard",
        "Ward", "Torres", "Peterson", "Gray", "Ramirez",
        "James", "Watson", "Brooks", "Kelly", "Sanders", 
        "Price", "Bennett", "Wood", "Barnes", "Ross",
        "Henderson", "Coleman", "Jenkins", "Perry", "Powell", 
        "Long", "Patterson", "Hughes", "Flores", "Washington",
        "Butler", "Simmons", "Foster", "Gonzales", "Bryant", 
        "Alexander", "Russell", "Griffin", "Diaz", "Hayes", 
        "Myers", "Ford", "Hamilton", "Graham", "Sullivan", 
        "Wallace", "Woods", "Cole", "West", "Jordan", 
        "Owens", "Reynolds", "Fisher", "Ellis", "Harrison", 
        "Gibson", "McDonald", "Cruz", "Marshall", "Ortiz"
        ]
    def __init__(self, first, last):
        pass

class Dealer(Player):
    def __init__(self, first, last):
        self.dealer = True
        self.first_name = first
        self.last_name = last
        self.full_name = 'Dealer ' + first
        self.hand_value = 0
        self.cards = []

class Gambler(Player):
    def __init__(self, first, last, bank, position, min, max):
        self.dealer = False
        self.first_name = first
        self.last_name = last
        self.full_name = first + ' ' + last
        self.bankroll = bank
        self.seat = position
        self.current_bet  = 0
        self.minimum_bet = min
        self.maximum_bet = max
        self.cards = []
        self.hand_value = 0
        self.hand = [card.card_title for card in self.cards]



        
    


