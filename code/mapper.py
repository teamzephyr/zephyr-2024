from flask import jsonify, request, abort

import response_esg


def testData():
    return {
  "esgResponse": [
    {
      "entityName": "string",
      "benchmarkDetails": 
        {
          "question": "ESG Risk Rating for MSCI",
          "esgType": "ESGScore",
          "esgIndicators": "MSCISustainalytics",
          "primaryDetails": "",
          "secondaryDetails": "",
          "citationDetails": "string",
          "pageNumber": 0
        },
      "metrics": {
        "timeTaken": 0,
        "leveragedModel": "string",
		"f1Score": 0
      }
    }
  ]
}

def testData2():
    return {
  "esgResponse": [
    {
      "entityName": "string",
      "benchmarkDetails": [
        {
          "question": "ESG Risk Rating for MSCI",
          "esgType": "ESGScore",
          "esgIndicators": "MSCISustainalytics",
          "primaryDetails": "",
          "secondaryDetails": "",
          "citationDetails": "string",
          "pageNumber": 0
        },
        {
          "question": "what is net zero target",
          "esgType": "Environment",
          "esgIndicators": "NetZeroTarget",
          "primaryDetails": "",
          "secondaryDetails": "",
          "citationDetails": "string",
          "pageNumber": 0
        },
        {
          "question": "what is the interim emission reduction target",
          "esgType": "Environment",
          "esgIndicators": "InterimEmissionsReductionTarget",
          "primaryDetails": "",
          "secondaryDetails": "",
          "citationDetails": "string",
          "pageNumber": 0
        },
        {
          "question": "what is the Renewable Electricity Target",
          "esgType": "Environment",
          "esgIndicators": "RenewableElectricityTarget",
          "primaryDetails": "",
          "secondaryDetails": "",
          "citationDetails": "string",
          "pageNumber": 0
        },
        {
          "question": "what is the Circularity Stratergy & targets",
          "esgType": "Environment",
          "esgIndicators": "CircularityStratergy",
          "primaryDetails": "",
          "secondaryDetails": "",
          "citationDetails": "string",
          "pageNumber": 0
        },
        {
          "question": "what is the Diversity, Equity and Inclusion target",
          "esgType": "Social",
          "esgIndicators": "DE&ITarget",
          "primaryDetails": "",
          "secondaryDetails": "string",
          "citationDetails": "string",
          "pageNumber": 0
        },
        {
          "question": "what is the employee health and Safety audit target",
          "esgType": "Goverance",
          "esgIndicators": "HealthAndSafetyTarget",
          "primaryDetails": "",
          "secondaryDetails": "string",
          "citationDetails": "string",
          "pageNumber": 0
        },
		{
          "question": "what is supply audit target",
          "esgType": "Goverance",
          "esgIndicators": "SuppluAuditTarget",
          "primaryDetails": "",
          "secondaryDetails": "string",
          "citationDetails": "string",
          "pageNumber": 0
        },
        {
          "question": "what is the SBTi rating",
          "esgType": "Reporting",
          "esgIndicators": "SBTi",
          "primaryDetails": "",
          "secondaryDetails": "string",
          "citationDetails": "string",
          "pageNumber": 0
        },
        {
          "question": "what is the CDP rating",
          "esgType": "Reporting",
          "esgIndicators": "CDP",
          "primaryDetails": "",
          "secondaryDetails": "string",
          "citationDetails": "string",
          "pageNumber": 0
        },
        {
          "question": "what is the GRI rating",
          "esgType": "Reporting",
          "esgIndicators": "GRI",
          "primaryDetails": "",
          "secondaryDetails": "string",
          "citationDetails": "string",
          "pageNumber": 0
        },
        {
          "question": "what is the SASB rating",
          "esgType": "Reporting",
          "esgIndicators": "SASB",
          "primaryDetails": "",
          "secondaryDetails": "string",
          "citationDetails": "string",
          "pageNumber": 0
        },
        {
          "question": "what is the TCFD rating",
          "esgType": "Reporting",
          "esgIndicators": "TCFD",
          "primaryDetails": "",
          "secondaryDetails": "string",
          "citationDetails": "string",
          "pageNumber": 0
        },
        {
          "question": "is the entity focussing on ESG assurance",
          "esgType": "Reporting",
          "esgIndicators": "Assurance",
          "primaryDetails": "",
          "secondaryDetails": "string",
          "citationDetails": "string",
          "pageNumber": 0
        }
      ],
      "metrics": {
        "timeTaken": 0,
        "leveragedModel": "string",
		"f1Score": 0
      }
    }
  ]
}


def safeFetch(json, fieldKey):
    value = ""
    print("_________________________________________________________")
    print(json)
    print("_________________________________________________________")

    try:
        return json[fieldKey]
    except KeyError or IndexError:
        return None


    return value

def mapUploadRequestType(json, entitiyName):
    json = testData()

    response = response_esg.UploadRequestType()

    response.esgResponse = safeFetch(json, 'esgResponse')

    print("()()()()")
    print(response.esgResponse)

    return response

def mapUploadRequest(json, entitiyName):
    json = testData2()

    response = response_esg.UploadRequest()

    response.esgResponse = safeFetch(json, 'esgResponse')
    
    print("()()()()")
    print(response.esgResponse)

    return response

