const readline = require('readline');

// Create an instance of the readline interface
const rl = readline.createInterface({
  input: process.stdin, // Read from the standard input (command line)
  output: process.stdout // Output to the standard output (command line)
});

// Ask the user for input
rl.question('Enter something: ', (userInput) => {
  // This function is called when the user enters input and presses Enter

  // Display the user input
  console.log('You entered:', userInput);

  // Close the readline interface after processing the input
  rl.close();
});

// The above code will prompt the user with "Enter something: " in the command line.
// After the user enters their input and presses Enter, the provided callback function is called with the user's input.
