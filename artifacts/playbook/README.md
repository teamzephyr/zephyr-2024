# artifacts/playbook
## ESG Benchmark automation deploy instructions
## All instructions to be done in GCP shell

git clone -b zucr  https://github.com/Hackathon2024-March/zephyr.git

gcloud app create --region=$AE_REGION

gcloud app deploy

######  It takes few mins to deploy to cloud, target url will be given on the screen

Go to Online Postman  to test  rest endpoints

https://web.postman.co/
type below rest endpoints for validation

https://TARGETURLesg/benchmark/keepalive  ( GET )

https://TARGETURL/esg/benchmark/pdf-report/{entityName}  ( POST )

https://TARGETURLesg/benchmark/upload/{entityName}  ( POST)

https://TARGETURL/esg/benchmark/upload/{entityName}/{esgType}/{esgIndicator}  ( POST )

https://TARGETURL/esg/benchmark/pdf-report/{entityName}  ( POST )
