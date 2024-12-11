"""UpSystem URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))



    ffmpeg -ss 00:00:00 -i autum.mp4 -t 00:02:00 -c:v libx264 -preset slow -crf 18 -c:a aac -ar 44100 -b:a 192k output_segment.mp4
    ffmpeg -ss 00:02:00 -i autum.mp4 -t 00:03:00 -c:v libx264 -preset slow -crf 18 -c:a aac -ar 44100 -b:a 192k output_segment02.mp4

ffmpeg -ss 00:00:00 -i wakxi.mp4 -t 00:03:00 -c:v libx264 -preset slow -crf 18 -an -movflags +faststart -profile:v high10 -pix_fmt yuv420p10le output_k1.mp4


ffmpeg -ss 00:00:00 -i wakxi.mp4 -t 00:05:00 -c:v libx264 -preset veryslow -crf 14 -an -movflags +faststart -profile:v high10 -level:v 5.1 -pix_fmt yuv420p10le -tune film -b:v 40M -x264-params "keyint=60:min-keyint=60" -vf "scale=3840:2160" output_k2.mp4

"""
from django.contrib import admin
from django.urls import path,include,re_path
from apps.up01 import views
from django.urls import path
from django.views.generic import TemplateView

urlpatterns = [


    # path("kai/", include( ([
    #
    #                path('index/', views.index, name="index"),
    #                path('login/?P<username>/?P<password>', views.login, name="login"),
    #
    #                        ], 'up01'
    # ))),


                              path('index/', views.index),
                              path('get_client_ip/<str:name>', views.get_client_ip),
                              path('login/<str:username>/<str:password>', views.login),
                              path('login_kk/<str:username>/<str:password>/<str:baseName>', views.login_kk),

                              path('home/', views.home),
                              path('admin/<str:name>', views.admin),
                              path('logout/', views.logout),
                              path('MakeDataP/', views.MakeDataP),
                              path('MakeDataPP/', views.MakeDataPP),
                              path('findAllDataBases/', views.findAllDataBases),
                              path('MkDataBasesave/', views.MkDataBasesave),
                              path('upload/', views.UploadFile, name='upload_file'),
                              path('download/', views.DownloadFile, name='download_file'),
                              path('findAllDataBases/<int:currentPage>/<int:itemsPerPage>', views.findAllDataBases),
                              path('finOne01/<str:name1>/<str:name2>', views.finOne01),
                              path('findAllDataBases02/<int:currentPage>/<int:itemsPerPage>/<str:BaseName>', views.findAllDataBases02),
                              path('file_name_update/<str:file_name>/<str:yuan_name>/<str:all_name>/<str:base_name>', views.file_name_update),
                              path('del02/<str:file_names>/<str:baseName>', views.del02),
                              path('FindOne/<str:name>', views.Findone),
                              path('delData/<str:ids>', views.delData),
                              path('FindAllData/<str:DataName>', views.FindAllData),
                              path('MkDataBaseupdate/', views.MkDataBaseupdate),
                              path('<str:param>', views.ToAdmin),

                              path('download_video/', views.download_video_view, name='download_video'),
                              path('video_formats/', views.video_formats, name='video_formats'),
                              path('get_folders/', views.get_folders, name='get_folders'),
                              path('download_progress/', views.download_progress_view, name='download_progress'),



]
