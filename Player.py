class Player:
    def __init__(self) -> None:
        self.hands = []
        self.hands_value = 0
        self.account_balance = 0
        
    # allow user to set their account balance
    def set_account_balance(self):
        balance = eval(input('Please enter your account balance: $'))
        while balance <= 0:
            balance = eval(input('Please enter a valid balance: $'))
        self.account_balance = balance
        print(f'Your account have a balance of ${self.account_balance}')
        
    # getter for account balance 
    def get_account_balance(self):
        return self.account_balance
    
    # when player win the rounds, payout is return
    def add_account_balance(self, value):
        self.account_balance += value
        
    # when player place a bet to the pool, money is withdrew
    def withdraw_for_bet(self, bet):
        self.account_balance -= bet
    
    # adding card to player when player chooses to hit
    def deal_card(self, card):
        self.hands.append(card)
    
    # getter for player's hands
    def get_player_hands(self):
        return self.hands
    
    # getter for hand values
    def get_hands_value(self):
        return self.hands_value
    
    # setter for hand values
    def set_hands_value(self, value):
        self.hands_value = value
    
    # add card to player's hand if the player is hit
    def add_card(self, new_card):
        self.hands. append(new_card)
        
    # reset player hands for a new round    
    def reset_hands(self):
        self.hands = []
