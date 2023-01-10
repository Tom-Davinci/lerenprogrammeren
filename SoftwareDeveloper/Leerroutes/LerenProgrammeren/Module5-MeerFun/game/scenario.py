scenarios = [
    {
        "name" : "plains",
        "desc" : "an empty field with few trees, and a house in the distance",
        "ways" : ["house", "cave", "tree"],
    },{
        "name" : "house",
        "desc" : "an abandoned house, you hear a loud noise in the basement",
        "ways" : ["plains", "attic", "basement"],
    },{
        "name" : "attic",
        "desc" : "nothing but dust",
        "ways" : ["house", "basement"],
    },{
        "name" : "basement",
        "desc" : "You fool! (you encounter big balls mcgee)",
        "ways" : "death"
    },{
        "name" : "tree",
        "desc" : "*vietnamese*",
        "ways" : ["in tree", "plains"]
    },{
        "name" : "in tree",
        "desc" : "ho chin mo, bing chilling",
        "ways" : ["john cena", "tree"]
    },{
        "name" : "john cena",
        "desc" : "AND HIS NAME IS JOHN CENA (you is die)",
        "ways" : "death"
    },{
        "name" : "cave",
        "desc" : "maybe theres diamonds",
        "ways" : ["deeper", "shiny gem", "plains"]
    },{
        "name" : "deeper",
        "desc" : "its getting dark, your exit is blocked by some rubble",
        "ways" : ["even deeper"]
    },{
        "name" : "even deeper",
        "desc" : "its getting hot",
        "ways" : ["deepest"]
    },{
        "name" : "deepest",
        "desc" : "You find the aether portal, its real... you win",
        "ways" : "win"
    },{
        "name" : "shiny gem",
        "desc" : "take it?",
        "ways" : ["take", "cave"]
    },{
        "name" : "take",
        "desc" : "YOU FOOL! its a trap!",
        "ways" : "death"
    }
]