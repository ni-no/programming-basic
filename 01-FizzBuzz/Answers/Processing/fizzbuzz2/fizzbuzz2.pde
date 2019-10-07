// fizzbuzz2.pde
// by kota ninomiya

String fizz_buzz(int number){
 if(number%15 == 0) return "Fizz Buzz";
 else if(number%3 == 0) return "Fizz";
 else if(number%5 == 0) return "Buzz";
 return str(number);
}

void setup(){
 for(int i=1; i<=200; i++){
   println(fizz_buzz(i));
 }
}
