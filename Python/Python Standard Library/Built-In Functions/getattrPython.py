class PlayerProfile:
    def __init__(self, name, position):
        self.name = name
        self.position = position

Salah = PlayerProfile('Mo Salah', 'Right Winger')

player_position = getattr(Salah, 'position')
print(player_position)
