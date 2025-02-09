from flask import Flask, jsonify, request, render_template
from app.config_manager import ConfigManager
from abstract_factory.scenario_factory import ScenarioCreator
from strategy.analysis_context import AnalysisContext
from strategy.medical_strategy import MedicalAnalysisStrategy
from strategy.industrial_strategy import IndustrialAnalysisStrategy

# Inicialização da aplicação Flask
app = Flask(__name__)

# Endpoint para obter a página de configuração
@app.route('/config_url', methods=['GET'])
def get_config():
    """
    Renderiza a página HTML de configuração da atividade.
    """
    return render_template('config.html')

# Endpoint para obter os parâmetros JSON da configuração
@app.route('/json_params_url', methods=['GET'])
def get_params():
    """
    Retorna uma lista de parâmetros esperados para configurar o cenário.
    """
    return jsonify([
        {"name": "scenario_type", "type": "string", "description": "Tipo de cenário (médico ou industrial)"},
        {"name": "radiation_threshold", "type": "integer", "description": "Limite seguro de radiação (μSv)"},
        {"name": "max_time", "type": "integer", "description": "Tempo máximo seguro (segundos)"},
        {"name": "suggested_distance", "type": "float", "description": "Distância segura (metros)"}
    ])

# Endpoint para criar cenários dinamicamente
@app.route('/create_scenario', methods=['POST'])
def create_scenario():
    """
    Processa os dados recebidos para criar um cenário dinâmico com base no tipo especificado.
    
    Returns:
        JSON contendo o ambiente e o equipamento criados.
        Retorna um erro 400 se o tipo de cenário for inválido.
    """
    data = request.json
    scenario_type = data.get("scenario_type")

    try:
        # Usa o criador de cenários dinâmicos (Strategy Pattern + Abstract Factory)
        creator = ScenarioCreator(scenario_type)
        result = creator.create_scenario()
    except ValueError as e:
        # Erro no tipo de cenário fornecido
        return jsonify({"error": str(e)}), 400

    return jsonify(result)

# Endpoint para análise médica usando o padrão Strategy
@app.route('/analyze/medical', methods=['POST'])
def analyze_medical():
    """
    Processa os dados enviados e executa uma análise usando a estratégia médica.
    
    Returns:
        JSON com os resultados da análise.
    """
    data = request.json.get('data', [])
    context = AnalysisContext()
    context.set_strategy(MedicalAnalysisStrategy())  # Configura a estratégia médica
    result = context.execute_analysis(data)
    return jsonify(result)

# Endpoint para análise industrial usando o padrão Strategy
@app.route('/analyze/industrial', methods=['POST'])
def analyze_industrial():
    """
    Processa os dados enviados e executa uma análise usando a estratégia industrial.
    
    Returns:
        JSON com os resultados da análise.
    """
    data = request.json.get('data', [])
    context = AnalysisContext()
    context.set_strategy(IndustrialAnalysisStrategy())  # Configura a estratégia industrial
    result = context.execute_analysis(data)
    return jsonify(result)

# Endpoint para simular o deployment de utilizadores
@app.route('/user_url', methods=['GET'])
def deploy():
    """
    Retorna a URL de atividade de um utilizador específico.
    O ID da instância deve ser fornecido como parâmetro na URL.
    """
    instance_id = request.args.get('instanceID', 'undefined')
    return jsonify({"activity_url": f"https://webservice-ap-radiation.onrender.com/user_url?instanceID={instance_id}"})

# Endpoint para obter análises quantitativas e qualitativas
@app.route('/analytics_url', methods=['POST'])
def get_analytics():
    """
    Retorna um conjunto de dados de análises quantitativas e qualitativas simuladas.
    """
    return jsonify([
        {
            "inveniraStdID": 1001,
            "quantAnalytics": [{"name": "Acedeu à atividade", "value": True}],
            "qualAnalytics": [{"Student activity profile": "https://your-app.onrender.com/?APAnID=11111111"}]
        }
    ])

# Endpoint para listar parâmetros de análises
@app.route('/analytics_list_url', methods=['GET'])
def analytics_list():
    """
    Retorna uma lista de descrições de métricas e parâmetros analíticos.
    """
    return jsonify([
        {"name": "suggested_time", "type": "integer", "description": "Tempo sugerido pelo técnico (segundos)"},
        {"name": "suggested_distance", "type": "float", "description": "Distância segura (metros)"}
    ])
