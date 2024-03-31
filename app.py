from flask import Flask, render_template, request, jsonify
import os

app = Flask(__name__)

class FaitsUtilisateur:
    def __init__(self):
        self.faits = []

    def ajouter_fait(self, fait):
        self.faits.append(fait)

    def supprimer_fait(self, fait):
        self.faits.remove(fait)

    def vider(self):
        self.faits = []

class SystemeExpert:
    def __init__(self):
        self.base_de_regles = []
        self.faits_utilisateur = FaitsUtilisateur()

    def charger_regle_base(self, file_path):
        with open(file_path, 'r') as f:
            for line in f:
                regle = line.strip().split(":")
                conditions = regle[0].split(",")
                organe = regle[1]
                new_regle = Regle(conditions, organe)
                self.base_de_regles.append(new_regle)

    def ajouter_fait_utilisateur(self, fait):
        self.faits_utilisateur.ajouter_fait(fait)

    def vider_faits_utilisateur(self):
        self.faits_utilisateur.vider()

    def raisonner(self):
        organes_en_panne = set()
        for regle in self.base_de_regles:
            if regle.satisfait(self.faits_utilisateur.faits):
                organes_en_panne.add(regle.organe_en_panne)
        return organes_en_panne

class Regle:
    def __init__(self, conditions, organe_en_panne):
        self.conditions = conditions
        self.organe_en_panne = organe_en_panne

    def satisfait(self, faits_utilisateur):
        return any(set(self.conditions).issubset(set(fait)) for fait in faits_utilisateur)

systeme_expert = SystemeExpert()

@app.route('/')
def index():
    systeme_expert.charger_regle_base("base.txt")
    return render_template('index.html', base_de_regles=systeme_expert.base_de_regles)

@app.route('/diagnose', methods=['POST'])
def diagnose():
    data = request.get_json()  # Retrieve JSON data from request
    selected_indices = data.get('selected_indices')  # Get selected indices from JSON data

    if not selected_indices:
        return jsonify({'status': 'error', 'message': 'Please select at least one symptom.'})

    faits_utilisateur = [systeme_expert.base_de_regles[int(index)].conditions for index in selected_indices]

    for fait_utilisateur in faits_utilisateur:
        systeme_expert.ajouter_fait_utilisateur(fait_utilisateur)

    organes_en_panne = systeme_expert.raisonner()

    if organes_en_panne:
        result_text = f"The potentially faulty components are: {', '.join(organes_en_panne)}"
    else:
        result_text = "No faulty component detected."

    systeme_expert.vider_faits_utilisateur()

    return jsonify({'status': 'success', 'message': result_text})


if __name__ == '__main__':
    app.run(debug=True)
