class Program{
    static void Main(string[] args){

    }
}

class Pokeball{
    public Charmander charmander;
    public bool hasCharmander;
    public bool isOpen;

    public Pokeball(Charmander charmander, bool hasCharmander, bool isOpen) {
        this.charmander = charmander;
        this.hasCharmander = hasCharmander;
        this.isOpen = isOpen;
    }

    public void Thrown() {
        this.hasCharmander = false;
    }

    public void Returned() {
        this.hasCharmander = true;
    }

    public void open() {
        this.isOpen = true;
    }

    public void close() {
        this.isOpen = false;
    }
}

class Charmander{
    public String nickname;
    public String strength;
    public String weakness;

    public Charmander(String nickname, String strength, String weakness) {
        this.nickname = nickname;
        this.strength = strength;
        this.weakness = weakness;
    }

    public void BattleCry() {
        Console.WriteLine("CHARMANDER!");
    }
}

class Trainer{
    public List<Pokeball> belt;
    public String name;

    public Trainer(List<Pokeball> belt, String name) {
        for(int i = 0; i < 5; i++) {
            //???????????
        }
        this.name = name;
    }

    public void ThrowPokeball(Pokeball pokeball) {
        pokeball.open();
        pokeball.Thrown();
    }

    public void ReturnPokeball(Pokeball pokeball) {
        pokeball.Returned();
        pokeball.close();
    }
}

class Game{
    public void GenerateTrainer(int trainerNr) {
        Console.WriteLine("Set name for traner: " + trainerNr);
        String trainerName = Console.ReadLine();
        Trainer trainer = new Trainer(iets , trainerName); //??????????
    }
}