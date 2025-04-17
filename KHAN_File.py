from fpdf import FPDF

class RapportKHAN(FPDF):
    def header(self):
        self.set_font("Arial", 'B', 14)
        self.cell(0, 10, 'CLASSIFICATION : SECRET DEFENSE', 0, 1, 'C')
        self.ln(5)

pdf = RapportKHAN()
pdf.add_page()

# TITRE
pdf.set_font("Arial", 'B', 20)
pdf.cell(0, 10, "DOSSIER CONFIDENTIEL", ln=True, align='C')
pdf.ln(10)

# INFOS DE BASE
pdf.set_font("Arial", 'B', 14)
pdf.cell(0, 10, "Nom de Code : KHAN", ln=True)
pdf.cell(0, 10, "Véritable Identité : ███████████████████████████", ln=True)
pdf.cell(0, 10, "Statut : INCONNU", ln=True)
pdf.cell(0, 10, "Dernière Localisation : INCONNUE", ln=True)
pdf.ln(10)

# CORPS DU RAPPORT
pdf.set_font("Arial", '', 12)
texte = """
CLASSIFICATION : NIVEAU BLACK - ACCES ULTRA RESTREINT

Profil :
Individu opérant sous le pseudonyme "KHAN".
Expert en stratégie de guerre numérique.
Possède un réseau massif de comptes secondaires ("Ombres").
Référence directe au manga Solo Leveling.

Méthodes :
- Maîtrise avancée de la tactique militaire virtuelle.
- Utilisation d'investissements massifs en ressources.
- Domination totale de royaumes virtuels en solo.
- Aucune fuite d'information personnelle.

Hypothèses d'identité :
- Ancien militaire spécialisé en cyber-guerre.
- Homme d'affaires influent opérant dans l'ombre.
- Agent gouvernemental ou freelance à haut risque.

Conclusion :
Sujet classé MENACE STRATEGIQUE DE PREMIER ORDRE.
Observation continue recommandée.
Aucune intervention sans autorisation spéciale.

Fin du Rapport.
"""

pdf.multi_cell(0, 8, texte)
pdf.ln(10)

# FOOTER
pdf.set_font("Arial", 'B', 12)
pdf.cell(0, 10, "SIGNATURE : ███████████████████", ln=True)

# Générer le fichier PDF
pdf.output("KHAN_RAPPORT.pdf")

print("RAPPORT PDF GENERE AVEC SUCCES.")

