// kuku_ans.pde
// by kota ninomiya

for (int i=1; i<10; i++) {
  for (int j=1; j<10; j++) {
    print(i+"*"+j+"=");
    if ( i*j < 10) {
      print(" ");
    }
    print(i*j);
    if ( j != 9) {
      print(", ");
    }
  }
  println();
}

/* 文字列結合バージョン */
println("####### 文字列結合バージョン #######");
for (int i=1; i<10; i++) {
  String message = "";
  for (int j=1; j<10; j++) {
    message += i+"*"+j+"=";
    if ( i*j < 10) {
      message += " ";
    }
    message += i*j;
    if ( j != 9) {
      message += ", ";
    }
  }
  println(message);
}
