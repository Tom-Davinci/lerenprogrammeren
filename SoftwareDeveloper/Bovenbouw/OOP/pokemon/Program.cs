using System.IO.Compression;

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

        Console.WriteLine("Give a name to the first trainer:");
        String trainerName = Console.ReadLine();
        Trainer trainer1 = new Trainer(belt, trainerName);

        Console.WriteLine("Give a name to the second trainer:");
        String trainer2Name = Console.ReadLine();
        Trainer trainer2 = new Trainer(belt, trainer2Name);

        Battle battle = new Battle(trainer1, trainer2);
        Arena arena = new Arena(battle);        


        int beltLength = belt.Count();
        if( beltLength > 6) {
            Console.WriteLine("Something went wrong");
        }

        bool restart = true;
        while(restart) {
            Arena.BattleAdder();
            Console.WriteLine("Battle: " + Arena.battles);            
            arena.Battling();

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

class Battle {
    public Trainer trainer1;
    public Trainer trainer2;
    public int rounds = 0;

    public Battle (Trainer trainer1, Trainer trainer2)
    {
        this.trainer1 = trainer1;
        this.trainer2 = trainer2;
    }

    public void BattleLoop() {
        bool battling = true;
        bool draw = false;
        List<Int16> pokemonOrder = [0,1,2,3,4,5];
        List<Int16> pokemonOrder1 = [0,1,2,3,4,5];
        pokemonOrder = pokemonOrder.OrderBy(x=> Random.Shared.Next()).ToList();
        pokemonOrder1 = pokemonOrder1.OrderBy(x=> Random.Shared.Next()).ToList();
        int currentMon = 0;
        int currentMon1 = 0;
        bool winner = false;
        bool winner1 = false;

        while(battling) {
            Arena.RoundAdder();
            Console.WriteLine("Round: " + Arena.rounds);
            trainer1.belt[pokemonOrder[currentMon]].pokemon.BattleCry();
            trainer2.belt[pokemonOrder1[currentMon1]].pokemon.BattleCry();

            if( trainer1.belt[pokemonOrder[currentMon]].pokemon.strength == "Fire") { //het spijt me
                if( trainer2.belt[pokemonOrder1[currentMon1]].pokemon.weakness == "Fire") {
                    Console.WriteLine("Trainer 1 wins!");
                    currentMon1 += 1;
                    winner = true;
                    winner1 = false;
                }

                else if( trainer2.belt[pokemonOrder1[currentMon1]].pokemon.strength == "Water") {
                    Console.WriteLine("Trainer 2 wins!");
                    currentMon += 1;
                    winner1 = true;
                    winner = false;                    
                }

                else if( trainer2.belt[pokemonOrder1[currentMon1]].pokemon.strength == "Fire") {
                    Console.WriteLine("Draw!");
                    draw = true;
                }
            }
            else if( trainer1.belt[pokemonOrder[currentMon]].pokemon.strength == "Water") {
                if( trainer2.belt[pokemonOrder1[currentMon1]].pokemon.weakness == "Water") {
                    Console.WriteLine("Trainer 1 wins!");
                    currentMon1 += 1;
                    winner = true;
                    winner1 = false;                    
                }

                else if( trainer2.belt[pokemonOrder1[currentMon1]].pokemon.strength == "Grass") {
                    Console.WriteLine("Trainer 2 wins!");
                    currentMon += 1;
                    winner1 = true;
                    winner = false;   
                }

                else if( trainer2.belt[pokemonOrder1[currentMon1]].pokemon.strength == "Water") {
                    Console.WriteLine("Draw!");
                    draw = true;
                }
            }
            else if( trainer1.belt[pokemonOrder[currentMon]].pokemon.strength == "Grass") {
                if( trainer2.belt[pokemonOrder1[currentMon1]].pokemon.weakness == "Grass") {
                    Console.WriteLine("Trainer 1 wins!");
                    currentMon1 += 1;
                    winner = true;
                    winner1 = false;                    
                }

                else if( trainer2.belt[pokemonOrder1[currentMon1]].pokemon.strength == "Fire") {
                    Console.WriteLine("Trainer 2 wins!");
                    currentMon += 1;
                    winner1 = true;
                    winner = false;                       
                }

                    draw = true;
                }

            if(draw) {
                if(winner) {
                    currentMon += 1;
                    winner = false;
                    winner1 = true;
                }
                else if(winner1) {
                    currentMon1 += 1;
                    winner1 = false;
                    winner = true;
                }
                else {
                    currentMon += 1;
                    currentMon1 += 1;
                }
                draw = false;
            }

            if( currentMon == 6 | currentMon1 == 6) {
                battling = false;
            }
        }
    }
}

class Arena {
    public Battle battle;
    public static int rounds;
    public static int battles;

    public Arena(Battle battle)
    {
        this.battle = battle;
    }

    public void Battling() {
        battle.BattleLoop(); //lol
    }

    public static void BattleAdder() {
        battles += 1;
    }

    public static void RoundAdder() {
        rounds += 1;
    }
}