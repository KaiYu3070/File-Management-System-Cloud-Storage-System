from django.shortcuts import render,HttpResponse,redirect
import os
from django.http import HttpResponse, Http404

from apps.up01.Tools import AuthLogin
from apps.up01.Tools.Datas import Mine
from apps.up01.Tools import mkDatas
from django.views.decorators.http import require_GET
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
from django.core import serializers
import json







@require_GET
def login_kk(request,username,password,baseName):

    flag = mkDatas.check_admin(username,password,baseName)
    if flag:

        print('a', flag)
        data = {'state': flag}
        request.session[baseName] = username+password+baseName
        return JsonResponse(data)

    else:
        print('b', flag)
        return render(request, 'up01/pages/login_kk.html')


@require_GET
def login(request,username,password):

    flag = AuthLogin.checkUser(username,password)
    if flag:

        print('a', flag)
        data = {'state': flag}
        request.session['kk_admin'] = "kawsar"
        return JsonResponse(data)

    else:
        print('b', flag)
        return render(request, 'up01/pages/login.html')

def logout(request):
    if request.session.items():
        del request.session["kk_admin"]
    return render(request, 'up01/pages/login.html')


def home(request):

    return render(request, 'up01/pages/index.html')

def admin(request,name):

    data = {'DataName': name}
    if request.session.items():
        try:
            session_name = request.session[name]
            userA = mkDatas.get_user(name)
            if session_name == userA:


                return render(request, 'up01/pages/mkTable.html', data)

            else:
                return render(request, 'up01/pages/login_kk.html', data)

        except Exception as e:

            return render(request, 'up01/pages/login_kk.html', data)
    else:

        return render(request, 'up01/pages/mkTable.html',data)

def MakeDataP(request):

    return render(request,'up01/pages/mkDataBase.html')


def MakeDataPP(request):

    return render(request,'up01/pages/downloader.html')

def findAllDataBases(request):
    pass

@csrf_exempt
@require_http_methods(["POST"])
def MkDataBaseupdate(request):

    if request.method == 'POST':
        try:
            data01 = json.loads(request.body)  # 解析请求体中的JSON数据
            data =Mine(data01);
            data.yuanName =data01.get('yuanName')


            print('data',str(data))

            flag = mkDatas.update_object(data)


            if flag:

                return JsonResponse({'msg': 'success.'})

            else:

                return JsonResponse({'msg': 'fail.'})

        except json.JSONDecodeError:
            return JsonResponse({'Msg': 'Invalid JSON in request body.'}, status=400)



@csrf_exempt
@require_http_methods(["POST"])
def MkDataBasesave(request):

    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            data=Mine(data);

            flag = mkDatas.store_object(data)

            if flag:

                return JsonResponse({'msg': 'success.'})

            else:

                return JsonResponse({'msg': 'fail.'})

        except json.JSONDecodeError:
            return JsonResponse({'Msg': 'Invalid JSON in request body.'}, status=400)



def findAllDataBases02(request,currentPage,itemsPerPage,BaseName):
    print(currentPage)
    print(itemsPerPage)
    print(BaseName)
    list_data= mkDatas.FindAll02(currentPage,itemsPerPage,BaseName)

    return JsonResponse(list_data)


def findAllDataBases(request,currentPage,itemsPerPage):

    list_data = mkDatas.FindAll(currentPage,itemsPerPage)
    print('findAllDataBases',currentPage,itemsPerPage)
    print('list_data',list_data)

    return JsonResponse(list_data)

@require_GET
def delData(request,ids):

   list_output = ids.split(',')
   mkDatas.DelData(list_output)

   return JsonResponse({'msg': list_output})

def finOne01(request,name1,name2):

    name11=mkDatas.cut_string_from_end(name1)


    return JsonResponse({'filename':name11,'filename2':name1})

@require_GET
def file_name_update(request,file_name,yuan_name,all_name,base_name):


    if file_name == yuan_name:
        return JsonResponse({'msg': "NO"})
    else:
        mkDatas.file_name_update(file_name,yuan_name,all_name,base_name)
        return JsonResponse({'msg': "ok"})

@require_GET
def Findone(request,name):

    print('name',name)
    myobj = mkDatas.FindOne(name)
    return JsonResponse(myobj)



def index(request):


    return render(request,'up01/pages/login.html')



@require_GET
def get_client_ip(request,name):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]+"/"+name
    else:
        ip = request.META.get('REMOTE_ADDR')+"/"+name

    domain_name = request.get_host()+"/"+"kk_"+name

    return JsonResponse({'myip': ip,'mydomain':domain_name})

def FindAllData(request,DataName):

    print("DataName"+DataName)
    data = {'DataName':DataName}

    return render(request,'up01/pages/mkTable.html',data)

