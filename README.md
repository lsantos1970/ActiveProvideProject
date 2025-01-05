AbstractFactoryProject/
│
├── app/                     # Código do servidor REST
│   ├── routes.py            # Rotas do Flask
│   ├── adapter.py           # Implementação do Adapter
│   └── factory_integration.py # Integração com o Abstract Factory
│
├── abstract_factory/        # Código do Abstract Factory
│   ├── scenario_factory.py
│   ├── medical_factory.py
│   ├── industrial_factory.py
│   ├── medical_environment.py
│   ├── industrial_environment.py
│   ├── lead_apron.py
│   └── protective_suit.py
│
├── templates/               # Templates HTML (se necessários)
│   └── config.html
│
├── requirements.txt         # Dependências do projeto
├── server.py                # Ponto de entrada do Flask
└── README.md                # Documentação básica

