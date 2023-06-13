function solution(nums) {
    var answer = 0;
    var cnt = nums.length / 2;

    // 중복 제거
    var arr = nums.filter((element, index) => {
        return nums.indexOf(element) === index;
    });

    if (arr.length >= cnt) {
        answer = cnt;
    } else {
        answer = arr.length;
    }
    return answer;
}