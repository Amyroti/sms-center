#!/usr/bin/env python

from suds.client import Client

try:
    soap = Client('http://127.0.0.1:8000/api/wsdl')
except Exception:
    print 'connection failed\nCheck your web service status!'
    sys.exit()
    
from flask import Flask,render_template,request

app = Flask(__name__)

@app.route('/',methods=['GET','POST'])
def send():
    if request.method == 'POST':
        mobile = request.form.get('mobile')
        sv = soap.service.check_sent(mobile)
        
        if sv == '3':
            action = soap.service.keygen(mobile,True)
            msg = 'key generated and sent to your phone'
        else:
            action = soap.service.resend(mobile)
            msg = 'key resent to your phone'
        return msg
    return render_template('send.html')

@app.route('/verify')
def verify():
    return render_template('verify.html')


if __name__ == "__main__":
    app.run(debug=True)