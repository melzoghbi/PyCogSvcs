from flask import Flask, render_template, request
import analyzeImage
import json

app = Flask(__name__)

@app.route("/")
def main():
    return render_template('index.html')

@app.route("/analyzeImage", methods = ['POST'])
def callCognitiveSvcs():
    u = request.form['imgUrl']
    k = request.form['key']
    
    print('image url is: ' + u)
    
    # pass image url and computer vision api key
    data = analyzeImage.getImageAnalysis(u, k)

    # convert the response to a string and then to a json object
    resp = json.loads(data.decode())
  
    # display tags
    print('image tags are:')
    imgTags = resp['description']['tags']
    for item in resp['description']['tags']:
        print(item + '\t')
    print('---------------')

    # display captions
    print('image captions are:')
    imgCaptions = resp['description']['captions']
    for item in resp['description']['captions']:
        print(item['text'] + '\t')
    print('---------------')
    
    return render_template('index.html', tags = imgTags, captions = imgCaptions)

if __name__ == "__main__":
    app.run()