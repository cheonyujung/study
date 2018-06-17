package com.company;

public class Main {

    public static void main(String[] args) {

        Eagle eagle = new Eagle("독수리");
        eagle.printName();
        eagle.cry();
	    eagle.fly();

	    Tiger tiger = new Tiger("호랑이");
	    tiger.printName();
	    tiger.cry();
	    tiger.fly();
	    
    }
}
