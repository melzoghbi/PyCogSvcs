
########### Python 3.2 #############
import http.client, urllib.request, urllib.parse, urllib.error, base64

def getImageAnalysis(imageUrl, key):
    headers = {
        # Request headers
        'Content-Type': 'application/json',
        'Ocp-Apim-Subscription-Key': key,
    }

    params = urllib.parse.urlencode({
        # Request parameters
        'maxCandidates': '1',
    })

    body = {
        'url' : imageUrl
    }


    #  convert dictationary to str and the bytes
    strBody = str(body)
    bodyBytes = str.encode(strBody)

    try:
        conn = http.client.HTTPSConnection('api.projectoxford.ai')
        conn.request("POST", "/vision/v1.0/describe?%s" % params, bodyBytes, headers)
        response = conn.getresponse()
        data = response.read()
        print(data)
        return data
        conn.close()
    except Exception as e:
        print("[Errno {0}] {1}".format(e.errno, e.strerror))

