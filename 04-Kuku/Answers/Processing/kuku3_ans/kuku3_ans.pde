// kuku3_ans.pde
// by kota ninomiya

/**10を底とする対数をとる関数
 *
 * @param x (int): logをとりたい数
 * @return (float): 10を底とする対数をとった値
 */
float log10(int x){
  return log(x)/log(10);
}

/**九九のテーブルを作成する関数
 *
 * @param num (int): 上限の値
 */
void createKukuTableAutoFormat(int num) {
  int termDigit = floor(log10(num-1));
  int answerDigit = floor(log10((num-1)*(num-1)));
  for (int i=1; i<num; i++) {
    String message = "";
    for (int j=1; j<num; j++) {
      message += autoFormatDigits(i, termDigit)+i+"*"+autoFormatDigits(j, termDigit)+j+"="+autoFormatDigits(i*j, answerDigit)+i*j;
      if ( j != num-1) {
        message += ", ";
      }
    }
    println(message);
  }
}

/**桁数を揃える関数
 *
 * @param vefifyValue (int): 検証する値
 * @param digit (int): そろえる桁数
 * @return (String) 必要なスペース
 */
String autoFormatDigits(int verifyValue, int digit){
  int numOfFill = digit - floor(log10(verifyValue));
  String spaces = "";
  for(int i=0; i<numOfFill; i++){
    spaces += " ";
  }
  return spaces;
}



void setup(){
 createKukuTableAutoFormat(11); 
}
