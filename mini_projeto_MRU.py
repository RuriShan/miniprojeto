import PySimpleGUI as sg

sg.theme('GrayGrayGray')

def converter_tempo_horas(tempo_decimal):
    horas = int(tempo_decimal)
    minutos_decimal = (tempo_decimal - horas) * 60
    minutos = int(minutos_decimal)
    if minutos == 0:
        return f'{horas} h'
    elif horas == 0:
        return f'{minutos} m'
    else:
        return f'{horas} h e {minutos} m'

def calcular_mru(velocidade, tempo, distancia, unidade):
    try: 
        velocidade = float(velocidade) if velocidade else None
        tempo = float(tempo) if tempo else None
        distancia = float(distancia) if distancia else None

        if distancia is not None:
            if velocidade is not None and tempo is None:
                tempo = distancia / velocidade
            elif tempo is not None and velocidade is None:
                velocidade = distancia / tempo

        elif tempo is not None and velocidade is not None:
            distancia = velocidade * tempo
                
        else:
            return f'Está faltando algum valor, é necessário preencher dois valores para que o terceiro seja calculado.'
        
        if unidade == 'm/s':
            return f'Velocidade: {velocidade:.2f} {unidade}\nTempo: {tempo:.2f} s\nDistância: {distancia:.2f} m'
        elif unidade == 'km/h':
            return f'Velocidade: {velocidade:.2f} {unidade}\nTempo: {converter_tempo_horas(tempo)}\nDistância: {distancia:.2f} km'

    except ValueError:
        return 'Não foram colocados valores válidos.'
    
layout = [
    [sg.Text('Escolha qual maneira você deseja calcular:', font=('Arial', 18))],
    [sg.Text('')],
    [sg.Button('Calcular MRU em m/s', size=(20, 2)), sg.Button('Calcular MRU em km/h', size=(20, 2))],
    [sg.Text('')]
]

window = sg.Window('Calculadora MRU', layout, element_justification="center")
 
while True:
    event, values = window.read()

    if event == sg.WINDOW_CLOSED:
        break

    elif event == 'Calcular MRU em m/s':
        unidade = 'm/s'
        popup_layout = [
            [sg.Text('Para fazer o cálculo do MRU, você deverá colocar no mínimo dois valores.', font=('Arial', 12), text_color=('red'))],
            [sg.Text('Para utilizar valores decimais use "."', font=('Arial', 12), text_color=('red'))],
            [sg.Text('')],
            [sg.Text('Velocidade (m/s):', font=('Arial', 12)), sg.Input(key='velocidade', size=(26, 2))],
            [sg.Text('Tempo (s):', font=('Arial', 12)), sg.Input(key='tempo', size=(32, 2))],
            [sg.Text('Distância (m):', font=('Arial', 12)), sg.Input(key='distancia', size=(29, 2))],
            [sg.Text('')],
            [sg.Button('Calcular', size=(13, 2)), sg.Button('Cancelar', size=(13, 2))],
        ]
        popup_window = sg.Window('Calculadora MRU em m/s', popup_layout, element_justification="center")

        while True:
            popup_event, popup_values = popup_window.read()

            if popup_event == sg.WINDOW_CLOSED or popup_event == 'Cancelar':
                break
            elif popup_event == 'Calcular':
                resultado = calcular_mru(popup_values['velocidade'], popup_values['tempo'], popup_values['distancia'], unidade)
                sg.popup(resultado, title='Resultado do MRU em m/s', font=('Arial', 11))

        popup_window.close()

    elif event == 'Calcular MRU em km/h':
        unidade = 'km/h'
        popup_layout = [
            [sg.Text('Para fazer o cálculo do MRU, você deverá colocar no mínimo dois valores.', font=('Arial', 12), text_color=('red'))],
            [sg.Text('Para utilizar valores decimais use "."', font=('Arial', 12), text_color=('red'))],
            [sg.Text('')],
            [sg.Text('Velocidade (km/h):', font=('Arial', 12)), sg.Input(key='velocidade', size=(26, 2))],
            [sg.Text('Tempo (h):', font=('Arial', 12)), sg.Input(key='tempo', size=(33, 2))],
            [sg.Text('Distância (km):', font=('Arial', 12)), sg.Input(key='distancia', size=(29, 2))],
            [sg.Text('')],
            [sg.Button('Calcular', size=(13, 2)), sg.Button('Cancelar', size=(13, 2))],
        ]
        popup_window = sg.Window('Calculadora MRU em km/h', popup_layout, element_justification="center")

        while True:
            popup_event, popup_values = popup_window.read()

            if popup_event == sg.WINDOW_CLOSED or popup_event == 'Cancelar':
                break
            elif popup_event == 'Calcular':
                resultado = calcular_mru(popup_values['velocidade'], popup_values['tempo'], popup_values['distancia'], unidade)
                sg.popup(resultado, title='Resultado do MRU em km/h', font=('Arial', 11))
                
        popup_window.close()

window.close()