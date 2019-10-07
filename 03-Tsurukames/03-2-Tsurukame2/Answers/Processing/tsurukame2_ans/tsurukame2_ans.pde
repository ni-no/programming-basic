// tsurukame2-ans.pde
// By kota ninomiya

for( int i=0; i<100; i++ ){
  int total_head = int( random( 2, 20 ) );
  int total_legs = int( random( total_head*2, 100 ) );
  int crane_legs = int( random( 1, 3 ) );
  int turtle_legs = int( random( 4, 6 ) );
  int num_crane = 0;
  int num_turtle = 0;
  boolean isError = true;
  
  // 以下にプログラムを作成せよ
  while(num_crane < total_head){
     num_turtle = total_head - num_crane;
     if(num_crane*crane_legs + num_turtle*turtle_legs ==  total_legs){
       isError =  false;
       break;
     }
     num_crane++;
   }
  
  
  
  // 最後の出力（if文の条件も埋めよ）
  println( "頭が" + total_head + "個で，足が" + total_legs + "本で" );
  println( "つるの足が" + crane_legs + "本で，かめの足が" + turtle_legs + "本のとき" );
  if(isError){
    println( "そんな状況はありません" );
  } else {
    println( "つるは" + num_crane + "匹，かめは" + num_turtle + "匹です" );
  }
  println();
}
