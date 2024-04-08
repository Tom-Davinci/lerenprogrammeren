class Program{ // "game"
    static void Main(string[] args){
        Pokemon charmander = new Charmander("Charmander", "Fire", "Water");
        Pokemon squirtle = new Squirtle("Squirtle", "Water", "Grass");
        Pokemon bulbasaur = new Bulbasaur("Bulbasaur", "Grass", "Fire");
        Pokeball Ball1 = new Pokeball(charmander, true);
        Pokeball Ball2 = new Pokeball(squirtle, true);
        Pokeball Ball3 = new Pokeball(bulbasaur, true);

        List<Pokeball> belt = [];
        for(int i = 0; i < 2; i++) {
            belt.Add(Ball1);
            belt.Add(Ball2);
            belt.Add(Ball3);
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
                trainer1.belt[i].pokemon.BattleCry();
                trainer2.ThrowBall(i);
                trainer2.belt[i].pokemon.BattleCry();
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

abstract class Pokemon {
    public String name;
    public String strength;
    public String weakness;

    public Pokemon (string name, string strength, string weakness)
    {
        this.name = name;
        this.strength = strength;
        this.weakness = weakness;
    }

    public abstract void BattleCry();
}

class Charmander : Pokemon {

public Charmander( String name, String strength, String weakness) : base(name, strength, weakness) {}

public override void BattleCry() {
    Console.WriteLine(this.name + "!!!");
}
}

class Squirtle : Pokemon {

public Squirtle( String name, String strength, String weakness) : base(name, strength, weakness) {}

public override void BattleCry() {
    Console.WriteLine(this.name + "!!!");
}
}

class Bulbasaur : Pokemon {

public Bulbasaur( String name, String strength, String weakness) : base(name, strength, weakness) {}

public override void BattleCry() {
    Console.WriteLine(this.name + "!!!");
}
}

class Pokeball{
    public Pokemon pokemon;

    public bool open = false;
    public bool containsPokemon;

    public Pokeball(Pokemon pokemon, bool containsPokemon)
    {
        this.pokemon = pokemon;
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