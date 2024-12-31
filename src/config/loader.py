import os
import re
import yaml


class ConfigLoader:
    _instance = None

    def __new__(cls, config_files=None):
        if cls._instance is None:
            cls._instance = super(ConfigLoader, cls).__new__(cls)
            cls._instance._init(config_files)
        return cls._instance

    def _init(self, config_files=None):
        # Default file paths, puoi aggiungere il percorso dei file YAML aggiuntivi
        if config_files is None:
            config_files = ["src/config/resources/config.yml"]

        self.config_files = config_files
        self.config = self._load_config()

    def _load_config(self):
        env = os.getenv("APP_ENV", "default")
        config_data = {}

        # Carica tutte le configurazioni da ciascun file
        for config_file in self.config_files:
            with open(config_file, "r") as file:
                content = file.read()
            content = self.format_custom_placeholders(content)
            data = yaml.safe_load(content)

            # Unisci le configurazioni
            config_data.update(data.get(env, data.get("default", {})))

        return config_data

    def format_custom_placeholders(self, content):
        def replace_with_env(match):
            env_var = match.group(1)
            return os.getenv(env_var, match.group(0))

        formatted_content = re.sub(r"\$\{([^}]+)\}", replace_with_env, content)
        return formatted_content

    def get(self, key, default=None):
        return self.config.get(key, default)
