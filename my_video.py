# coding: utf-8

import os
import json
import time
import sys

print('*' * 50)

video_dir = "H:\\import backups\\手动摇杆驱动程序\\91porn"
# 用来存储video目录的mtime信息，判断目录是否改动过,以及上次扫描到的video目录内的文件信息
# json_path="C:\\Users\renyouyin\\Desktop\\temp.temp"
json_path = "C:\\Users\\renyo\\Desktop\\temp.temp"


# 获取video目录最新info信息的function
# 参数为目录
def get_video_info_list(dir_path):
    temp_res_dict = {}
    video_info_list = []
    # 遍历当前目录文件信息
    for video_file in os.listdir(dir_path):
        # video file path
        temp_info = {}
        video_path = dir_path + "\\" + video_file
        # insert video info into temp dict
        temp_info['name'] = video_file
        temp_info['path'] = video_path
        video_info_list.append(temp_info)
    # 拼接为最终的dict
    temp_res_dict['name'] = dir_path
    temp_res_dict['last_mtime_value'] = os.lstat(dir_path)[8]
    temp_res_dict['video_info'] = video_info_list
    return temp_res_dict

# 得到res_dict，包含video目录的mtime以及info信息
try:
    res_dict = {}
    os.lstat(json_path)
except FileNotFoundError as e:
    # except OSError as e:
    print('未找到上次的结果文件,获取目录当前信息并进行存储~')
    # 直接拿本次目录mtime存进去
    res_dict = get_video_info_list(video_dir)
    print("当前获取到的video目录mtime为：" + time.ctime(os.lstat(video_dir)[8]))
    print('*' * 50)
    # 结果文件进行序列化
    with open('C:\\Users\\renyo\\Desktop\\temp.temp', 'w') as fileh:
        json.dump(res_dict, fileh)
else:
    # 上次结果文件还在，直接load
    print("结果文件还在，加载mtime信息~")
    with open('C:\\Users\\renyo\\Desktop\\temp.temp', 'r') as fileh:
        res_dict = json.load(fileh)
    print("上次记录video目录mtime为：" + time.ctime(res_dict['last_mtime_value']))
    last_dir_mtime = res_dict['last_mtime_value']
    newest_dir_mtime = os.lstat(video_dir)[8]
    # 比对当前video目录的mtime
    if last_dir_mtime == newest_dir_mtime:
        print("video目录未发生变动，当前读取到的info_list可用~")
        print('*' * 50)
    elif newest_dir_mtime > last_dir_mtime:
        print("video目录文件有改动，当前读取到的info_list已经过期，需要更新info_list！")
        print('*' * 50)
        res_dict = get_video_info_list(video_dir)
        # 对最新结果文件进行序列化
        with open('C:\\Users\\renyo\\Desktop\\temp.temp', 'w') as fileh:
            json.dump(res_dict, fileh)
    else:
        print("什么鬼？？？mtime时间戳比对出现异常")
        print('*' * 50)

try:
    filter_word = sys.argv[1]
except IndexError as e:
    print('木有关键字~')
else:
    # 遍历video list,单独的dict
    print('以下为过滤结果：')
    for video in res_dict['video_info']:
        # print(video)
        # {'name':"",'path':""}
        if filter_word in video['name']:
            print(video['path'])
finally:
    print('*' * 50)
    print('当前目录文件总数为：' + str(len(res_dict['video_info'])))

