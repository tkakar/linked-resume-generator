import json

from flask import Flask, request, make_response, jsonify
from flask_cors import CORS, cross_origin

from scrap import scrape_profile, li_login

app = Flask(__name__)
CORS(app, resources={r'/api/*': {'origins': '*'}})


@app.route('/api/profile', methods=['GET', 'POST'])
def get_profile():
   input_params = request.args.getlist("params")
   url = None
   if(input_params is not None and len(input_params) > 0):
      url = input_params[0]
      try:
         li_login()
         print("Login Succesfful")     
      except Exception as e:
         print('Login Failed')
         return make_response("Unauthorized", 401)
      try:
            response = scrape_profile(url)
            print("Data scrapping successful!")
            return jsonify(response)
      except Exception as e:
         print(f'Error in Scrapping profile {e}')  
         return make_response("Record not found", 400)    
      
if __name__ == '__main__':
   app.run(
    host="0.0.0.0",
    port=5555
   )