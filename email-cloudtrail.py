import json
import boto3

sns = boto3.client('sns')

def lambda_handler(event, context):
    
    #Extract details from JSON event
    detailType= event["detail-type"]
    region = event["region"]
    accountId = event["account"] 
    
    #Security Hub Insight Results
    if (detailType == "Security Hub Insight Results"):
        
        action = event["detail"]["actionDescription"]
        
        message = "Alert: %s in %s for account: %s\n Action description: %s" % (detailType, region,accountId,action)
    
    elif  ("Security Hub Findings" in detailType):
        
        finding = event["detail"]["findings"][0] 
        findingTime = finding["FirstObservedAt"]
        findingType = finding["Types"][0]
        findingDescription = finding["Description"]
        remediation = finding["Remediation"]["Recommendation"]["Text"]
        
        #Security Hub Findings - Custom finding
        if(detailType == "Security Hub Findings - Custom"):
            complianceStatus = finding["Compliance"]["Status"]
            severity = finding["Severity"]["Label"]
            remediationUrl = finding["Remediation"]["Recommendation"]["Url"]
            
            message = "Alert: %s in %s for account: %s\n\nFinding regarding: [%s] %s\n Severity: %s\nDescription: %s\nFirst observed at: %s\n%s: %s" % (detailType, region, accountId, complianceStatus, findingType, 
            severity, findingDescription, findingTime, remediation, remediationUrl)
        
        #Security Hub Findings - Imported finding
        else:
            message = "Alert: %s in %s for account: %s\n\nFinding regarding: %s\nFirst observed at: %s\nRemediation recommendation: %s" % (detailType, region, accountId, findingDescription,findingTime, remediation)
    
    #AWS API Call via CloudTrail finding
    elif (detailType == "AWS API Call via CloudTrail"):
        
        time = event["detail"]["eventTime"]
        eventName = event["detail"]["eventName"]
        userIdentity = event["detail"]["userIdentity"]["arn"]
        eventID = event["detail"]["eventID"]
        requestParameters = event["detail"]["requestParameters"]
        
        message = "ALERT: %s in %s for account: %s\n\n EVENT: %s \n USER IDENTITY: %s \n EVENT TIME: %s \n EVENT ID: %s \n REQUEST PARAMETERS: %s" % (detailType, region, accountId, eventName, userIdentity, time, eventID, requestParameters)
        
        
    #If the event doesn't match any of the above, return the event     
    else:
        message = str(event)
    
    response = sns.publish(
            TopicArn = "arn:aws:sns:sa-east-1:xxxxxxxxxx:Notifica-email-security",
            Message = message
            )
    
    return {
      'statusCode': 200,
      'body': json.dumps('Success!')
}

##Criar um eventbridge
#{
#  "detail-type": ["AWS API Call via CloudTrail"],
#  "detail": {
#    "eventName": [{
#      "prefix": "Create"
#    }, {
#      "prefix": "Delete"
#    }],
#    "userIdentity": {
#      "sessionContext": {
#        "sessionIssuer": {
#          "userName": ["role-usada"]
#        }
#      }
#    }
#  }
#}

#Criar um topico sns via email
#Utilizar opcao "Create a new role from AWS policy templates" e policy "Amazon SNS publish policy" 