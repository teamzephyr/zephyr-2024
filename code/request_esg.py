
from flask import Flask, request, abort


class UploadRequest:
    entityName = ''
    documentUpload = ''
    
    def __init__(self, json, param):
        self.entityName = param
        self.documentUpload= json['documentUpload']
    

class UploadRequestType:
    entityName = ''
    esgType = ''
    esgIndicator = ''

    documentUpload = ''
    
    def __init__(self, json, entityName, esgType, esgIndicator):
        self.entityName = entityName
        self.entityName = esgType
        self.entityName = esgIndicator

        self.documentUpload= json['documentUpload']

class PDFReportRequest:
    entityName = ''
    documentUpload = ''
    
    def __init__(self, json, entityName):
        self.entityName = entityName
        self.documentUpload= json['documentUpload']