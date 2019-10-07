// tsurukame1-ans.pde
// By kota ninomiya

for( int i=0; i<100; i++ ){
   int total_head = int( random( 2, 30 ) );
   int total_legs = int( random( total_head*2, 100 ) );
   int num_crane = 0;
   int num_turtle = 0;
   boolean isError =  true;
   
   // 以下にプログラムを作成せよ
   while(num_crane < total_head){
     num_turtle = total_head - num_crane;
     if(num_crane*2 + num_turtle*4 ==  total_legs){
       isError =  false;
       break;
     }
     num_crane++;
   }
   
   
   
   // 最後の出力（if文の条件も埋めよ）
   println( "頭が" + total_head + "個で，足が" + total_legs + "本のとき" );
   if(isError){
     println( "そんな状況はありません" );
   } else {
     println( "つるは" + num_crane + "匹，かめは" + num_turtle + "匹です" );
   }
   println();
 } 
