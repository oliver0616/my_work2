package bibJason;

public class check {
	boolean exists = false;
	String online ="online";
	String inproceedings ="inproceedings";
	String article ="article";
	String techreport ="techreport";
	String book ="book";
	String phdthesis ="phdthesis";
	String[] types = {online,inproceedings,article,techreport,book,phdthesis};
	boolean in = true;
	
	/*article articleClass = new article();
	book bookClass = new book();
	inproceedings inproceedingsClass = new inproceedings();
	online onlineClass = new online();
	phdthesis phdthesisClass = new phdthesis();
	techreport techreportClass = new techreport();*/

	public check()
	{
		
	}
	
//===============================================================================================	
	// check types
	public String[] typesResult(StringBuilder input)
	{
		int readIn =0; //read in data
		int errorData = 0; //error data 
		String splitString[] = input.toString().split("@");
		boolean exists = false;
		for(int i =0; i<splitString.length;i++)
		{
			String n = splitString[i].substring(0, Math.min(splitString[i].length(), 15));
			exists = checkTypes(n);	// Check Types Exists or not
			if(exists) 
			{
				readIn++;
			}
			else 
			{
				errorData++;
				System.out.println("This doesnt Exists:"+splitString[i]);
			}
		}
		System.out.println("Read in Data:"+readIn);
		System.out.println("Error data:"+errorData);
		return splitString;
	}
	
	private boolean checkTypes(String input)
	{
		for(int i = 0; i < types.length;i++)
		{
			exists = input.toLowerCase().contains(types[i].toLowerCase());
			if(exists)
			{
				return exists;
			}
		}
		return exists;
	}
//===============================================================================================	
	//convert format
	public StringBuilder convertFormat(String input)
	{
		String[] splitString = input.split("NEWLINE");
		StringBuilder sb = new StringBuilder();
		
		for(int i=0;i<splitString.length;i++)
		{
			//System.out.println(splitString[i]);
			if(i == 0)
			{
				String firstLine = splitString[i];
				if(!firstLine.equals(""))
				{
					firstLine = firstLine.replaceAll(",", "");
					firstLine = firstLine.replaceAll("\\{", "REPLACE");
					String[] splitFirst = firstLine.split("REPLACE");
					firstLine ="{\"datatype\":\""+splitFirst[0]+"\",\"key\":\""+splitFirst[1]+"\",";
				}
				sb.append(firstLine);
			}
			else
			{
				if(!splitString[i].equals("}")&&!splitString[i].equals(""))
				{
					splitString[i]=splitString[i].replaceAll("\\{", "");
					splitString[i]=splitString[i].replaceAll("\\}", "");
					if(!splitString[i].contains("="))
					{
						if(in)
						{
							sb.deleteCharAt(sb.length()-1);
							sb.deleteCharAt(sb.length()-1);
							in = false;
						}
						splitString[i] = splitString[i].replaceAll("&","");
						splitString[i] = splitString[i].replaceAll("\\\\","");
						splitString[i] = splitString[i].replaceAll("\"", "");
						sb.append(" "+splitString[i]);
						
					}
					else
					{
						//System.out.println(splitString[i]);
						String[] splitEqual = splitString[i].split("=");
						String name = splitEqual[0];
						name = name.replaceAll("\\s+", "");
						name ="\""+name+"\":";
					
						String data = splitEqual[1];
						if(data.charAt(data.length()-1)==',')//take out camma at the end
						{
							data = data.substring(0, data.length()-1);
						}
						data = data.replaceAll("\\{", "");
						data = data.replaceAll("\\}", "");
						if(data.charAt(0)==' '||data.charAt(0)=='\t')
						{
							data = data.substring(1); // take out space at front
						}
						data = data.replaceAll("\"",""); // replace "
						data = data.replaceAll("&",""); //replace &
						data = data.replaceAll("\\\\",""); //replace \
						data = "\""+data+"\",";
						
						String finalString = name+data;
						in = true;
						sb.append(finalString);
						
					}
				}
			}		
		}
		//System.out.println(sb);
		return sb;
	}
}