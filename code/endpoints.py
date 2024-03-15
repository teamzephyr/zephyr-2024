from dataclasses import asdict
from main import app
from markupsafe import escape
from flask import Flask, jsonify, request, abort


import request_esg
import response_esg
import mapper
import blobUpload

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
    
    responseUpload = response_esg.UploadRequest()
    responseUpload = mapper.mapUploadRequest(None, entityName)

    blobUpload.upload_blob(file)

    #get response logic
    #TODO

    
    # Response should use class:
    #   response_esg.UploadRequest 
    return jsonify(asdict(responseUpload)), 200


#    summary: Fetch specific ESG indicator for given entity
@app.route('/api/esg/benchmark/upload/<entityName>/<esgType>/<esgIndicator>', methods=['POST'])
def esgUpload(entityName, esgType, esgIndicator):

    file = upload_file(request, entityName)

    if isError(file):
        return jsonify(file), 400

    myRequestObj = request_esg.UploadRequestType(file, entityName, esgType, esgIndicator)

    responseUploadType = response_esg.UploadRequestType()
    responseUploadType = mapper.mapUploadRequestType(None, entityName)

    blobUpload.upload_blob(file)

    #get response logic
    #TODO

    # Response should use class:  
    #   response_esg.UploadRequestType
    return jsonify(responseUploadType), 200


#   summary: Find status of the benchakring service
@app.route('/api/esg/benchmark/keepalive', methods=['GET'])
def keepAlive():

    responseKeepAlive = response_esg.KeepAliveRepsonse()
    responseKeepAlive.status = 'UP'
    responseKeepAlive.message = 'the service is up'

    # why does this end point exist???


    # Response should use class: 
    #   response_esg.keepAliveRepsonse
    return jsonify(asdict(responseKeepAlive)), 200


#   summary: get PDF URL for given entity name
@app.route('/api/esg/benchmark/pdf-report/<entityName>', methods=['POST'])
def pdfReport(entityName):

    file = upload_file(request, entityName)

    if isError(file):
        return jsonify(file), 400
    
    myRequestObj = request_esg.PDFReportRequest(file, entityName)
    response = response_esg.PDFReportRepsonse()
    response.pdfUrlPath = ""

    response.pdfUrlPath = blobUpload.findPath(entityName)
    
    # do logic with file in request and fill response
    #TODO

    # Response should use class: 
    #   response_esg.pdfReportRepsonse    
    return jsonify(asdict(response)), 200


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
    # file.save(fullpath)

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
