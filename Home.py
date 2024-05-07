import streamlit

st.set_page_config(page_title="Read Docs", page_icon="📄", layout="wide", initial_sidebar_state="auto", menu_items=None)

##################### SETTINGS ######################
# [0] Setting Page Settings
def page_settings():
    st.image("https://github.com/peteciank/public_files/blob/main/images/aitb_icon.png?raw=true", width=100)

    st.title("Read Docs")
    st.subheader("Upload PDF Documents and Extract the text in it.")
    # [0] Sidebar Settings
    with st.sidebar:
        st.image("https://github.com/peteciank/public_files/blob/main/images/aitb_icon.png?raw=true", width=100)
        
        import streamlit.components.v1 as components
        st.markdown(
            """
            <style>
                section[data-testid="stSidebar"] {
                    width: 400px !important; # Set the width to your desired value
                }
            </style>
            """,
            unsafe_allow_html=True,
        )
        components.html(
            """
            <script src="https://platform.linkedin.com/badges/js/profile.js" async defer type="text/javascript"></script>
            <div class="badge-base LI-profile-badge" data-locale="en_US" data-size="large" data-theme="dark" data-type="HORIZONTAL" data-vanity="pedrociancaglini" data-version="v1">
            <a class="badge-base__link LI-simple-link" href="https://es.linkedin.com/in/pedrociancaglini/en?trk=profile-badge"></a></div>
            """,
        height=300,
        )

page_settings()
