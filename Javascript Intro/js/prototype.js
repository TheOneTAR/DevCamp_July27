/**
 * Created by TheOneTAR on 9/3/15.
 */


function Plant() {
    this.country = "Mexico";
    this.isOrganic = true;
}

Plant.prototype.showNameAndColor =  function () {
    console.log("I am a " + this.name + " and my color is " + this.color);
};

Plant.prototype.amIOrganic = function () {
    if (this.isOrganic) {

        console.log("I am organic, Baby!");
    }
};

function Fruit (fruitName, fruitColor){
    this.name = fruitName;
    this.color = fruitColor;
    this.country = "Italy";
}
Fruit.prototype = new Plant();

Fruit.prototype.toString = function () {
    return "I am a " + this.name;
};

var aBanana = new Fruit("Banana", "Yellow");
console.log(aBanana.name); // Banana​

console.log(aBanana.toString());
aBanana.showNameAndColor(); // I am a Banana and my color is yellow.
aBanana.amIOrganic();
console.log(aBanana.__proto__.country);
console.log(Fruit.prototype.country);




