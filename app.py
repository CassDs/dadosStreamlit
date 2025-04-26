import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Carregar dados
data_path = "c:\\Users\\Aluno\\Downloads\\Projeto Streamlit\\dadosStreamlit\\health_data.csv"
df = pd.read_csv(data_path)

# Título e Introdução
st.title("Saúde sob Pressão: Uma Análise dos Principais Fatores de Risco Cardiovascular")
st.markdown("""
No cenário atual da saúde, condições como hipertensão, diabetes e asma representam riscos consideráveis à qualidade de vida.
A partir da base de dados de pacientes, foi feito a analise de perfis de risco a partir da idade, gênero, níveis de pressão arterial e colesterol.
O objetivo é entender quem são os pacientes mais vulneráveis e propor estratégias de prevenção.
""")

# Perfil dos Pacientes
st.header("Perfil Demográfico dos Pacientes")

col1, col2 = st.columns(2)
with col1:
    st.subheader("Distribuição por Idade")
    plt.figure(figsize=(6,3))
    plt.hist(df['Age'], bins=10, color='skyblue', edgecolor='black')
    plt.xlabel("Idade")
    plt.ylabel("Número de Pacientes")
    st.pyplot(plt)
with col2:
    st.subheader("Distribuição por Gênero")
    gender_counts = df['Gender'].value_counts()
    plt.figure(figsize=(6,4))
    sns.barplot(x=gender_counts.index, y=gender_counts.values, palette="pastel")
    plt.xlabel("Gênero")
    plt.ylabel("Número de Pacientes")
    st.pyplot(plt)

# Diagnósticos
st.header("Principais Diagnósticos")
diag_counts = df['Diagnosis'].value_counts()
plt.figure(figsize=(6,4))
sns.barplot(x=diag_counts.index, y=diag_counts.values, palette="muted")
plt.xlabel("Diagnóstico")
plt.ylabel("Número de Pacientes")
plt.title("Distribuição dos Diagnósticos")
st.pyplot(plt)

# Análise de Risco: Pressão Arterial e Colesterol
st.header("Riscos de Saúde: Pressão Arterial e Colesterol")

col3, col4 = st.columns(2)
with col3:
    st.subheader("Histograma - Pressão Arterial")
    plt.figure(figsize=(6,3))
    plt.hist(df['Blood_Pressure'], bins=10, color='salmon', edgecolor='black')
    plt.xlabel("Pressão Arterial")
    plt.ylabel("Número de Pacientes")
    st.pyplot(plt)
with col4:
    st.subheader("Histograma - Colesterol")
    plt.figure(figsize=(6,3))
    plt.hist(df['Cholesterol_Level'], bins=10, color='gold', edgecolor='black')
    plt.xlabel("Colesterol (mg/dL)")
    plt.ylabel("Número de Pacientes")
    st.pyplot(plt)

# Comparativo entre Gêneros
st.header("Comparativo: Homens vs Mulheres")
col5, col6 = st.columns(2)
with col5:
    st.subheader("Boxplot - Pressão Arterial por Gênero")
    plt.figure(figsize=(5,3))
    sns.boxplot(x='Gender', y='Blood_Pressure', data=df, palette="Set2")
    plt.xlabel("Gênero")
    plt.ylabel("Pressão Arterial")
    st.pyplot(plt)
with col6:
    st.subheader("Boxplot - Colesterol por Gênero")
    plt.figure(figsize=(5,3))
    sns.boxplot(x='Gender', y='Cholesterol_Level', data=df, palette="Set2")
    plt.xlabel("Gênero")
    plt.ylabel("Colesterol (mg/dL)")
    st.pyplot(plt)

# Análises Detalhadas para Sustentar Conclusões
st.header("Análises Detalhadas")

# Análise 1: Colesterol Médio
st.subheader("Colesterol Médio dos Pacientes")
colesterol_medio = df['Cholesterol_Level'].mean()
st.write(f"O colesterol médio dos pacientes é **{colesterol_medio:.1f} mg/dL**.")
if colesterol_medio > 200:
    st.warning("⚠️ Recomendado criar um programa de acompanhamento nutricional.")
else:
    st.success("Níveis médios de colesterol estão dentro do recomendado.")

# Distribuição do colesterol
plt.figure(figsize=(6, 4))
sns.histplot(df['Cholesterol_Level'], bins=10, kde=True, color='gold', edgecolor='black')
plt.axvline(colesterol_medio, color='red', linestyle='--', label=f"Média: {colesterol_medio:.1f} mg/dL")
plt.xlabel("Colesterol (mg/dL)")
plt.ylabel("Número de Pacientes")
plt.title("Distribuição dos Níveis de Colesterol")
plt.legend()
st.pyplot(plt)

# Análise 2: Hipertensão e Idade
st.subheader("Distribuição de Idade entre Pacientes com Hipertensão")
hipertensos = df[df['Diagnosis'] == 'Hypertension']
hipertensos_50 = hipertensos[hipertensos['Age'] > 50].shape[0]
hipertensos_total = hipertensos.shape[0]
pct_hipertensos_50 = (hipertensos_50 / hipertensos_total * 100) if hipertensos_total > 0 else 0
st.write(f"{pct_hipertensos_50:.1f}% dos pacientes com hipertensão têm mais de 50 anos.")
if pct_hipertensos_50 > 50:
    st.warning("⚠️ Promover campanhas de controle de pressão para pacientes acima de 50 anos.")
else:
    st.success("Distribuição equilibrada entre faixas etárias.")

# Gráfico de distribuição de idade para hipertensos
plt.figure(figsize=(6, 4))
sns.histplot(hipertensos['Age'], bins=10, kde=True, color='skyblue', edgecolor='black')
plt.axvline(50, color='red', linestyle='--', label="Idade: 50 anos")
plt.xlabel("Idade")
plt.ylabel("Número de Pacientes com Hipertensão")
plt.title("Distribuição de Idade entre Pacientes com Hipertensão")
plt.legend()
st.pyplot(plt)

# Análise 3: Pressão Arterial por Gênero
st.subheader("Comparação de Pressão Arterial por Gênero")
pressao_homens = df[df['Gender'] == 'Male']['Blood_Pressure'].mean()
pressao_mulheres = df[df['Gender'] == 'Female']['Blood_Pressure'].mean()
st.write(f"Homens apresentam pressão arterial média de **{pressao_homens:.1f} mmHg**, mulheres **{pressao_mulheres:.1f} mmHg**.")
if pressao_homens > pressao_mulheres:
    st.warning("⚠️ Incentivar check-ups regulares para homens a partir dos 40 anos.")
else:
    st.success("Pressão arterial média entre gêneros está equilibrada.")

# Gráfico comparativo de pressão arterial por gênero
plt.figure(figsize=(6, 4))
sns.boxplot(x='Gender', y='Blood_Pressure', data=df, palette="Set2")
plt.xlabel("Gênero")
plt.ylabel("Pressão Arterial")
plt.title("Pressão Arterial por Gênero")
st.pyplot(plt)

# Proposta Final
st.header("Proposta Final")
st.markdown("""
- **Implantação de um programa de triagem anual para colesterol e pressão arterial para todos pacientes acima de 40 anos.**
- **Promover campanhas educativas para controle de pressão arterial em pacientes acima de 50 anos.**
- **Incentivar check-ups regulares para homens a partir dos 40 anos.**
""")
