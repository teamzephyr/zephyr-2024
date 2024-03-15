
class UploadRequest:
    entityName = ''
    documentUpload = None
    
    def __init__(self, file, param):
        self.entityName = param
        self.documentUpload= file
    

class UploadRequestType:
    entityName = ''
    esgType = ''
    esgIndicator = ''

    documentUpload = None
    
    def __init__(self, file, entityName, esgType, esgIndicator):
        self.entityName = entityName
        self.entityName = esgType
        self.entityName = esgIndicator

        self.documentUpload= file

class PDFReportRequest:
    entityName = ''
    documentUpload = None
    
    def __init__(self, file, entityName):
        self.entityName = entityName
        self.documentUpload= file