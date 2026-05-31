# Mission Control AI
### Sistema Inteligente de Monitoramento de Missão Espacial
### com Módulo de Energias Renováveis e Sustentabilidade

**Missão:** Alpha Century  
**Equipe:** FIAP COSMICA  
**Disciplina:** GS2026.1 — Pensamento Computacional e Automação com Python  
**Tema Global Solution:** Soluções em Energias Renováveis e Sustentáveis (SERS)

---

## Descrição do Projeto

O **Mission Control AI** é um sistema desenvolvido em Python que simula o monitoramento inteligente de uma missão espacial experimental. O sistema analisa dados operacionais e energéticos de 6 ciclos de monitoramento, com foco especial na **eficiência dos painéis solares fotovoltaicos** como fonte de energia renovável da missão.

A solução aplica conceitos de **energia, potência, energias renováveis e sustentabilidade** na análise dos sistemas do módulo espacial, gerando alertas automáticos, calculando o Índice de Sustentabilidade Energética (ISE) e apresentando um relatório final completo.

---

## Conexão com o Tema SERS

O espaço é um ambiente onde **energia solar é a única fonte renovável viável**. Este projeto modela essa realidade:

- **Painéis solares fotovoltaicos (FV)** são a fonte primária de energia da missão
- O sistema monitora a **irradiância solar** (W/m²), a **geração de energia** (kWh) e a **eficiência real** dos painéis a cada ciclo
- O **balanço energético** (geração vs. consumo) determina se a missão está operando de forma sustentável ou consumindo suas reservas
- O **Índice de Sustentabilidade Energética (ISE)** mede a autonomia energética renovável da missão ao longo de todos os ciclos

---

## Estrutura do Repositório

```
GS-SERS-2026/
│
├── README.md
└── SERS.py
```

---

## Como Executar

Nenhuma biblioteca externa é necessária. Basta ter o Python 3 instalado.

```bash
python3 SERS.py
```

---

## Estrutura dos Dados

### Dados Operacionais — `dados_missao`

Cada linha representa um ciclo. Ordem obrigatória das colunas:

```
[temperatura(°C), comunicacao(%), bateria(%), oxigenio(%), estabilidade(%)]
```

| Posição | Informação   | Unidade |
|---------|--------------|---------|
| 0       | Temperatura  | °C      |
| 1       | Comunicação  | %       |
| 2       | Bateria      | %       |
| 3       | Oxigênio     | %       |
| 4       | Estabilidade | %       |

### Dados Energéticos — `dados_energeticos`

Adicionados para atender ao tema SERS. Cada linha corresponde ao mesmo ciclo de `dados_missao`:

```
[potencia_consumida_kw, geracao_solar_kw, irradiancia_solar_w_m2]
```

| Posição | Informação             | Unidade | Descrição                                          |
|---------|------------------------|---------|----------------------------------------------------|
| 0       | Potência consumida     | kW      | Potência total consumida pelo módulo no ciclo      |
| 1       | Geração solar          | kW      | Potência gerada pelos painéis solares FV           |
| 2       | Irradiância solar      | W/m²    | Intensidade da radiação solar recebida pelos painéis |

> **Referência:** A constante solar média é ~1361 W/m². Os valores simulados variam entre 980–1300 W/m², representando variações de orientação e distância orbital.

**Parâmetros fixos do módulo:**
- Duração de cada ciclo: **2 horas**
- Área dos painéis solares: **8 m²**
- Eficiência de referência dos painéis: **30%**

---

## Regras de Alerta Operacional

### Temperatura (°C)
| Condição              | Classificação |
|-----------------------|---------------|
| ≤ 18°C                | ATENCAO       |
| > 18°C e ≤ 30°C       | NORMAL        |
| > 30°C e ≤ 35°C       | ATENCAO       |
| > 35°C                | CRITICO       |

### Comunicação (%)
| Condição       | Classificação |
|----------------|---------------|
| < 30%          | CRITICO       |
| ≥ 30% e < 60%  | ATENCAO       |
| ≥ 60%          | NORMAL        |

### Bateria (%)
| Condição       | Classificação |
|----------------|---------------|
| < 20%          | CRITICO       |
| ≥ 20% e < 50%  | ATENCAO       |
| ≥ 50%          | NORMAL        |

### Oxigênio (%)
| Condição       | Classificação |
|----------------|---------------|
| < 80%          | CRITICO       |
| ≥ 80% e < 90%  | ATENCAO       |
| ≥ 90%          | NORMAL        |

### Estabilidade (%)
| Condição       | Classificação |
|----------------|---------------|
| < 40%          | CRITICO       |
| ≥ 40% e < 70%  | ATENCAO       |
| ≥ 70%          | NORMAL        |

