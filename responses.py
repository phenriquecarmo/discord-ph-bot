from random import choice, randint

def get_response(user_input: str) -> str:
    lowered: str = user_input.lower()

    if lowered == '':
        return 'Well, you\'re awfully silent...'
    elif 'oi' in lowered:
        return 'oi ja jogou quantas vezes hoje?'
    else: return choice([
        'tendi não..',
        'an? '
        'repete nrml'
    ])
    