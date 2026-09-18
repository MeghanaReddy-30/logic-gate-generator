import streamlit as st
from logic_engine import parse_expression, generate_truth_table, build_circuit_graph

st.set_page_config(page_title="Logic Gate & Truth Table Generator", layout="wide")
st.title("⚡ Logic Gate & Truth Table Generator")

expr_input = st.text_input("Enter Boolean Expression:", value="(A AND B) OR (NOT C)")

if expr_input:
    try:
        parsed = parse_expression(expr_input)
        col1, col2 = st.columns(2)
        
        with col1:
            st.subheader("📋 Truth Table")
            st.dataframe(generate_truth_table(parsed), use_container_width=True)
            
        with col2:
            st.subheader("🔌 Circuit Diagram")
            st.graphviz_chart(build_circuit_graph(parsed))
    except Exception as e:
        st.error(f"Error parsing expression: {e}")