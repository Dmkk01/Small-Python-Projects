
import random


class PlayerCharacter:
    ABILITIES = ["Strength", "Dexterity", "Constitution", "Intelligence", "Wisdom", "Charisma"]

    SKILLS_TO_ABILITIES = {"Acrobatics": "Dexterity", "Animal Handling": "Wisdom", "Arcana": "Intelligence",
                           "Athletics": "Strength", "Deception": "Charisma", "History": "Intelligence",
                           "Insight": "Wisdom", "Intimidation": "Charisma", "Investigation": "Intelligence",
                           "Medicine": "Wisdom", "Nature": "Intelligence", "Perception": "Wisdom",
                           "Performance": "Charisma", "Persuasion": "Charisma", "Religion": "Intelligence",
                           "Sleight of Hand": "Dexterity", "Stealth": "Dexterity", "Survival": "Wisdom"}

    ABILITY_SCORES_TO_MODIFIERS = {1: -5, 2: -4, 3: -4, 4: -3, 5: -3, 6: -2, 7: -2, 8: -1, 9: -1, 10: 0,
                                   11: 0, 12: 1, 13: 1, 14: 2, 15: 2, 16: 3, 17: 3, 18: 4, 19: 4, 20: 5}

    def __init__(self, character_name, race, character_class, hit_die, armor_class):
        self.__name = character_name
        self.__race = race
        self.__class = character_class
        self.__hit_die = hit_die
        self.__armor_class = 10
        if armor_class:
            self.__armor_class = armor_class
        self.__level = 1

        a = {}
        for i in PlayerCharacter.ABILITIES:
            x = PlayerCharacter.roll_ability_score()
            a[i] = x
        self.__ability_scores = a

        self.__max_hp = self.__hit_die + PlayerCharacter.ABILITY_SCORES_TO_MODIFIERS[self.__ability_scores['Constitution']]
        self.__hp = self.__max_hp

    def get_name(self):
        return self.__name

    def get_race(self):
        return self.__race

    def get_class(self):
        return self.__class

    def get_level(self):
        return self.__level

    def is_downed(self):
        if self.__hp == 0:
            return True
        else:
            return False

    def get_ability_modifier(self, ability):
        if ability in self.__ability_scores:
            a = self.__ability_scores[ability]
            b = PlayerCharacter.ABILITY_SCORES_TO_MODIFIERS[a]
            return b
        else:
            return None

    def get_skill_level(self, skill):
        if skill in PlayerCharacter.SKILLS_TO_ABILITIES:
            c = PlayerCharacter.SKILLS_TO_ABILITIES[skill]
            if c in self.__ability_scores:
                a = self.__ability_scores[c]
                b = PlayerCharacter.ABILITY_SCORES_TO_MODIFIERS[a]
                return b
            else:
                return None
        else:
            return None

    def skill_check(self, skill, result_to_pass):
        if skill in PlayerCharacter.SKILLS_TO_ABILITIES:
            skill_level = self.get_skill_level(skill)
            number = PlayerCharacter.roll_die(20)
            result = number + skill_level
            if result >= result_to_pass:
                return True
            else:
                return False
        else:

            return None

    def level_up(self):
        self.__level = self.__level + 1
        die = PlayerCharacter.roll_die(self.__hit_die)
        self.__hp = self.__hp + die
        self.__max_hp = self.__max_hp + die
        return die

    def attack(self, other_character):
        throw_die = PlayerCharacter.roll_die(20)
        dict_class = {'Fighter': 6, 'Ranger': 8, 'Wizard': 10, 'Rogue': 4}
        if throw_die >= other_character.__armor_class:
            your_dmg = dict_class[self.__class]
            new_die = PlayerCharacter.roll_die(your_dmg)
            check_hp = other_character.__hp
            if check_hp < new_die:
                other_character.__hp = 0
                return check_hp
            else:
                other_character.__hp = other_character.__hp - new_die
                return new_die
        else:
            return 0


    def heal(self):
        heal_die = PlayerCharacter.roll_die(5)
        if self.__hp + heal_die > self.__max_hp:
            self.__hp = self.__max_hp
            return self.__max_hp - self.__hp
        else:
            self.__hp += heal_die
            return heal_die

    def __str__(self):
        string = '{}, a level {} {} {}'.format(self.__name, self.__level, self.__race, self.__class)
        string1 = 'HP: {}/{}'.format(self.__hp, self.__max_hp)
        string2 = 'STR: {}   DEX: {}   CON: {}   INT: {}   WIS: {}   CHA: {}  '.format(self.__ability_scores['Strength'], self.__ability_scores['Dexterity'], self.__ability_scores['Constitution'], self.__ability_scores['Intelligence'], self.__ability_scores['Wisdom'], self.__ability_scores['Charisma'])
        return string + string1 + string2
    @staticmethod
    def roll_die(die_sides):
        return random.randint(1, die_sides)

    @staticmethod
    def roll_ability_score():
        roll_results = [PlayerCharacter.roll_die(6) for i in range(4)]  # throwing 4 6-sided dies
        smallest = 1000  # just some very large value
        for result in roll_results:  # choosing 3 largest results
            if result < smallest:
                smallest = result
        roll_results.remove(smallest)  # removing smallest result
        roll_sum = sum(roll_results)  # adding 3 largest results
        return roll_sum
