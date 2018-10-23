package bibJason;

import java.util.Scanner;
import java.io.BufferedReader;
import java.io.File;
import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.PrintWriter;
import java.lang.StringBuilder;

public class Main {

	public static void main(String [ ] args) throws IOException, FileNotFoundException {
//==================================================================================================		
		check checkClass = new check();
		File testFile = new File("test.bib");
		BufferedReader in = new BufferedReader(
			    new InputStreamReader(
			        new FileInputStream(testFile),
			        "UTF-8"));
		in.mark(1);
		if (in.read() != 0xFEFF)
		  in.reset();
		
		Scanner scan = new Scanner(in);
		String input;
		StringBuilder sb = new StringBuilder();
		int counter=0;
		
		while(scan.hasNextLine())	//clean up spaces
		{
			input = scan.nextLine();
			if(!input.equals(""))
			{
				input = input+"NEWLINE";
				sb.append(input);
			}
		}
		scan.close();
		
		String[] stringArray = checkClass.typesResult(sb);	//Separate out each data
		StringBuilder output;
		PrintWriter writer = new PrintWriter("result.json");
		String result;
		
		for(int i =0; i<stringArray.length;i++)
		{
			if(!stringArray[i].equals("")) //make sure data pass in is not a blank new line
			{
				counter++;
				output = checkClass.convertFormat(stringArray[i]);
				String index="{\"index\":{\"_id\":\""+counter+"\"}}";
				if(checkClass.in == false)
				{
					result = output.toString().substring(0,output.length()-1)+"\"}";
				}
				else
				{
					result = output.toString().substring(0,output.length()-1)+"}";
				}
				writer.println(index);
				writer.println(result);
				//System.out.println(index);
				//System.out.println(output);
			}
		}
		writer.close();
		
	}
}
