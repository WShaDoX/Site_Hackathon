# =============================================================================
# Script Python : crée ton site web complet en 5 secondes
# Copie-colle tout ça dans un fichier "creer_site.py" et lance-le
# =============================================================================

code_html = """<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Les Pépites de Beauvais - Bio-énergie & Innovation</title>
    <style>
        /* 1. Assurons-nous que le fond est BLANC pur */
        body {font-family: Arial, sans-serif; margin:0; background:white; color:#333; line-height:1.6;}

        header {background: linear-gradient(135deg, #2e7d32, #4caf50); color:white; padding:20px; text-align:center;}
        .logo {max-width:200px; margin:15px auto; display:block;} /* Centrage du logo dans le header */

        nav {background:#1b5e20; padding:15px; text-align:center;} /* Centrage des liens de navigation */
        nav a {color:white; margin:0 25px; text-decoration:none; font-weight:bold;}
        nav a:hover {color:#c8e6c9;}

        /* 2. Centrage du contenu du corps de page */
        .hero {
            color:green; padding:100px 20px; text-align:center;
            /* Le Hero doit être centré sur les pages larges */
            max-width: 1100px; 
            margin: 0 auto;
            text-shadow: 2px 2px 5px rgba(0,0,0,0.8);
        }

        /* Centrage des sections principales */
        section {
            max-width:1100px; 
            margin:30px auto; /* Centrage du bloc section */
            background:white; 
            padding:30px; 
            border-radius:12px; 
            box-shadow:0 5px 20px rgba(0,0,0,0.1);
            text-align: center; /* Centrage des éléments inline à l'intérieur des sections */
        }

        h2 {color:#2e7d32; text-align:center;}

        /* Les listes et les éléments sont centrés via text-align: center; sur la section parente */
        ul {list-style:none; padding:0; display: inline-block; text-align: left; /* Permet de centrer le bloc UL lui-même, mais les puces restent à gauche */}
        ul li {background:#e8f5e8; margin:15px 0; padding:20px; border-radius:8px; border-left:6px solid #4caf50;}

        /* Centrage des images dans les sections */
        section img {
            max-width: 100%;
            height: auto;
            display: block;
            margin: 20px auto; /* Pour centrer l'image qui est un élément de bloc */
        }

        footer {background:#1b5e20; color:white; text-align:center; padding:30px;}
        .logo-footer {max-width:130px; margin:15px auto; display:block;} /* Centrage du logo dans le footer */
    </style>
</head>
<body>

    <header>
        <img src="logo.png" alt="Logo Les Pépites de Beauvais" class="logo">
        <h1>Les Pépites de Beauvais</h1>
        <p>Système hybride géothermie + biomasse – Eau chaude & chauffage 100 % renouvelable</p>
    </header>

    <nav>
        <a href="#accueil">Accueil</a>
        <a href="#solution">La Solution</a>
        <a href="#avantages">Avantages</a>
        <a href="#fonctionnement">Fonctionnement</a>
        <a href="#contact">Contact</a>
    </nav>

    <div class="hero" id="accueil">
        <img src="logo1.png" alt="Logo Les Pépites de Beauvais">
        <h1>De l’eau chaude grâce à la Terre et à la biomasse locale</h1>
        <p>Jusqu’à 80 % d’économies – 100 % renouvelable </p>
    </div>

    <section id="solution">
        <h2>Notre Système Hybride Géothermie + Biomasse</h2>
        <ul>
            <li>Pompe à chaleur géothermique (captage vertical ou horizontal)</li>
            <li>Chaudière biomasse automatique (pellets/plaquettes locales)</li>
            <li>Pilotage intelligent : géothermie en priorité, biomasse en appoint</li>
        </ul>
        <img src="schema.png" alt="Schéma de fonctionnement Géothermie Biomasse">
    </section>

    <section id="avantages">
        <h2>Les Avantages</h2>
        <ul>
            <li>Économies sur votre facture</li>
            <li>Réduction des gaz à effets de serre</li>
            <li>Biomasse locale = circuit court & emplois locaux</li>
            <li>Indépendance totale aux énergies fossiles</li>
            <li>Retour sur investissement 5 à 8 ans</li>
        </ul>
    </section>

    <section id="fonctionnement">
        <h2>Comment ça marche ?</h2>
        <p>Le chauffage final à haute température nécessaire pour l'industrie est ensuite assuré par la chaudière biomasse.</p>
            </p>Le Rôle : La chaudière reçoit l'eau déjà chauffée à 60°.</p>
            </p>L'Action : Elle utilise exclusivement du bois-énergie (plaquettes ou granulés) provenant des forêts et des filières gérées localement dans l'Oise.</p>
            </p>Le Bénéfice : Le gaz fossile (méthane) est totalement substitué par cette bioénergie locale.</p>
            </p>Le CO2 émis est compensé par la croissance des arbres, rendant le cycle carbone neutre.</p>
        
        
        <img src="flyer.png" alt="Schéma de fonctionnement Géothermie Biomasse">
    </section>

    <section id="contact">
        <h2>Contactez-nous</h2>
        <p>Étude gratuite et devis sous 48h</p>
        <p>contact@lespepitesdebeauvais.fr<br>
           06 12 34 56 78<br>
           Beauvais & toute la région Hauts-de-France</p>
    </section>

    <footer>
        <img src="logo.png" alt="Logo" class="logo-footer">
        <p>© 2025 Les Pépites de Beauvais – Bio-énergie & Innovation</p>
    </footer>

</body>
</html>"""

# Création du fichier index.html sur ton bureau (ou dans le dossier où tu lances le script)
with open("index.html", "w", encoding="utf-8") as fichier:
    fichier.write(code_html)

print("Ton site est prêt !")
print("Le fichier 'index.html' a été créé ici :")
import os

print(os.path.abspath("index.html"))
print("\nDouble-clique dessus pour le voir dans ton navigateur")
