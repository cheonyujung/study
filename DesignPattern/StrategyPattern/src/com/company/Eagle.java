package com.company;

public class Eagle extends Animal{

    String name;

    public Eagle(String name) {
        this.name = name;
        cry = new EagleCry();
        fly = new FlyWithWings();
    }

    public void printName() {
        System.out.println(name);
    }
}
