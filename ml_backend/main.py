from model.ResNet import BasicBlock, ResNet
import torch
from flask import Flask, request, jsonify, Response, send_file
from src.DataLoader import CIFAR_10_Test, CIFAR_10_train
from PIL import Image
import numpy as np
from io import BytesIO
import base64


trainset = CIFAR_10_train('worse_label')
mean, std = trainset.get_norm_params()
testset = CIFAR_10_Test((mean, std))


model = ResNet(BasicBlock, [3,4,6,3], num_classes = 10)
model.load_state_dict(torch.load('./model/coresinstance0.6best.pth.tar')['state_dict'])
model.eval()


def num2label(id):
    if(id == 0):
        return 'airplane'
    elif(id == 1):
        return 'automobile'
    elif(id == 2):
        return 'bird'
    elif(id == 3):
        return 'cat'
    elif(id == 4):
        return 'deer'
    elif(id == 5):
        return 'dog'
    elif(id == 6):
        return 'frog'
    elif(id == 7):
        return 'horse'
    elif(id == 8):
        return 'ship'
    elif(id == 9):
        return 'truck'


def get_mothod(id: int):

    with torch.no_grad():

        img_tensor, label = trainset[id]


        output = model(img_tensor.reshape(1,3,32,32))

        pred_label = output.argmax(dim=1)

        prob = torch.softmax(output, dim=1).max(dim=1)[0].item()

        img_data = img_tensor.numpy()
        new_img_data = np.zeros((32, 32, 3))

        new_img_data[:,:,0] = img_data[0]*std[0].item() + mean[0].item()
        new_img_data[:,:,1] = img_data[1]*std[1].item() + mean[1].item()
        new_img_data[:,:,2] = img_data[2]*std[2].item() + mean[2].item()

        new_img_data = new_img_data.astype(np.int8)
        
        return (label.item(), pred_label.item(), prob, new_img_data)



app = Flask(__name__)

@app.route('/api/predict/<int:id>', methods=['GET'])
def predict(id):
    if(id >=50000 or id <0):
        return 'None'

    label, pred_label, prob, new_img_data = get_mothod(id)

    img = Image.fromarray(new_img_data, mode='RGB')

    img_io = BytesIO()

    img.save(img_io, format='PNG')

    resp = Response(img_io.getvalue(), mimetype='image/png')

    resp.headers['label'] = num2label(label)
    resp.headers['pred_label'] = num2label(pred_label)
    resp.headers['prob'] = str(prob)

    return resp



if __name__ == '__main__':
   app.run(host='127.0.0.1', port=5000, debug=False)



