/* Convert string to binary */
const value1 = process.argv[2];

// write your solution here
let letters = value1.split(""), output = "";
letters.forEach(item => output += "0" + item.charCodeAt(0).toString(2));
console.log(output);



/* Fibonaci Numbers */
const value1 = process.argv[2];
const value2 = process.argv[3];

// write your solution here
let start = parseInt(value1), steps = parseInt(value2), fib = [0, 1], i = 0, totalFib = "";
while (steps != 0) {

    //If We're Now Counting Past The Starting Value, Then Begin To Add To The Values In Sequence
    if (fib[0] > value1){
        //This Ternary is To Prevent The End From Aquiring An Extra Comma
        totalFib += fib[0] + (steps != 1 ? "," : "");
        steps -= 1;
    }

    //Assigns New Sequence Numbers To The Newest Number and Sums the Current Total To Get A New Number
    fib = [fib[1], fib.reduce((count, number) => count += number)];
}
console.log(totalFib);



/* Check scrambled string */
const value1 = process.argv[2];

// write your solution here

//Creates The Two Lists Of Characters, Then Strings => Arrays that are sorted via charcode => Back Into Strings
list = value1.split(",").map(string => string.split("").sort((a, b) => a.charCodeAt(0) - b.charCodeAt(0)).toString());
console.log(list[0] == list[1] ? "Yes" : "No");



/* Zipper merge */
const value1 = process.argv[2];
const value2 = process.argv[3];

// write your solution here
const combine = (a, b) => (a+","+b);
let list1 = value1.split(","), list2 = value2.split(","), output = "";
for (let i = 0; i < list1.length; i++){
    output += combine(list1[i], list2[i]);
    output += i < list1.length-1 ? "," : "";
}
console.log(output);



/* Find Most Common Characters */
const value1 = process.argv[2];

// write your solution here
let highestCount = 0, chars = [], list = value1;

while (list) {
    //Gets The Character, Creates A Global Flag Regex For It, Then Counts It's Occurances
    let char = list[0], matches = RegExp(char, "g"), count = list.match(matches).length;

    if (count >= highestCount) {
        //Chars is Chars + Char if (The Highest Count is Equal To The Current Count), Otherwise Chars is now [Char]
        chars = (count == highestCount) ? chars.concat([char]) : [char], highestCount = count;
    }
    list = list.replace(matches, "");
}

console.log(chars.join(","))



/* Digit Sum Even or Odd */
const value1 = process.argv[2];

// write your solution here

//Turns the input string into a list, then maps all of the chars as a number
let list = value1.split("").map(char => parseInt(char));

//Reduces A List of Ints Into A Sum
let count = list.reduce((acc, cur) => acc + cur);

console.log( (count%2 == 0) ? "even" : "odd");



/* Recursive Sum */
const value1 = parseInt(process.argv[2]);

// write your solution here
let data = [...value1.toString()];
function reduceToOne(a,b) {
    let total = parseInt(a)+parseInt(b);
    return(total < 10 ? total : [...total.toString()].reduce(reduceToOne));
}

console.log(data.reduce(reduceToOne));



/* How long ago? */
//This challenge has a rare edge case where it estimates one day higher than it should
//When I go through and re-update solutions to these challenges I'll fix this.

const value1 = process.argv[2];

// write your solution here

//Creates two data points, and then splits them into arrays of their date components
let data = value1.split(",").map(item => item.split("-"));
let multiplierDictionary = {0:365, 1:31, 2:1};
let distance = [0, 0, 0]

let reducer = (acc, val) => acc+val;

for (i = 0; i < 3; i++){
    //The Year, Date, or Month component of B is taken from A and then is converted to days.
    distance[i] = multiplierDictionary[i]*(parseInt(data[0][i])-parseInt(data[1][i]));
}

console.log(distance.reduce(reducer))
