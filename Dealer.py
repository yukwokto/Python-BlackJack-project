class Dealer:
    def __init__(self):
        self.hands = []
        self.hands_value = 0
        
   # adding card to player when player chooses to hit
    def deal_card(self, card):
        self.hands.append(card)
    
    # getter for player's hands
    def get_dealer_hands(self):
        return self.hands
    
    # getter for hand values
    def get_hands_value(self):
        return self.hands_value
    
    # setter for hand values
    def set_hands_value(self, value):
        self.hands_value = value
        
    # add a new card to dealer's hands
    def add_card(self, new_card):
        self.hands. append(new_card)
      
    # reset player hands for a new round  
    def reset_hands(self):
        self.hands = []    
