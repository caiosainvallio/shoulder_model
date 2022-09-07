import streamlit as st
import pandas as pd
import numpy as np
import pycaret.classification as caret


st.title('When rotator cuff repair may not be indicated: Machine Learning can Predict Non-Achievement of Clinically Significant Outcomes After Rotator Cuff Surgical Repair')
st.write('Probability of Non-Archivement of Clinical Significant Outcomes After Rotator Cuff Surgical Repair')


# aba lateral
st.sidebar.title('Predictors')

## features


# Idade
# anos
idade = st.sidebar.slider(label='Age (years)', min_value=30, max_value=78, value=56)

# Sexo
# 0 = mulher; 1 = homem 
homen = st.sidebar.radio(label='Biological Sex', options=('Male', 'Female'), horizontal=True)
if homen == 'Male':
    homen = 1
else:
    homen = 0

# Diabete
# 0 = ausência de diabetes; 1 = presença de Diabetes
diabetes = st.sidebar.radio(label='Diabetes', options=('Yes', 'No'), horizontal=True)
if diabetes == 'Yes':
    diabetes = 1
else:
    diabetes = 0

# AR
# 0 = ausência de Artrite Reumatóide; 1 = presença de Artrite Reumatóide
ar = st.sidebar.radio(label='Rheumatoid rthritis', options=('Yes', 'No'), horizontal=True)
if ar == 'Yes':
    ar = 1
else:
    ar = 0

# Tabagismo
# 0 = não tabagista; 1 = ex tabagista; 2 = tabagista
tabaco = st.sidebar.radio(label='Smoking', options=('Current Smoker', 'Past Smoker', 'Non Smoker'))
if tabaco == 'Current Smoker':
    ex_tabagista = 0
    tabagista = 1
elif tabaco == 'Past Smoker':
    ex_tabagista = 1
    tabagista = 0
else:
    ex_tabagista = 0
    tabagista = 0

# Trauma
# 0 = ausência de trumas prévios; 1 = presença de trumas prévios
trauma = st.sidebar.radio(label='Previous Trauma', options=('Yes', 'No'), horizontal=True)
if trauma == 'Yes':
    trauma = 1
else:
    trauma = 0

# Trabalhista
# 0 = ausência de problemas trabalhistas; 1 = presença de problemas trabalhistas
trabalhista = st.sidebar.radio(label="worker's Compensation", options=('Yes', 'No'), horizontal=True)
if trabalhista == 'Yes':
    trabalhista = 1
else:
    trabalhista = 0

# Infiltracao
# 0 = sem histótrico de infiltração; 1 = histórico de infiltração
infiltracao = st.sidebar.radio(label='Previous Injection with Corticosteroids', options=('Yes', 'No'))
if infiltracao == 'Yes':
    infiltracao = 1
else:
    infiltracao = 0

# supra_espessura3
# 0 = integro; 1 = routura parcial; 2 = transfixante 
supra_espessura3 = st.sidebar.radio(label='Supraspinatus Thickness', options=('Intact', 'Partial tear', 'Full-thickness tear'))
if supra_espessura3 == 'Full-thickness tear':
    supra_transfixante = 1
    supra_parcial = 0
if supra_espessura3 == 'Partial tear':
    supra_transfixante = 0
    supra_parcial = 1
else:
    supra_transfixante = 0
    supra_parcial = 0

# supra_ret2
# 1 < 3cm; 2 > 3cm
supra_ret_m3cm = st.sidebar.radio(label='Espessura do supra', options=('< 3cm', '> 3cm'))
if supra_ret_m3cm == '> 3cm':
    supra_ret_m3cm = 1
else:
    supra_ret_m3cm = 0

# todo_supra
# 0 = sem acometimento de toda extensão do supra; 1 = acometimento de toda extensão do supra
todo_supra = st.sidebar.radio(label='Todo supra', options=('Acometimento de toda extensão do supra', 'Sem acometimento de toda extensão do supra'))
if todo_supra == 'Acometimento de toda extensão do supra':
    todo_supra = 1
else:
    todo_supra = 0

# supra_anterior
#  0 = sem acometimento da porção anterior do supra; 1 = acometimento da porção anterior do supra
supra_anterior = st.sidebar.radio(label='Todo supra', options=('Acometimento da porção anterior do supra', 'Sem acometimento da porção anterior do supra'))
if supra_anterior == 'Acometimento da porção anterior do supra':
    supra_anterior = 1
else:
    supra_anterior = 0

