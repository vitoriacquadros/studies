
# Costante = 'Variáveis' que não mudam de valor durante a execução do programa.
# Muitas condições no mesmo if(ruim)
# # .... <- Contagem de complexidade (ruim)
# Constantes

velocidade = 61
local_carro = 101
RADAR_1  = 60 #velocidade máxima do radar 1
LOCAL_1 = 100 #local onde o radar 1 está
RADAR_RANGE = 1 #Alcance do radar 1

vel_carro_passou_radar_1 = velocidade > RADAR_1
carro_passou_radar_1 = local_carro >= (LOCAL_1 + RADAR_RANGE) and \
    local_carro <= (LOCAL_1 + RADAR_RANGE)
carro_multado_radar_1 = carro_passou_radar_1 and vel_carro_passou_radar_1

if vel_carro_passou_radar_1:
    print('Você passou do radar 1')

if carro_passou_radar_1:
    print('Você passou pelo radar 1')
    
if carro_multado_radar_1:
    print('Você foi multado no radar 1')