import azure.functions as func
import os
import sys
import requests
import urllib3
import datetime
import json
import calendar
import random
import time
import ast
import logging

sys.path.insert(0, '/home/site/wwwroot/zetm-common/')

from KVConnection import getZETMHeaders

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

API_AUDIT_LOGS = "https://att.yourzephyr.com/flex/services/rest/v3/ui/auditLogs"
API_AUDIT_LOGS2 = "https://att.yourzephyr.com/flex/services/rest/v3/ui/auditLogs?offset=0&pagesize=RESULT_SIZE"

ATT_PROXY = {
    "https": "http://sub.proxy.att.com:8080",
    "http": "http://one.proxy.att.com:8080"
}

AZ_FUN_VM_PATH_PARENT = "/home/site/"
AZ_FUN_VM_PATH_CHILD = AZ_FUN_VM_PATH_PARENT + "audit-log/"

skeleton_data = {
    "entity": "",
    "operation": None,
    "userName": None,
    "fromDate": "",
    "toDate": "",
    "toDateVal": "",
    "fromDateVal": ""
}


def __fileNameSuffix():
    currentDate = datetime.datetime.now()
    s = calendar.timegm(currentDate.timetuple())
    randStr = ''.join(random.choice('0123456789ABCDEF') for i in range(8))
    return currentDate.strftime("%m") + currentDate.strftime("%d") + currentDate.strftime("%Y") + "_" + str(randStr)


def dateDifference(dayDiffValue, withTime=False):
    """
    @format: MM/DD/YYYY
    @return: str
    """
    if dayDiffValue == 0 or dayDiffValue == None:
        return False
    yesterDate = datetime.datetime.today() - datetime.timedelta(days=dayDiffValue)
    if withTime:
        return yesterDate.strftime("%Y-%m-%dT00:00:00.000Z")
    else:
        return yesterDate.strftime("%Y-%m-%d")


def submitRequest(requestUrl, requestBody, headers):
    if len(requestUrl) == 0 or len(requestBody) == 0 or len(headers) == 0:
        return False
    try:
        logging.info("inside submit request - before try")
        resp = requests.post(url=requestUrl,
                             json=requestBody,
                             headers=headers,
                             verify=False)

        logging.info(resp)
        logging.info("response received")
        if len(resp.text) > 1:
            response = json.loads(resp.text)
            return response
        else:
            return {}
    except Exception as e:
        print(e)


def constructRequestBody():
    skeleton_data["fromDate"] = dateDifference(2)
    skeleton_data["toDate"] = dateDifference(1)
    skeleton_data["fromDateVal"] = dateDifference(3, withTime=True)
    skeleton_data["toDateVal"] = dateDifference(2, withTime=True)
    return skeleton_data


def getAuditLogResultSize():
    try:
        logging.info("inside Audit Log Result Size Function.")
        logging.info(constructRequestBody())
        resp = submitRequest(requestUrl=API_AUDIT_LOGS,
                             requestBody=constructRequestBody(),
                             headers=getZETMHeaders())
        logging.info("Response Received as Dataset")
        return resp['resultSize']
    except Exception as e:
        logging.info("inside else")
        logging.info(e)
        print(e)


def getAuditLogsByOffset(offsetValue):
    if type(offsetValue) is not int:
        return False
    try:
        logging.info("Audit Log by OffsetValue")
        requestURL = API_AUDIT_LOGS2.replace("RESULT_SIZE", str(offsetValue))
        resp = submitRequest(requestUrl=requestURL,
                             requestBody=constructRequestBody(),
                             headers=getZETMHeaders())
        logging.info("Response Received as JSON Dataset")
        dataResponse = resp
        return dataResponse['results']
    except Exception as e:
        logging.info(e)
        print(e)


def mainMethod():
    logging.info("Inside the Audit Log capturing process")
    existingFiles = [f for f in os.listdir(AZ_FUN_VM_PATH_CHILD) if os.path.isfile(os.path.join(AZ_FUN_VM_PATH_CHILD, f))]
    logging.info(existingFiles)

    logging.info("Does any files already existing the VM machine?")
    if len(existingFiles) > 0:
        logging.info("Yes, it does")
        for file in existingFiles:
            logging.info(file)
            os.remove(AZ_FUN_VM_PATH_CHILD + file)
        logging.info("All the existing/old json datasets files are removed from the directory.")

    try:
        logging.info("Trying to get AuditLog Result Size")
        logSize = getAuditLogResultSize()
        logging.info("the audit log results size is " + str(logSize))
        zetm_audit_logs = getAuditLogsByOffset(logSize)
        logging.info("the audit log array size is " + str(len(zetm_audit_logs)))
        logging.info("try completed")
    except Exception as e:
        logging.error(e)
        logging.info("inside main else. ")
        zetm_audit_logs = []

    if len(zetm_audit_logs) > 0:
        logging.info("audit log size greater than 0")
        isExist = os.path.exists(AZ_FUN_VM_PATH_CHILD)
        logging.info("Does the directory exist? " + str(isExist))
        if not isExist:
            logging.info("creating a path")
            os.makedirs(AZ_FUN_VM_PATH_CHILD)
            logging.info("path created successfully")
        logging.info("file pushing to the folder..")
        with open("/home/site/audit-log/zetm_events_" + __fileNameSuffix() + '.json', 'w', encoding='utf-8') as f:
            json.dump(zetm_audit_logs, f, ensure_ascii=False, indent=4)
        logging.info("Process completed")


def main(mytimer: func.TimerRequest) -> None:
    logging.info("test")
    logging.info("Python timer trigger function for Audit Logs")
    mainMethod()
