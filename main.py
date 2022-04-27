import cv2
import numpy as np
import yuvio

def convert(input, output):
    rgbData = cv2.imread(input)
    yuvData = cv2.cvtColor(rgbData, cv2.COLOR_BGR2YUV_I420)

    height = rgbData.shape[0]
    width = rgbData.shape[1]



    uData = yuvData[height: height + height // 4, :]
    uData = uData.reshape((1, height // 4 * width))
    vData = yuvData[height + height // 4: height + height // 2, :]
    vData = vData.reshape((1, height // 4 * width))
    uvData = np.zeros((1, height // 4 * width * 2),dtype=np.uint8)
    uvData[:, 0::2] = vData
    uvData[:, 1::2] = uData
    uvData = uvData.reshape((height // 2, width))
    nv21Data = np.zeros((height + height // 2, width),dtype=np.uint8)
    nv21Data[0:height, :] = yuvData[0:height, :]
    nv21Data[height:, :] = uvData

    nv21Data.tofile(output)



if __name__ == '__main__':
    convert('zelda.jpg','out.nv21')
