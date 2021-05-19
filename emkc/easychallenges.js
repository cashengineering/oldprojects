/* Reverse a String */
const value1 = process.argv[2];

// write your solution here
//Turns the String Into an Array, Reverses It, Then Back Into A String
console.log(value1.split("").reverse().join(""));



/* Count number frequency */
const value1 = process.argv[2];

// write your solution here
let string = value1, numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9], highestOcc = [0, -1];
numbers.forEach(num => {
    var occurances = string.length - string.replace(RegExp(num.toString(), "g"), "").length;
    if (occurances > highestOcc[0]) {
        highestOcc[0] = occurances;
        highestOcc[1] = num;
    }
});
console.log(highestOcc[1]);



/* Sum a list of numbers */
const value1 = process.argv[2];

// write your solution here
let list = value1.split(","), output = 0;
list.forEach(element => output += parseInt(element));
console.log(output);



/* Integer list sorting */
const value1 = process.argv[2];

// write your solution here

//This line creates an array of items based upon the comma, then will turn them into an Int using the Map Function
let list = value1.split(',').map(item => parseInt(item));

/*
This line sorts the numbers by determining the largest and smallest,
then reverses them (as they're in ascending order), then turns them into a string.
*/
output = list.sort((a, b) => a - b).reverse().join(",");
console.log(output);



/* Find longest word */
const value1 = process.argv[2];

// write your solution here

/*
The first line lowercases the string, then removes all white space, and sorts the list from largest to smallest.
The second line creates a new list with items that are only greater than or equal to the first item, then this is converted into a string.
*/

list = value1.toLowerCase().replace(/\s/g, "").split(",").sort((a, b) => b.length - a.length);
output = list.filter(word => word.length >= list[0].length).join(",");
console.log(output);



/* Find The Cookie */
const value1 = process.argv[2];

// write your solution here
let cookie, jar;
[cookie, jar] = value1.split(",");
console.log(jar.indexOf(cookie)+jar.lastIndexOf(cookie)+cookie.length-1);



/* Spiral Sum */
const value1 = process.argv[2];

// write your solution here
size = parseInt(value1.split("x")[0]);
fullsize = size**2, output = 0;

//Starting Point Is The Area of the Inner + 1
i = start = ((size-2)**2)+1;

while (i < fullsize){
    i += (i!= start || i != 1 && size-2 != 0 ? size-1 : size-2);
    output += i;
}

console.log(output-4);
