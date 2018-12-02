#!/usr/bin/env python3


import requests
import sys 
import re 
import json 
import os 

page_url = "https://www.pornhd.com/videos"

video_url_info = "https://api.pornhd.com/videos/get-download-url?videoId=%d&resolution=720"

post_headers = {
 # ":authority" : "api.pornhd.com",
 # ":method": "POST",
 # ":scheme": "https",
  "accept": "*/*",
  "accept-encoding": "gzip, deflate, br",
  "accept-language": "zh-CN,zh;q=0.9",
  "content-type": "application/x-www-form-urlencoded; charset=UTF-8",
  "origin": "https://www.pornhd.com",
 # "referer": "https://www.pornhd.com/videos/44756/peta-jensen-is-a-fucking-perfect-bombshell-hd-porn-video"
  "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.75 Safari/537.36"
}


download_path = "/var/video/pornhd"

def main():
  if not os.path.isdir(download_path):
    os.makedirs(download_path)

  vid = sys.argv[1] or 0
  if vid:
    try:
      vid = int(vid)
    except Exception as e:
      print(e)
      sys.exit(1)

    v_url = "%s/%d" % (page_url, vid)

    try:
      html_res = requests.get(v_url)
    except Exception as e:
      print('[Error] requests send get request error!')

    html_content = html_res.text
    location = html_res.headers
    print(location)
    csrf_token = re.search('\w{0,}\=\=', html_content).group()

    if csrf_token:
      header_path = "/videos/get-download-url?videoId=%d&resolution=720" % vid 
      #post_headers[":path"] = header_path
      post_url = video_url_info % vid 
      r = requests.post(post_url, data={'_csrf-frontend':csrf_token, 'domain': 'www.pornhd.com', '_jwt':'' }, headers=post_headers)
      print("----------------------------------------------------------------------")
      print(r.status_code)
      print(r.headers)
      print(r.text.encode('unicode_escape').decode('utf-8'))
      print("----------------------------------------------------------------------")
      if r.status_code == 200:
        res_dict = json.loads(r.text)
        if res_dict.get('status') == 'success':
          video_download_url = res_dict.get('result') or None 
          if video_download_url:
            print(video_download_url)
            sys.exit(0)
          else:
            print("[Error] result field is empty!")
            sys.exit(1)
        else:
          print('[Error] status is not success!')
          sys.exit(1)
      else:
        print('[Error] status code is not 200!')
        sys.exit(1)
    else:
      print('[Error] csrf_token get error!')
      sys.exit(1)
  else:
    print('[Error] vid is None!')
    sys.exit(1)







if __name__ == '__main__':
  if len(sys.argv) != 2:
    print('[Error] params passwd error!')
	  sys.exit(1)
  main()
  