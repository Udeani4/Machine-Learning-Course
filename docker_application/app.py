# CREATING Docker Image

from flask import Flask
import os
app=Flask(__name__)

@app.route('/',methods=['GET'])
def home():
    return 'Hello world'

if __name__=='__main__':
    app.run(debug=True,host='0.0.0.0',port=5000)

    ## the host set as 0.0.0.0 is used to help us use any of the local host. eg https://localhost:5000, https://0.0.0.0/home, https://127.0.0.1:5000, 

    ## you can even use your ip address
    # Type ipconfig in the command prompt to get it
    ## you can now host with [localIpAddress]:5000 but this is not secure


# import sys
# print(sys.executable)