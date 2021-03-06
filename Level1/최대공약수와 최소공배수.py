'''두 수를 입력받아 두 수의 최대공약수와 최소공배수를 반환하는 함수, solution을 완성해 보세요. 배열의 맨 앞에 최대공약수, 그다음 최소공배수를 넣어 반환하면 됩니다. 예를 들어 두 수 3, 12의 최대공약수는 3, 최소공배수는 12이므로 solution(3, 12)는 [3, 12]를 반환해야 합니다.

제한 사항
두 수는 1이상 1000000이하의 자연수입니다.
입출력 예
n	m	return
3	12	[3, 12]
2	5	[1, 10]
입출력 예 설명
입출력 예 #1
위의 설명과 같습니다.

입출력 예 #2
자연수 2와 5의 최대공약수는 1, 최소공배수는 10이므로 [1, 10]을 리턴해야 합니다.'''
def gcd(n,m):
    mod = m % n
    if mod != 0:
        m, n = n, mod
        return gcd(n, m)
    else:
        return n

def solution(n,m):
    return [gcd(n,m),int(m*n/gcd(n,m))]
print(solution(3,12))
print(solution(2,5))
# 아 나 머리아파 죽을거 같음,,, 오늘 마크다운 정리 했으니깐 이거 내일풀게,,,
#야 그래 놓고 너 안풀었잖아,,,, 집가면 진짜 열심히 해라,,,
'''
유클리드 호제법이용
유클리드 호제법 : 두 수의 최대공약수를 구하는 알고리즘이다.
유클리드(Euclid)에 의해 기원전 300년경에 발견된 가장 오래된 알고리즘이다.
호제법이란? 두 수가 서로 상대방 수를 나누어서 결국 원하는 수를 얻는 알고리즘을 말한다.
'''