# 요약
* 사용언어 : R
* 데이터 수집 : Kaggle 제공 Data(지금은 Kaggle에서 이용 불가)
	참고 - https://github.com/Niteeshkanungo/Tftb/blob/master/BreadBasket_DMS.csv
* 데이터 전처리 : R의 dplyr 명령어를 활용하여 다양한 변수 생성(날짜 -> 월, 일, 요일 등)
* EDA : 시간과 판매량의 관계를 통해 다양한 판매 전략 수립
* 모델링 : Transaction 형태로 변형하여 Apriori 알고리즘 적용. 
		특이점 : 지지도(support)와 향상도(lift)로 나타내는데 한계가 있어서 IS측도를 통해 연관분석 진행.
