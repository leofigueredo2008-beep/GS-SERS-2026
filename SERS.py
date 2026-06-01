# ==============================================================
# MISSION CONTROL AI - Sistema de Monitoramento de Missao Espacial
# Com modulo de Energias Renovaveis e Sustentabilidade
# Missao: Alpha Century | Equipe: FIAP COSMICA
# ==============================================================

# --------------------------------------------------------------
# DADOS SIMULADOS DA MISSAO
# Cada ciclo: [temperatura(°C), comunicacao(%), bateria(%), oxigenio(%), estabilidade(%)]
# Valores realistas para modulo espacial
# --------------------------------------------------------------
dados_missao = [
    [27, 31, 35, 34, 39],
    [32, 48, 56, 89, 72],
    [38, 94, 30, 48, 75],
    [41, 96, 81, 99, 56],
    [19, 98, 76, 52, 15],
    [36, 98, 89, 45, 34]
]

# --------------------------------------------------------------
# DADOS ENERGETICOS SIMULADOS POR CICLO
# Cada ciclo: [potencia_consumida_kw, geracao_solar_kw, irradiancia_solar_w_m2]
#   potencia_consumida_kw : total de potencia consumida pelo modulo no ciclo
#   geracao_solar_kw      : energia gerada pelos paineis solares no ciclo
#   irradiancia_solar_w_m2: intensidade da radiacao solar recebida (W/m²)
# Referencia: paineis solares espaciais operam com irradiancia ~1361 W/m² (constante solar)
# --------------------------------------------------------------
dados_energeticos = [
    [4.2, 3.1, 1180],
    [3.8, 3.5, 1240],
    [5.1, 2.9, 1100],
    [4.6, 3.8, 1300],
    [6.3, 2.4,  980],
    [5.0, 3.2, 1150]
]

DURACAO_CICLO_HORAS = 2.0

AREA_PAINEL_SOLAR_M2 = 8.0

EFICIENCIA_REFERENCIA = 30.0

pts_ciclos = [[], [], [], [], [], []]

areas_monitoradas = [
    "Temperatura", "Comunicacao", "Bateria", "Oxigenio", "Estabilidade"
]

pts_areas_monitoradas = [
    "Temperatura interna",
    "Comunicacao com a base",
    "Sistema de energia",
    "Suporte de oxigenio",
    "Estabilidade operacional"
]

temperaturas      = []
comunicacao_lista = []
bateria_lista     = []
oxigenio_lista    = []
estabilidade_lista = []

pts_total_ciclo    = []
pts_total_atributos = []

energia_consumida_total = 0.0
energia_gerada_total    = 0.0

num_ciclo    = 0
ciclo_aux    = 0
ciclo_critico = 0

# ==============================================================
print("==============================================================")
print("         MISSION CONTROL AI — FIAP COSMICA                   ")
print("         Solucoes em Energias Renovaveis e Sustentabilidade   ")
print("==============================================================")
print(f"Missao  : Alpha Century")
print(f"Equipe  : FIAP COSMICA")
print(f"Ciclos  : {len(dados_missao)}")
print("==============================================================\n")

def verificar_temperatura(temperatura, indice_ciclo):
    if temperatura <= 18:
        pts_ciclos[indice_ciclo].append(1)
        return "ATENCAO | Temperatura muito baixa, risco de congelamento"
    elif temperatura > 18 and temperatura <= 30:
        pts_ciclos[indice_ciclo].append(0)
        return "NORMAL | Temperatura estavel"
    elif temperatura > 30 and temperatura <= 35:
        pts_ciclos[indice_ciclo].append(1)
        return "ATENCAO | Temperatura elevada"
    else:
        pts_ciclos[indice_ciclo].append(2)
        return "CRITICO | Temperatura muito alta, risco de superaquecimento"

def verificar_comunicacao(comunicacao, indice_ciclo):
    if comunicacao < 30:
        pts_ciclos[indice_ciclo].append(2)
        return "CRITICO | Comunicacao com a base em nivel critico"
    elif comunicacao >= 30 and comunicacao < 60:
        pts_ciclos[indice_ciclo].append(1)
        return "ATENCAO | Comunicacao instavel"
    else:
        pts_ciclos[indice_ciclo].append(0)
        return "NORMAL | Comunicacao estavel"

