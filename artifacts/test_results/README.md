

# artifacts/test_results

1. Below is service endpoint for an upload method-
POST
/esg/benchmark/upload/{entityName}
Upload ESG for given entity and retrieve all ESG benchmark document

https://wells-fargo-genai24-8370.uc.r.appspot.com/api/esg/benchmark/upload/esgdoc

2.Below is service endpoint for an upload method with entiyName,esgType and esgIndicator as parameters
POST
/esg/benchmark/upload/{entityName}/{esgType}/{esgIndicator}
Fetch specific ESG indicator for given entity

https://wells-fargo-genai24-8370.uc.r.appspot.com/api/esg/benchmark/upload/esgdoc/abc/cold

https://wells-fargo-genai24-8370.uc.r.appspot.com/api/esg/benchmark/upload/ESG/ESGScore/MSCISustainalytics

3.Below is service endpoint for an keepalive method -healthcheck
GET
/esg/benchmark/keepalive
Find status of the benchmarking service

https://wells-fargo-genai24-8370.uc.r.appspot.com/api/esg/benchmark/keepalive

4.Below is service endpoint for a method to get the generated report PDF url for the entiyName as parameter
POST
/esg/benchmark/pdf-report/{entityName}
get PDF URL for given entity name

https://wells-fargo-genai24-8370.uc.r.appspot.com/api/esg/benchmark/pdf-report/esg