# fuchs_supra
# 1 = pouca infiltração gordurosa; 2 = média infiltração gordurosa; 3 = muita infiltração gordurosa
fuchs_supra = st.sidebar.radio(label='FUCHS Supra', options=('Pouca infiltração gordurosa', 'Média infiltração gordurosa', 'Muita infiltração gordurosa'))
if fuchs_supra == 'Média infiltração gordurosa':
    fucs_supra_media_infiltracao_gordurosa = 1
    fucs_supra_muita_infiltracao_gordurosa = 0
elif fuchs_supra == 'Muita infiltração gordurosa':
    fucs_supra_media_infiltracao_gordurosa = 0
    fucs_supra_muita_infiltracao_gordurosa = 1
else:
    fucs_supra_media_infiltracao_gordurosa = 0
    fucs_supra_muita_infiltracao_gordurosa = 0

# infra_espessura
# 0 = integro; 1 = routura parcial; 2 = transfixante
infra_espessura = st.sidebar.radio(label='Espessura do infra', options=('Íntegro', 'Routura parcial', 'Transfixante'))
if infra_espessura == 'Routura parcial':
    infra_parcial = 1
    infra_transfixante = 0
elif infra_espessura == 'Transfixante':
    infra_parcial = 0
    infra_transfixante = 1
else:
    infra_parcial = 0
    infra_transfixante = 0

# infra_ret2
# 1 < 3cm; 2 > 3cm
infra_ret_m3cm = st.sidebar.radio(label='Espessura do infra', options=('< 3cm', '> 3cm'))
if infra_ret_m3cm == '> 3cm':
    infra_ret_m3cm = 1
else:
    infra_ret_m3cm = 0

# infra_extensao
# 0 = íntegro, 1 = porção superior; 2 = todo o tendão
infra_extensao = st.sidebar.radio(label='Extensão infra', options=('Íntegro', 'Porção superior', 'Todo o tendão'))
if infra_extensao == 'Porção superior':
    infra_extensao_superior = 1
    infra_extensao_todo_tendao = 0
elif infra_extensao == 'Todo o tendão':
    infra_extensao_superior = 1
    infra_extensao_todo_tendao = 0
else:
    infra_extensao_superior = 0
    infra_extensao_todo_tendao = 0


# fuchs_infra
# 1 = pouca infiltração gordurosa; 2 = média infiltração
fuchs_infra = st.sidebar.radio(label='FUCHS infra', options=('Pouca infiltração gordurosa', 'Média infiltração gordurosa', 'Muita infiltração gordurosa'))
if fuchs_infra == 'Média infiltração gordurosa':
    fucs_infra_media_infiltracao_gordurosa = 1
    fucs_infra_muita_infiltracao_gordurosa = 0
elif fuchs_infra == 'Muita infiltração gordurosa':
    fucs_infra_media_infiltracao_gordurosa = 0
    fucs_infra_muita_infiltracao_gordurosa = 1
else:
    fucs_infra_media_infiltracao_gordurosa = 0
    fucs_infra_muita_infiltracao_gordurosa = 0

# sub_extensão4
# 0 = íntegro, 1 = parcial; 2 = terço superior; 3 = transfixante 2/3 ou todo tendão
sub_extensão4 = st.sidebar.radio(label='Extensão subescapular', options=('Íntegro', 'Parcial', 'Terço superior', 'Transfixante 2/3 ou todo tendão'))
if sub_extensão4 == 'Parcial':
    sub_extensao_parcial = 1
    sub_extensao_terco_superior = 0
    sub_extensao_transfixante = 0
elif sub_extensão4 == 'Terço superior':
    sub_extensao_parcial = 0
    sub_extensao_terco_superior = 1
    sub_extensao_transfixante = 0
elif sub_extensão4 == 'Transfixante 2/3 ou todo tendão':
    sub_extensao_parcial = 0
    sub_extensao_terco_superior = 0
    sub_extensao_transfixante = 1
else:
    sub_extensao_parcial = 0
    sub_extensao_terco_superior = 0
    sub_extensao_transfixante = 0

# fuchs_sub
# 1 = pouca infiltração gordurosa; 2 = média infiltração
fuchs_sub = st.sidebar.radio(label='FUCHS subescapular', options=('Pouca infiltração gordurosa', 'Média infiltração gordurosa', 'Muita infiltração gordurosa'))
if fuchs_sub == 'Média infiltração gordurosa':
    fucs_sub_media_infiltracao_gordurosa = 1
    fucs_sub_muita_infiltracao_gordurosa = 0
elif fuchs_sub == 'Muita infiltração gordurosa':
    fucs_sub_media_infiltracao_gordurosa = 0
    fucs_sub_muita_infiltracao_gordurosa = 1
else:
    fucs_sub_media_infiltracao_gordurosa = 0
    fucs_sub_muita_infiltracao_gordurosa = 0

