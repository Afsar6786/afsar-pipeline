"""
Example: Logging messages using log_utils
"""

from afsar_pipeline import log_utils

logger = log_utils.get_logger("pipeline")

logger.info("Starting the pipeline...")
logger.warning("This is just a test warning.")
logger.error("An error occurred in the pipeline.")