@csrf_exempt
@require_http_methods(["POST"])
def DownloadFile(request):
    data = json.loads(request.body)
    file_name = data.get('name')
    base_name = data.get('dataName')


    folder_path = mkDatas.dj_data_datas() + '/' + base_name + '/' + file_name

    try:
        response = HttpResponse(read_file(folder_path))
        response['content_type'] = "application/octet-stream"
        response['Content-Disposition'] = 'attachment; filename' + os.path.basename(folder_path)
        return response
    except Exception:
        raise Http404



def read_file(url, chunk_size=1024):
    with open(url, "rb") as f:
        while True:
            c = f.read(chunk_size)
            if c:
                yield c
            else:
                break


@csrf_exempt
@require_http_methods(["POST"])
def UploadFile(request):

    print('file:', request.FILES)
    dataName= request.POST['dataName']
    mkDatas.saveFile(request.FILES,dataName)
    return JsonResponse({'msg': 'ok'})

def del02(request,file_names,baseName):

    list_output = file_names.split(',')
    mkDatas.DelFiles(list_output,baseName)

    return JsonResponse({'msg': "ok"})


def ToAdmin(request,param):

    if "kk_" in param:

        return JsonResponse({'Msg': 'success'})
    else:
        return JsonResponse({'Msg': 'not found'}, status=404)

import subprocess

download_progress = {
    "percent": 0.0,
    "eta": "未知",
    "total":"未知",
    'pers':'0.0',
    "complete": False,
    "downloading": True,
    "merging": False,
    "error": False,
    "error_message": ""
}

import os
import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import yt_dlp
import time
import threading

download_progress = {"percent": 0, "eta": None, "complete": False}

def download_video(url, cookiefile=None,format=None,folder=None):
    global download_progress
    folder = mkDatas.dj_data_datas() + "/" + folder+"/"
    download_progress = {
        "percent": 0.0,
        "eta": "Unknown",
        "complete": False,
        "downloading": True,
        "merging": False,
        "error": False,
        "error_message": ""
    }

    resolution, extension = format.split('.')
    resolution = resolution[:-1]

    print(f'fpath:{folder}')
    print(f'resolution:{resolution}')
    print(f'extension:{extension}')
    ydl_opts = {


        'format': f'bestvideo[height={resolution}][ext={extension}]',
        'outtmpl': f'{folder}%(title)s_%(resolution)s.%(ext)s',
        'progress_hooks': [progress_hook],
        'cookiefile': cookiefile,

    }

    if cookiefile:
        ydl_opts['cookiefile'] = cookiefile

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        try:
            ydl.download([url])
            download_progress["complete"] = True

            print('下载成功了 .....')


        except Exception as e:
            download_progress["complete"] = True
            download_progress["error"] = True
            download_progress["error_message"] = str(e)
            print(f"download fail: {e}")

def progress_hook(d):
    global download_progress


    def format_bytes(size):
        for unit in ['B', 'KB', 'MB', 'GB']:
            if size < 1024.0:
                return f"{size:.2f} {unit}"
            size /= 1024.0
        return f"{size:.2f} TB"


    def format_eta(seconds):
        if seconds is None or seconds <= 0:
            return '未知'
        seconds = int(seconds)
        if seconds < 60:
            return f"{seconds} second"
        elif seconds < 3600:
            minutes = seconds // 60
            seconds = seconds % 60
            return f"{minutes} minute {seconds} second"
        else:
            hours = seconds // 3600
            minutes = (seconds % 3600) // 60
            return f"{hours} hour {minutes} minute"

    if d['status'] == 'downloading':

        download_progress["percent"] = float(d.get('_percent_str', '0.00%').replace('%', ''))


        downloaded_bytes = d.get('downloaded_bytes', 0)
        total_bytes = d.get('total_bytes', d.get('total_bytes_estimate', 0))


        speed = d.get('speed', 0)


        if total_bytes and total_bytes > 0 and downloaded_bytes and downloaded_bytes >= 0:
            remaining_bytes = total_bytes - downloaded_bytes
        else:
            remaining_bytes = 0


        if speed and speed > 0:
            eta_seconds = remaining_bytes / speed
        else:
            eta_seconds = None


        download_progress["eta"] = format_eta(eta_seconds)


        downloaded_size = format_bytes(downloaded_bytes)
        total_size = format_bytes(total_bytes) if total_bytes > 0 else 'none'
        speed_formatted = format_bytes(speed)
        download_progress["pers"] = speed_formatted
        download_progress["total"] = total_size


        print(
            f"downloading: {download_progress['percent']}% ({downloaded_size} / {total_size}), ETA: {download_progress['eta']}")




    elif d['status'] == 'finished':
        download_progress["downloading"] = False
        download_progress["merging"] = True

    elif d['status'] == 'error':
        download_progress["error"] = True
        download_progress["error_message"] = d.get('error', 'none')