def verificar_bateria(bateria, indice_ciclo):
    if bateria < 20:
        pts_ciclos[indice_ciclo].append(2)
        return "CRITICO | Bateria em nivel critico"
    elif bateria >= 20 and bateria < 50:
        pts_ciclos[indice_ciclo].append(1)
        return "ATENCAO | Bateria abaixo do recomendado"
    else:
        pts_ciclos[indice_ciclo].append(0)
        return "NORMAL | Bateria estavel"

def verificar_oxigenio(oxigenio, indice_ciclo):
    if oxigenio < 80:
        pts_ciclos[indice_ciclo].append(2)
        return "CRITICO | Oxigenio em nivel critico"
    elif oxigenio >= 80 and oxigenio < 90:
        pts_ciclos[indice_ciclo].append(1)
        return "ATENCAO | Nivel de oxigenio abaixo do ideal"
    else:
        pts_ciclos[indice_ciclo].append(0)
        return "NORMAL | Oxigenio estavel"

def verificar_estabilidade(estabilidade, indice_ciclo):
    if estabilidade < 40:
        pts_ciclos[indice_ciclo].append(2)
        return "CRITICO | Estabilidade operacional critica"
    elif estabilidade >= 40 and estabilidade < 70:
        pts_ciclos[indice_ciclo].append(1)
        return "ATENCAO | Estabilidade operacional reduzida"
    else:
        pts_ciclos[indice_ciclo].append(0)
        return "NORMAL | Estabilidade operacional adequada"

def classificar_ciclo(soma):
    if soma <= 2:
        return "MISSAO ESTAVEL"
    elif soma > 2 and soma <= 5:
        return "MISSAO EM ATENCAO"
    else:
        return "MISSAO CRITICA"

def gerar_recomendacoes(indice_ciclo):
    recomendacoes = {
        0: "Verificar controle termico",
        1: "Verificar sistemas de comunicacao",
        2: "Recarregar ou substituir bateria",
        3: "Verificar suprimento de oxigenio",
        4: "Verificar estabilidade operacional"
    }
    resultado = ""
    for area in range(len(areas_monitoradas)):
        if pts_ciclos[indice_ciclo][area] == 2:
            resultado += f"  [!] {recomendacoes[area]}\n"
        elif pts_ciclos[indice_ciclo][area] == 1:
            resultado += f"  [~] Monitorar {areas_monitoradas[area]} de perto\n"
    if resultado == "":
        return "  [OK] Nenhuma acao necessaria\n"
    return resultado

def risco_ciclo(indice_ciclo):
    soma = sum(pts_ciclos[indice_ciclo])
    pts_total_ciclo.append(soma)
    return soma

def analisar_tendencia():
    if pts_total_ciclo[0] > pts_total_ciclo[-1]:
        return "A missao tem tendencia a melhorar"
    elif pts_total_ciclo[0] < pts_total_ciclo[-1]:
        return "A missao tem tendencia a piorar"
    else:
        return "A missao permaneceu estavel em relacao ao inicio"

def classificacao_final(soma_final):
    if soma_final >= 36:
        return "MISSAO CRITICA"
    elif soma_final < 36 and soma_final >= 18:
        return "MISSAO EM ATENCAO"
    else:
        return "MISSAO ESTAVEL"

def calcular_consumo_energetico(potencia_kw, horas):

    return potencia_kw * horas

def calcular_geracao_solar(geracao_kw, horas):

    return geracao_kw * horas

def calcular_eficiencia_solar(irradiancia_w_m2, geracao_kw, area_m2):

    potencia_incidente = irradiancia_w_m2 * area_m2
    potencia_gerada_w  = geracao_kw * 1000
    if potencia_incidente == 0:
        return 0.0
    eficiencia = (potencia_gerada_w / potencia_incidente) * 100
    return round(eficiencia, 2)

def gerar_alerta_energetico(consumo_kwh, geracao_kwh, eficiencia, eficiencia_ref):

    alertas = []
    balanco = geracao_kwh - consumo_kwh

    if balanco >= 0:
        alertas.append(f"  [OK] Balanco energetico positivo: +{round(balanco,2)} kWh (geracao supera consumo)")
    elif balanco >= -2.0:
        alertas.append(f"  [~] Balanco energetico negativo: {round(balanco,2)} kWh (consumo supera geracao)")
    else:
        alertas.append(f"  [!] DEFICIT ENERGETICO CRITICO: {round(balanco,2)} kWh — ativar modo economia de energia")

    degradacao = eficiencia_ref - eficiencia
    if degradacao <= 2.0:
        alertas.append(f"  [OK] Paineis solares eficientes: {eficiencia}% (referencia: {eficiencia_ref}%)")
    elif degradacao <= 5.0:
        alertas.append(f"  [~] Leve degradacao dos paineis solares: {eficiencia}% (referencia: {eficiencia_ref}%)")
    else:
        alertas.append(f"  [!] DEGRADACAO CRITICA dos paineis solares: {eficiencia}% (referencia: {eficiencia_ref}%)")

    return "\n".join(alertas)

