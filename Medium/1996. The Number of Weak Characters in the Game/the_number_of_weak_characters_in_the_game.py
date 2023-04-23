class Character:

    def __init__(self, attack, defense):
        self.defense = defense
        self.attack = attack

    def __lt__(self, other):
        if self.attack == other.attack:
            return self.defense < other.defense
        else:
            return self.attack > other.attack

    def __str__(self):
        return f" {self.attack}, {self.defense} "


class Solution:
    def numberOfWeakCharacters(self, properties: List[List[int]]) -> int:

        character_list = []

        for prop in properties:
            character_list.append(Character(prop[0], prop[1]))

        character_list.sort()
        maxx_defense = 0

        result = 0
        for character in character_list:

            if character.defense >= maxx_defense:
                maxx_defense = character.defense
            else:
                result += 1

        return result