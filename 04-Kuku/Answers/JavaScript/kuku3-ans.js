// kuku3-ans.js
// By kota ninomiya

/**
 * 九九の表を作る関数，桁数自動調整版
 * @param {Number} number 上限となる数字
 */
function createKukuTableAutoFormat(number){
    message = ''
    termDigit = Math.floor(Math.log10((number-1)))
    answerDigit = Math.floor(Math.log10((number-1)*(number-1)))
    for(let i=1; i<number; i++){
        for(let j=1; j<number; j++){
            message += `${autoFormatDigits(i, termDigit) + i}*${autoFormatDigits(j, termDigit) + j}=${autoFormatDigits(i*j, answerDigit)}${i*j}, `
        }
        message = message.slice(0, -2)
        message += `\n`
    }
    console.log(message)
}

/**
 * 桁数にあわせてスペースで埋め合わせる関数
 * @param {Number} verifyValue 検証する値
 * @param {Number} digit 揃える桁数
 */
function autoFormatDigits(verifyValue, digit){
    numOfFill = digit - Math.floor(Math.log10(verifyValue))
    spaces = ''
    for(let i=0; i<numOfFill; i++){
        spaces += ' '
    }
    return spaces
}

createKukuTableAutoFormat(11)