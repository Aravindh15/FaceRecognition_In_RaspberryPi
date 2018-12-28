# 人脸管理
# 查看、增加、删除人脸

import numpy as np  # 数据处理的库 numpy
import pandas as pd  # 数据处理的库 Pandas
import csv
import shutil
import os

import new_face_sign_up
import get_features

# 人脸数据库
path_features_known_csv = "data/faces_database.csv"
path_faces = "data/data_faces_from_camera/"
path_csvs = "data/data_csvs_from_camera/"

# 读取已知人脸数据
def read_faces_database_csv():
    try:    
        csv_rd = pd.read_csv(path_features_known_csv, header=None)
    except:
        print("empty\n")
        return [],[]
    
    faces_known_arr = []  # array of faces in database
    names_arr = []  # array of names in database
    for i in range(csv_rd.shape[0]):
        names_arr.append(csv_rd.ix[i, :][0])  # read name
        features_someone_arr = []
        for j in range(1, len(csv_rd.ix[i, :])):
            features_someone_arr.append(csv_rd.ix[i, :][j])
        faces_known_arr.append(features_someone_arr)  # read face feature
    print(len(faces_known_arr), "Faces in Database.")
    print("Names in Database: ", names_arr)
    return names_arr, faces_known_arr


faces_known_arr = []  # array of faces in database
names_arr = []  # array of names in database
names_arr, faces_known_arr = read_faces_database_csv()


# Delete a face
def delete_a_face(name):
    global names_arr
    global faces_known_arr
    csv_rd = pd.read_csv(path_features_known_csv, header=None)
    if name in names_arr:
        # in database
        index = names_arr.index(name)
        #csv_rd.drop(index,inplace=True)
        #print(csv_rd)
        with open(path_features_known_csv, "w", newline="") as csvfile:
            writer = csv.writer(csvfile)
            for i in range(csv_rd.shape[0]):
                if i != index:
                    writer.writerow(csv_rd.ix[i, :])
        shutil.rmtree(path_faces + name)
        os.remove(path_csvs + name + '.csv')
        print("Delete", name, "\n")
    else:
        # not in database
        print(name, "not found\n")


while 1 == 1:
    command = input("Please input command:\n")
    if command == "d" or command == "delete":
        name_to_delete = input("Name to detele:\n")
        delete_a_face(name_to_delete)
    elif command == "n" or command == "new":
        name_to_add = input("Your name:\n")
        if name_to_add in names_arr:
            print("error")
        else:
            new_face_sign_up.add_face(name_to_add)
    elif command =="s" or command=="save":
        get_features.calculate()
    else:
        print("error")
    names_arr, faces_known_arr = read_faces_database_csv()