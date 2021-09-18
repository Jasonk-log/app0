# file name : app0.py
from flask import Flask, request, render_template, flash, redirect, url_for
from flask import current_app as current_app
 
from module import dbModule

import json
import requests

app0 = Flask(__name__)

@app0.route('/', methods=['GET'])
def index():
    
    res_app1 = requests.get("http://app1:8000")
    res_app2 = requests.get("http://app2:8000")

    json_data1 = res_app1.json()
    json_data2 = res_app2.json()

#    data1 = json.dumps(json_data1)
#    print(type(res_app1), flush=True)
#    print(type(json_data1), flush=True)
#    print(type(json_data1[0]), flush=True)
#    print(json_data1[0]['emp_no'], flush=True)
#    return json_data1[0]

    return render_template('app0.html',
                            result=None,
                            resultData1=json_data1[0],
                            resultData2=json_data2[0],
                            resultUPDATE=None)
 
if __name__ == '__main__':
    app0.run(host='0.0.0.0', port=8000, debug=True)
 
