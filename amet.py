import PySimpleGUI as sg

layout = [
    [sg.Input('0', size=(3, 1), font='Any 12', justification='r', key='-SPIN-', enable_events=True)],
    [sg.Button('', size=(1, 1), font='Any 7', border_width=0, button_color=(sg.theme_text_color(), sg.theme_background_color()), key='-UP-')],
    [sg.Button('', size=(1, 1), font='Any 7', border_width=0, button_color=(sg.theme_text_color(), sg.theme_background_color()), key='-DOWN-')]
]

window = sg.Window('Spinner simulation', layout, use_default_focus=False)

while True:
    event, values = window.read()
    if event == sg.WINDOW_CLOSED:
        break
    elif event == '-SPIN-':
        # Handle the Spin event here
        new_value = values['-SPIN-']
        # Do something with the new value

window.close()
