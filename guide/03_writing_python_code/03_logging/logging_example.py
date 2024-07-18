
import logging

# Create a custom logger
logger = logging.getLogger(__name__)

# Create handlers
c_handler = logging.StreamHandler()
f_handler = logging.FileHandler('file.log')
c_handler.setLevel(logging.WARNING)
f_handler.setLevel(logging.ERROR)

# Create formatters and add it to handlers
c_format = logging.Formatter('%(name)s - %(levelname)s - %(message)s')
f_format = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
c_handler.setFormatter(c_format)
f_handler.setFormatter(f_format)

# Add handlers to the logger
logger.addHandler(c_handler)
logger.addHandler(f_handler)

# Log that the test has started
logger.warning('This test has started...')

# Log the results of the first test
if 100 / 10 == 10:
    logger.warning('First test passed...')
else:
    logger.error('First test failed...')
   
# Log the results of the second test 
if 100 / 10 == 2:
    logger.warning('Second test passed...')
else:
    logger.error('Second test failed...')

# Log that the test has ended
logger.warning('This test has completed..')
