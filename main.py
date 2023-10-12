from flask import Flask
from flask_restful import Resource, Api, request
import openai, os, logging

openai.api_key = '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'

app = Flask(__name__)
api = Api(app)


class SendToAI(Resource):
    def post(self):
        image = request.files['image']
        logging.warning(image)

        mask = request.files['mask']
        logging.warning(mask)

        prompt = request.args.get('prompt')

        response = openai.Image.create_edit(
            image = image,
            mask = mask,
            prompt = prompt,
            n = 1,
            size = "1024x1024"
        )

        image_url = response['data'][0]['url']
        logging.warning(image_url)
        return { "url" : image_url }

def allowed_file(filename):
    ALLOWED_EXTENSIONS = {'png'}
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


api.add_resource(SendToAI, '/upload')

if __name__ == '__main__':
    app.run(debug=True)