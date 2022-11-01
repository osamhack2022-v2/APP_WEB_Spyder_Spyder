<h1 align="center"> 촘촘한 보안망, Spyder <h1>
<p align="center">
![Spyder_Gif_AdobeExpress](https://user-images.githubusercontent.com/60809681/199347082-f33599b5-4c8b-4dde-83b3-b513b183b834.gif)
</p>

## 프로젝트 소개
- Spyder는 기존 국방모바일보안 앱을 보완한 솔루션으로, 머신러닝을 이용한 군장병 기밀 유출 보안 솔루션입니다. 휴대폰 안에 저장된 사진들의 GPS 데이터를 검사하여 부대 내에서 찍은 미디어를 감지하고 Spyder Web에 업로드 시킵니다. 감지된 사진들은 모바일 기기에서 즉시 삭제됩니다. Spyder Web에 업로드 된 후, 감지된 사진들은 1차적 OpenCV 머신러닝 검증과 2차적 간부의 수동 확인 후 병사의 휴대폰에서 다시 원본 파일의 다운로드가 가능합니다. 

- 처음 입대하거나 휴가에서 복귀하는 장병들은 Spyder을 활성화 시킴으로서 휴대폰 안에 저장된 사진들을 빠르게 분석해 군 기밀 유출을 차단합니다. 기존 보안 앱과 달리 카메라 사용이 가능하기 때문에 향상된 업무 효율성과 신속한 상황 보고가 가능하고, 관리자 모니터링 웹페이지를 통해 부대 내에 있는 휴대폰들의 Spyder App이 켜져 있는지 실시간으로 보여줌으로서 강력한 보안성을 자랑합니다.


##  :page_facing_up: 목차

 - 1.[기능 설명 ](#hammer-기능-설명-및-시연-영상)
 - 2.[컴퓨터 구성 / 필수 조건 안내](#earth_asia-컴퓨터-구성--필수-조건-안내-prerequisites)
 - 3.[기술 스택](#computer-기술-스택-technique-used)
 - 4.[설치 안내](#inbox_tray-설치-안내-installation-process)
 - 5.[팀원 정보](#two_men_holding_hands-팀-정보-team-information)
 - 6.[저작권 및 사용권 정보](#clipboard-저작권-및-사용권-정보-copyleft--end-user-license)


## :hammer: 기능 설명 
 - ## APP
     - <img width="800" alt="Screen Shot 2022-10-31 at 1 04 38 AM" src="https://user-images.githubusercontent.com/60809681/198888840-beff93a3-102b-4530-958d-cbdf551ad611.png">
     - <img width="800" alt="Screen Shot 2022-10-31 at 1 06 27 AM" src="https://user-images.githubusercontent.com/60809681/198888925-efefeeb8-3524-465e-8fdc-b6c39a229cba.png">

 - ## WEB
     - <img width="800" alt="Screen Shot 2022-10-31 at 1 07 03 AM" src="https://user-images.githubusercontent.com/60809681/198888980-a42edb4f-ec45-4121-af9a-6817d92ef3c5.png">
     - <img width="800" alt="Screen Shot 2022-10-31 at 1 07 29 AM" src="https://user-images.githubusercontent.com/60809681/198889003-8ffd1a74-d95a-4124-b8e3-7b7e06ef84f9.png">
     - <img width="800" alt="Screen Shot 2022-10-31 at 1 07 43 AM" src="https://user-images.githubusercontent.com/60809681/198889021-fed51d73-974e-47f6-b8f4-c357da39beb5.png">
     - <img width="800" alt="Screen Shot 2022-10-31 at 1 08 02 AM" src="https://user-images.githubusercontent.com/60809681/198889041-07802c67-fa91-439c-a10f-088f382b48b0.png">
     - <img width="800" alt="Screen Shot 2022-10-31 at 1 14 40 AM" src="https://user-images.githubusercontent.com/60809681/198889359-fb498d1b-8f71-4278-a21b-597f3f95ae7d.png">
     - <img width="800" alt="Screen Shot 2022-10-31 at 1 15 01 AM" src="https://user-images.githubusercontent.com/60809681/198889374-b3ecfd9b-73cf-4e03-b580-f54885b161ab.png">


## :earth_asia: 컴퓨터 구성 / 필수 조건 안내 (Prerequisites)

* <img width="30" height="30" alt="image_es6" src="https://user-images.githubusercontent.com/81582559/198014278-87725be1-b3cb-4d23-b097-e22d90e2bcab.jpg" /> ECMAScript 6 지원 브라우저 사용
* <img width="30" alt="image_chrome" src="https://user-images.githubusercontent.com/81582559/198014428-799a5490-0fb3-43e2-a871-e8b56679fc8a.png" />Google Chrome 버젼 77 이상 (권장)
* <img width="30" alt="image_andriod_Oreo" src="https://user-images.githubusercontent.com/81582559/198014556-9f54c0cf-acca-4ffb-a3a0-a93aafae5afb.png" /> Android 버전 8.0 (Oreo) 이상 (권장)


## :computer: 기술 스택 (Technique Used) 

Below is the specification for technologies used in Spyder:

* [ Infrastructure] - AWS (Amazon Web Service) - EC2, S3 (Cloud Storage)
* [ Database ] - Postgresql
* [ Language ] - Java (App), Python 3.8 (Web BackEnd), Html, Javascript, CSS (Web FrontEnd)
* [ Framework ] - Django (BackEnd), Bootstrap (FrontEnd)
* [ IDE ] - Android Studio (App), Visual Studio Code (Web)
* [ Open-source Libraries ] - OpenCV (for face identification), EXIF Analysis (for image analysis), Django (rest_framework) 


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
 
 
## :two_men_holding_hands: 팀 정보 (Team Information)

|  팀원  |         소속          |     GitHub     |         Email         |
| :----: | :-------------------: | :------------: | :-------------------: |
| 조용인 |  육군 17사단   | yongincho |    choyongin21@gmail.com    |
| 김진 | 육군 수도군단 |  kimjin1425@naver.com   | kimjin1425@naver.com |


## :clipboard: 저작권 및 사용권 정보 (Copyleft / End User License)
 * [MIT](https://github.com/osam2020-WEB/Sample-ProjectName-TeamName/blob/master/license.md)

This project is licensed under the terms of the MIT license.
