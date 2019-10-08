// kuku-ans.js
// By kota ninomiya

message = ''
for(let i=1; i<10; i++){
    for(let j=1; j<10; j++){
        message += `${i}*${j}=`
        if(i*j < 10){
            message += ' '
        }
        message += `${i*j}`
        if(j != 9){
            message += ', '
        }
    }
    message += `\n`
}

console.log(message)


// 三項演算子とスライスを用いた方法
message = ''
for(let i=1; i<10; i++){
    for(let j=1; j<10; j++){
        message += `${i}*${j}=${i*j<10 ? ' ' : ''}${i*j}, `
    }
    message = message.slice(0, -2)
    message += `\n`
}
console.log('<!-----三項演算子とスライスバージョンの出力-----!>')
console.log(message)
