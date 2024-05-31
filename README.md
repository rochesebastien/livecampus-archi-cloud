
# Livecampus - Architecture & Cloud


# API : FastAPI

## Mise en place & Installation : 

- Clone du repo et création de l'environnement virtuel :
```bash
git clone https://github.com/rochesebastien/livecampus-archi-cloud.git
cd livecampus-archi-cloud
cd api
python3 -m venv venv
```

- Activation de l'environnement virtuel :
```bash
source venv/bin/activate #Linux/Unix
venv/Scripts/activate #Windows
```

- Installation des dépendances : 
```bash
pip install -r requirements.txt
```

- Lancement de l'API
```bash
uvicorn app.main:app --reload --port 8000 --host 0.0.0.0
```

## Test Unitaire : 
```bash
python -m unittest discover -s /tests -p 'test_*.py’
```

