// tsurukame3-ans.pde
// By kota ninomiya

void setup() {
  checkCraneAndTurtle( 10, 32, 2, 4 ); // 「鶴が4匹，亀が6匹」と出力
  checkCraneAndTurtle( 65, 52, 18, 76 ); // 「そんな状況はありません」と出力
  checkCraneAndTurtle( 90, 8, 46, 47 ); // 「そんな状況はありません」と出力
  checkCraneAndTurtle( 4, 12, 3, 3 ); // 「そんな状況はありません」と出力
  checkCraneAndTurtle( 2, 2, 1, 1 ); // 「鶴が1匹，亀が1匹」と出力

  for ( int i=0; i<100; i++ ) {
    int _total_head = int( random( 2, 20 ) );
    int _total_legs = int( random( 2, 50 ) );
    int _crane_legs = int( random( 1, 10 ) );
    int _turtle_legs = int( random( 1, 10 ) );

    checkCraneAndTurtle( _total_head, _total_legs, _crane_legs, _turtle_legs );
  }
}

void checkCraneAndTurtle( int total_head, int total_legs, int crane_legs, int turtle_legs ) {
  println( "頭の数が"+total_head+"で，足の数が"+total_legs );
  println( "鶴の足の数が"+crane_legs+"で，亀の足の数が"+turtle_legs+"のとき" );
  int numOfPairs = 0;
  int num_crane = 0;
  int num_turtle = 0;

  while (num_crane < total_head) {
    num_turtle = total_head - num_crane;
    if (num_crane*crane_legs + num_turtle*turtle_legs ==  total_legs) {
      numOfPairs++;
    }
    num_crane++;
  }
  
  if (numOfPairs == 1) {
    println( "つるは" + num_crane + "匹，かめは" + num_turtle + "匹です" );
  } else {
    println( "そんな状況はありません" );
  }
  println();
}
