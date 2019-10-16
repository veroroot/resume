# 요약
* 사용언어 : Python
* 데이터 수집 : KRX(한국 거래소)제공 데이터
	참고 - http://www.krx.co.kr/main/main.jsp
* 데이터 수집 : Forexfactory(셰계외환시장 관련 사이트) 크롤링 및 스크래핑
	참고 - https://www.forexfactory.com/
* 데이터 전처리 : 결측치 처리, 날짜 및 기술 분석을 위한 파생변수 생성(MA, BB, ATR, Stochastic),
     Forex 데이터 전처리 후 일별 기준으로 선물종가 데이터와 병합
* EDA : 일반적으로 증권시장에서 진행하는 기술적 분석
* 모델링 : KRX 데이터를 활용하여 ARIMA를 통한 시계열 분석 및 선형회귀 분석 진행.
     Forex 데이터 병합 전과 후로 나누어서 분류 모델 진행(-1, 0, 1).
     모델링 방법은 SVC, LGBM, RandomForest를 이용.
