import logging
import logging.config
import yaml

with open('task5.yml', 'r') as f:
    config = yaml.safe_load(f.read())
    logging.config.dictConfig(config)

logger = logging.getLogger('sampleLogger')
logger.debug("This is a debug msg")
