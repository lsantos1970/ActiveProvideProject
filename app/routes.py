from flask import Flask, jsonify, request
from strategy.analysis_context import AnalysisContext
from strategy.medical_strategy import MedicalAnalysisStrategy
from strategy.industrial_strategy import IndustrialAnalysisStrategy
from abstract_factory.medical_factory import MedicalFactory
from abstract_factory.industrial_factory import IndustrialFactory
from adapters.adapter import RESTToFactoryAdapter

app = Flask(__name__)

# 1. Endpoint para análise médica
@app.route('/analyze/medical', methods=['POST'])
def analyze_medical():
    data = request.json.get('data', [])
    context = AnalysisContext()
    context.set_strategy(MedicalAnalysisStrategy())
    result = context.execute_analysis(data)
    return jsonify(result)

# 2. Endpoint para análise industrial
@app.route('/analyze/industrial', methods=['POST'])
def analyze_industrial():
    data = request.json.get('data', [])
    context = AnalysisContext()
    context.set_strategy(IndustrialAnalysisStrategy())
    result = context.execute_analysis(data)
    return jsonify(result)

# 3. Endpoint para criar cenários com o Adapter
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

# 4. Endpoint para a página de configuração
@app.route('/config_url', methods=['GET'])
def get_config():
    return render_template('config.html')

# 5. Endpoint para lista de parâmetros configuráveis
@app.route('/json_params_url', methods=['GET'])
def get_params():
    return jsonify([
        {"name": "scenario_type", "type": "string", "description": "Tipo de cenário (médico ou industrial)"},
        {"name": "radiation_threshold", "type": "integer", "description": "Limite seguro de radiação (μSv)"},
        {"name": "max_time", "type": "integer", "description": "Tempo máximo seguro (segundos)"},
        {"name": "suggested_distance", "type": "float", "description": "Distância segura (metros)"}
    ])

# 6. Endpoint para deploy da atividade
@app.route('/user_url', methods=['GET'])
def deploy():
    instance_id = request.args.get('instanceID', 'undefined')
    return jsonify({"activity_url": f"https://webservice-ap-radiation.onrender.com/user_url?instanceID={instance_id}"})

# 7. Endpoint para dados analíticos de uma instância
@app.route('/analytics_url', methods=['POST'])
def get_analytics():
    return jsonify([
        {
            "inveniraStdID": 1001,
            "quantAnalytics": [
                {"name": "Acedeu à atividade", "value": True},
                {"name": "Download documento 1", "value": False},
                {"name": "Evolução pela atividade (%)", "value": "50.0"}
            ],
            "qualAnalytics": [
                {"Student activity profile": "https://your-app.onrender.com/?APAnID=11111111"},
                {"Activity Heat Map": "https://your-app.onrender.com/?APAnID=21111111"}
            ]
        }
    ])


# 8. Endpoint para lista de analytics disponíveis
@app.route('/analytics_list_url', methods=['GET'])
def analytics_list():
    return jsonify([
        {"name": "suggested_time", "type": "integer", "description": "Tempo sugerido pelo técnico (segundos)"},
        {"name": "suggested_distance", "type": "float", "description": "Distância sugerida pelo técnico (metros)"},
        {"name": "chosen_epi", "type": "string", "description": "Equipamento de proteção individual escolhido"}
    ])

if __name__ == '__main__':
    app.run(debug=True)
