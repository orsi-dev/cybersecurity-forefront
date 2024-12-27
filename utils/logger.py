import logging
import logging.config
import yaml
from typing import Optional, Dict


class LoggerConfig:
    def __init__(self, config_path: Optional[str] = None, logger_config: Optional[Dict] = None):
        """
        Inizializza la configurazione del logger.

        Args:
            config_path (str, opzionale): Percorso al file di configurazione YAML.
            logger_config (Dict, opzionale): Dizionario per configurare il logger.
        """
        self.config_path = config_path
        self.logger_config = logger_config

    def setup_logger(self) -> None:
        """
        Configura il logger utilizzando un file YAML o un dizionario di configurazione.
        """
        if self.config_path:
            with open(self.config_path, "r") as file:
                config = yaml.safe_load(file)
                logging.config.dictConfig(config)
        elif self.logger_config:
            logging.config.dictConfig(self.logger_config)
        else:
            logging.basicConfig(level=logging.INFO)

        logger = logging.getLogger(__name__)

        logger.info("Logger configuration completed.")

    @staticmethod
    def get_logger(name: str) -> logging.Logger:
        """
        Ritorna un logger con il nome specificato.

        Args:
            name (str): Nome del logger.

        Returns:
            logging.Logger: Istanza del logger.
        """
        return logging.getLogger(name)
