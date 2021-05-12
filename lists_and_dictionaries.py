def list_clear(x, y, z):
    for list_1 in [x, y, z]:
        list.clear()


scale = 1
font_scale = 1

transparent = '#787878'

label_config = {
    'bg': '#787878',
    'font': 'helvetica 25 bold',
    'fg': 'white'

}

label_config_2 = {
    'bg': '#787878',
    'font': 'helvetica 13 bold',
    'fg': 'white'

}

button_config = {
    'bg': 'green',
    'fg': 'white',
    'relief': 'flat',
    'font': ('helvetica', 12 * scale, 'bold'),
    'activebackground': '#004d05',
    'activeforeground': 'white'
}

settings_label = {'bg': transparent,
                  'fg': 'white',
                  'font': 'Helvetica 25 underline'}

already_answered_root = []

already_answered_opt = []

already_answered_two = []

seconds_left = 30

minutes_left = 5
