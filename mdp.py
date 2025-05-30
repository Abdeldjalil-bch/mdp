import streamlit as st
import hashlib

# Configuration de la page
st.set_page_config(
    page_title="Mon Application",
    page_icon="👤",
    layout="wide"
)

# Liste des utilisateurs autorisés (email : mot_de_passe)
USERS = {
    "user1@example.com": "password123",
    "user2@company.com": "motdepasse456", 
    "admin@domain.com": "admin789"
}

def authenticate_user(email, password):
    return email in USERS and USERS[email] == password

def login_form():
    st.title("🔐 Connexion Requise")
    
    with st.form("login_form"):
        email = st.text_input("📧 Email", placeholder="votre.email@exemple.com")
        password = st.text_input("🔒 Mot de passe", type="password")
        submit = st.form_submit_button("Se connecter", use_container_width=True)
        
        if submit:
            if authenticate_user(email, password):
                st.session_state["authenticated"] = True
                st.session_state["user_email"] = email
                st.success("Connexion réussie!")
                st.rerun()
            else:
                st.error("❌ Email ou mot de passe incorrect")
    
    # Afficher les utilisateurs de test
    with st.expander("👥 Utilisateurs de test"):
        st.write("**Comptes de démonstration :**")
        for email in USERS.keys():
            st.write(f"• {email}")

# Initialiser l'état de session
if "authenticated" not in st.session_state:
    st.session_state["authenticated"] = False

# Vérifier l'authentification
if not st.session_state["authenticated"]:
    login_form()
else:
    # L'utilisateur est connecté - afficher l'application
    user_email = st.session_state["user_email"]
    
    # Header avec informations utilisateur
    st.title("🎯 Mon Application Streamlit")
    
    # Sidebar avec informations utilisateur
    with st.sidebar:
        st.markdown("### 👤 Informations Utilisateur")
        st.write(f"**Email :** {user_email}")
        st.write(f"**Statut :** ✅ Connecté")
        
        # Bouton de déconnexion
        if st.button("Se déconnecter", type="secondary"):
            st.session_state["authenticated"] = False
            st.session_state.pop("user_email", None)
            st.rerun()
    
    # Contenu principal
    st.markdown("---")
    
    # Affichage des informations utilisateur dans la page principale
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown("### 👋 Bienvenue !")
        st.success(f"Vous êtes connecté en tant que : **{user_email}**")
        
        # Votre contenu d'application ici
        st.markdown("### 📊 Contenu de l'Application")
        st.write("Ici vous pouvez ajouter le contenu de votre application...")