def calcular_sustentabilidade(energia_gerada_total, energia_consumida_total):

    if energia_consumida_total == 0:
        return 0.0
    ise = (energia_gerada_total / energia_consumida_total) * 100
    return round(ise, 2)

def classificar_sustentabilidade(ise):
    if ise >= 80:
        return "SUSTENTAVEL — missao energeticamente autonoma com energia solar"
    elif ise >= 50:
        return "PARCIALMENTE SUSTENTAVEL — dependencia moderada das reservas de bateria"
    else:
        return "NAO SUSTENTAVEL — alto consumo das reservas, necessario plano de economia"


# ==============================================================
# LOOP PRINCIPAL — ANALISE POR CICLO
# ==============================================================

for ciclo in dados_missao:
    ciclo_aux += 1
    dados_e = dados_energeticos[ciclo_aux - 1]

    print(f"--------------------------------------------------------------")
    print(f" CICLO {ciclo_aux}")
    print(f"--------------------------------------------------------------")

    num_ciclo = 0
    for info in ciclo:
        if num_ciclo == 4:
            print(f"  {areas_monitoradas[num_ciclo]}: {ciclo[num_ciclo]}% | {verificar_estabilidade(ciclo[num_ciclo], ciclo_aux - 1)}")
            estabilidade_lista.append(ciclo[num_ciclo])
        elif num_ciclo == 3:
            print(f"  {areas_monitoradas[num_ciclo]}: {ciclo[num_ciclo]}% | {verificar_oxigenio(ciclo[num_ciclo], ciclo_aux - 1)}")
            oxigenio_lista.append(ciclo[num_ciclo])
        elif num_ciclo == 2:
            print(f"  {areas_monitoradas[num_ciclo]}: {ciclo[num_ciclo]}% | {verificar_bateria(ciclo[num_ciclo], ciclo_aux - 1)}")
            bateria_lista.append(ciclo[num_ciclo])
        elif num_ciclo == 1:
            print(f"  {areas_monitoradas[num_ciclo]}: {ciclo[num_ciclo]}% | {verificar_comunicacao(ciclo[num_ciclo], ciclo_aux - 1)}")
            comunicacao_lista.append(ciclo[num_ciclo])
        else:
            print(f"  {areas_monitoradas[num_ciclo]}: {ciclo[num_ciclo]} graus C | {verificar_temperatura(ciclo[num_ciclo], ciclo_aux - 1)}")
            temperaturas.append(ciclo[num_ciclo])
        num_ciclo += 1

    potencia_cons = dados_e[0]
    potencia_ger  = dados_e[1]
    irradiancia   = dados_e[2]

    consumo_ciclo = calcular_consumo_energetico(potencia_cons, DURACAO_CICLO_HORAS)
    geracao_ciclo = calcular_geracao_solar(potencia_ger, DURACAO_CICLO_HORAS)
    eficiencia    = calcular_eficiencia_solar(irradiancia, potencia_ger, AREA_PAINEL_SOLAR_M2)

    energia_consumida_total += consumo_ciclo
    energia_gerada_total    += geracao_ciclo

    print(f"\n  [ENERGIA RENOVAVEL]")
    print(f"  Potencia consumida   : {potencia_cons} kW  |  Energia no ciclo: {round(consumo_ciclo,2)} kWh")
    print(f"  Geracao solar (FV)   : {potencia_ger} kW  |  Energia gerada  : {round(geracao_ciclo,2)} kWh")
    print(f"  Irradiancia solar    : {irradiancia} W/m²  |  Eficiencia painel: {eficiencia}%")
    print(f"\n  [ALERTAS ENERGETICOS]")
    print(gerar_alerta_energetico(consumo_ciclo, geracao_ciclo, eficiencia, EFICIENCIA_REFERENCIA))

    # --- Risco e classificacao do ciclo ---
    print(f"\n  Pontuacao de risco do ciclo: {risco_ciclo(ciclo_aux - 1)}")
    print(f"  {classificar_ciclo(sum(pts_ciclos[ciclo_aux - 1]))}")
    print(f"\n  [RECOMENDACOES OPERACIONAIS]")
    print(gerar_recomendacoes(ciclo_aux - 1))

