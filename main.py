import random
from enum import Enum
from typing import Dict


class _Winner(Enum):
    USER = 'User'
    COMPUTER = 'Computer'
    DRAW = 'Draw'


class _GameOption(Enum):
    ROCK = 'Rock'
    PAPER = 'Paper'
    SCISSOR = 'Scissor'


def _create_game_options_dict() -> Dict[int, _GameOption]:
    game_options = {}
    i = 1

    for option in _GameOption:
        game_options[i] = option
        i += 1

    return game_options


def _print_game_options(game_options: Dict[int, _GameOption]):
    for index, option in game_options.items():
        print(index, option.value)


def _get_users_choice(game_options: Dict[int, _GameOption]) -> _GameOption:
    while True:
        try:
            users_choice = int(input('Please enter your choice: '))

            if users_choice < 1 or users_choice > len(game_options):
                print('Invalid choice')
                continue

            break

        except ValueError:
            print('You must enter a number!')

    return game_options[users_choice]


def _get_computers_choice(game_options: Dict[int, _GameOption]) -> _GameOption:
    computers_choice = random.choice(list(game_options.values()))

    return computers_choice


def _select_winner(users_choice: _GameOption, computers_choice: _GameOption) -> _Winner:
    did_user_win = (users_choice == _GameOption.ROCK and computers_choice == _GameOption.SCISSOR) or \
                   (users_choice == _GameOption.SCISSOR and computers_choice == _GameOption.PAPER) or \
                   (users_choice == _GameOption.PAPER and computers_choice == _GameOption.ROCK)

    is_a_draw = users_choice == computers_choice

    if did_user_win:
        winner = _Winner.USER
    elif is_a_draw:
        winner = _Winner.DRAW
    else:
        winner = _Winner.COMPUTER

    return winner


def _print_winner(users_choice: _GameOption, computers_choice: _GameOption, winner: _Winner):
    print()
    print('You used', users_choice.value)
    print('The computer used', computers_choice.value, '\n')

    print('So the winner is', winner.value)
    print('Thanks for playing!')


def __main__():
    # Initialize game
    game_options = _create_game_options_dict()

    # Start game
    _print_game_options(game_options)

    # Get player's choices
    users_choice = _get_users_choice(game_options)
    computers_choice = _get_computers_choice(game_options)

    # Announce the winner
    winner = _select_winner(users_choice, computers_choice)
    _print_winner(users_choice, computers_choice, winner)


__main__()
