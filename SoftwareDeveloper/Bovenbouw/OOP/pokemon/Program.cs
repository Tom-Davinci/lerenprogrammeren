class Program{ // "game"
    static void Main(string[] args){
        Pokemon charmander = new Charmander("Charmander", PokemonTypes.Fire, PokemonTypes.Water);
        Pokemon squirtle = new Squirtle("Squirtle", PokemonTypes.Water, PokemonTypes.Grass);
        Pokemon bulbasaur = new Bulbasaur("Bulbasaur", PokemonTypes.Grass, PokemonTypes.Fire);
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
        string? trainerName = Console.ReadLine();
        Trainer trainer1 = new Trainer(belt, trainerName);

        Console.WriteLine("Give a name to the second trainer:");
        string? trainer2Name = Console.ReadLine();
        Trainer trainer2 = new Trainer(belt, trainer2Name);

        Battle battle = new Battle(trainer1, trainer2);
        Arena arena = new Arena(battle);        


        int beltLength = belt.Count();
        if( beltLength > (int) BeltCheck.beltLen) {
            Console.WriteLine("Something went wrong");
        }

        bool restart = true;
        while(restart) {
            Arena.BattleAdder();
            Console.WriteLine("Battle: " + Arena.battles);            
            arena.Battling();

            while(true) {
                Console.WriteLine("Go again? (Y/N)");
                string? yesno = Console.ReadLine();
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

enum BeltCheck{
    beltLen = 6
}

abstract class Pokemon {
    private string name {get;set;}
    private PokemonTypes strength {get;set;}
    private PokemonTypes weakness {get;set;}

    public Pokemon (string name, PokemonTypes strength, PokemonTypes weakness)
    {
        this.name = name; 
        this.strength = strength;
        this.weakness = weakness;
    }
    public PokemonTypes GetStrength() {
        return this.strength;
    }
    public PokemonTypes GetWeakness() {
        return this.weakness;
    }
    public string GetName() {
        return this.name;
    }

    public abstract void BattleCry();
}

class Charmander : Pokemon {

public Charmander( String name, PokemonTypes strength, PokemonTypes weakness) : base(name, strength, weakness) {}

public override void BattleCry() {
    Console.WriteLine(this.GetName() + "!!!");
}
}

class Squirtle : Pokemon {

public Squirtle( String name, PokemonTypes strength, PokemonTypes weakness) : base(name, strength, weakness) {}

public override void BattleCry() {
    Console.WriteLine(this.GetName() + "!!!");
}
}

class Bulbasaur : Pokemon {

public Bulbasaur( String name, PokemonTypes strength, PokemonTypes weakness) : base(name, strength, weakness) {}

public override void BattleCry() {
    Console.WriteLine(this.GetName() + "!!!");
}
}

enum PokemonTypes{
    Fire,
    Water,
    Grass
}

class Pokeball{
    public readonly Pokemon pokemon;

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
    public string? name;

    public Trainer (List<Pokeball> belt, string? name)
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

            if( trainer1.belt[pokemonOrder[currentMon]].pokemon.GetStrength() == PokemonTypes.Fire) { //het spijt me
                if( trainer2.belt[pokemonOrder1[currentMon1]].pokemon.GetWeakness() == PokemonTypes.Fire) {
                    Console.WriteLine("Trainer 1 wins!");
                    currentMon1 += 1;
                    winner = true;
                    winner1 = false;
                }

                else if( trainer2.belt[pokemonOrder1[currentMon1]].pokemon.GetStrength() == PokemonTypes.Water) {
                    Console.WriteLine("Trainer 2 wins!");
                    currentMon += 1;
                    winner1 = true;
                    winner = false;                    
                }

                else if( trainer2.belt[pokemonOrder1[currentMon1]].pokemon.GetStrength() == PokemonTypes.Fire) {
                    Console.WriteLine("Draw!");
                    draw = true;
                }
            }
            else if( trainer1.belt[pokemonOrder[currentMon]].pokemon.GetStrength() == PokemonTypes.Water) {
                if( trainer2.belt[pokemonOrder1[currentMon1]].pokemon.GetWeakness() == PokemonTypes.Water) {
                    Console.WriteLine("Trainer 1 wins!");
                    currentMon1 += 1;
                    winner = true;
                    winner1 = false;                    
                }

                else if( trainer2.belt[pokemonOrder1[currentMon1]].pokemon.GetStrength() == PokemonTypes.Grass) {
                    Console.WriteLine("Trainer 2 wins!");
                    currentMon += 1;
                    winner1 = true;
                    winner = false;   
                }

                else if( trainer2.belt[pokemonOrder1[currentMon1]].pokemon.GetStrength() == PokemonTypes.Water) {
                    Console.WriteLine("Draw!");
                    draw = true;
                }
            }
            else if( trainer1.belt[pokemonOrder[currentMon]].pokemon.GetStrength() == PokemonTypes.Grass) {
                if( trainer2.belt[pokemonOrder1[currentMon1]].pokemon.GetWeakness() == PokemonTypes.Grass) {
                    Console.WriteLine("Trainer 1 wins!");
                    currentMon1 += 1;
                    winner = true;
                    winner1 = false;                    
                }

                else if( trainer2.belt[pokemonOrder1[currentMon1]].pokemon.GetStrength() == PokemonTypes.Fire) {
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