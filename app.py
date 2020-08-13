from flask import Flask, render_template, request, send_file
import logging
import os
from helpers import generate_svg, generate_code39_pdf
app = Flask(__name__)
app.config['SECRET_KEY'] = '7d441f27d441f27567d441f2b6176a'

# define logger
logging.basicConfig(filename='app.log',
                    filemode='w',
                    format='%(name)s - %(levelname)s - %(asctime)s - %(message)s',
                    datefmt='%d-%b-%y %H:%M:%S',
                    level=logging.DEBUG)

# create generated_pdfs if not exists
try:
    os.mkdir('generated_pdfs')
except FileExistsError:
    pass


@app.route('/', methods=['GET'])
def index():
    try:
        return render_template('generate_code39.html')
    except Exception as err:
        logging.error(err)
        return str(err)


@app.route('/', methods=['POST'])
def generate_pdf():
    try:
        text = request.form['text']
        logging.info(text)
        generate_svg(text)
        filename = generate_code39_pdf()
        return send_file('generated_pdfs/'+filename+'.pdf', attachment_filename=filename+'.pdf')
    except Exception as err:
        logging.error(err)
        return str(err)


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=False)
