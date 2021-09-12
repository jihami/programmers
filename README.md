# 간단정리
### 함수
 - 내장함수
    - min() 제일 작은 값 찾음 [제일 작은 수 제거하기.py]
    - max() 가장큰 값 찾아줌
    - sum() 값을 더해줌(디폴트 값 : 0 | ex : sum(list_a,1))
    - reversed() 딕셔너리 지원 X, ex : list_a = list(reversed(a)) [자연수 뒤집어 배열로 만들기.py]
    - join() 문자열로 만들어줌, ex : " ".join(list_a)
 - list()
    - remove() 값 삭제 [제일 작은 수 제거하기.py]
    - append() 리스트에 값추가 [자연수 뒤집어 배열로 만들기.py]
    - reversed() 값을 뒤집는 함수, 값을 반환하지 않고 변환한다. [자연수 뒤집어 배열로 만들기.py]
- 모듈
  - datetime
   - date 
    - datetime.date 객체는 년,월,일을 인수로 전달하여 생성 가능
    - today() 오늘 날짜 구함 ex : today=date.today() # 앞에있는 today는 변수
    - year 년을 구함 : toay.year
    - month 월을 구함 ex : toay.month
    - day 일을 구함 ex : toay.day
    - weekday() 요일을 구함,월요일부터 0으로 반환 ex : toay.weekday()
    - repalce() 객체의 년,월,일을 바꿈 ex : date1.replace(day=31)
     
 <!--  - time
   - datetime
   https://windybay.net/post/20/ 참고하기 -->
