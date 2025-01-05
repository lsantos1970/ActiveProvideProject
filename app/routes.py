from flask import Flask, request, jsonify
from app.adapter import RESTToFactoryAdapter
from abstract_factory.medical_factory import MedicalFactory
from abstract_factory.industrial_factory import IndustrialFactory

app = Flask(__name__)

# Endpoint para criar cenários com o Adapter
@app.route('/create_scenario', methods=['POST'])
def create_scenario():
    data = request.json
    scenario_type = data.get("scenario_type")

    if scenario_type == "medical":
        factory = MedicalFactory()
    elif scenario_type == "industrial":
        factory = IndustrialFactory()
    else:
        return jsonify({"error": "Tipo de cenário inválido"}), 400

    # Usa o Adapter para processar a solicitação
    adapter = RESTToFactoryAdapter(factory)
    result = adapter.process_request(data)

    return jsonify(result)
