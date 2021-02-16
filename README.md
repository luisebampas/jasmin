# Jasmin 웹 사이트 프로젝트

## 2.2 (화)

* 기획서 작성
* 개발계획 수립
* ERD Cloud 제작
  * https://www.erdcloud.com/d/cQk8e3RjMckBzT2u4
* mySQL 데이터베이스 sql문 작성
  * 테이블 및 샘플 데이터
* django framework와 bootstrap을 이용하여 웹 페이지 제작
  * 기초적인 틀 구상



## 2.3 (수)

* django framework와 bootstrap을 이용하여 웹 페이지 제작

  * 로그인 페이지 작성
  * 메인페이지, 아이템목록 css 수정 및 작성
  
  


## 2.4 (목)

* django framework와 bootstrap을 이용하여 웹 페이지 제작
  
* 아이템 상세정보 페이지 작성
  
* 각자 화면구현 작업 시작
  * base 템플릿 구현
  * base의 nav, side bar 공통요소 공유하며 다른 페이지들 제작
  * login, join, itemlist, itemdetail, payment 템플릿의 section 구현.
  * 추후 과제 : base 템플릿, 조원 각자의 템플릿 정교화.
  
  

## 2.5 (금)

* django framework와 bootstrap을 이용하여 웹 페이지 제작
  * 아이템 상세정보 페이지 css 작업과 jQuery를 이용한 기능추가

  * 로그인 페이지
  * 메인페이지, 아이템목록 css 수정 및 작성
* 각자 화면구현 작업 계속
* paydetail 화면 구현
* 각자 branch에 작업물 저장. 



## 2.8 (월)

* 각자 진행중인 작업물 병합
* 인터프리터, db, 경로, 규격 표준화 작업. 



## 2.9 (화)

* 상품 목록의 페이지 번호 구현
  
  * django를 이용하여 상품 목록의 페이지 번호가 생성되도록 추가
  
  

## 2.10 (수)

* 성시영  작업 내역

   - 결제 요청시 로그인 상태면 payment 템플릿으로 이동, 비로그인 상태면 login템플릿으로 redirect 기능 구현.

   - itemcontent에서 아이템  정보를 불러와 회원이 원하는 아이템 결제 가능하도록 구현. 

   - payment, paydetail 화면 수정. 기능 보완.

   - 추후 처리 작업 

     ​	1) 결제 관련 정보  DB의 payment, orderlist 등 테이블에 인서트

     ​	2) viewr 화면 및 기능 구현.  cartlist 화면 구현

     ​    3) 이미지 로고 제작, ui 꾸미기 등 기타 디자인 작업
   
* 상품 검색 기능 구현

   * SQL문의 LIKE를 이용하여 검색결과 출력
   * 검색할 파라미터를 지정하고 현재 보고 있는 카테고리에 따라 검색되도록 연결함

* 상품 목록 정렬 기능 구현

   *  SQL문의 ORDER BY를 이용하여 정렬
   * django와 jQuery를 이용하여 구현
   * jQuery를 통해 <select>를 바꾸는 것으로 <form>이 submit 되도록 함

* 상품 목록의 페이지 번호 수정

   * HTML의 <form> - <select> - <option>의 기본값 selected 속성을 django로 지정하는 것을   jQuery를 이용하여 지정하도록 수정



## 2.10 (목)

* 상품 목록 페이지에서 정렬 기능을 만들고 검색 기능과 연동해서 사용될 수 있게 수정



## 2.15 (월)

* 연휴 동안 작업한 내용을 병합
* 관리자 페이지를 따로 만든 것을 합침
* 대문 페이지 제작, 폰트 수정, 영어로 된 메뉴를 한글로 수정
* 관리자 상품 추가 페이지 기능 추가 관련 수정과 이를 이용한 DB 삽입작업
  * 저자 검색을 하여 최근 저서 5개의 목록과 함께 선택한 저서의 데이터를 '새 책 추가' 공간에 입력되는 버튼을 만듬
* 직접 작업한 CSS들을 하나로 합침



## 2.16 (화)

