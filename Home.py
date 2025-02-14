import streamlit as st
# from streamlit_option_menu import option_menu

# with st.sidebar:
#     selecao = option_menu(
#         menu_title="App",
#         options=["Início", "Projetos", "Contato"]
#     )

# selecao = option_menu(
#     menu_title="App",
#     options=["Início", "Projetos", "Contato"],
#     icons=["house", "graph-up-arrow", "envelope-at"],
#     menu_icon="app-indicator",
#     orientation="horizontal"
# )

# if selecao == "Início":
#     st.title(f'Você selecionou o menu {selecao}')

# if selecao == "Projetos":
#     st.title(f'Você selecionou o menu {selecao}')

# if selecao == "Contato":
#     st.title(f'Você selecionou o menu {selecao}')

st.set_page_config(
    page_title="Multipage App"
)

st.title("Home page")
# st.sidebar.success("Escolha a página")