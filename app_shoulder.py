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
idade = st.sidebar.slider(label='Age (years)', min_value=18, max_value=80, value=56)

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
infiltracao = st.sidebar.radio(label='Previous Injection with Corticosteroids', options=('Yes', 'No'), horizontal=True)
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
supra_ret_m3cm = st.sidebar.radio(label='Supraspinatus Retraction', options=('< 3cm', '≥ 3cm'))
if supra_ret_m3cm == '< 3cm':
    supra_ret_m3cm = 0
else:
    supra_ret_m3cm = 1

# todo_supra
# 0 = sem acometimento de toda extensão do supra; 1 = acometimento de toda extensão do supra
todo_supra = st.sidebar.radio(label='Entire Estension of the Supraspinatus Affected', options=('Yes', 'No'), horizontal=True)
if todo_supra == 'Yes':
    todo_supra = 1
else:
    todo_supra = 0

# supra_anterior
#  0 = sem acometimento da porção anterior do supra; 1 = acometimento da porção anterior do supra
supra_anterior = st.sidebar.radio(label='Anterior Portion of the Supraspinatus Affected', options=('Yes', 'No'), horizontal=True)
if supra_anterior == 'Yes':
    supra_anterior = 1
else:
    supra_anterior = 0

# fuchs_supra
# 1 = pouca infiltração gordurosa; 2 = média infiltração gordurosa; 3 = muita infiltração gordurosa
fuchs_supra = st.sidebar.radio(label='Fatty Degeneration of the Supraspinatus', options=('Grade 1', 'Grade 2', 'Grade 3'))
if fuchs_supra == 'Grade 2':
    fucs_supra_media_infiltracao_gordurosa = 1
    fucs_supra_muita_infiltracao_gordurosa = 0
elif fuchs_supra == 'Grade 3':
    fucs_supra_media_infiltracao_gordurosa = 0
    fucs_supra_muita_infiltracao_gordurosa = 1
else:
    fucs_supra_media_infiltracao_gordurosa = 0
    fucs_supra_muita_infiltracao_gordurosa = 0

# infra_espessura
# 0 = integro; 1 = routura parcial; 2 = transfixante
infra_espessura = st.sidebar.radio(label='Infraspinatus Thickness', options=('Intact', 'Partial tear', 'Full-thickness tear'))
if infra_espessura == 'Partial tear':
    infra_parcial = 1
    infra_transfixante = 0
elif infra_espessura == 'Full-thickness tear':
    infra_parcial = 0
    infra_transfixante = 1
else:
    infra_parcial = 0
    infra_transfixante = 0

# infra_ret2
# 1 < 3cm; 2 > 3cm
infra_ret_m3cm = st.sidebar.radio(label='Infraspinatus Retraction', options=('< 3cm', '≥ 3cm'))
if infra_ret_m3cm == '< 3cm':
    infra_ret_m3cm = 0
else:
    infra_ret_m3cm = 1

# infra_extensao
# 0 = íntegro, 1 = porção superior; 2 = todo o tendão
infra_extensao = st.sidebar.radio(label='Extension of the Infraspinatus Affected', options=('Intact', 'Superior portion', 'Entire tendon'))
if infra_extensao == 'Superior portion':
    infra_extensao_superior = 1
    infra_extensao_todo_tendao = 0
elif infra_extensao == 'Entire tendon':
    infra_extensao_superior = 1
    infra_extensao_todo_tendao = 0
else:
    infra_extensao_superior = 0
    infra_extensao_todo_tendao = 0


# fuchs_infra
# 1 = pouca infiltração gordurosa; 2 = média infiltração
fuchs_infra = st.sidebar.radio(label='Fatty Degeneration of Infraspinatus', options=('Grade 1', 'Grade 2', 'Grade 3'))
if fuchs_infra == 'Grade 2':
    fucs_infra_media_infiltracao_gordurosa = 1
    fucs_infra_muita_infiltracao_gordurosa = 0
elif fuchs_infra == 'Grade 3':
    fucs_infra_media_infiltracao_gordurosa = 0
    fucs_infra_muita_infiltracao_gordurosa = 1
