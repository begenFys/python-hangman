from game import Game
from game_status import GameStatus


def chars_list_to_str(chars):
    return ''.join(chars)

game = Game()
word = game.generate_word

letters_count = len(word)

print(f'The word consists of {letters_count} letters.')
print('Try to guess the word letter by letter')

while game.game_status == GameStatus.IN_PROGRESS:
    letter = input("Pick = letter.\n")
    state = game.guess_letter(letter)

    print(chars_list_to_str(state))
    print(f'Remaining tries = {game.remaining_tries}')
    print(f'Tried letter: {chars_list_to_str(game.tries_letters)}')

if game.game_status == GameStatus.LOST:
    print('You\'re hanger!')
    print(f'The word was: {game.word}')
else:
    print('Congratulations! You won!')

