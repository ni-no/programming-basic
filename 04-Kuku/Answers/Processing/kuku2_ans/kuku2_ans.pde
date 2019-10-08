// kuku2_ans.pde
// by kota ninomiya

/**九九のテーブルを作成する関数
 *
 * @param num (int): 上限の値
 */
void createKukuTable(int num) {
  for (int i=1; i<num; i++) {
    String message = "";
    for (int j=1; j<num; j++) {
      message += i+"*"+j+"=";
      if ( i*j < 10) {
        message += " ";
      }
      message += i*j;
      if ( j != num-1) {
        message += ", ";
      }
    }
    println(message);
  }
}

void setup(){
 createKukuTable(5); 
}