pts_atributos = list(map(list, zip(*pts_ciclos)))

for qnt_cri in pts_total_ciclo:
    if qnt_cri > 5:
        ciclo_critico += 1

media_temp = sum(temperaturas)      / len(temperaturas)
media_comu = sum(comunicacao_lista) / len(comunicacao_lista)
media_bate = sum(bateria_lista)     / len(bateria_lista)
media_oxi  = sum(oxigenio_lista)    / len(oxigenio_lista)
media_esta = sum(estabilidade_lista)/ len(estabilidade_lista)

ise = calcular_sustentabilidade(energia_gerada_total, energia_consumida_total)
status_sustentabilidade = classificar_sustentabilidade(ise)

soma_total   = sum(pts_total_ciclo)
classificacao = classificacao_final(soma_total)

print("\n==============================================================")
print("         RELATORIO FINAL DA MISSAO                           ")
print("==============================================================\n")

print(f"Missao  : Alpha Century")
print(f"Equipe  : FIAP COSMICA")
print(f"Ciclos analisados: {len(dados_missao)}\n")

print("--- MEDIAS OPERACIONAIS ---")
print(f"  Temperatura media  : {round(media_temp,2)} graus C")
print(f"  Comunicacao media  : {round(media_comu,2)} %")
print(f"  Bateria media      : {round(media_bate,2)} %")
print(f"  Oxigenio medio     : {round(media_oxi,2)} %")
print(f"  Estabilidade media : {round(media_esta,2)} %\n")

print("--- RESUMO DE RISCO ---")
print(f"  Ciclo mais critico        : {pts_total_ciclo.index(max(pts_total_ciclo)) + 1}")
print(f"  Maior pontuacao de risco  : {max(pts_total_ciclo)}")
print(f"  Risco medio da missao     : {round(soma_total / len(pts_total_ciclo), 2)}")
print(f"  Quantidade de ciclos criticos: {ciclo_critico}\n")

print("--- TENDENCIA ---")
print(f"  {analisar_tendencia()}\n")

print("--- PONTUACAO ACUMULADA POR AREA ---")
ciclo_aux = 0
for ciclo in range(len(pts_areas_monitoradas)):
    print(f"  {pts_areas_monitoradas[ciclo_aux]}: {sum(pts_atributos[ciclo_aux])} pts")
    pts_total_atributos.append(sum(pts_atributos[ciclo_aux]))
    ciclo_aux += 1

print(f"\n  Area mais afetada: {pts_areas_monitoradas[pts_total_atributos.index(max(pts_total_atributos))]}\n")

print("--- BALANCO ENERGETICO DA MISSAO (ENERGIA RENOVAVEL) ---")
print(f"  Energia total consumida      : {round(energia_consumida_total,2)} kWh")
print(f"  Energia solar total gerada   : {round(energia_gerada_total,2)} kWh")
print(f"  Balanco energetico total     : {round(energia_gerada_total - energia_consumida_total,2)} kWh")
print(f"  Indice de Sustentabilidade   : {ise}%")
print(f"  Status : {status_sustentabilidade}\n")

print("--- CLASSIFICACAO FINAL ---")
print(f"  {classificacao}\n")

print("Conclusao:")
if classificacao == "MISSAO CRITICA":
    print("  A missao apresentou situacao critica durante a operacao. Multiplos sistemas")
    print("  estiveram em risco simultaneamente. E necessario acionar todos os protocolos")
    print("  de emergencia e priorizar o suporte a vida, energia e comunicacao.")
elif classificacao == "MISSAO EM ATENCAO":
    print("  A missao apresentou instabilidade relevante durante a operacao. Apesar de")
    print("  nao atingir estado critico, existem sistemas que requerem atencao continua.")
    print("  A equipe deve manter o plano de contingencia ativo e monitorar as areas afetadas.")
else:
    print("  A missao transcorreu de forma estavel. Todos os sistemas operaram dentro")
    print("  dos limites esperados. Recomenda-se manter o monitoramento continuo para")
    print("  garantir a estabilidade nas proximas fases da missao.")

print("\n==============================================================\n")