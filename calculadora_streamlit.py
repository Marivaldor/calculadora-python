import streamlit as st
import math

# Configuração da página
st.set_page_config(
    page_title="Calculadora Streamlit",
    page_icon="🧮",
    layout="centered"
)

# CSS personalizado
st.markdown("""
<style>
    .stButton > button {
        width: 100%;
        border-radius: 10px;
        height: 50px;
        font-size: 20px;
        font-weight: bold;
        margin: 2px;
    }
    .number-button > button {
        background-color: #4a5568;
        color: white;
    }
    .number-button > button:hover {
        background-color: #2d3748;
    }
    .operation-button > button {
        background-color: #ecc94b;
        color: white;
    }
    .operation-button > button:hover {
        background-color: #d69e2e;
    }
    .clear-button > button {
        background-color: #f56565;
        color: white;
    }
    .clear-button > button:hover {
        background-color: #c53030;
    }
    .equals-button > button {
        background-color: #48bb78;
        color: white;
    }
    .equals-button > button:hover {
        background-color: #38a169;
    }
    .display {
        background-color: #2d3748;
        color: white;
        padding: 20px;
        border-radius: 10px;
        text-align: right;
        font-family: monospace;
        margin-bottom: 20px;
    }
</style>
""", unsafe_allow_html=True)

# Inicialização do estado da calculadora
if 'display' not in st.session_state:
    st.session_state.display = '0'
if 'previous_value' not in st.session_state:
    st.session_state.previous_value = None
if 'operation' not in st.session_state:
    st.session_state.operation = None
if 'new_number' not in st.session_state:
    st.session_state.new_number = False

# Funções da calculadora
def append_number(number):
    if st.session_state.new_number:
        st.session_state.display = str(number)
        st.session_state.new_number = False
    else:
        if st.session_state.display == '0':
            st.session_state.display = str(number)
        else:
            st.session_state.display += str(number)

def set_operation(op):
    if op == 'sqrt':
        try:
            value = float(st.session_state.display)
            if value < 0:
                st.session_state.display = 'Erro'
            else:
                st.session_state.display = str(math.sqrt(value))
        except:
            st.session_state.display = 'Erro'
        return

    if op == 'percent':
        try:
            if st.session_state.previous_value:
                result = (float(st.session_state.display) / 100) * float(st.session_state.previous_value)
            else:
                result = float(st.session_state.display) / 100
            st.session_state.display = str(result)
        except:
            st.session_state.display = 'Erro'
        return

    st.session_state.previous_value = st.session_state.display
    st.session_state.operation = op
    st.session_state.new_number = True

def calculate():
    if not st.session_state.previous_value or not st.session_state.operation:
        return

    try:
        num1 = float(st.session_state.previous_value)
        num2 = float(st.session_state.display)
        
        if st.session_state.operation == '+':
            result = num1 + num2
        elif st.session_state.operation == '-':
            result = num1 - num2
        elif st.session_state.operation == '*':
            result = num1 * num2
        elif st.session_state.operation == '/':
            if num2 == 0:
                st.session_state.display = 'Erro: Divisão por zero!'
                return
            result = num1 / num2
        elif st.session_state.operation == 'pow':
            result = math.pow(num1, num2)
        
        st.session_state.display = str(result)
        st.session_state.previous_value = None
        st.session_state.operation = None
        st.session_state.new_number = True
    except:
        st.session_state.display = 'Erro'

def clear():
    st.session_state.display = '0'
    st.session_state.previous_value = None
    st.session_state.operation = None
    st.session_state.new_number = False

# Interface da calculadora
st.title("Calculadora Streamlit")

# Display
st.markdown(f'<div class="display"><h1>{st.session_state.display}</h1></div>', unsafe_allow_html=True)

# Botões
col1, col2, col3, col4 = st.columns(4)

