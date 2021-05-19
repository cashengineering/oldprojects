/* Detect and fix invalid JSON */
const value1 = process.argv[2];

// write your solution here

//Ignore This Nonsense, It Just Allows JS To Use A Terrible Version of Python's Replace Method
const format = (string, inputs) => string.split("{}").slice(0, string.split("{}").length-1).map((section, index) => section + inputs[index]).join("")

//This Starts The Output With A Left Bracket, and then creates a "Pair String" that is filled out with pairs and appropriate commas or brackets
let output = "{", pair = "\"{}\":\"{}\"{}";

//Grabs All The Data From The Broken String
let strings = value1.match(RegExp("[A-Za-z]+", "g"));

//Goes Through On Increments Of Two And Creates A JSON String With The Matches
for (let i = 0; i < strings.length; i += 2){
    output += format(pair, [strings[i], strings[i+1], ((i+2 != strings.length) ? "," : "}")])
}

console.log(output)



/* Roman Numeral conversion */
const value1 = process.argv[2];

// write your solution here
const numerals = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}, subtractive = {"IV":4, "IX":9, "XL":40, "XC":90, "CD":400, "CM":900};
let romanNumerals = value1, output = 0;

for (let key in subtractive){
    let matches = romanNumerals.match(RegExp(key, "g"))
    output += subtractive[key]*(matches != null ? matches.length : 0);
    romanNumerals = romanNumerals.replace(key, "")
}

for (let key in numerals){
    let matches = romanNumerals.match(RegExp(key, "g"))
    output += numerals[key]*(matches != null ? matches.length : 0);
    ronamNumerals = romanNumerals.replace(key, "")
}

console.log(output)



/* Pig latin translator */
const value1 = process.argv[2];

// write your solution here
let fragments = value1.split(" ").map(frag => unpig(frag))
function unpig(word){
    let pigPart = [word.indexOf("-"), word.lastIndexOf("ay")]
    if (pigPart[0] != -1){
        return (word.slice(pigPart[0]+1, pigPart[1]).concat(word.slice(0, pigPart[0])))
    }

    else {
        return (word.slice(0, word.length-3))
    }
}

console.log(fragments.join(" "))



/* Answer the Quadratic */
const value1 = process.argv[2];

// write your solution here
stringToEvaluate = value1.slice(0, value1.length-2).replace("^2", "");
let [a, b, c] = stringToEvaluate.split("x").map(value => value == '' ? 1 : parseInt(value));
xValues = [1, -1];

function quadraticEquation(xValue){
    bSection = -1*b;
    insideSqrt = (b*b)-(4*a*c);
    divisor = 2*a;

    if (insideSqrt != Math.abs(insideSqrt)){
        return("imaginary");
    }

    else {
        solution = (bSection+(xValue*Math.sqrt(insideSqrt)))/divisor;
        solution = Math.abs(solution.toString().length) >= 8 ? solution.toString().slice(0, (solution < 0 ? 8 : 7)) : solution
        return(solution);
    }

}

let output = xValues.map(quadraticEquation).join(",");
console.log(output);
