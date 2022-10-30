# 촘촘한 보안망, Spyder
<img width="244" alt="spyderLogo" src="https://user-images.githubusercontent.com/60809681/198888652-c4a7a945-79b5-418e-bd7c-43118678cfad.png">

## 프로젝트 소개
- Spyder는 기존 국방모바일보안 앱을 보완한 솔루션으로, 머신러닝을 이용한 군장병 기밀유출 보안 솔루션입니다. 휴대폰 안에 저장된 사진들의 GPS 데이터를 이용해 검사하여 부대 내에서 찍은 미디어를 감지하고 스파이더 웹에 업로드 시킵니다. 감지된 사진들은 모바일 기기에서 즉시 삭제됩니다. Spyder 웹에 업로드 된 후, 감지된 사진들은 1차적 OpenCV 머신러닝 검증과 2차적 간부의 확인 후 병사의 휴대폰에서 다시 원본 파일의 다운로드가 가능합니다. 

- 처음 입대하거나 휴가에서 복귀하는 장병들은 Spyder을 활성화 시킴으로서 휴대폰 안에 저장된 사진들을 빠르게 분석해 군 기밀 유출을 차단합니다. 또한, 기존 보안 앱과 달리 관리자 모니터링 웹페이지를 통해, 부대 내에 있는 휴대폰들의 Spyder가 켜져 있는지 실시간으로 보여줌으로서 강력한 보안성을 자랑합니다.


##  :page_facing_up: 목차

 - 1.[기능 설명 및 시연 영상 ](#hammer-기능-설명-및-시연-영상)
 - 2.[컴퓨터 구성 / 필수 조건 안내](#earth_asia-컴퓨터-구성--필수-조건-안내-prerequisites)
 - 3.[기술 스택](#computer-기술-스택-technique-used)
 - 4.[설치 안내](#inbox_tray-설치-안내-installation-process)
 - 5.[팀원 정보](#two_men_holding_hands-팀-정보-team-information)
 - 6.[저작권 및 사용권 정보](#clipboard-저작권-및-사용권-정보-copyleft--end-user-license)



## :hammer: 기능 설명 및 시연 영상 
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
### WEB(Back-end)
 - <img width="100" alt="image_python" src="https://user-images.githubusercontent.com/81582559/198014024-c03350ba-2b5a-4a12-a8f3-3f62a55d128f.png"/> 
     
     - Framework:    <img width="100" alt="image_Django" src="https://user-images.githubusercontent.com/81582559/198014308-01ba2f85-fcc2-4cca-afbb-b499528a92ed.png"/>
 - <img width="40" alt="image_aws EC2" src="https://user-images.githubusercontent.com/81582559/198014468-f9f456b7-99c1-461a-a0ad-be70699db730.png"/> AWS EC2
 
### WEB(Front-end)
 - <img width="35" alt="image_html" src="https://user-images.githubusercontent.com/81582559/198014244-a5d2ce2b-131f-4ce4-a55e-121833d33d9f.png"/> HTML,<img width="25" alt="image_css" src="https://user-images.githubusercontent.com/81582559/198014364-be4745d7-ed32-4af1-a231-789f38ae68e1.png"/> CSS, <img width="35" alt="image_js" src="https://user-images.githubusercontent.com/81582559/198014147-177a9e5d-354f-4a6f-9105-0b25a165019f.png" /> JS

### APP
 - <img width="35"  alt="image_java" src="https://user-images.githubusercontent.com/81582559/198014214-88a75a96-c77d-4268-986d-aaebea2e579d.PNG" /> Java
     - IDE: <img width="35" alt="image_android_studio" src="https://user-images.githubusercontent.com/81582559/198014502-36293595-5244-4e96-b057-12aaa74b5895.png" /> Android Studio

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