# Primeira linha
with col1:
    st.markdown('<div class="clear-button">', unsafe_allow_html=True)
    if st.button("AC"):
        clear()
    st.markdown('</div>', unsafe_allow_html=True)
with col2:
    st.markdown('<div class="operation-button">', unsafe_allow_html=True)
    if st.button("√"):
        set_operation('sqrt')
    st.markdown('</div>', unsafe_allow_html=True)
with col3:
    st.markdown('<div class="operation-button">', unsafe_allow_html=True)
    if st.button("%"):
        set_operation('percent')
    st.markdown('</div>', unsafe_allow_html=True)
with col4:
    st.markdown('<div class="operation-button">', unsafe_allow_html=True)
    if st.button("÷"):
        set_operation('/')
    st.markdown('</div>', unsafe_allow_html=True)

# Segunda linha
with col1:
    st.markdown('<div class="number-button">', unsafe_allow_html=True)
    if st.button("7"):
        append_number(7)
    st.markdown('</div>', unsafe_allow_html=True)
with col2:
    st.markdown('<div class="number-button">', unsafe_allow_html=True)
    if st.button("8"):
        append_number(8)
    st.markdown('</div>', unsafe_allow_html=True)
with col3:
    st.markdown('<div class="number-button">', unsafe_allow_html=True)
    if st.button("9"):
        append_number(9)
    st.markdown('</div>', unsafe_allow_html=True)
with col4:
    st.markdown('<div class="operation-button">', unsafe_allow_html=True)
    if st.button("×"):
        set_operation('*')
    st.markdown('</div>', unsafe_allow_html=True)

# Terceira linha
with col1:
    st.markdown('<div class="number-button">', unsafe_allow_html=True)
    if st.button("4"):
        append_number(4)
    st.markdown('</div>', unsafe_allow_html=True)
with col2:
    st.markdown('<div class="number-button">', unsafe_allow_html=True)
    if st.button("5"):
        append_number(5)
    st.markdown('</div>', unsafe_allow_html=True)
with col3:
    st.markdown('<div class="number-button">', unsafe_allow_html=True)
    if st.button("6"):
        append_number(6)
    st.markdown('</div>', unsafe_allow_html=True)
with col4:
    st.markdown('<div class="operation-button">', unsafe_allow_html=True)
    if st.button("-"):
        set_operation('-')
    st.markdown('</div>', unsafe_allow_html=True)

# Quarta linha
with col1:
    st.markdown('<div class="number-button">', unsafe_allow_html=True)
    if st.button("1"):
        append_number(1)
    st.markdown('</div>', unsafe_allow_html=True)
with col2:
    st.markdown('<div class="number-button">', unsafe_allow_html=True)
    if st.button("2"):
        append_number(2)
    st.markdown('</div>', unsafe_allow_html=True)
with col3:
    st.markdown('<div class="number-button">', unsafe_allow_html=True)
    if st.button("3"):
        append_number(3)
    st.markdown('</div>', unsafe_allow_html=True)
with col4:
    st.markdown('<div class="operation-button">', unsafe_allow_html=True)
    if st.button("+"):
        set_operation('+')
    st.markdown('</div>', unsafe_allow_html=True)

# Quinta linha
with col1:
    st.markdown('<div class="number-button">', unsafe_allow_html=True)
    if st.button("0"):
        append_number(0)
    st.markdown('</div>', unsafe_allow_html=True)
with col2:
    st.markdown('<div class="number-button">', unsafe_allow_html=True)
    if st.button("."):
        if '.' not in st.session_state.display:
            append_number('.')
    st.markdown('</div>', unsafe_allow_html=True)
with col3:
    st.markdown('<div class="operation-button">', unsafe_allow_html=True)
    if st.button("^"):
        set_operation('pow')
    st.markdown('</div>', unsafe_allow_html=True)
with col4:
    st.markdown('<div class="equals-button">', unsafe_allow_html=True)
    if st.button("="):
        calculate()
    st.markdown('</div>', unsafe_allow_html=True) 