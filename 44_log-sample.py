import logging
import employee

logger = logging.getLogger(__name__)

logging.basicConfig(filename='sample.log',
                    level=logging.INFO,
                    format='%(asctime)s - %(name)s- %(message)s')

def add(x,y):
    """add function"""
    return x+y

def subtract(x,y):
    """subtract function"""
    return x-y

def multiply(x,y):
    """multiply function"""
    return x*y

def divide(x,y):
    """divide function"""
    return x/y


logging.info('Addition of 3 and 4 gives us: {}'.format(add(3,4)))
logging.info('Subtraction of 3 and 4 gives us: {}'.format(subtract(3,4)))
logging.info('Multiplication of 3 and 4 gives us: {}'.format(multiply(3,4)))
logging.info('Division of 3 and 4 gives us: {}'.format(divide(3,4)))