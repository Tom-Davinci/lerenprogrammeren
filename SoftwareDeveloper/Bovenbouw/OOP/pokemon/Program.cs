class Program{ // "game"
    static void Main(string[] args){
        Pokemon charmander = new Pokemon("Charmander", "Fire", "Water");
        Pokeball Ball = new Pokeball(charmander, true);

        List<Pokeball> belt = [];
        for(int i = 0; i < 6; i++) {
            belt.Add(Ball);
        }

        int beltLength = belt.Count();
        if( beltLength > 6) {
            Console.WriteLine("Something went wrong");
        }

        bool restart = true;
        while(restart) {
            Console.WriteLine("Give a name to the first trainer:");
            String trainerName = Console.ReadLine();
            Trainer trainer1 = new Trainer(belt, trainerName);

            Console.WriteLine("Give a name to the second trainer:");
            String trainer2Name = Console.ReadLine();
            Trainer trainer2 = new Trainer(belt, trainer2Name);

            for(int i = 0; i < 6; i++) {
                trainer1.ThrowBall(i);
                trainer1.belt[i].charmander.BattleCry();
                trainer2.ThrowBall(i);
                trainer2.belt[i].charmander.BattleCry();
                trainer1.ReturnBall(i);
                trainer2.ReturnBall(i);
            }

            while(true) {
                Console.WriteLine("Go again? (Y/N)");
                String yesno = Console.ReadLine();
                if(yesno != "Y" && yesno != "N") {
                    Console.WriteLine("Please enter Y/N");
                }
                else if(yesno == "Y") {
                    break;
                }
                else if(yesno == "N") {
                    restart = false;
                    Console.WriteLine("Goodbye :)");
                    break;
                }
            }
        }
    }
}

class Pokemon {
    public String name;
    public String strength;
    public String weakness;

    public Pokemon (string name, string strength, string weakness)
    {
        this.name = name;
        this.strength = strength;
        this.weakness = weakness;
    }

    public void BattleCry() {
        Console.WriteLine(this.name + "!!!");
    }
}

class Pokeball{
    public Pokemon charmander;

    public bool open = false;
    public bool containsPokemon;

    public Pokeball(Pokemon charmander, bool containsPokemon)
    {
        this.charmander = charmander;
        this.containsPokemon = containsPokemon;
    }

    public void Thrown() {
        this.open = true;
        this.containsPokemon = false;
    }

    public void Returned() {
        this.containsPokemon = true;
        this.open = false;
    }
}

class Trainer{
    public List<Pokeball> belt;
    public String name;

    public Trainer (List<Pokeball> belt, string name)
    {
        this.belt = belt;
        this.name = name;
    }

    public void ThrowBall(int beltIndex) {
        belt[beltIndex].Thrown();
    }

    public void ReturnBall(int beltIndex) {
        belt[beltIndex].Returned();
    }
}