// tsurukame3-ans.js
// By kota ninomiya

/**
 *randomInt - 指定範囲内のおいて整数を乱数生成
 *
 * @param {Number} min 最小値
 * @param {Number} max 最大値
 * @return {Number} 乱数
 */
function randomInt(min, max) {
  return Math.floor(Math.random() * (max - min) + min)
}

/**
  *checkCraneAndTurtle - つるとかめの数を数える
  *
  * @param {Number} total_legs 足の本数の合計
  * @param {Number} total_head 頭の数の合計
  * @param {Number} crane_legs つるの足の数
  * @param {Number} turtle_legs かめの足の数
  * @return {null} 
  */
function checkCraneAndTurtle(total_head, total_legs, crane_legs, turtle_legs) {
  console.log(`頭が${total_head}個で，足が${total_legs}本で`)
  console.log(`つるの足が${crane_legs}本で，かめの足が${turtle_legs}本のとき`)
  numOfPairs = 0

  // ここに色々処理を書く
  // 以下にプログラムを作成せよ
  num_crane = 0

  while (num_crane < total_head) {
    num_turtle = total_head - num_crane
    if (num_crane * crane_legs + num_turtle * turtle_legs == total_legs) {
      numOfPairs++
    }
    num_crane++
  }
  if (numOfPairs == 1) {
    console.log(`鶴は${num_crane}匹，亀は${num_turtle}匹です`)
  } else {
    console.log('そんな状況はありません')
  }
  console.log('\n')
}

checkCraneAndTurtle(10, 2, 2, 4); // 「鶴が4匹，亀が6匹」と出力
checkCraneAndTurtle(65, 52, 18, 76); // 「そんな状況はありません」と出力
checkCraneAndTurtle(90, 8, 46, 47); // 「そんな状況はありません」と出力
checkCraneAndTurtle(4, 12, 3, 3); // 「そんな状況はありません」と出力
checkCraneAndTurtle(2, 2, 1, 1); // 「鶴が1匹，亀が1匹」と出力

for (let i = 0; i < 100; i++) {
  _total_head = randomInt(2, 20)
  _total_legs = randomInt(2, 50)
  _crane_legs = randomInt(1, 10)
  _turtle_legs = randomInt(1, 10)

  checkCraneAndTurtle(_total_head, _total_legs, _crane_legs, _turtle_legs)
}