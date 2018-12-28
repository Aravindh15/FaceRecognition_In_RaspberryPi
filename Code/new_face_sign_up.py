# sign up new face

import dlib  # 人脸处理的库 Dlib
import numpy as np  # 数据处理的库 Numpy
import cv2  # 图像处理的库 OpenCv

import os  # 读写文件
import shutil  # 读写文件


def add_face(name):

    # Dlib 正向人脸检测器
    detector = dlib.get_frontal_face_detector()

    # Dlib 68 点特征预测器
    #predictor = dlib.shape_predictor(
    #    'data/data_dlib/shape_predictor_68_face_landmarks.dat')

    # OpenCv 调用摄像头
    cap = cv2.VideoCapture(0)

    # 设置视频参数
    cap.set(3, 480)

    # 人脸截图的计数器
    cnt_ss = 0

    # 存储人脸的文件夹
    current_face_dir = 0

    # 保存的路径
    path_make_dir = "data/data_faces_from_camera/"
    path_csv = "data/data_csvs_from_camera/"
    current_face_dir = path_make_dir + str(name)
    os.makedirs(current_face_dir)

    # The flag of if u can save images
    save_flag = 1

    while cap.isOpened():
        # 480 height * 640 width
        flag, img_rd = cap.read()
        kk = cv2.waitKey(500)

        img_gray = cv2.cvtColor(img_rd, cv2.COLOR_RGB2GRAY)

        # 人脸数 faces
        faces = detector(img_gray, 0)

        # 待会要写的字体
        font = cv2.FONT_HERSHEY_COMPLEX

        if len(faces) == 0:
            cv2.putText(img_rd, "No face detected", (20, 30), font, 0.8,
                        (0, 0, 255), 1, cv2.LINE_AA)
        elif len(faces) > 0:
            # 检测到人脸

            # 矩形框
            for k, d in enumerate(faces):

                # 计算矩形大小
                # (x,y), (宽度width, 高度height)
                pos_start = tuple([d.left(), d.top()])
                pos_end = tuple([d.right(), d.bottom()])

                # 计算矩形框大小
                height = (d.bottom() - d.top())
                width = (d.right() - d.left())

                hh = int(height / 2)
                ww = int(width / 2)

                # 设置颜色 / The color of rectangle of faces detected
                color_rectangle = (255, 255, 255)
                if (d.right() + ww) > 640 or (d.bottom() + hh > 480) or (
                        d.left() - ww < 0) or (d.top() - hh < 0):
                    cv2.putText(img_rd, "OUT OF RANGE", (20, 300), font, 0.8,
                                (0, 0, 255), 1, cv2.LINE_AA)
                    color_rectangle = (0, 0, 255)
                    save_flag = 0
                else:
                    color_rectangle = (255, 255, 255)
                    save_flag = 1

                cv2.rectangle(img_rd, tuple([d.left() - ww,
                                             d.top() - hh]),
                              tuple([d.right() + ww,
                                     d.bottom() + hh]), color_rectangle, 2)

                if len(faces) > 1:
                    cv2.putText(img_rd, "Too many faces detected", (20, 30),
                                font, 0.8, (0, 0, 255), 1, cv2.LINE_AA)
                else:

                    # 根据人脸大小生成空的图像
                    im_blank = np.zeros((int(height * 2), width * 2, 3),
                                        np.uint8)

                if save_flag:
                    cnt_ss += 1
                    for ii in range(height * 2):
                        for jj in range(width * 2):
                            im_blank[ii][jj] = img_rd[d.top() - hh +
                                                      ii][d.left() - ww + jj]
                    cv2.imwrite(
                        current_face_dir + "/img_face_" + str(cnt_ss) + ".jpg",
                        im_blank)
                    print(
                        "写入本地：",
                        str(current_face_dir) + "/img_face_" + str(cnt_ss) +
                        ".jpg")

            # 显示人脸数
        #cv2.putText(img_rd, "Faces: " + str(len(faces)), (20, 100), font, 0.8, (0, 255, 0), 1, cv2.LINE_AA)

        # 按下 'q' 键或拍满10张退出
        if kk == ord('q') or cnt_ss >= 10:
            break

        # 窗口显示
        # cv2.namedWindow("camera", 0) # 如果需要摄像头窗口大小可调
        cv2.imshow("Sign up: " + name, img_rd)

    # 释放摄像头
    cap.release()

    # 删除建立的窗口
    cv2.destroyAllWindows()