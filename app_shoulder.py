import streamlit as st
import pandas as pd
import numpy as np
import pycaret.classification as caret


st.title('When rotator cuff repair may not be indicated: Machine Learning can Predict Non-Achievement of Clinically Significant Outcomes After Rotator Cuff Surgical Repair')
st.header('Probability of Non-Archivement of Clinical Significant Outcomes After Rotator Cuff Surgical Repair')


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
ar = st.sidebar.radio(label='Rheumatoid arthritis', options=('Yes', 'No'), horizontal=True)
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
trabalhista = st.sidebar.radio(label="Worker's Compensation", options=('Yes', 'No'), horizontal=True)
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
todo_supra = st.sidebar.radio(label='Entire Extension of the Supraspinatus Affected', options=('Yes', 'No'), horizontal=True)
if todo_supra == 'Yes':
    todo_supra = 0
else:
    todo_supra = 1

# supra_anterior
#  0 = sem acometimento da porção anterior do supra; 1 = acometimento da porção anterior do supra
supra_anterior = st.sidebar.radio(label='Anterior Portion of the Supraspinatus Affected', options=('Yes', 'No'), horizontal=True)
if supra_anterior == 'Yes':
    supra_anterior = 1
else:
    supra_anterior = 0

# fuchs_supra
# 1 = pouca infiltração gordurosa; 2 = média infiltração gordurosa; 3 = muita infiltração gordurosa
fuchs_supra = st.sidebar.radio(label='Fatty Degeneration of the Supraspinatus', options=('Goutallier 0+1', 'Goutallier 2', 'Goutallier 3+4'))
if fuchs_supra == 'Goutallier 2':
    fucs_supra_media_infiltracao_gordurosa = 1
    fucs_supra_muita_infiltracao_gordurosa = 0
elif fuchs_supra == 'Goutallier 3+4':
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
fuchs_infra = st.sidebar.radio(label='Fatty Degeneration of Infraspinatus', options=('Goutallier 0+1', 'Goutallier 2', 'Goutallier 3+4'))
if fuchs_infra == 'Goutallier 2':
    fucs_infra_media_infiltracao_gordurosa = 1
    fucs_infra_muita_infiltracao_gordurosa = 0
elif fuchs_infra == 'Goutallier 3+4':
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
fuchs_sub = st.sidebar.radio(label='Fatty Degeneration of the Subscapularis', options=('Goutallier 0+1', 'Goutallier 2', 'Goutallier 3+4'))
if fuchs_sub == 'Goutallier 2':
    fucs_sub_media_infiltracao_gordurosa = 1
    fucs_sub_muita_infiltracao_gordurosa = 0
elif fuchs_sub == 'Goutallier 3+4':
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
    'Age': [idade],
    'Biological_Sex_Male': [homen],
    'Diabetes_Yes': [diabetes],
    'Rheumatoid_arthritis_Yes': [ar],
    'Past_Smoker': [ex_tabagista],
    'Current_Smoker': [tabagista],
    'Previous_Trauma_Yes': [trauma],
    'Workers_Compensation_Yes': [trabalhista],
    'Previous_Injection_with_Corticosteroids_Yes': [infiltracao],
    'Supraspinatus_Thickness_Partial_tear': [supra_transfixante],
    'Supraspinatus_Thickness_Full_thickness_tear': [supra_parcial],
    'Supraspinatus_Retraction_more_3cm': [supra_ret_m3cm],
    'Entire_Extension_of_the_Supraspinatus_Affected_Yes': [todo_supra],
    'Anterior_Portion_of_the_Supraspinatus_Affected_Yes': [supra_anterior],
    'Fatty_Degeneration_of_the_Supraspinatus_Goutallier_2': [fucs_supra_media_infiltracao_gordurosa],
    'Fatty_Degeneration_of_the_Supraspinatus_Goutallier_3to4': [fucs_supra_muita_infiltracao_gordurosa],
    'Infraspinatus_Thickness_Partial_tear': [infra_parcial],
    'Infraspinatus_Thickness_Full_thickness_tear': [infra_transfixante],
    'Infraspinatus_Retraction_more_3cm': [infra_ret_m3cm],
    'Extension_of_the_Infraspinatus_Affected_Superior_portion': [infra_extensao_superior],
    'Extension_of_the_Infraspinatus_Affected_Entire_tendon': [infra_extensao_todo_tendao],
    'Fatty_Degeneration_of_Infraspinatus_Goutallier_2': [fucs_infra_media_infiltracao_gordurosa],
    'Fatty_Degeneration_of_Infraspinatus_Goutallier_3to4': [fucs_infra_muita_infiltracao_gordurosa],
    'Extension_of_the_Subscapularis_Affected_Partial_tear_of_the_upper_third': [sub_extensao_parcial],
    'Extension_of_the_Subscapularis_Affected_Full_thickness_tear_of_the_upper_third': [sub_extensao_terco_superior],
    'Extension_of_the_Subscapularis_Affected_Full_thickness_tear_of_the_upper_two_thirds_or_more': [sub_extensao_transfixante],
    'Fatty_Degeneration_of_the_Subscapularis_Goutallier_2': [fucs_sub_media_infiltracao_gordurosa],
    'Fatty_Degeneration_of_the_Subscapularis_Goutallier_3to4': [fucs_sub_muita_infiltracao_gordurosa],
    'Injury_of_the_Long_Head_of_the_Biceps_Partial_tear': [biceps_lesao_parcial],
    'Injury_of_the_Long_Head_of_the_Biceps_Complete_tear': [biceps_lesao_completa],
    'Instability_of_the_Log_Head_of_the_Biceps_Subluxated': [biceps_estabilidade_subluxado],
    'Instability_of_the_Log_Head_of_the_Biceps_Dislocated': [biceps_estabilidade_luxado],
    'Instability_of_the_Log_Head_of_the_Biceps_Complete_tear': [biceps_estabilidade_roto],
    'Glenohumeral_Arthrosis_Yes': [artrose],
    'Preoperative_ASES_Score': [asespre]
})



model = caret.load_model('artfacts/modelo_rf_pipeline')

predicition = caret.predict_model(model, data=df)


if predicition.loc[0, 'prediction_label'] == 1:
    score = predicition.loc[0, 'prediction_score']
else:
    score = 1 - predicition.loc[0, 'prediction_score']

score = np.round(score*100, 2)

st.subheader(f"""
The probability of this patient do not achieve the ASES minimal clinically important difference at 24 months is of **{score}%**
""")