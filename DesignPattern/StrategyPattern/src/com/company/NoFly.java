package com.company;

public class NoFly implements Fly{

    @Override
    public void fly() {
        System.out.println("날지 못해요");
    }
}
