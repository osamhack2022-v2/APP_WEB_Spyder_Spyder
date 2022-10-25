# 촘촘한 보안망, Spyder
<img width="244" alt="image" src="https://user-images.githubusercontent.com/60809681/196021756-80256d4a-08dc-4b0f-a035-0b539141f8f0.png">

## 프로젝트 소개
- Spyder는 기존 국방모바일보안 앱을 보완한 보안 솔루션으로, 카메라 차단 기능뿐만 아니라, 휴대폰 안에 저장된 사진들을 검사하여 국방보안에 위험요소가 있는지 분석해줍니다. 처음 입대하거나 휴가에서 복귀하는 장병들은 Spyder을 활성화 시킴으로서 카메라 기능을 차단하고 휴대폰 안에 저장된 사진들을 빠르게 분석해 군 기밀 유출을 차단합니다.

- 또한, 기존 보안 앱과 달리 관리자 모니터링 웹페이지를 통해, 부대 내에 있는 휴대폰들의 Spyder가 켜져 있는지 실시간으로 보여줍니다. 카메라 기능이 켜져 있는 휴대폰을 바로 알려주고 통제가 가능하며, 저장된 사진 중 관리자가 설정한 위치정보 내에서 촬영된 사진들만 검사하여 모니터링이 가능합니다. 


##  :page_facing_up: 목차

 - 1.[기능 설명 및 시연 영상 ](#hammer-기능-설명-및-시연-영상)
 - 2.[컴퓨터 구성 / 필수 조건 안내](#earth_asia-컴퓨터-구성--필수-조건-안내-prerequisites)
 - 3.[기술 스택](#computer-기술-스택-technique-used)
 - 4.[설치 안내](#inbox_tray-설치-안내-installation-process)
 - 5.[팀원 정보](#two_men_holding_hands-팀-정보-team-information)
 - 6.[저작권 및 사용권 정보](#clipboard-저작권-및-사용권-정보-copyleft--end-user-license)



## :hammer: 기능 설명 및 시연 영상 
 - APP
   
     - GPS 강제 ON
     - 부대 GPS 내에서 찍은 사진 감지
     - 감지된 사진 꺠트리고 서버에 업로드
     - 확인된 사진 서버에서 다운로드
     - 카메라 차단 기능
     - 위치정보 설정 기능
     - 사진의 위치정보 분석 기능 (EXIF Analysis)
 - WEB
     - 관리자 로그인
     - 부대 모바일 기기 리스트
     - APP on/off 체크 및 기록
     - GPS 구간 설정
     - 지정된 구역에서 찍은 사진 서버에서 다운로드
     - OpenCV 이용한 ML 무기 감지
     - 앱이 설치된 단말기 감시 기능
     - 간부의 수동 체크
     - 사진 파일 원상 복구 및 서버 업로드
     - 앱 강제 종료 감시 기능
     - 위치정보에 위반되는 사진 모니터링 기능

## :earth_asia: 컴퓨터 구성 / 필수 조건 안내 (Prerequisites)


* <img width="50" height="50" alt="image_es6" src="https://github.com/newbie10001/zoomClone/blob/24f9b04b975873d6fc0e981655f82116427922de/img/es6.jpg" /> ECMAScript 6 지원 브라우저 사용
* <img width="50" alt="image_chrome" src="https://github.com/newbie10001/zoomClone/blob/de54e4f293ee9c72574ce6ac2c7cb54266ef906e/img/chrome.png" />Google Chrome 버젼 77 이상 (권장)
* <img width="50" alt="image_andriod_Oreo" src="https://github.com/newbie10001/zoomClone/blob/e7f4ec0a22e3bb15a0fff473cf27ac63a4bc2dca/img/andriod_Oreo.png" /> Android 버전 8.0 (Oreo) 이상 (권장)

## :computer: 기술 스택 (Technique Used) 
### WEB(Back-end)
 - <img width="100" alt="image_python" src="https://github.com/newbie10001/zoomClone/blob/e7f4ec0a22e3bb15a0fff473cf27ac63a4bc2dca/img/python.png"/> 
     
     - Framework:    <img width="100" alt="image_Django" src="https://github.com/newbie10001/zoomClone/blob/e7f4ec0a22e3bb15a0fff473cf27ac63a4bc2dca/img/django-_ogo.png"/>
 - <img width="40" alt="image_aws EC2" src="https://github.com/newbie10001/zoomClone/blob/49029d63a2fcbafb7344881408a7faedad4424e5/img/aws%20EC2.png"/> AWS EC2
 
### WEB(Front-end)
 - <img width="35" alt="image_html" src="https://github.com/newbie10001/zoomClone/blob/e7f4ec0a22e3bb15a0fff473cf27ac63a4bc2dca/img/HTML.png"/> HTML,<img width="25" alt="image_css" src="https://github.com/newbie10001/zoomClone/blob/b6dc316efac472f6a657369c3d09c2eff07a9649/img/css.png"/> CSS, <img width="35" alt="image_js" src="https://github.com/newbie10001/zoomClone/blob/824f915c61987210c7a2a37caa69f24cf9dc913a/img/js_logo.png" /> JS

### APP
 - <img width="35"  alt="image_java" src="https://github.com/newbie10001/zoomClone/blob/e7f4ec0a22e3bb15a0fff473cf27ac63a4bc2dca/img/java.PNG" /> Java
     - IDE: <img width="35" alt="image_android_studio" src="https://github.com/newbie10001/zoomClone/blob/e7f4ec0a22e3bb15a0fff473cf27ac63a4bc2dca/img/android_studio.png" /> Android Studio

## :inbox_tray: 설치 안내 (Installation Process)
```bash
$ git clone git주소
$ yarn or npm install
$ yarn start or npm run start
```
 
## :two_men_holding_hands: 팀 정보 (Team Information)

|  팀원  |         소속          |     GitHub     |         Email         |
| :----: | :-------------------: | :------------: | :-------------------: |
| 조용인 |  육군 17사단   | yongincho |    choyongin21@gmail.com    |
| 김진 | 육군 수도군단 |  kimjin1425@naver.com   | kimjin1425@naver.com |

## :clipboard: 저작권 및 사용권 정보 (Copyleft / End User License)
 * [MIT](https://github.com/osam2020-WEB/Sample-ProjectName-TeamName/blob/master/license.md)

This project is licensed under the terms of the MIT license.
