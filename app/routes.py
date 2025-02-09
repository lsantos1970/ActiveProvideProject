from flask import Flask, jsonify, request, render_template
from app.config_manager import ConfigManager
from abstract_factory.scenario_factory import ScenarioCreator
from strategy.analysis_context import AnalysisContext
from strategy.medical_strategy import MedicalAnalysisStrategy
from strategy.industrial_strategy import IndustrialAnalysisStrategy

app = Flask(__name__)

@app.route('/config_url', methods=['GET'])
def get_config():
    return render_template('config.html')

@app.route('/json_params_url', methods=['GET'])
def get_params():
    return jsonify([
        {"name": "scenario_type", "type": "string", "description": "Tipo de cenário (médico ou industrial)"},
        {"name": "radiation_threshold", "type": "integer", "description": "Limite seguro de radiação (μSv)"},
        {"name": "max_time", "type": "integer", "description": "Tempo máximo seguro (segundos)"},
        {"name": "suggested_distance", "type": "float", "description": "Distância segura (metros)"}
    ])

@app.route('/create_scenario', methods=['POST'])
def create_scenario():
    data = request.json
    scenario_type = data.get("scenario_type")

    # Criar o cenário dinamicamente
    try:
        creator = ScenarioCreator(scenario_type)
        result = creator.create_scenario()
    except ValueError as e:
        return jsonify({"error": str(e)}), 400

    return jsonify(result)

# Endpoints de análise com Strategy
@app.route('/analyze/medical', methods=['POST'])
def analyze_medical():
    data = request.json.get('data', [])
    context = AnalysisContext()
    context.set_strategy(MedicalAnalysisStrategy())
    result = context.execute_analysis(data)
    return jsonify(result)

@app.route('/analyze/industrial', methods=['POST'])
def analyze_industrial():
    data = request.json.get('data', [])
    context = AnalysisContext()
    context.set_strategy(IndustrialAnalysisStrategy())
    result = context.execute_analysis(data)
    return jsonify(result)
@app.route('/user_url', methods=['GET'])
def deploy():
    instance_id = request.args.get('instanceID', 'undefined')
    return jsonify({"activity_url": f"https://webservice-ap-radiation.onrender.com/user_url?instanceID={instance_id}"})

@app.route('/analytics_url', methods=['POST'])
def get_analytics():
    return jsonify([
        {
            "inveniraStdID": 1001,
            "quantAnalytics": [{"name": "Acedeu à atividade", "value": True}],
            "qualAnalytics": [{"Student activity profile": "https://your-app.onrender.com/?APAnID=11111111"}]
        }
    ])

@app.route('/analytics_list_url', methods=['GET'])
def analytics_list():
    return jsonify([
        {"name": "suggested_time", "type": "integer", "description": "Tempo sugerido pelo técnico (segundos)"},
        {"name": "suggested_distance", "type": "float", "description": "Distância segura (metros)"}
    ])
