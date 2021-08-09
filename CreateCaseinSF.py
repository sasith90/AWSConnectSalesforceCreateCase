import json
import requests
import base64
import os,time
import datetime


def lambda_handler(event, context):
   ## print (event)
    
##Getting Calling Number from Connect
    e164num = event['Details']['Parameters']['ANI']
    ROC = event['Details']['Parameters']['ReasonOfContact']
    orinumber =e164num[3:]
    today = datetime.date.today()
    print (today)
    today =str(today)
    
##defining parameters for Authentication
    params={
        "grant_type":"password",
        "client_id":"Conencted APp user ID",
        "client_secret" : "YConnected App secret",
        "username":"SF Login user name",
        "password" :"SF Login user password"
    }
##Getting access token
    r=requests.post("https://login.salesforce.com/services/oauth2/token",params=params);
    access_token=r.json().get("access_token")
    instance_url=r.json().get("instance_url")

##creating instance URL for Create Case   
    url = instance_url+'/services/data/v46.0/sobjects/Case'
    
##Updating the number format
    orinumber =str(orinumber)
    ##orinumber =str(phonenumbers.parse(orinumber, None).national_number)
    print (orinumber)
    
##Creating the Body  
    body = {"Origin": "IVR Helpdesk","Contact_No__c":orinumber,"Status":"New","Type":"Centre Related","Subject":"From IVR","RecordTypeId":"01290000001QHPMAA4","Date__c":today,"Description":ROC}
    headers = {'Authorization':'Bearer '+ access_token, "Content-Type":"application/json"}
    r = requests.post(url =url, headers = headers, data=json.dumps(body))
    print (r.status_code)
    return (r.json())
    
                
    
