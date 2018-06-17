package com.company;

public class Animal {

    protected Cry cry;
    protected Fly fly;

    public Animal() {

    }

    public void cry() {
        cry.cry();
    }

    public void fly() {
        fly.fly();
    }

    public void move() {
        System.out.println("움직인다");
    }
}
