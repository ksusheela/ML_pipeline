from flask import Flask
import os, sys
#from src.logger.logs import logging
from src.logger import logging
from src.exception import CustomException

app = Flask(__name__)

@app.route('/', methods=['GET','POST'])
def index():

    try:
        raise Exception("we are testing our custom exception file")
    except Exception as e:
        test = CustomException(e, sys)

        logging.info(test.error_message )
        
        logging.info("we are testing ourlogging module")
        return " success"

if __name__ =='__main__':
    app.run(debug=True)  #500