# biceps_lesao
# 0 = íntegro, 1 = lesão parcial; 2 = lesão completa
biceps_lesao = st.sidebar.radio(label='Extensão da lesão do bíceps', options=('Íntegro', 'Lesão parcial', 'Lesão completa'))
if biceps_lesao == 'Lesão parcial':
    biceps_lesao_parcial = 1
    biceps_lesao_completa = 0
elif biceps_lesao == 'Lesão completa':
    biceps_lesao_parcial = 0
    biceps_lesao_completa = 1
else:
    biceps_lesao_parcial = 0
    biceps_lesao_completa = 0

# biceps_estabilidade
# 0 = tópico; 1 - subluxado; 2 = luxado; 3 = roto
biceps_estabilidade = st.sidebar.radio(label='Estabilidade do bíceps', options=('Tópico', 'Subluxado', 'Luxado', 'Roto'))
if biceps_estabilidade == 'Subluxado':
    biceps_estabilidade_subluxado = 1
    biceps_estabilidade_luxado = 0
    biceps_estabilidade_roto = 0
elif biceps_estabilidade == 'Luxado':
    biceps_estabilidade_subluxado = 0
    biceps_estabilidade_luxado = 1
    biceps_estabilidade_roto = 0
elif biceps_estabilidade == 'Roto':
    biceps_estabilidade_subluxado = 0
    biceps_estabilidade_luxado = 0
    biceps_estabilidade_roto = 1
else:
    biceps_estabilidade_subluxado = 0
    biceps_estabilidade_luxado = 0
    biceps_estabilidade_roto = 0


# artrose
# 0 = ausência de artrose; 1 = presença de artrose
artrose = st.sidebar.radio(label='Artrose', options=('Ausência de artrose', 'Presença de artrose'))
if artrose == 'Ausência de artrose':
    artrose = 0
else:
    artrose = 1

# asespre
# score pré-operatório 0 = more disability and 100 = less disability
asespre = st.sidebar.slider(label='ASES pré-operatório', min_value=1, max_value=100, value=42)



# dataframe to predict
df = pd.DataFrame(data={
    'idade': [idade],
    'homen': [homen],
    'diabetes': [diabetes],
    'ar': [ar],
    'ex_tabagista': [ex_tabagista],
    'tabagista': [tabagista],
    'trauma': [trauma],
    'trabalhista': [trabalhista],
    'infiltracao': [infiltracao],
    'supra_transfixante': [supra_transfixante],
    'supra_parcial': [supra_parcial],
    'supra_ret_m3cm': [supra_ret_m3cm],
    'todo_supra': [todo_supra],
    'supra_anterior': [supra_anterior],
    'fucs_supra_media_infiltracao_gordurosa': [fucs_supra_media_infiltracao_gordurosa],
    'fucs_supra_muita_infiltracao_gordurosa': [fucs_supra_muita_infiltracao_gordurosa],
    'infra_parcial': [infra_parcial],
    'infra_transfixante': [infra_transfixante],
    'infra_ret_m3cm': [infra_ret_m3cm],
    'infra_extensao_superior': [infra_extensao_superior],
    'infra_extensao_todo_tendao': [infra_extensao_todo_tendao],
    'fucs_infra_media_infiltracao_gordurosa': [fucs_infra_media_infiltracao_gordurosa],
    'fucs_infra_muita_infiltracao_gordurosa': [fucs_infra_muita_infiltracao_gordurosa],
    'sub_extensao_parcial': [sub_extensao_parcial],
    'sub_extensao_terco_superior': [sub_extensao_terco_superior],
    'sub_extensao_transfixante': [sub_extensao_transfixante],
    'fucs_sub_media_infiltracao_gordurosa': [fucs_sub_media_infiltracao_gordurosa],
    'fucs_sub_muita_infiltracao_gordurosa': [fucs_sub_muita_infiltracao_gordurosa],
    'biceps_lesao_parcial': [biceps_lesao_parcial],
    'biceps_lesao_completa': [biceps_lesao_completa],
    'biceps_estabilidade_subluxado': [biceps_estabilidade_subluxado],
    'biceps_estabilidade_luxado': [biceps_estabilidade_luxado],
    'biceps_estabilidade_roto': [biceps_estabilidade_roto],
    'artrose': [artrose],
    'asespre': [asespre]
})


model = caret.load_model('artfacts/modelo_rf_pipeline')


predicition = caret.predict_model(model, data=df)

if predicition.loc[0, 'Label'] == 1:
    score = predicition.loc[0, 'Score']
else:
    score = 1 - predicition.loc[0, 'Score']

score = np.round(score*100, 2)

diff_prevalencia = score - 17.2
diff_prevalencia = np.round(diff_prevalencia, 2)
st.metric('Predição (%)', score, diff_prevalencia)