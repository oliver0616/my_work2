package pack;

public class Variables {
	
	String userInput;
	
	//when user didn't type in any variable
	public Variables()
	{
		userInput = null;
	}
	
	//when user give a variable
	public Variables(String input)
	{
		userInput = input;
	}
	
	public void checkTypes()
	{
		if(userInput.equals("String"))
		{
			System.out.println("This is String Type");
		}
		else if(userInput.equals("int"))
		{
			System.out.println("This is Integer Type");
		}
		else if(userInput.equals("double"))
		{
			System.out.println("This is a Double Type");
		}
		else if(userInput.equals("byte"))
		{
			System.out.println("This is Byte type");
		}
		else if(userInput.equals("short"))
		{
			System.out.println("This is Short Type");
		}
		else if(userInput.equals("long"))
		{
			System.out.println("This is Long Type");
		}
		else if(userInput.equals("float"))
		{
			System.out.println("This is Float Type");
		}
		else if(userInput.equals("boolean"))
		{
			System.out.println("This is Boolean Type");
		}
		else if(userInput.equals("char"))
		{
			System.out.println("This is Char Type");
		}
		else if(userInput.equals("")) 
		{
			System.out.println("You didn't enter anything");
		}
		else
		{
			System.out.println("Seems like there is a error"
					+ ", either its not a types or cases are wrong. Check over again.");
		}
	}
}
