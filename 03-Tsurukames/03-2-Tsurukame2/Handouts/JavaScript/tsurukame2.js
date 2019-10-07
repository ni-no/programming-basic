// tsurukame2.js
// By kota ninomiya

/**
 *randomInt - 指定範囲内のおいて整数を乱数生成
 *
 * @param {Number} min 最小値
 * @param {Number} max 最大値
 * @return {Number} 乱数
 */
function randomInt(min, max){
  return Math.floor(Math.random()*(max - min) + min)
  }

for(var i=0; i<100; i++){
  total_head = randomInt(2, 20)
  total_legs = randomInt(total_head*2, 100)
  crane_legs = randomInt(1, 3)
  turtle_legs = randomInt(4, 6)
  num_crane = 0
  num_turtle = 0
  
  // 以下にプログラムを作成せよ





  // 最後の出力(if文の条件も埋めよ）
  console.log(`頭が${total_head}個で，足が${total_legs}本で`)
  console.log(`つるの足が${crane_legs}本で，かめの足が${turtle_legs}本のとき`)
  if(/* ここに条件を記載 */){
    console.log('そんな状況はありません')
  } else {
    console.log(`鶴は${num_crane}匹，亀は${num_turtle}匹です`)
  }
  console.log('\n')
} 