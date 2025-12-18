import yaml
import os

def load_yaml(file_path):
    with open(file_path, encoding="utf-8") as f:
        return yaml.safe_load(f)

def get_config():
    base_dir = os.path.dirname(os.path.dirname(__file__))
    config_path = os.path.join(base_dir, "config", "config.yaml")
    config = load_yaml(config_path)
    env = config["env"]
    return config[env]

def load_test_data(file_name, key):
    base_dir = os.path.dirname(os.path.dirname(__file__))
    path = os.path.join(base_dir, "data", file_name)
    data = load_yaml(path)
    return list(data.get(key).values())
