import streamlit as st

# Configuração da página
st.set_page_config(page_title="Calorias por Dani", page_icon="🔥")

# Título
st.title("🔥 Calculadora de Calorias")
st.markdown("Descubra sua meta diária de forma simples e rápida")

st.markdown("---")

# Inputs
col1, col2 = st.columns(2)

with col1:
    idade = st.number_input("Idade", min_value=0)
    peso = st.number_input("Peso (kg)", min_value=0.0)

with col2:
    altura = st.number_input("Altura (cm)", min_value=0.0)
    sexo = st.selectbox("Sexo", ["feminino", "masculino"])

# Nível de atividade
st.markdown("---")
st.subheader("Nível de atividade")

activity_options = {
    "Sedentário": 1.2,
    "Levemente ativo": 1.375,
    "Moderadamente ativo": 1.55,
    "Muito ativo": 1.725,
    "Extremamente ativo": 1.9,
}

activity_label = st.selectbox("Escolha seu nível", list(activity_options.keys()))
activity_multiplier = activity_options[activity_label]

# Objetivo
st.markdown("---")
st.subheader("Objetivo")

goal = st.radio(
    "Qual seu objetivo?",
    ["Emagrecer", "Manter", "Ganhar massa"],
    horizontal=True,
)

if goal in ["Emagrecer", "Ganhar massa"]:
    intensidade = st.slider(
        "Intensidade (calorias/dia)",
        min_value=100,
        max_value=1000,
        value=500,
        step=50,
    )
    ajuste = intensidade if goal == "Ganhar massa" else -intensidade
else:
    ajuste = 0

# Botão de cálculo
if st.button("Calcular minhas calorias 🔥", use_container_width=True):

    # Cálculo da TMB
    if sexo == "masculino":
        tmb = 10 * peso + 6.25 * altura - 5 * idade + 5
    else:
        tmb = 10 * peso + 6.25 * altura - 5 * idade - 161

    # Cálculo total
    tdee = tmb * activity_multiplier
    meta = tdee + ajuste

    st.markdown("---")
    st.header("Seus Resultados")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("TMB", f"{tmb:.0f} kcal")

    with col2:
        st.metric("Manutenção", f"{tdee:.0f} kcal")

    with col3:
        st.metric("Meta diária", f"{meta:.0f} kcal")

    # Macronutrientes
    st.markdown("---")
    st.subheader("Macronutrientes")

    proteina = round(peso * 2)
    gordura = round(meta * 0.25 / 9)
    carbo = round((meta - proteina * 4 - gordura * 9) / 4)

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("Proteína", f"{proteina} g")

    with col2:
        st.metric("Gordura", f"{gordura} g")

    with col3:
        st.metric("Carboidrato", f"{carbo} g")
    if goal == "Emagrecer":
        ajuste = -500
    elif goal == "Ganhar massa":
        ajuste = 500
    else:
        ajuste = 0
        # Estimativa semanal
        st.markdown("---")
        st.subheader("Estimativa semanal")

    mudanca = ajuste * 7 / 7700

    if mudanca == 0:
        st.info("Peso tende a se manter")
    elif mudanca < 0:
        st.info(f"Perda estimada: {abs(mudanca):.2f} kg/semana")
    else:
        st.info(f"Ganho estimado: {mudanca:.2f} kg/semana")

    # CTA
    st.markdown("---")
    st.markdown("💬 Quer um plano personalizado? Me chama no Instagram 👉 @seuuser")
