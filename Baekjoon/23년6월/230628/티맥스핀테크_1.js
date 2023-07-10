function solution(penter, pexit, pescape, data) {
  let answer = "";
  // 원소들의 길이 len 변수 선언
  let len = penter.length;
  // 원소의 시작지점 s, 끝지점 e, 현재 data 문자열 저장해줄 변수 now 설정
  let s = 0;
  let e = len - 1;
  let now = "";
  // data 앞에 penter 붙이기
  answer += penter;
  // e가 data 끝에 닿을때까지 반복해서 문자열 점검
  while (e < data.length) {
    // 원소 하나를 now에 저장
    for (i = s; i <= e; i++) {
      now += data[i];
    }
    // now가 이진문자열들과 같다면 원소 앞에 pescape 붙혀주기
    console.log(now);
    if (now == penter || now == pexit || now == pescape) {
      answer += pescape;
    }
    // 원소 붙혀주고 now 초기화
    answer += now;
    now = "";
    // s, e 재설정
    s += len;
    e += len;
  }
  // data 끝에 pexit 붙혀주기
  answer += pexit;
  return answer;
}

solution("1100", "0010", "1001", "1101100100101111001111000000");
solution("10", "11", "00", "00011011");
