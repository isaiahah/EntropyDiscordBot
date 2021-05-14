from random import randint
import re
import json

with open('spells.json') as j:
    spells = json.load(j)
with open('weapons.json') as j:
    weapons = json.load(j)


def command_handler(message: str) -> str:
    """
    Determine which command should be run from the input message. Then,
    run that command with the message as input.

    Command Priority Order:
    - Roll
    - Weapons
    - Spells
    """
    match_roll = re.compile('roll \d*d\d+( [+-]\d+)?\Z')
    match_modifier = re.compile('[+-]\d+\Z')
    if match_roll.match(message) is not None:
        return dice_handler(message)
    if (message.split()[0] in weapons and
            ((len(message.split()) == 1) or (len(message.split()) == 2 and
             match_modifier.match(message.split()[1]) is not None))):
        return weapon_handler(message)
    if (message.split()[0] in spells and
            ((len(message.split()) == 1) or (len(message.split()) == 2 and
             match_modifier.match(message.split()[1]) is not None))):
        return spell_handler(message)


def dice_handler(message: str) -> str:
    """
    Roll dice, as specified by the input message. If number of dice or modifier
        is not specified, they are assumed to be 1 and 0 respectively.

    Precondition: The input message is of the form 'roll adn +b'.
    """
    match_digits = re.compile('\d+')
    message = message[5:]
    dice_count_match = match_digits.match(message)
    if dice_count_match is not None:
        dice_count = int(dice_count_match.group())
        message = message[dice_count_match.end() + 1:]
    else:
        dice_count = 1
        message = message[1:]
    dice_sides_match = match_digits.match(message)
    dice_sides = int(dice_sides_match.group())
    message = message[dice_sides_match.end() + 1:]
    dice_modifier = 0
    if message != '':
        dice_modifier = int(message)
    dice_rolls, total = roll_dice(dice_count, dice_sides, dice_modifier)
    if dice_modifier == 0:
        dice_modifier = ''
    else:
        if dice_modifier > 0:
            dice_modifier = ' +' + str(dice_modifier)
        else:
            dice_modifier = ' ' + str(dice_modifier)
    response = 'Rolling ' + str(dice_count) + 'd' + str(dice_sides) + \
               dice_modifier + '\nResults: ' + \
               str(dice_rolls).strip('[]') + '\nTotal: ' + str(total)
    return response


def weapon_handler(message: str) -> str:
    """
    Give the result of attacking with the weapon given in the message, using
        the information given in the weapon JSON file.
    Precondition: Message is a weapon in the JSON file with an optional
        modifier.
    """
    message = message.split()
    weapon = message[0]
    if len(message) == 2:
        modifier = int(message[1])
    else:
        modifier = 0
    dice_count = weapons[weapon]['dice_count']
    dice_sides = weapons[weapon]['dice_sides']
    dice_modifier = weapons[weapon]['modifier'] + modifier
    dice_rolls, total = roll_dice(dice_count, dice_sides, dice_modifier)
    if dice_modifier == 0:
        dice_modifier = ''
    else:
        if dice_modifier > 0:
            dice_modifier = ' +' + str(dice_modifier)
        else:
            dice_modifier = ' ' + str(dice_modifier)
    response = weapons[weapon]['name'] + ': ' + str(dice_count) + 'd' + \
               str(dice_sides) + dice_modifier + '\nResults: ' + \
               str(dice_rolls).strip('[]') + '\nTotal: ' + str(total)
    return response


def spell_handler(message: str) -> str:
    """Give the result of attacking with the spell given in the message, using
        the information given in the spell JSON file.
    Precondition: Message is a spell in the JSON file with an optional modifier.
    """
    message = message.split()
    spell = message[0]
    if len(message) == 2:
        modifier = int(message[1])
    else:
        modifier = 0
    dice_count = spells[spell]['dice_count']
    dice_sides = spells[spell]['dice_sides']
    dice_modifier = spells[spell]['modifier'] + modifier
    dice_rolls, total = roll_dice(dice_count, dice_sides, dice_modifier)
    if dice_modifier == 0:
        dice_modifier = ''
    else:
        if dice_modifier > 0:
            dice_modifier = ' +' + str(dice_modifier)
        else:
            dice_modifier = ' ' + str(dice_modifier)
    response = spells[spell]['name'] + ': ' + str(dice_count) + 'd' + \
               str(dice_sides) + dice_modifier + '\nResults: ' + \
               str(dice_rolls).strip('[]') + '\nTotal: ' + str(total)
    return response


def roll_dice(dice_count: int = 1, dice_sides: int = 20,
              dice_modifier: int = 0) -> (list, str):
    """
    Roll <dice_count> dice, where each die has <dice_sides> sides labelled
        from 1 to <dice_sides>. Return a tuple containing the dice rolls as a
        list and the sum of dice rolls and the dice modifier."""
    dice_rolls = [-1] * dice_count
    for i in range(len(dice_rolls)):
        dice_rolls[i] = randint(1, dice_sides)
    total = sum(dice_rolls) + dice_modifier
    return (dice_rolls, total)
