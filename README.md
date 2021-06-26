# connected-vehicle-iot



```
cd src
virtualenv venv
source venv/bin/activate
pip install -r requirements.txt
```

AWS GreenGrass IoT
- install GreenGrass IoT on RPi
```
$ sudo -E java -Droot="/greengrass/v2" -Dlog.store=FILE \
  -jar ./GreengrassCore/lib/Greengrass.jar \
  --aws-region us-east-2 \
  --thing-name CTV-250-GreengrassCore \
  --thing-group-name CTVGreengrassCoreGroup \
  --tes-role-name GreengrassV2TokenExchangeRole \
  --tes-role-alias-name GreengrassCoreTokenExchangeRoleAlias \
  --component-default-user ggc_user:ggc_group \
  --provision true \
  --setup-system-service true

$ sudo chmod 755 /greengrass/v2 && sudo chmod 755 /greengrass
```

```
$ sudo systemctl start greengrass.service
$ sudo systemctl stop greengrass.service
$ sudo systemctl restart greengrass.service
$ sudo systemctl status greengrass.service
```



#### Lambda Component
```
lambda-function-component.json
{
  "lambdaFunction": {
    "lambdaArn": "arn:aws:lambda:us-east-2:575711874019:function:CVT-IoT-dev-SmartBox-function:3",
    "componentName": "CVTLambda",
    "componentVersion": "1.0.0"
  }
}


Create deployment on device
$ aws greengrassv2 create-component-version --cli-input-json file://lambda-function-component.json

Get Deployable status
$ aws greengrassv2 describe-component \
  --arn "arn:aws:greengrass:us-east-2:575711874019:components:CVTLambda:versions:1.0.0"


deployment.json
{
  "targetArn": "arn:aws:iot:us-east-2:575711874019:thing/CTV-250-GreengrassCore",
  "components": {
    "CVTLambda": {
      "componentVersion": "1.0.0",
      "configurationUpdate": {
        "merge": "{\"pythonVersion\":\"3.7\"}"
      }
    }
  }
}

$ aws greengrassv2 create-deployment \
  --cli-input-json file://deployment.json

$ aws greengrassv2 list-deployments


Get device health status
$aws greengrassv2 get-core-device   --core-device-thing-name CTV-250-GreengrassCore
```