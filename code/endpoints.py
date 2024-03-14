from main import app
from markupsafe import escape
from flask import Flask, request, abort

import request_esg

# not important
@app.route('/')
def index():
    return "Home page"

#      summary: Upload ESG for given entity and retrieve all ESG benchmark document
@app.route('/esg/benchmark/upload/<entityName>', methods=['POST'])
def esgEntityName(entityName):
    myRequestObj = request_esg.UploadRequest(request.json, entityName)
    print("*********")
    print(myRequestObj.entityName)
    print(myRequestObj.documentUpload)
    print("*********")

    return f"<p>Hello{entityName}</p>"

#    summary: Fetch specific ESG indicator for given entity
@app.route('/esg/benchmark/upload/<entityName>/<esgType>/<esgIndicator>', methods=['POST'])
def esgUpload(entityName, esgType, esgIndicator):
    myRequestObj = request_esg.UploadRequestType(request.json, entityName, esgType, esgIndicator)

    return f"<p>Hello /esg/benchmark/upload/{entityName}/{esgType}/{esgIndicator}</p>"

#   summary: Find status of the benchakring service
@app.route('/esg/benchmark/keepalive', methods=['GET'])
def keepAlive():
    return "<p>Hello keepalive</p>"

#   summary: get PDF URL for given entity name
@app.route('/esg/benchmark/pdf-report/<entityName>', methods=['POST'])
def pdfReport(entityName):
    myRequestObj = request_esg.PDFReportRequest(request.json, entityName)
    return f"<p>Hello{entityName}</p>"
