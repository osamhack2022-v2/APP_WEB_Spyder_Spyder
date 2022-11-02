<p align="center">
  <img width="180" alt="Screen Shot 2022-11-02 at 11 13 57 AM" src="https://user-images.githubusercontent.com/60809681/199389756-5b85cce3-f571-48ad-b741-3233236efc81.png">
</p>

<p align="center">
  <img src="https://user-images.githubusercontent.com/60809681/199347082-f33599b5-4c8b-4dde-83b3-b513b183b834.gif" alt="animated" />
</p>

##  :page_facing_up: 목차

1. [개요](#개요-Abstract)
2. [소개](#소개-Introduction)
3. [시연 영상](#시연-영상)
4. [기능 설명](#hammer-기능-설명)
5. [컴퓨터 구성 / 필수 조건 안내](#earth_asia-컴퓨터-구성--필수-조건-안내-prerequisites)
6. [기술 스택](#computer-기술-스택-technique-used)
7. [설치 안내](#inbox_tray-설치-안내-installation-process)
8. [기대효과 및 전망](#rocket-기대효과-및-전망)
9. [팀원 정보](#two_men_holding_hands-팀-정보-team-information)
10. [저작권 및 사용권 정보](#clipboard-저작권-및-사용권-정보-copyleft--end-user-license)

&nbsp;

## 개요 Abstract

> Spyder는 머신러닝을 이용한 군장병 기밀 유출 보안 솔루션입니다.

오늘도 대한민국을 지키는 우리 국군 장병들! 장병들이 지켜야 할 가장 중요한 것은 무엇일까요!? 무기? 식량? 초소? 바로 국방의 기초가 되는 보안입니다! 
 
2022년 3월, 한국 주요 방송사 KBS 뉴스의 인터뷰로 인해 우크라이나 국제군단의 소재지가 노출 되는 사건이 있었습니다. 의도치 않은 사고였겠지만, 우크라이나 군은 러시아의 폭격에 당할 수 있는 큰 위험에 놓였습니다. *주요 방송사도 실수하는 기밀 유출, 군 장병이 보안을 지킬 수 있을까요?*

국방의 보안을 위한 카메라 차단 보안 앱이 마련되어있지만, 카메라를 원천 차단하면 발생할 수 있는 불편함과 비콘이 있는 위병소로 직접 가서 앱을 활성화 하고 비활성화 해야 하는 비효율적인 방식, 그리고 앱의 정상작동 유무확인을 위해 간부들이 직접 일일이 병사들의 모바일 기기를 확인해야 하는 방식은 기존 솔루션을 "*매우 불편한 앱*"으로 만들고 있습니다. 그렇다면 이런 단점들을 보완하며 더 발전시킬 방법은 없을까요?

&nbsp;
 
## 소개 Introduction

머신러닝을 이용한 군장병 기밀 유출 보안 솔루션, Spyder입니다.

Spyder은 기존 국방모바일보안 앱을 보완한 솔루션으로, 크게 두가지 플랫폼으로 나누어져 있습니다. 병사들이 간편히 사용할 수 있는 모바일 앱과 간부나 어드민이 사용 가능한 모니터링 웹 입니다. 장병들은 부대 안에 들어가는 순간 APP 스위치를 활성화 시킵니다. 스파이더를 활성화 하는 순간, 장병의 모바일 기기 안에 저장된 사진들은 사진의 gps 정보를 불러와 보안구역 내에서 찍은 사진들을 Spyder WEB에 업로드 시키고 기기에서는 삭제됩니다. 이는 앱의 활성화 된 상태에서 찍힌 모든 사진과 비디오에 적용됩니다. Spyder Web에 업로드 된 후, 감지된 사진들은 1차적 머신러닝 검증과 2차적 간부의 수동 확인 후 병사의 휴대폰에서 다시 원본 파일의 다운로드가 가능합니다. 
 
처음 입대하거나 휴가에서 복귀하는 장병들은 Spyder을 활성화 시킴으로서 휴대폰 안에 저장된 사진들을 빠르게 분석해 군 기밀 유출을 차단합니다. 기존 보안 앱과 달리 카메라 사용이 가능하기 때문에 향상된 업무 효율성과 신속한 상황 보고가 가능하고, 관리자 모니터링 웹페이지를 통해 부대 내에 있는 휴대폰들의 Spyder App이 켜져 있는지 실시간으로 보여줌으로서 강력한 보안성을 자랑합니다.

&nbsp;

## 시연 영상
https://user-images.githubusercontent.com/60809681/199351144-b570d4dd-5a10-4217-bc30-a665b2035fdd.mp4

&nbsp;
 
## :hammer: 기능 설명 
 - ## APP
  - **APP 첫 화면**: 앱을 설치한 날짜를 알려주는 문구와 간부의 확인을 얻은 사진을 서버에서 다운로드 받을 수 있는 버튼, 앱을 활성화 하고 비활성화 하는 스위치, 그리고 기기의 ID를 보여주는 문구 등이 있습니다. 
 <p align="center">
    <img width="250" alt="Screen Shot 2022-11-02 at 7 25 49 AM" src="https://user-images.githubusercontent.com/60809681/199353739-f4351837-ae8a-40bb-84dd-9e00f6bd2261.png">


   - **APP GPS 사용 동의**: 스파이더는 사진 및 영상의 gps 정보를 사용하기 때문에 유저 gps를 상시 사용하는 동의를 얻습니다.
 <p align="center">
    <img width="250" alt="Screen Shot 2022-11-02 at 7 32 49 AM" src="https://user-images.githubusercontent.com/60809681/199354585-c77830b6-437a-4b1c-a181-998172f060c4.png">
 </p>
 
   - **APP 활성화**: 장병들은 부대 안에 들어가는 순간 스위치를 활성화 시킵니다. 앱의 활성화는 간부도 즉시 웹 알람으로 확인이 가능하며, 스파이더를 활성화 하는 순간, 장병의 모바일 기기 안에 저장된 사진들은 사진의 gps 정보를 불러와 보안구역 내에서 찍은 사진들을 서버에 업로드 시키고 기기에서는 삭제됩니다. 이는 앱의 활성화 된 상태에서 찍힌 모든 사진과 비디오에 적용됩니다.
 <p align="center">
    <img width="250" alt="Screen Shot 2022-11-02 at 7 36 05 AM" src="https://user-images.githubusercontent.com/60809681/199354989-e11e57cd-120c-4cb0-8c6b-168149bca870.png">
 </p>
 
   - **APP 다운로드**: Spyder WEB에서 간부의 확인이 된 사진은 APP에서 다운 받을 수 있습니다. 
 <p align="center">
    <img width="250" alt="Screen Shot 2022-11-02 at 12 30 06 PM" src="https://user-images.githubusercontent.com/60809681/199388888-c9d6173c-f1d9-4984-acd7-f1d4d3c12aa4.png">
 </p>
 
   - **APP 비활성화**: 비활성화 하는 즉시 간부의 웹으로 확인이 가능합니다. 
 <p align="center">
    <img width="250" alt="Screen Shot 2022-11-02 at 7 41 08 AM" src="https://user-images.githubusercontent.com/60809681/199355801-357dc15a-89b1-4728-a0c1-56cd71cf34f9.png">
 </p>

   - ### App 기능들
 <p align="center">
    <img width="800" alt="Screen Shot 2022-10-31 at 1 04 38 AM" src="https://user-images.githubusercontent.com/60809681/198888840-beff93a3-102b-4530-958d-cbdf551ad611.png">
    <img width="800" alt="Screen Shot 2022-10-31 at 1 06 27 AM" src="https://user-images.githubusercontent.com/60809681/198888925-efefeeb8-3524-465e-8fdc-b6c39a229cba.png">
 </p>

&nbsp;
 
 - ## WEB
 
  - **로그인 페이지**: 관리자(간부)의 간편한 로그인/가입 페이지
 <p align="center">
    <img width="800" alt="Screen Shot 2022-11-02 at 12 46 39 PM" src="https://user-images.githubusercontent.com/60809681/199390737-0cd3ed1c-9746-41cd-a1fd-7b3d2db6d267.png">
 </p>
      
  - **모니터링 페이지**: 모니터링 페이지에서는 등록된 용사 수, 등록된 GPS 범위, 업로드 사진 수, 이상행위 탐지 수 등의 통계 확인이 가능하며, 업로드 사진 통계는 기간조정을 통해 그래프로 시각화하여 손쉽게 모니터링이 가능합니다. 또한 이상행위 탐지가 어떤 모바일 기기에서 탐지가 되었는지도 확인이 가능하고 요주 용사 또한 확인할 수 있습니다. 
 <p align="center">
    <img width="800" alt="Screen Shot 2022-11-02 at 12 48 05 PM" src="https://user-images.githubusercontent.com/60809681/199390928-b9d19636-1a78-4d4b-8d9e-dd26ad936599.png">
 </p>

  - **용사 관리 페이지**: 용사 관리 페이지에서는 간부가 Spyder APP이 활성화된 병사들과 비활성화된 병사들을 구분하여 한눈에 볼수 있으며, APP이 얼마나 비활성화 되어있었는지도 확인이 가능합니다.
 <p align="center">
    <img width="800" alt="Screen Shot 2022-11-02 at 12 50 39 PM" src="https://user-images.githubusercontent.com/60809681/199391240-0d38c257-9d70-4e8d-967f-06f672fd28df.png">
 </p>
 
   - **GPS 범위 등록 페이지**: GPS 범위 등록 페이지에서는 관리자(간부)가 Spyder의 보안구역을 설정할 수 있습니다. 설정된 보안구역 안에서는 Spyder 기능이 활성화 됩니다. 
 <p align="center">
    <img width="800" alt="Screen Shot 2022-11-02 at 12 52 48 PM" src="https://user-images.githubusercontent.com/60809681/199391543-1d4bcd43-651e-47fa-a1c8-b5759a21c55a.png">
 </p>

   - **업로드 사진 목록 페이지**: 업로드 사진 목록 페이지에서는 병사들이 찍은 사진들이 실시간으로 올라오는 것을 확인할 수 있습니다. openCV Image Processing을 통해 사진들은 1차적으로 검증이 되며, 간부들의 2차적 수동적인 확인을 통해 수락 또는 거절을 할 수 있습니다. 수락된 사진은 다시 병사들의 앱에서 다운로드 받아 확인이 가능하며, 거절된 사진은 확인이 불가합니다.
 <p align="center">
    <img width="800" alt="Screen Shot 2022-11-02 at 12 53 32 PM" src="https://user-images.githubusercontent.com/60809681/199391642-9b125637-6b46-4e92-97bc-bba44bacc0ac.png">
 </p>
 
   - ### Web 기능들
 <p align="center">
     <img width="800" alt="Screen Shot 2022-10-31 at 1 07 03 AM" src="https://user-images.githubusercontent.com/60809681/198888980-a42edb4f-ec45-4121-af9a-6817d92ef3c5.png">
     <img width="800" alt="Screen Shot 2022-10-31 at 1 07 29 AM" src="https://user-images.githubusercontent.com/60809681/198889003-8ffd1a74-d95a-4124-b8e3-7b7e06ef84f9.png">
     <img width="800" alt="Screen Shot 2022-10-31 at 1 07 43 AM" src="https://user-images.githubusercontent.com/60809681/198889021-fed51d73-974e-47f6-b8f4-c357da39beb5.png">
     <img width="800" alt="Screen Shot 2022-10-31 at 1 08 02 AM" src="https://user-images.githubusercontent.com/60809681/198889041-07802c67-fa91-439c-a10f-088f382b48b0.png">
     <img width="800" alt="Screen Shot 2022-10-31 at 1 14 40 AM" src="https://user-images.githubusercontent.com/60809681/198889359-fb498d1b-8f71-4278-a21b-597f3f95ae7d.png">
     <img width="800" alt="Screen Shot 2022-10-31 at 1 15 01 AM" src="https://user-images.githubusercontent.com/60809681/198889374-b3ecfd9b-73cf-4e03-b580-f54885b161ab.png">
 </p>

&nbsp;

## :earth_asia: 컴퓨터 구성 / 필수 조건 안내 (Prerequisites)

* <img width="20" height="20" alt="image_es6" src="https://user-images.githubusercontent.com/81582559/198014278-87725be1-b3cb-4d23-b097-e22d90e2bcab.jpg" /> ECMAScript 6 지원 브라우저 사용
* <img width="20" alt="image_chrome" src="https://user-images.githubusercontent.com/81582559/198014428-799a5490-0fb3-43e2-a871-e8b56679fc8a.png" />Google Chrome 버젼 77 이상 (권장)
* <img width="20" alt="image_andriod_Oreo" src="https://user-images.githubusercontent.com/81582559/198014556-9f54c0cf-acca-4ffb-a3a0-a93aafae5afb.png" /> Android 버전 8.0 (Oreo) 이상 (권장)

&nbsp;

## :computer: 기술 스택 (Technique Used) 

Below is the specification for technologies used in Spyder:

* [ Infrastructure] - AWS (Amazon Web Service) - EC2, S3 (Cloud Storage)
* [ Database ] - Postgresql
* [ Language ] - Java (App), Python 3.8 (Web BackEnd), Html, Javascript, CSS (Web FrontEnd)
* [ Framework ] - Django (BackEnd), Bootstrap (FrontEnd)
* [ IDE ] - Android Studio (App), Visual Studio Code (Web)
* [ Open-source Libraries ] - OpenCV (for image processing), EXIF Analysis (for image analysis), Django (rest_framework) 

[![My Skills](https://skills.thijs.gg/icons?i=py,java,postgres,js,html,css,md)](https://skills.thijs.gg)

&nbsp;

## :inbox_tray: 설치 안내 (Installation Process)

Install from git. Download zip file or git clone.

Install python dev and pip3:
```sh
$ apt-get install python3-dev
$ apt-get install python3-pip
```

For production environment:
```sh
$ pip3 install virtualenv
$ virtualenv envspyder
```

Enter environment:
```sh
$ cd envspyder/bin
$ source activate
```
If virtualenv is successfully activated, the command line should look like (envspyder) ~~~

Spyder requires a number of python libraries to run. Install requirements.txt:
```sh
$ pip3 install -r requirements.txt
```

Install OpenCV Library:
```sh
$ brew install ninja pkg-config
$ wget http://dlib.net/files/dlib-19.2.tar.bz2 -O /tmp/dlib-19.2.tar.bz2
$ tar xvjf /tmp/dlib-19.2.tar.bz2 -C ./
$ cd dlib-19.2
$ mkdir build && cd build
$ cmake -G Ninja ..
$ cmake --build . --config Release
$ cd ../
$ sudo python setup.py install
```
If installing setup.py does not work:
```sh
$ brew cask install xquartz
$ brew install gtk+3 boost
$ brew install boost-python3
$ pip3 install face_recognition
$ pip3 install opencv-python
```

Migrate Postgres DB:
```sh
$ python3 manage.py makemigrations
$ python3 manage.py migrate
```

Create superuser for Postgres DB:
```sh
$ python3 manage.py createsuperuser
```

Collect static and Run server (port: 8080):
```sh
$ python3 manage.py collectstatic
$ python3 manage.py runserver 0.0.0.0:8080
```

&nbsp;

## :rocket: 기대효과 및 전망

#### 기대효과
- **업무 효율성 증가**: 카메라의 안전한 사용을 통해 장병들의 업무 효율성과 속도가 증가할 수 있습니다.
- **강력한 보안**: 간부의 실시간 WEB 모니터링을 통해 보안 유출을 방지하고 더욱 강력한 보안성을 자랑합니다.
- **신속한 상황 보고**: 군 부대 내 병영생활 문제에 대한 신속한 상황보고가 가능합니다.

#### 전망
- **데이터 수집 ML 강화**: 지속된 정보 및 데이터 수집으로 스파이더의 사진 분석 머신러닝을 강화할 수 있습니다.
- **AI 기밀유출 탐지**: 축적된 데이터로 학습 시킨 AI를 이용해 기밀유출 사진을 탐지하여 국방 보안을 지킬 수 있습니다.
- **보안 사례 통계분석**: 지속된 정보와 데이터 수집을 활용한 보안 사고 및 사례의 통계 분석으로 보안 사고를 예방할 수 있습니다.

<p align="center">
  <img width="900" src="https://user-images.githubusercontent.com/60809681/199394662-dfe6c8b8-7a16-4bd9-908f-1e761868e07f.gif" alt="animated" />
</p>

&nbsp;
 
## :two_men_holding_hands: 팀 정보 (Team Information)

|  팀원  |         소속          |     GitHub     |         Email         |
| :----: | :-------------------: | :------------: | :-------------------: |
| 조용인 |  육군 17사단   | yongincho |    choyongin21@gmail.com    |
| 김진 | 육군 수도군단 |  kimjin1425@naver.com   | kimjin1425@naver.com |

- #### :man_teacher: 멘토: 장기영 멘토님 

&nbsp;

## :clipboard: 저작권 및 사용권 정보 (Copyleft / End User License)
 * [MIT](https://github.com/osam2020-WEB/Sample-ProjectName-TeamName/blob/master/license.md)

This project is licensed under the terms of the MIT license.
