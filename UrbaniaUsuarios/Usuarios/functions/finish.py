import json
import azure.functions as func 

def finish(result, statusCode):
    ret = dict()
    ret['result'] = result
    return func.HttpResponse(json.dumps(ret),status_code=statusCode)