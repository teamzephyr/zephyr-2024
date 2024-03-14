
from contextlib import nullcontext


class UploadRequest:
    entityName = ''
    documentUpload = nullcontext
    
    def __init__(self, file, param):
        self.entityName = param
        self.documentUpload= file
    

class UploadRequestType:
    entityName = ''
    esgType = ''
    esgIndicator = ''

    documentUpload = nullcontext
    
    def __init__(self, file, entityName, esgType, esgIndicator):
        self.entityName = entityName
        self.entityName = esgType
        self.entityName = esgIndicator

        self.documentUpload= file

class PDFReportRequest:
    entityName = ''
    documentUpload = nullcontext
    
    def __init__(self, file, entityName):
        self.entityName = entityName
        self.documentUpload= file