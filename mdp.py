import streamlit as st

if not st.user.is_logged_in:
    if st.button("Log in :material/login:"):
        st.login()
else:
    if st.button("Log out :material/logout:"):
        st.logout()
    
    st.markdown(
        f"""<p style='font-size: 20pt;'>Hello <img src='{st.user.picture}' style='height: 40px; width: 40px; vertical-align: middle;'> <b>{st.user.name}</b>.</p>
        <p style='font-size: 20pt;'>You have successfully logged in with <b>{st.user.email}</b>.</p>""",
        unsafe_allow_html=True
    )
