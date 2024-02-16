from flask import Flask
#from src.logger.logs import logging
from src.logger import logging

app = Flask(__name__)

@app.route('/', methods=['GET','POST'])
def index():
    logging.info("we are testing ourlogging module")
    return " success"

if __name__ =='__main__':
    app.run(debug=True)  #500