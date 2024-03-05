import pyautogui
import time
import subprocess

# Caminho para o abrir o script dirf.sh
#caminho_script_dirf = "/opt/Programas RFB/Dirf2024/dirf.sh"

# Executa o script (abrir) dirf.sh
#subprocess.Popen(["bash", caminho_script_dirf])



#Apertar no programa pra começar a rodar
pyautogui.click(2888, 644)

# Inicializa o contador para o número de vezes que o scroll será clicado
scroll_clicks = 2

# Lista de códigos
codigos = [14493, 14389, 13334, 14412, 13669, 13752, 14375, 14369, 14339, 10083, 13023, 11217, 13115, 13130, 14109, 13898, 14445, 14044, 13397,
            10415, 10098, 13172, 14506, 13137, 14505, 13406, 13284, 11275, 13246, 10657, 10147, 11136, 13364, 13386, 13435, 13060, 13468, 13445,
              13391, 13188, 10725, 14111, 13006, 13221, 10035, 10451, 10252, 13191, 13225, 13388, 10677, 13390, 13213, 11188, 13186, 13166, 13340,
                10047, 13423, 13113, 13064, 13290, 11086, 13345, 13138, 13288, 13311, 13149, 13024, 12024, 10275, 10082, 13293, 13100, 10705, 13074,
                  14333, 13252, 13389, 13019, 13118, 13249, 13228, 13039, 13475, 13104, 13443, 13134, 13400, 14269, 10233, 13367, 14065, 13929, 14082,
                    13153, 13066, 13103, 13598, 13615, 10676, 14481, 13818, 10557, 14338, 10624, 14420, 14282, 13708, 10320, 14433, 13664, 14088, 14008,
                      14107, 10391, 14240, 10673, 14466, 13957, 13863, 13728, 13479, 14527, 14081, 13758, 14514, 14161, 13357, 13563, 10486, 14244, 14139,
                        13082, 11191, 13190, 11222, 13038, 13207, 13491, 13787, 13280, 11218, 13618, 13672, 14114, 13061, 13132, 13085, 13176, 13636, 14149,
                          13531, 13712, 10281, 10043, 14430, 13419, 13775, 13151, 13732, 13625, 14020, 13004, 10287, 13398, 14376, 13079, 13063, 10016, 14485,
                            13409, 11076, 10488, 13267, 10534, 14257, 14294, 14532, 13320, 13394, 13418, 13315, 14236, 13845, 13856, 13421, 14022, 14036, 13614,
                              10602, 13109, 14328, 10540, 13877, 13786, 14285, 14519, 10175, 13466, 10542, 13347, 13896, 11026, 14061, 14180, 10182, 13889, 13209,
                                14096, 13358, 14097, 10204, 14220, 14003, 11219, 13123, 14106, 13989, 14012, 13482, 14025, 13950, 13289, 13416, 13938, 13928, 14019,
                                  13757, 13212, 13927, 14334, 11301, 13197, 13951, 13944, 14086, 13450, 13501, 13488, 13277, 13027]

# Índice inicial para o código a ser escrito
indice_codigo = 0

time.sleep(5)

while True:
    # Aguarda 5 segundos antes de iniciar
    time.sleep(5)
    
    # Apertar x pra sair do programa que inicia quando a dirf abre (Só se for abrir com o subprocess.Popen)
    #pyautogui.click(3091, 338)
    #time.sleep(2)
    
    # Pressiona Ctrl+M
    pyautogui.hotkey('ctrl', 'm')
    time.sleep(2)

    # Clica no scroll várias vezes
    for _ in range(scroll_clicks):
        pyautogui.click(2888, 644)
        #time.sleep(0.1) para delay do mouse no scroll
    scroll_clicks += 1 # Incrementa o contador para a próxima execução

    # Clica em várias coordenadas específicas
    
    time.sleep(2)
    pyautogui.click(2482, 635) # Apertar no Predio
    time.sleep(2)
    pyautogui.click(2739, 681) # Apertar no OK
    time.sleep(10)
    pyautogui.click(1610, 188) # Apertar em Salvar
    time.sleep(2)
    pyautogui.doubleClick(2054, 489) # Apertar na Pasta DIRF
    time.sleep(3)
    pyautogui.click(2063, 660) # ApertarPara escrever
    time.sleep(2)

    # Escreve "d" seguido do código específico do loop
    pyautogui.write(f"d{codigos[indice_codigo]}")
    time.sleep(1) # Aguarda um segundo antes de escrever o próximo código

    # Atualiza o índice para o próximo código
    indice_codigo += 1
    if indice_codigo >= len(codigos):
        indice_codigo = 0 # Volta ao início da lista de códigos

    # Clicar em salvar
    time.sleep(2)
    pyautogui.click(2262, 722)

    # Clica para fechar (x)
    time.sleep(2)
    pyautogui.click(2649, 161)