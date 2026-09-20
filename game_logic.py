def create_placeholder(word):
    placeholder = ""

    for letter in word:
        placeholder += "_"

    return placeholder


def update_display(word, guessed_letters):
    display = ""

    for letter in word:
        if letter in guessed_letters:
            display += letter
        else:
            display += "_"

    return display


def check_guess(word, guess):
    if guess in word:
        return True
    else:
        return False


def word_completed(display):
    if "_" not in display:
        return True
    else:
        return False