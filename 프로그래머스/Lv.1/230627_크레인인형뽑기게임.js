function solution(board, moves) {
  const basket = [];
  let answer = 0;
  moves.forEach((move) => {
    for (let j = 0; j < board.length; j++) {
      if (move - 1 != j) continue;
      for (let i = 0; i < board.length; i++) {
        if (move - 1 == j && board[i][j]) {
          basket.push(board[i][j]);
          board[i][j] = 0;
          break;
        }
      }
    }
    if (
      basket.length >= 2 &&
      basket[basket.length - 1] == basket[basket.length - 2]
    ) {
      basket.pop();
      basket.pop();
      answer += 2;
    }
  });
  return answer;
}

const result = solution(
  [
    [0, 0, 0, 0, 0],
    [0, 0, 1, 0, 3],
    [0, 2, 5, 0, 1],
    [4, 2, 4, 4, 2],
    [3, 5, 1, 3, 1],
  ],
  [1, 5, 3, 5, 1, 2, 1, 4]
);
console.log(result);
