# making a cool nickname revealer
from pyscript import display, document


# runs when the button is clicked
def country_nickname(event):
    # get the nickname stored in the chosen dropdown option
    nickname = document.getElementById('country_input').value

    # show it in the empty display div, replacing old answer
    display(f'Nickname: {nickname}', target='display')