// kuku2-ans.js
// By kota ninomiya

/**
 * 九九の表を作る関数
 * @param {Number} number 上限となる数字
 */
function createKukuTable(number){
    message = ''
    for(let i=1; i<number; i++){
        for(let j=1; j<number; j++){
            message += `${i}*${j}=${i*j<10 ? ' ' : ''}${i*j}, `
        }
        message = message.slice(0, -2)
        message += `\n`
    }
    console.log(message)
}

createKukuTable(5)