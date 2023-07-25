
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
    dealer = None
    bankroll = None
    first_name = ''
    last_name = ''
    full_name = ''
    current_bet = 0
    minimum = 0
    maximum = 0
    current_hand = None
    seat = None
    def __init__(self, first, last, bank):
        self.dealer = False
        self.first_name = first
        self.last_name = last
        self.bankroll = bank
        self.full_name = first + ' ' + last
    def min_bet(self,minimum):
        self.current_bet = minimum
    def mid_bet(self,minimum):
        self.current_bet = minimum * 0.5
    def high_bet(self,maximum):
        self.current_bet = maximum 


class Dealer(Player):
    def __init__(self, first, last, bank):
        self.dealer = True
        self.first_name = first
        self.last_name = last
        self.full_name = 'Dealer ' + first

