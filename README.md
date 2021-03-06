# Deep_Learning_DBDBDeep!_Recommend_OOTD
# :dress: _주제: 딥러닝을 이용한 나만의 코디 추천_ :tshirt:
------------------------------------------------------------
## 사용언어 :computer:

<img src="https://img.shields.io/badge/Python-3766AB?style=flat-square&logo=Python&logoColor=white"/></a>      _(파이썬)_

-----------------------------------------------------------

## 개발기간 :computer:

2021/03/26 ~ 2021/05/22

-----------------------------------------------------------

## 개발자 :computer:


**사호진**[@Hojin-Sa](https://github.com/Hojin-Sa)   **한현수**[@hyun-s](https://github.com/hyun-s)   **김진성**[@KimJinSungDataScientist](https://github.com/KimJinSungDataScientist)   **고동천**[@cheon4050](https://github.com/cheon4050)

-----------------------------------------------------------


## 목적 및 기획 배경 :seedling:
패션에 대한 관심 증대!

👉옷을 잘 못 입는 ‘패션 고자’들 등장!

👉옷에 관심이 생겼는데 어떻게 입어야 할지 모르겠어!

👉옷은 많은데 어떻게 매치해야할지 모르겠어!
        
🚩
**"자신의 옷장에 있는 옷으로 모델들의 트렌디한 코디를 토대로 조합을 추천 해주는 프로그램!"**


------------------------------------------------------------


## 사용프로그램 :computer:

**Pycharm** : 데이터셋 가져오기, 모델 만들기, UI 구현하기

-----------------------------------------------------------

## 개발전략
- 저희는 우선 파이썬을 사용해 데이터크롤링을 진행하였습니다. 말 그대로 웹페이지 내용 중 필요한 데이터를 끌어와 쓰는 기법으로 저희는 코디의 사진과 이름을 가져왔습니다.
- 딥러닝 중에서 주로 이미지 인식에 많이 사용되는 CNN은 한국말로는 합성곱 신경망입니다. CNN을 사용하여 이미지 분류 정확도를 최대화하는 필터를 자동으로 학습할 수 있습니다.
- CNN 기반의 딥러닝 모델의 구조를 결정하는 방법을 제안한 EfficientNet입니다. EfficientNet 메인 아이디어는 CNN에서 모델의 깊이, 채널의 크기, 이미지의 해상도의 최적의 비율을 결정하는 것입니다. 
- 크롤링을 통해 단계로 각 상품의 카테고리 정보와 색상 정보를 추출했습니다.
- 이후 저희는 기존의 imagenet으로 학습된 efficinetnet b3 모델을 사용하여 이미지의 feature를 추출하고, classifier만 학습하는 형식의 transfer learning을 이용하여 모델을 구현하였습니다.

---------------------------------------------------------

## 결과
<img width="566" alt="KakaoTalk_20210523_203246383" src="https://user-images.githubusercontent.com/69353667/119258858-75f8d700-bc06-11eb-84e2-8ecce7408d60.png">

<img width="562" alt="KakaoTalk_20210523_203246383_01" src="https://user-images.githubusercontent.com/69353667/119258881-9cb70d80-bc06-11eb-9093-56f9ded0463b.png">

<img width="562" alt="KakaoTalk_20210523_203246383_02" src="https://user-images.githubusercontent.com/69353667/119258896-a8a2cf80-bc06-11eb-9570-296954ae22c0.png">


<img width="562" alt="KakaoTalk_20210523_203246383_03" src="https://user-images.githubusercontent.com/69353667/119258904-b0fb0a80-bc06-11eb-8b20-128f40ee283e.png">

<img width="564" alt="KakaoTalk_20210523_203246383_04" src="https://user-images.githubusercontent.com/69353667/119258917-b8baaf00-bc06-11eb-8cd2-6f47921a1d33.png">


