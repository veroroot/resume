# 요약
* 사용언어 : Python
* 데이터 수집 : Kaggle 제공 Data
	참고 - https://www.kaggle.com/rounakbanik/the-movies-dataset
* 데이터 전처리 : 결측치 처리, metadata와 다른 데이터들과 병합, 분석에 필요한 파생변수 생성
* EDA : 영화 관련 장르, 배우, 감독 등 wordcloud와 그래프를 통해 빈도수 분석, 수익률과 영화 제작 관련 요소와의 관계 분석
* 모델링 : User Id에 해당되는 평점과 해당 영화 간의 유사도를 측정하여 KNN방식과 SVD방식을 통해 영화 추천 시스템 구축. 
	영화 평점은 Scaling을 통해 정규화. Suprise 패키지 이용.
