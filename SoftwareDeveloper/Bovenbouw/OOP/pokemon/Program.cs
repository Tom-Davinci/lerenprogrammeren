using System;
using System.Security.Cryptography.X509Certificates;

class Program{
    static void Main(string[] args){
        Charmander charmander = new Charmander("charmander", "fire", "water");
        int x = 0;
        while(x == 0) {
            charmander.SetName();
            charmander.BattleCry();
        }
    }
}

class Charmander{
    public String name;
    public String strength;
    public String weakness;

    public Charmander(string name, string strength, string weakness) {
        this.name = name;
        this.strength = strength;
        this.weakness = weakness;
    }
    
    public void SetName() {
        Console.WriteLine("Set nickname for Charmander:");
        this.name = Console.ReadLine();
    }

    public void BattleCry() {
        for(int i = 0; i < 10; i++) {
            Console.WriteLine(this.name + "!");
        }
    }
} 