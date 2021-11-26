from search_term_data.BackgroundProcess import BackgroundProcess
import logging
import logging.config
import yaml


def main():
    with open('./config/logging.yaml', 'r') as f:
        config = yaml.safe_load(f.read())
        logging.config.dictConfig(config)

    logger = logging.getLogger(__name__)
    logger.info('Starting the background process')
    background_process = BackgroundProcess()
    background_process.start_daemon()


if __name__ == '__main__':
    main()