def is_cookies_valid(cookiefile):

    if not os.path.exists(cookiefile):
        return False
    try:
        with open(cookiefile, 'rb') as f:

            if f.read(1):
                return True
    except Exception:
        return False
    return False



@csrf_exempt
def video_formats(request):
    if request.method == 'POST':
        url = request.POST.get('url')
        cookiefile = f'./cookies/cookie.txt'  # makesure cookies file path

        # If the cookies file exists, check its validity
        if os.path.exists(cookiefile) and is_cookies_valid(cookiefile):
            print("Use the existing valid cookies file.")
        else:
            # Check if a new cookies file has been uploaded
            if 'cookies' in request.FILES:
                cookie_file = request.FILES['cookies']
                cookiefile = f'./cookies/{cookie_file.name}'

                # Ensure the cookies directory exists
                os.makedirs(os.path.dirname(cookiefile), exist_ok=True)

                with open(cookiefile, 'wb') as f:
                    for chunk in cookie_file.chunks():
                        f.write(chunk)

                if not is_cookies_valid(cookiefile):
                    return JsonResponse({'success': False,'error': 'The uploaded cookies file is invalid. Please upload a valid cookies file.'})

            else:
                return JsonResponse({'success': False, 'error': 'No valid cookies file found. Please upload one.'})

        response_data = check_formats(url)  # Assuming this returns a list or something other than a dictionary

        return JsonResponse(response_data, safe=False)


@csrf_exempt
def download_video_view(request):
    if request.method == 'POST':
        url = request.POST.get('url')
        format = request.POST.get('format')
        folder = request.POST.get('folder')
        cookiefile = f'./cookies/cookie.txt'  # makesure cookies file path

        # If the cookies file exists, check its validity
        if os.path.exists(cookiefile) and is_cookies_valid(cookiefile):
            print("Use the existing valid cookies file.")
        else:
            # Check if a new cookies file has been uploaded
            if 'cookies' in request.FILES:
                cookie_file = request.FILES['cookies']
                cookiefile = f'./cookies/{cookie_file.name}'

                # Ensure the cookies directory exists
                os.makedirs(os.path.dirname(cookiefile), exist_ok=True)

                with open(cookiefile, 'wb') as f:
                    for chunk in cookie_file.chunks():
                        f.write(chunk)

                if not is_cookies_valid(cookiefile):
                    return JsonResponse({'success': False,'error': 'The uploaded cookies file is invalid. Please upload a valid cookies file.'})

            else:
                return JsonResponse({'success': False, 'error': 'No valid cookies file found. Please upload one.'})


        thread = threading.Thread(target=download_video, args=(url, cookiefile,format,folder))
        thread.start()
        return JsonResponse({'success': True})

def format_filesize(filesize):

    if filesize == 'Unknown':
        return filesize
    if filesize < 1024:
        return f"{filesize} B"
    elif filesize < 1024 ** 2:
        return f"{filesize / 1024:.2f} KB"
    elif filesize < 1024 ** 3:
        return f"{filesize / 1024 ** 2:.2f} MB"
    else:
        return f"{filesize / 1024 ** 3:.2f} GB"


def check_formats(url):

    with yt_dlp.YoutubeDL() as ydl:
        try:
            # Extract information about the video
            info_dict = ydl.extract_info(url, download=False)

            # 获取视频的格式数据
            formats = info_dict.get('formats', [])
            available_formats = []


            seen_formats = set()


            for fmt in formats:

                if fmt.get('filesize', 'Unknown') == 'Unknown' or any(x in fmt.get('format_note', '').lower() for x in ['ultralow','low','drc','medium','low, drc']):
                    continue


                if fmt.get('ext') not in ['mp4', 'webm']:
                    continue


                format_identifier = f"{fmt.get('height')}_{fmt.get('ext')}"

                if format_identifier not in seen_formats:
                    seen_formats.add(format_identifier)


                    formatted_filesize = format_filesize(fmt.get('filesize', 'Unknown'))

                    format_info = {
                        'format': fmt.get('format_note', 'Unknown'),
                        'extension': fmt.get('ext', 'Unknown'),
                        'filesize': formatted_filesize,
                        'height': fmt.get('height', 'Unknown'),
                        'fps': fmt.get('fps', 'Unknown'),
                    }
                    available_formats.append(format_info)


            return {"formats": available_formats}

        except Exception as e:
            print(f"Error retrieving formats: {e}")
            return {"formats": []}

def download_progress_view(request):
    return JsonResponse(download_progress)

def get_folders(request):

    list_data = mkDatas.FindAllByNotPage()
    print('FindAllByNotPage->',list_data)


    return JsonResponse(list_data)

