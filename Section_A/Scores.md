# Scores
---
## Correctness 2/4
## Efficiency 2/4
## Style 3/4
## Documentation 3/4
---
## Positive Aspects of the Submission 
Great Submission, your solution is almost there! With some minor reworking I was able to run your code with the desired output. However without the modifications it does not meet the task requirements, 

---

## Aspects of the Submission that Could be Improved
In Java although the placement of indents and parenthesis does not produce the same errors as in python, we must adhere to the Java style guide, 

---

```java
public static String reverse_string(String myStr)
	{
		if (myStr.isEmpty()){
		System.out.println("String in now Empty"); 
		return myStr;
		//Calling Function Recursively
		System.out.println("String to be passed in Recursive Function: "+myStr.substring(1));
		return reversestring(myStr.substring(1)) + myStr.charAt(0);}
```

With a small adjustment in your formatting it will be perfect, Remember to delete your unneccesary System.out.println() when submitting your code. 
```java
public static String reverse_string(String myStr){ // Remove line break from line 19, Ensure opening brace is on the same line as method. 
		if (myStr.isEmpty()){
		     return myStr; // Delete Line 21 and Indent line22 within our if statement.  
		   
		}
		//Calling Function Recursively
	    //Remove line 25 as this line is not required for othe final output. 
		return reverse_string(myStr.substring(1)) + myStr.charAt(0); // Line 26 Remove closing brace from end of line and line up with opening statement. 
}
```
The Java formatting guidelines helps maintain readability wthin our code. 

---

When calling methods it is important to ensure the correct syntax is used, 
```java
return reversestring(myStr.substring(1)) + myStr.charAt(0);}
```
The method above is undefined as you have missed the "_" in the "reverse_string" method. 
```
return reverse_string(myStr.substring(1)) + myStr.charAt(0);} // Line 26 add _ to call method. 
```

---

Recursive functions required an if else statement, the base call and the recursive statement. By editing the below code block to return an ArrayList rather than void (no return value) . Adding all arguements as we wish to display a series of fibonacci numbers, num1, num2, num3, count and a numbers list. We need to call the function in our return sequence until there is nothing left to return. Lastly we call the function and label the output to the user. 

```java
public static <T> void function(T maxNumber) {
		// Set it to the number of elements you want in the Fibonacci Series
		int maxNumber = 10; 
		int previousNumber = 0;
		int nextNumber = 1;
		 
	    System.out.print("Fibonacci Series of "+maxNumber+" numbers:");
 
	for (int i = 1; i <= maxNumber; ++i){
	    System.out.print(previousNumber+" ");
	    // On each iteration, we are assigning second number
	    // to the first number and assigning the sum of last two
	    // numbers to the second number
	    int sum = previousNumber + nextNumber;
	    previousNumber = nextNumber;
	    nextNumber = sum;
	    }
 
	}
```
here are the changes I have made, declare the variables. lines 8-12. 
```java
    // Declare variables
		String myStr = "emosewA si avaJ";
		ArrayList<String> numbers = new ArrayList<>();
		int num1 = 0, num2 = 1, num3 = num1 + num2; 
		int n = 10;
		int count = -1;
```
Call the function and label the output to te user: line 17. 
```java
        System.out.println("Fibonacci sequence is: "+ fibonacciCalc(n, num1, num2, num3, count, numbers));
```
A recursive function for calculating fibonacci sequence: lines 32-50.
```java
public static ArrayList fibonacciCalc(int n, int num1, int num2, int num3, int count, ArrayList numbers) {
		
		// Set it to the number of elements you want in the Fibonacci Series
		if (count == n){
			return numbers;
		}
		else{
			count += 1;

			// Add number to list. 
			numbers.add(num1);
            
            // Assign variables their new values.
			num3 = num1 + num2;
			num1 = num2;
			num2 = num3;
            
            // Return function wih new values until we reach n. 
			return fibonacciCalc(n, num1, num2, num3,count, numbers);
		}
	}
```
With this feedback I am positive your next submission will be awesome!

---

## Overall Feedback 
Please implement the changes I have suggested above, Your string_reverse function worked perfectly! Keep up the good work! I look forward to te resubmission. Remember to comment your code thoroughly and accurately throughout to ensure others can follow our thought process. I removed a point from style due to the formatting in your first function, 

