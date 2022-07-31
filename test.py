import PySimpleGUI as sg

# ------ Menu Definition ------ # 
menu_d = [
    ['Настройки', ['База данных', ['Порт подключения',
                                    'Редактировать расстановку объектов',
                                    'Настройка чувствительности звука'],
                   ['Настройка защиты'], ], ],
    ['Помощь', 'About...']
]

# ------ GUI Defintion ------ #
layout = [
    [sg.Menu(menu_d)],
    [sg.Output(size=(50, 20))],
    [sg.Button('Выход')]
]       

# ------ Creat the Window ------ #
window = sg.Window('Telegramm bot control panel', layout, icon='icon.ico')

window_2_active = False
window_3_active = False
window_4_active = False
window_5_active = False
window_6_active = False
window_7_active = False
window_8_active = False

while True:
    
    event, values = window.read(timeout = 100)
    
    if event is None:   # Exit button or X
        break
    # f = open("log.txt", 'a')
    # f.write(event)
    # f.close()
    # print("ev: ", event, "val: ", values) # отладочная печать  

# ------ Дочерние окна конфигурации ------ #    
    # ------ Дочернее окно настройки названия кнопок ------ #
    if not window_2_active and event == 'Порт подключения':
        window_2_active = True
        
        # ------ GUI Defintion ------#
        layout_2 = [
            [sg.Text('Настройки порта подключения')],
            [sg.li],
            [sg.Button('Save'), sg.Button('Выход')],
            ]
        
        # ------ Создание дочернего окна ------#
        window_2 = sg.Window('Название кнопок', layout_2, size = (1000, 600))
    
    # ------ Управление дочерним окном ------#
    if window_2_active:
        event2, values2 = window_2.Read(timeout=100)
        
        # if event in (None, ):
        #     break
        
        # ------ Загрузка изображения ------#
        if event2 in ('Show'):
            if values2['-FILE-'] and values2['-FILE-'][-3:] in ['png', 'gif']:
                window_2.FindElement('Image').Update(filename = values2['-FILE-'])
        
        # ------ Закрытие дочернего окна ------#
        if event2 in (None, 'Выход'):
            window_2_active  = False
            window_2.close()
    
    # ------ Дочернее окно редактировать расстановку объектов------ #
    if not window_3_active and event == 'Редактировать расстановку объектов':
        window_3_active = True
        
        # ------ GUI Defintion ------#
        layout_3 = [
            [sg.Text('Вы вошли в дочернее окно')],
            [sg.Button('Save'), sg.Button('Выход')]
            ]
        
        # ------ Создание дочернего окна ------#
        window_3 = sg.Window('Редактор объектов', layout_3)
    
    # ------ Управление дочерним окном ------#
    if window_3_active:
        event3, values3 = window_3.Read(timeout=100)
        
        # ------ Закрытие дочернего окна ------#
        if event3 in (None, 'Выход'):
            window_3_active  = False
            window_3.close()
    
    # ------ Дочернее окно ------ #
    if not window_4_active and event == 'Настройка чувствительности звука':
        window_4_active = True
        
        # ------ GUI Defintion ------#
        layout_4 = [
            [sg.Text('Вы вошли в дочернее окно')],
            [sg.Button('Save'), sg.Button('Выход')]
            ]
        
        # ------ Создание дочернего окна ------#
        window_4 = sg.Window('Настройка чувствительности', layout_4)
    
    # ------ Управление дочерним окном ------#
    if window_4_active:
        event4, values4 = window_4.Read(timeout=100)
        
        # ------ Закрытие дочернего окна ------#
        if event4 in (None, 'Выход'):
            window_4_active  = False
            window_4.close()
    
    # ------ Дочернее окно ------ #
    if not window_5_active and event == 'Загрузка аудиофайлов':
        window_5_active = True
        
        # ------ GUI Defintion ------#
        layout_5 = [
            [sg.Text('Вы вошли в дочернее окно')],
            [sg.Button('Save'), sg.Button('Выход')]
            ]
        
        # ------ Создание дочернего окна ------#
        window_5 = sg.Window('Загрузчик', layout_5)
    
    # ------ Управление дочерним окном ------#
    if window_5_active:
        event5, values5 = window_5.Read(timeout=100)
        
        # ------ Закрытие дочернего окна ------#
        if event5 in (None, 'Выход'):
            window_5_active  = False
            window_5.close()
    
    # ------ Дочернее окно ------ #
    if not window_6_active and event == 'Воспроизведение аудиофайлов':
        window_6_active = True
        
        # ------ GUI Defintion ------#
        layout_6 = [
            [sg.Text('Вы вошли в дочернее окно')],
            [sg.Button('Save'), sg.Button('Выход')]
            ]
        
        # ------ Создание дочернего окна ------#
        window_6 = sg.Window('Media Player', layout_6)
    
    # ------ Управление дочерним окном ------#
    if window_6_active:
        event6, values6 = window_6.Read(timeout=100)
        
        # ------ Закрытие дочернего окна ------#
        if event6 in (None, 'Выход'):
            window_6_active  = False
            window_6.close()
    
    # ------ Дочернее окно ------ #
    if not window_7_active and event == 'Настройка защиты':
        window_7_active = True
        
        # ------ GUI Defintion ------#
        layout_7 = [
            [sg.Text('Вы вошли в дочернее окно')],
            [sg.Button('Save'), sg.Button('Выход')]
            ]
        
        # ------ Создание дочернего окна ------#
        window_7 = sg.Window('Защита управления', layout_7)
    
    # ------ Управление дочерним окном ------#
    if window_7_active:
        event7, values7 = window_7.Read(timeout=100)
        
        # ------ Закрытие дочернего окна ------#
        if event7 in (None, 'Выход'):
            window_7_active  = False
            window_7.close()
    
    # ------ Дочернее окно ------ #
    if not window_8_active and event == 'About...':
        window_8_active = True
        
        # ------ GUI Defintion ------#
        layout_8 = [
            [sg.Text('Вы вошли в дочернее окно')],
            [sg.Button('Save'), sg.Button('Выход')]
            ]
        
        # ------ Создание дочернего окна ------#
        window_8 = sg.Window('About', layout_8)
    
    # ------ Управление дочерним окном ------#
    if window_8_active:
        event8, values8 = window_8.Read(timeout=100)
        
        # ------ Закрытие дочернего окна ------#
        if event8 in (None, 'Выход'):
            window_8_active  = False
            window_8.close()
    
    # ------ Закрытие программмы ------ #
    if event in (None, 'Выход'):   # if user closes window or clicks cancel
        break

window.close()