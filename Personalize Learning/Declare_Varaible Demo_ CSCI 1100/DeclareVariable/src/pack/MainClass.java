package pack;

import java.util.Scanner;

public class MainClass {
	public static void main(String[] args) 
	{
		String userInput;
		Scanner scan = new Scanner(System.in);
		
		while(true)
		{
			System.out.println("Declare a variable:");
			userInput = scan.nextLine();
			if(userInput.charAt(userInput.length()-1) != ';')
			{
				System.out.println("Missing the semicolon at the end");
			}
			else if(!(userInput.contains("=")))
			{
				System.out.println("You are missing the equal sign");
			}
			else
			{
				String splitString [] = userInput.split(" ");
				Variables test = new Variables(splitString[0]);
				test.checkTypes();		
			}
	
		}

	}
}