---

## Regras de Alerta Energético (SERS)

### Balanço Energético por Ciclo
`Balanço (kWh) = Energia gerada — Energia consumida`

| Condição               | Alerta                                              |
|------------------------|-----------------------------------------------------|
| Balanço ≥ 0            | OK — Geração supera consumo                         |
| -2,0 ≤ Balanço < 0     | ATENCAO — Consumo supera geração moderadamente      |
| Balanço < -2,0         | CRITICO — Déficit energético, ativar modo economia  |

### Eficiência dos Painéis Solares
`Eficiência (%) = (Potência gerada W / (Irradiância W/m² × Área m²)) × 100`

| Degradação vs. referência | Alerta                              |
|---------------------------|-------------------------------------|
| ≤ 2%                      | OK — Painéis operando normalmente   |
| > 2% e ≤ 5%               | ATENCAO — Leve degradação detectada |
| > 5%                      | CRITICO — Degradação crítica        |

---

## Pontuação de Risco Operacional

| Classificação | Pontos |
|---------------|--------|
| NORMAL        | 0      |
| ATENCAO       | 1      |
| CRITICO       | 2      |

### Classificação por Ciclo
| Pontuação total | Classificação     |
|-----------------|-------------------|
| 0 a 2 pontos    | MISSAO ESTAVEL    |
| 3 a 5 pontos    | MISSAO EM ATENCAO |
| 6 a 10 pontos   | MISSAO CRITICA    |

### Classificação Final (pontuação acumulada — máx. 60 pts)
| Pontuação acumulada | Classificação Final |
|---------------------|---------------------|
| ≥ 36 pontos         | MISSAO CRITICA      |
| ≥ 18 e < 36 pontos  | MISSAO EM ATENCAO   |
| < 18 pontos         | MISSAO ESTAVEL      |

> Os limiares representam 60% e 30% do máximo possível (60 pts), refletindo se a maioria dos ciclos foi crítica ou apenas uma parcela.

---

## Índice de Sustentabilidade Energética (ISE)

O ISE mede a proporção da energia consumida que foi suprida por fonte renovável (solar):

```
ISE (%) = (Energia solar total gerada / Energia total consumida) × 100
```

| ISE             | Classificação                                                  |
|-----------------|----------------------------------------------------------------|
| ≥ 80%           | SUSTENTAVEL — missão energeticamente autônoma                  |
| ≥ 50% e < 80%   | PARCIALMENTE SUSTENTAVEL — dependência moderada das reservas   |
| < 50%           | NAO SUSTENTAVEL — alto consumo das reservas não renováveis     |

---

## Funções do Sistema

### Funções Operacionais
| Função                     | Descrição                                                           |
|----------------------------|---------------------------------------------------------------------|
| `verificar_temperatura()`  | Classifica a temperatura e atribui pontuação ao ciclo              |
| `verificar_comunicacao()`  | Classifica a comunicação e atribui pontuação ao ciclo              |
| `verificar_bateria()`      | Classifica a bateria e atribui pontuação ao ciclo                  |
| `verificar_oxigenio()`     | Classifica o oxigênio e atribui pontuação ao ciclo                 |
| `verificar_estabilidade()` | Classifica a estabilidade e atribui pontuação ao ciclo             |
| `classificar_ciclo()`      | Retorna a classificação textual do ciclo pela pontuação total      |
| `gerar_recomendacoes()`    | Gera recomendações automáticas baseadas nos alertas do ciclo       |
| `risco_ciclo()`            | Calcula e armazena a pontuação total de risco do ciclo             |
| `analisar_tendencia()`     | Compara primeiro e último ciclo para indicar tendência da missão   |
| `classificacao_final()`    | Classifica a missão com base na pontuação acumulada               |

### Funções Energéticas (SERS)
| Função                          | Descrição                                                            |
|---------------------------------|----------------------------------------------------------------------|
| `calcular_consumo_energetico()` | Calcula energia consumida no ciclo: E = P × t (kWh)                |
| `calcular_geracao_solar()`      | Calcula energia gerada pelos painéis FV no ciclo: E = P × t (kWh)  |
| `calcular_eficiencia_solar()`   | Calcula eficiência real dos painéis: η = P_gerada / P_incidente     |
| `gerar_alerta_energetico()`     | Avalia balanço e degradação dos painéis, gera alertas automáticos   |
| `calcular_sustentabilidade()`   | Calcula o ISE da missão (% energia renovável sobre total consumido) |
| `classificar_sustentabilidade()`| Retorna o status de sustentabilidade com base no ISE                |
