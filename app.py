from flask import Flask, jsonify, request, send_file
from models import db, Consulta, Parente, Lembrete
import json, os, requests
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

# Criação inicial do BD com dados de exemplo
with app.app_context():
    db.create_all()
    if not Consulta.query.first():
        if os.path.exists("dados_iniciais.json"):
            with open("dados_iniciais.json", encoding="utf-8") as f:
                dados = json.load(f)
                for c in dados.get("consultas", []):
                    db.session.add(Consulta(**c))
                for p in dados.get("parentes", []):
                    nome, telefone, parentesco, email = p
                    db.session.add(Parente(nome=nome, telefone=telefone, parentesco=parentesco, email=email))
                for l in dados.get("lembretes", []):
                    db.session.add(Lembrete(**l))
                db.session.commit()

# ROTAS CRUD
@app.route("/consultas", methods=["GET"])
def listar_consultas():
    return jsonify([c.to_dict() for c in Consulta.query.all()])

@app.route("/consultas", methods=["POST"])
def criar_consulta():
    data = request.json
    consulta = Consulta(**data, data_cadastro=datetime.now().strftime("%d/%m/%Y %H:%M"))
    db.session.add(consulta)
    db.session.commit()
    return jsonify(consulta.to_dict()), 201

@app.route("/consultas/<int:id>", methods=["PUT"])
def editar_consulta(id):
    consulta = Consulta.query.get_or_404(id)
    data = request.json
    for k,v in data.items():
        setattr(consulta, k, v)
    db.session.commit()
    return jsonify(consulta.to_dict())

@app.route("/consultas/<int:id>", methods=["DELETE"])
def deletar_consulta(id):
    consulta = Consulta.query.get_or_404(id)
    db.session.delete(consulta)
    db.session.commit()
    return jsonify({"status":"ok"})

# ROTAS PARENTES E LEMBRETES
@app.route("/parentes", methods=["GET"])
def listar_parentes():
    return jsonify([p.to_dict() for p in Parente.query.all()])

@app.route("/lembretes", methods=["GET"])
def listar_lembretes():
    return jsonify([l.to_dict() for l in Lembrete.query.all()])

# EXPORTAR PARA JSON
@app.route("/exportar", methods=["GET"])
def exportar():
    dados = {
        "consultas": [c.to_dict() for c in Consulta.query.all()],
        "parentes": [p.to_dict() for p in Parente.query.all()],
        "lembretes": [l.to_dict() for l in Lembrete.query.all()]
    }
    fname = f"export_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
    with open(fname, "w", encoding="utf-8") as f:
        json.dump(dados, f, ensure_ascii=False, indent=2)
    return send_file(fname, mimetype="application/json", as_attachment=True)

# API EXTERNA (exemplo: importar médicos fictícios)
@app.route("/importar_medicos", methods=["POST"])
def importar_medicos():
    r = requests.get("https://jsonplaceholder.typicode.com/users?_limit=3")
    medicos = r.json()
    resultado = []
    for m in medicos:
        consulta = Consulta(
            paciente=m["name"],
            data="01/12/2025",
            medico=m["username"],
            especialidade="Clínico Geral",
            link="https://meet.google.com/xyz",
            horario="09:00",
            local="HCFMUSP",
            observacoes="Consulta criada via API externa",
            data_cadastro=datetime.now().strftime("%d/%m/%Y %H:%M")
        )
        db.session.add(consulta)
        resultado.append(m["name"])
    db.session.commit()
    return jsonify({"importados": resultado})

# FRONTEND
@app.route("/")
def index():
    return send_file("static/index.html")

if __name__ == "__main__":
    app.run(debug=True)
