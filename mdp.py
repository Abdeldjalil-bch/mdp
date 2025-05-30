import streamlit as st

# Configuration de la page
st.set_page_config(
    page_title="Mon Application",
    page_icon="👤",
    layout="wide"
)

# Vérifier si l'utilisateur est connecté
if not st.user.is_logged_in:
    # Page de connexion
    st.title("🔐 Connexion Requise")
    st.write("Veuillez vous connecter pour accéder à l'application.")
    
    # Boutons de connexion (choisissez le fournisseur approprié)
    col1, col2, col3 = st.columns(3)
    
    with col1:
        if st.button("Se connecter avec Google", use_container_width=True):
            st.login("google")
    
    with col2:
        if st.button("Se connecter avec Microsoft", use_container_width=True):
            st.login("microsoft")
    
    with col3:
        if st.button("Se connecter avec GitHub", use_container_width=True):
            st.login("github")

else:
    # L'utilisateur est connecté - afficher l'application
    
    # Header avec informations utilisateur
    st.title("🎯 Mon Application Streamlit")
    
    # Sidebar avec informations utilisateur
    with st.sidebar:
        st.markdown("### 👤 Informations Utilisateur")
        st.write(f"**Nom :** {st.user.name}")
        st.write(f"**Email :** {st.user.email}")
        
        # Bouton de déconnexion
        if st.button("Se déconnecter", type="secondary"):
            st.logout()
    
    # Contenu principal
    st.markdown("---")
    
    # Affichage des informations utilisateur dans la page principale
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown("### 👋 Bienvenue !")
        st.success(f"Vous êtes connecté en tant que : **{st.user.email}**")
        
        # Votre contenu d'application ici
        st.markdown("### 📊 Contenu de l'Application")
        st.write("Ici vous pouvez ajouter le contenu de votre application...")
        
        # Exemple de contenu
        tab1, tab2, tab3 = st.tabs(["📈 Dashboard", "📝 Données", "⚙️ Paramètres"])
        
        with tab1:
            st.write("Contenu du dashboard...")
            st.line_chart([1, 2, 3, 4, 5])
        
        with tab2:
            st.write("Vos données...")
            st.dataframe({
                'Colonne 1': [1, 2, 3, 4],
                'Colonne 2': ['A', 'B', 'C', 'D']
            })
        
        with tab3:
            st.write("Paramètres de l'application...")
            st.slider("Paramètre 1", 0, 100, 50)
    
    with col2:
        # Carte d'informations utilisateur
        st.markdown("### 🏷️ Profil Utilisateur")
        with st.container():
            st.markdown(f"""
            <div style="
                background-color: #f0f2f6;
                padding: 20px;
                border-radius: 10px;
                border-left: 5px solid #1f77b4;
                margin: 10px 0;
            ">
                <h4 style="margin: 0; color: #1f77b4;">👤 {st.user.name}</h4>
                <p style="margin: 5px 0; color: #666;">📧 {st.user.email}</p>
                <p style="margin: 5px 0; color: #666;">🔗 Connecté via OAuth</p>
            </div>
            """, unsafe_allow_html=True)
        
        # Statistiques ou informations supplémentaires
        st.markdown("### 📊 Statistiques")
        st.metric("Sessions", "12", "2")
        st.metric("Dernière connexion", "Aujourd'hui")
    
    # Footer avec email
    st.markdown("---")
    st.markdown(f"<p style='text-align: center; color: #666;'>Session active pour {st.user.email}</p>", 
                unsafe_allow_html=True)
