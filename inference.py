import os
import cv2
from detector import Retinaface_Detector

'''
# default parameters ()
params = {'mobnet_weights_file':'./mnet.25.pth',
          'threshold': 0.8,
          'pixel_means': [0,0,0],
          'pixel_stds': [1.0,1.0,1.0],
          'pixel_scale': 1.0,
          'target_size': 1024, # size to resize smaller dimension of input piture
          'max_size': 1980 # size to further resize bigger dimension it its too big
    }

detector = Retinaface_Detector(params)
'''


detector = Retinaface_Detector()
# can be used to update some params on runtime, even model can be reloaded, if different file is provided
# detector.set_params(params)

test_images = os.listdir('./test_images')

for image in test_images:
    imgpath = os.path.join('./test_images', image)
    print (imgpath)

    img = cv2.imread(imgpath)
    results = detector.detect(img, threshold=None) # if None, default threshold from params is used

    print (len(results), ' faces found.')

    if len(results) == 0:
        continue

    for result in results:
        face = result[0]
        landmark = result[1]

        color = (0, 0, 255)
        cv2.rectangle(img, (face[0], face[1]), (face[2], face[3]), color, 2)

        for l in range(landmark.shape[0]):
            color = (0, 0, 255)
            if l == 0 or l == 3:
                color = (0, 255, 0)
            cv2.circle(img, (landmark[l][0], landmark[l][1]), 1, color, 2)

        cv2.imwrite('./test_results/' + image, img)
