import cv2
import os

game = 'bowling'
filenames_list = os.listdir(path='./videos/'+ game )
print(filenames_list)

if not os.path.exists('saved_model'):
  os.mkdir('saved_model')

if not os.path.exists('runs'):
  os.mkdir('runs')

for filename in filenames_list:
    filename_chunk = filename.split('-')
    model_name = filename_chunk[0]

    # READ MOVIE
    movie = cv2.VideoCapture('./videos/' + game + '/' + filename)
    nframe = int(movie.get(cv2.CAP_PROP_FRAME_COUNT))

    for i in range(nframe):
        ret, frame = movie.read()
        #print(frame.shape)
        cropped_frame = frame[50:180, 0:160]
        savepath = './torch_images_label/' + game + '/' + model_name + '/'
        if not os.path.exists(savepath):
            os.mkdir(savepath)
        cv2.imwrite(savepath + model_name + '_' + str(i) + '.png', cropped_frame)
        #break

'''
breakout:frame[32:192, 8:152]
amidar:frame[32:197, 8:152]
alien:frame[10:175, 8:152]
assault:[50:240, 8:152]
asterix:[10:180, 8:152]
atrantis:frame[0:190, 0:160]
battlezone:frame[0:175, 10:160]
berzerk:frame[0:180, 0:160]
bowling:frame[50:180, 0:160]
boxing:frame[30:180, 0:160]
chopper:frame[25:190, 0:160]
fishing:frame[18:190, 0:160]
freeway:frame[18:195, 0:160]
icehockey:frame[30:190, 0:160]
kungfumaster:frame[30:190, 0:160]
montezuma:frame[15:210, 0:160]
mspacman:frame[0:185, 0:160]
pong:frame[30:200, 0:160]
qbert:frame[16:210, 0:160]
seaquest:frame[20:210, 0:160]
skiing:frame[50:210, 0:160]
spaceinveders:frame[20:210, 0:160]
'''
