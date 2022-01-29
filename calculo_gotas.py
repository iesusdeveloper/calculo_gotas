# ESTE SISTEMA É UTILIZADO POR EQUIPE MÉDICA E PRINCIPALMENTE PELA A EQUIPE DE ENFERMAGEM PARA A ADMINISTRAÇÃO DE MEDICAÇÕES LÍQUIDAS POR UM DERTERMINADO TEMPO E COM UMA DETERMINADA VELOCIDADE, SENDO MEDIDO PELA QUANTIDADE DE GOTAS POR MINUTO.
tipo = str(input(
    'Digite o nome do cálculo, se é MACROGOTAS ou MICROGOTAS: ')).strip().upper()
while tipo != 'MACROGOTAS' and tipo != 'MICROGOTAS':
    tipo = str(input(
        'Digite novamente o nome CORRETO do cálculo, se é MACROGOTAS ou MICROGOTAS: ')).strip().upper()
volume = int(input('Quantos ml serão infudido? '))
tempo = float(input('Em quantas horas foi prescrito? '))
calculo_macro = volume / (tempo * 3)
calculo_micro = volume / tempo
if tipo == 'MACROGOTAS' or tipo == 'MACROGOTA':
    print('O resultado é {} macrogotas/minuto.'.format(round(calculo_macro)))
if tipo == 'MICROGOTAS' or tipo == 'MICROGOTA':
    print('O resultado é {} microgotas/minuto.'.format(round(calculo_micro)))