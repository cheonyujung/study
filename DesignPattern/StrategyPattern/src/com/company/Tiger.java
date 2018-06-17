package com.company;

public class Tiger extends Animal{

    String name;

    public Tiger(String name) {
        this.name = name;
        cry = new TigerCry();
        fly = new NoFly();
    }

    public void printName() {
        System.out.println(name);
    }
}
