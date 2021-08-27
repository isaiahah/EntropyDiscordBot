from typing import Optional
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
    - Help
    - Roll
    - Weapons
    - Spells
    """
    if message.startswith('help'):
        return help_handler(message)

    match_roll = re.compile('roll \d*d\d+( [+-]\d+)?\Z')
    if match_roll.match(message) is not None:
        return dice_handler(message)

    match_modifier = re.compile('[+-]\d+\Z')
    if (message.split()[0] in weapons and
            ((len(message.split()) == 1) or (len(message.split()) == 2 and
             match_modifier.match(message.split()[1]) is not None))):
        return weapon_handler(message)
    if (message.split()[0] in spells and
            ((len(message.split()) == 1) or (len(message.split()) == 2 and
             match_modifier.match(message.split()[1]) is not None))):
        return spell_handler(message)
    else:
        return misc_handler(message)


def help_handler(message: str) -> str:
    """
    Return the help page specified. Help Pages:
    - General and Dice (accessed with no modifier or invalid modifier)
    - Weapons (accessed with 'weapons' or 'w' modifier)
    - Spells (accessed with 'spells' or 's' modifier)

    Precondition: message is of the form 'help modifier' where modifier may be
        none.
    """
    if len(message.split()) == 1:
        modifier = ''
    else:
        modifier = message.split()[1]
    if modifier == 'weapons' or modifier == 'w':
        output = 'Weapons:\n'
        for weapon in weapons:
            output += '{0}: {1}d{2}\n'.format(weapons[weapon]['name'],
                                              weapons[weapon]['dice_count'],
                                              weapons[weapon]['dice_sides'])
        return output
    if modifier == 'spells' or modifier == 's':
        output = 'Spells:\n'
        for spell in spells:
            output += '{0}: {1}d{2}'.format(spells[spell]['name'],
                                            spells[spell]['dice_count'],
                                            spells[spell]['dice_sides'])
            if spells[spell]['modifier'] != 0:
                output += ' +{0}'.format(spells[spell]['modifier'])
            output += '\n'
        return output
    else:
        output = 'To roll X D-sided dice with a modifier M, enter ' \
                 '`!roll xdD +M`.\n For commands on weapons or spells, type ' \
                 '`help weapons` or `help spells`.'
        return output


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
    """
    Give the result of attacking with the spell given in the message, using
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


def misc_handler(message: str) -> Optional[str]:
    """
    Handle miscellaneous commands (currently only memes).
    This could load from JSON like weapons or spells, but doesn't as I don't
        expect many new miscellaneous commands.
    """
    if message == 'kinsey':
        dice_rolls, total = roll_dice(dice_count=1, dice_sides=7,
                                      dice_modifier=-1)
        return str(total)


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
