
import requests
import numpy as np
import json



def post(joints,targetpos):
    URL = "http://127.0.0.1:7777/set_joint_positions"
    #jntconv=np.array(joints,dtype=String)
    #posconv=np.array(targetpos,dtype=float32)
    #list(jntconv.astype(float)),
    jsn={
        'names': joints,
        'positions': np.ndarray.tolist(targetpos)
        }
    #print(json.dumps(jsn))
    # sending get request and saving the response as response object
    response = requests.post(url = URL, json =jsn )
    #print(response.json())