else:
    fucs_infra_media_infiltracao_gordurosa = 0
    fucs_infra_muita_infiltracao_gordurosa = 0

# sub_extensão4
# 0 = íntegro, 1 = parcial; 2 = terço superior; 3 = transfixante 2/3 ou todo tendão
sub_extensão4 = st.sidebar.radio(label='Extension of the Subscapularis Affected', options=('Intact', 'Partial tear of the upper third', 'Full-thickness tear of the upper third', 'Full-thickness tear of the upper two thirds or more'))
if sub_extensão4 == 'Partial tear of the upper third':
    sub_extensao_parcial = 1
    sub_extensao_terco_superior = 0
    sub_extensao_transfixante = 0
elif sub_extensão4 == 'Full-thickness tear of the upper third':
    sub_extensao_parcial = 0
    sub_extensao_terco_superior = 1
    sub_extensao_transfixante = 0
elif sub_extensão4 == 'Full-thickness tear of the upper two thirds or more':
    sub_extensao_parcial = 0
    sub_extensao_terco_superior = 0
    sub_extensao_transfixante = 1
else:
    sub_extensao_parcial = 0
    sub_extensao_terco_superior = 0
    sub_extensao_transfixante = 0

# fuchs_sub
# 1 = pouca infiltração gordurosa; 2 = média infiltração
fuchs_sub = st.sidebar.radio(label='Fatty Degeneration of the Subscapularis', options=('Grade 1', 'Grade 2', 'Grade 3'))
if fuchs_sub == 'Grade 2':
    fucs_sub_media_infiltracao_gordurosa = 1
    fucs_sub_muita_infiltracao_gordurosa = 0
elif fuchs_sub == 'Grade 3':
    fucs_sub_media_infiltracao_gordurosa = 0
    fucs_sub_muita_infiltracao_gordurosa = 1
else:
    fucs_sub_media_infiltracao_gordurosa = 0
    fucs_sub_muita_infiltracao_gordurosa = 0

# biceps_lesao
# 0 = íntegro, 1 = lesão parcial; 2 = lesão completa
biceps_lesao = st.sidebar.radio(label='Injury of the Long Head of the Biceps', options=('Intact', 'Partial tear', 'Complete tear'))
if biceps_lesao == 'Partial tear':
    biceps_lesao_parcial = 1
    biceps_lesao_completa = 0
elif biceps_lesao == 'Complete tear':
    biceps_lesao_parcial = 0
    biceps_lesao_completa = 1
else:
    biceps_lesao_parcial = 0
    biceps_lesao_completa = 0

# biceps_estabilidade
# 0 = tópico; 1 - subluxado; 2 = luxado; 3 = roto
biceps_estabilidade = st.sidebar.radio(label='Instability of the Log Head of the Biceps', options=('Topical', 'Subluxated', 'Dislocated', 'Complete tear'))
if biceps_estabilidade == 'Subluxated':
    biceps_estabilidade_subluxado = 1
    biceps_estabilidade_luxado = 0
    biceps_estabilidade_roto = 0
elif biceps_estabilidade == 'Dislocated':
    biceps_estabilidade_subluxado = 0
    biceps_estabilidade_luxado = 1
    biceps_estabilidade_roto = 0
elif biceps_estabilidade == 'Complete tear':
    biceps_estabilidade_subluxado = 0
    biceps_estabilidade_luxado = 0
    biceps_estabilidade_roto = 1
else:
    biceps_estabilidade_subluxado = 0
    biceps_estabilidade_luxado = 0
    biceps_estabilidade_roto = 0


# artrose
# 0 = ausência de artrose; 1 = presença de artrose
artrose = st.sidebar.radio(label='Glenohumeral Arthrosis', options=('Yes', 'No'), horizontal=True)
if artrose == 'Yes':
    artrose = 1
else:
    artrose = 0

# asespre
# score pré-operatório 0 = more disability and 100 = less disability
asespre = st.sidebar.slider(label='Preoperative ASES Score', min_value=1, max_value=100, value=42)



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

st.subheader(f"""
The probability of this patient do not achieve the ASES minimal clinically important difference as 24 months is of **{score}%**
""")