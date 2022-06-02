class PlayerProfile:
    def __init__(self, name, position):
        self.name = name
        self.position = position

player1 = PlayerProfile('Mo Salah', 'Right Winger')

if hasattr(player1, 'rating'):
    print('Attribute is present')
else:
    print('Attribute Missing')
