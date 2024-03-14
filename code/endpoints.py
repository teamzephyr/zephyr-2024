from main import app
from markupsafe import escape
from flask import Flask, jsonify, request, abort

import request_esg
import response_esg

# good for testing the endpoint is alive
@app.route('/')
def index():
    return escape("hello this is the home index")


#      summary: Upload ESG for given entity and retrieve all ESG benchmark document
@app.route('/api/esg/benchmark/upload/<entityName>', methods=['POST'])
def esgEntityName(entityName):

    file = upload_file(request, entityName)
    
    if isError(file):
        return jsonify(file), 400
    
    myRequestObj = request_esg.UploadRequest(file, entityName)
    
    # do logic with file in request

    return jsonify({'response': 'did not fail'}), 200


#    summary: Fetch specific ESG indicator for given entity
@app.route('/api/esg/benchmark/upload/<entityName>/<esgType>/<esgIndicator>', methods=['POST'])
def esgUpload(entityName, esgType, esgIndicator):

    file = upload_file(request, entityName)

    if isError(file):
        return jsonify(file), 400

    myRequestObj = request_esg.UploadRequestType(file, entityName, esgType, esgIndicator)

    # do logic with file in request

    return jsonify({'response': 'did not fail'}), 200


#   summary: Find status of the benchakring service
@app.route('/api/esg/benchmark/keepalive', methods=['GET'])
def keepAlive():
    return "Hello keepalive"


#   summary: get PDF URL for given entity name
@app.route('/esg/benchmark/pdf-report/<entityName>', methods=['POST'])
def pdfReport(entityName):

    file = upload_file(request, entityName)

    if isError(file):
        return jsonify(file), 400
    
    myRequestObj = request_esg.PDFReportRequest(file, entityName)

    # do logic with file in request

    
    return f"<p>Hello{entityName}</p>"


is_pdf = lambda filename: '.' in filename and filename.rsplit('.', 1)[1].lower() in 'pdf'


# these are utils that help the endpoints work
def upload_file(request, entityName):
    
    if 'documentUpload' not in request.files:
        return {'error': 'No file in request'}

    file = request.files['documentUpload']

    if not is_pdf(file.filename):
        return {'error': 'file uploaded is not a PDF'}

    if file.filename == '':
        return {'error': 'No selected file'}
    

    file_path = "code/uploads/"
    fullpath = f'{file_path}{entityName}.pdf'
    easyPrint(fullpath)
    file.save(fullpath)

    return file


def isError(file):
    try:
        if 'error' in file:
            return True
        else:
            return False
    except Exception:
        easyPrint("")
        return False
    
def easyPrint(s):
    print("\n*****************")
    print(s)
    print("*****************\n")
