// fizzbuzz2.js
// By kota ninomiya

/** 
 * fizzBuzz - fizzBuzzを判断して返す関数
 *
 *@param number {Number} 検証する値
 * @return {String} いずれの場合にも該当しない場合numberを返す
 */
function fizzBuzz(number){
    if(number%15 == 0) return 'FizzBuzz'
    if(number%3 == 0) return 'Fizz'
    if(number%5 == 0) return 'Buzz'
    return number
}

for(let i=1; i<=200; i++){
    console.log(fizzBuzz(i))
}