from smart_open import open as sopen  
import flask


def uploadFile(req):
    with sopen("gs://garage-labs/chinese-whisperer/latest.webm", "wb") as fp:
        content = req.files.get('file').read()
        fp.write(content)
    
    response = flask.jsonify({'some': 'data'})
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

