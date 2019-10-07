// colorcirlce.pde
// By kota ninomiya

void setup(){
  size(400, 400);
}

void draw(){
  background(255);
  for(int i=0; i<10;  i++){
    for(int j=0; j<10; j++){
      fill(255);
      if(i==0 || i==9 || j==0 || j==9) fill(255, 0, 0);
      else if(i==1 || i==8 || j==1 || j==8) fill(0, 0, 255);
      ellipse(i*40+20, j*40+20, 40, 40);
    }
  }
}
