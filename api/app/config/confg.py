import yaml

class Config:
    def __init__(self):
        self.config = self.load_config()

    def __getattr__(self, name):
        return self.config.get(name)

    @staticmethod
    def load_config():
        with open('app/config/config.yml', 'r') as file:
            config = yaml.safe_load(file)
        return config

config = Config()