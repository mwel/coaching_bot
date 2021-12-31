import logging

# Enable logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.DEBUG #.DEBUG OR .INFO
    # change logger config to print sent messages to terminal
)

logger = logging.getLogger(__name__)

