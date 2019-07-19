import logging

import azure.functions as func


def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    fd = open('response.csv', 'rb')
    data = fd.read()
    fd.close()

    return func.HttpResponse(data, 
        mimetype="text/csv", 
        headers={'Content-Disposition': 'attachment;filename=response.csv'})
