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


def formatFloat(num):
    return '{:.2f}'.format(num)


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
    csrf_token = re.search('\w{0,}\=\=', html_content).group()
    meta_name = re.search('<meta name="og:url"(.*?)">', html_content).group()
    
    if not csrf_token or not meta_name:
      print("[Error] parse html goes error! Please Check!")
      sys.exit(1)

    meta_list = meta_name.split('"')
    if len(meta_list) < 3:
      print(meta_name)
      print("[Error] meta info parse error! Please check!")
      sys.exit(1)
    video_url = meta_list[3] or None 

    if not video_url:
      print(meta_list)
      print("[Error] video_url cant be parsed from meta_list! Please check!")
      sys.exit(1)

    post_headers["referer"] = video_url

    video_name_list = video_url.split('/')

    video_name = video_name_list[-1]

    post_url = video_url_info % vid 
    r = requests.post(post_url, data={'_csrf-frontend':csrf_token, 'domain': 'www.pornhd.com', '_jwt':'' }, headers=post_headers)
   # print("----------------------------------------------------------------------")
   # print(r.status_code)
   # print(r.headers)
   # print(r.text.encode('unicode_escape').decode('utf-8'))
   # print("----------------------------------------------------------------------")
    if r.status_code == 200:
      res_dict = json.loads(r.text)
      if res_dict.get('status') == 'success':
        video_download_url = res_dict.get('result') or None 
        if video_download_url:
          print("video_url: %s" % video_url)
          print("video_download_url: %s" % video_download_url)
          print("begin to download this video---------------------------------->")

          f_name = "%s/%s" % (download_path, video_name)
          print(f_name)
          request_video = requests.get(video_download_url, stream=True)
          length = float(request_video.headers['content-length'])
          with open("%s/%s" % (download_path, video_name), 'wb') as f:
            count = 0
            count_tmp = 0
            time1 = time.time()
            for chunk in request_video.iter_content(chunk_size = 512):
              if chunk:
                f.write(chunk)
                count += len(chunk)
                if time.time() - time1 > 2:
                  p = count / length * 100
                  speed = (count - count_tmp) / 1024 / 1024 / 2
                  count_tmp = count
                  print(video_name + ': ' + formatFloat(p) + '%' + ' Speed: ' + formatFloat(speed) + 'M/S')
                  time1 = time.time()
          print("------------------------------------->video download finished!")
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
    print('[Error] vid is None!')
    sys.exit(1)







if __name__ == '__main__':
  if len(sys.argv) != 2:
    print('[Error] params passwd error!')
    sys.exit(1)
  main()
  