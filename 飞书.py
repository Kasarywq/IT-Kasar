#!/usr/bin/python3
# -*- coding: utf-8 -*-
import requests
import json
import sys
import os
import time

headers = {'Content-Type': 'application/json;charset=utf-8'}
time=time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

api_url = "你的飞书机器人地址"     


def msg(text,title):
    json_text= {
    "msg_type": "post",
    "content": {
        "post": {
            "zh_cn": {
                "title": title,
                "content": [
                    [
                        {
                            "tag": "text",
                            "text": text,
                        },
                        {"tag": "at"
                        "user_id": "用户ID"
                        }
                        
                    ]
                    
                ]
            }
        }
    }
}
    print (requests.post(api_url,data=json.dumps(json_text),headers=headers).json())

if __name__ == '__main__':
    text = sys.argv[1]
    title = sys.argv[2]
    msg(text,title)
