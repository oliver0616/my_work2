package pack;

import java.io.File;
import java.io.FileNotFoundException;
import java.io.PrintWriter;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.util.Scanner;
import java.util.ArrayList;

public class Main {

	public static void main(String[] arg) throws FileNotFoundException
	{
		Path current =Paths.get(System.getProperty("user.dir"));
		Path infoPath = Paths.get(current.toString(),"input","info");
		Path queryPath = Paths.get(current.toString(),"input","cranqrel.txt");
		Path precisionPath = Paths.get(current.toString(),"output","output.txt");
		Path detailPath = Paths.get(current.toString(),"output","detailOutput.txt");
		
		File infoFolder = new File(infoPath.toString());
		File[] infoListFile = infoFolder.listFiles();
		File queryFile = new File(queryPath.toString());
		ArrayList<String> queryList = new ArrayList<String>();
		Main i = new Main();
		//Scan cranqrel data
		Scanner queryScan = new Scanner(queryFile);
		String over="";
		while(queryScan.hasNextLine())
		{
			String now = queryScan.nextLine();
			if(!(now.contains("-1")))
			{
				over = over + now+"\n";
			}
			else
			{
				queryList.add(over);
				over="";
			}
		}
		queryScan.close();
		
		//scan each query and match them
		PrintWriter outputWriter = new PrintWriter(precisionPath.toString());
		PrintWriter detailWriter = new PrintWriter(detailPath.toString());
		double precisionNumerator;
		double precisionDenominator=0;
		double precision;
		double recallDenominator;
		double recall;
		
		
		for(File file:infoListFile)
		{
			Scanner scan = new Scanner(file);
			ArrayList<String> fileFatch= new ArrayList<String>();
			fileFatch.add(file.getName());
			while(scan.hasNextLine())
			{
				String now = scan.nextLine();
				String[] splitString = now.split("\\\\");
				String fileName = splitString[splitString.length-1];
				fileFatch.add(fileName);
				precisionDenominator+=1;
			}
			scan.close();
			precisionNumerator= i.calPreNumerator(queryList ,fileFatch);
			precision=precisionNumerator/precisionDenominator;
			
			String fileName = fileFatch.get(0).replace(".txt", "");
			int fileNum = Integer.parseInt(fileName);
			String query = queryList.get(fileNum-1);
			String[] splitQuery = query.split("\n");
			recallDenominator= splitQuery.length;
			recall = precisionNumerator/recallDenominator;
			
			//output
			outputWriter.println("Query "+ fileNum+":{"+"precision: "+precision+", recall:"+recall+"}");
			detailWriter.println("Query "+ fileNum+"{"+"precision: "+precision+"="+precisionNumerator+"/"
			+precisionDenominator+", recall: "+recall+"="+precisionNumerator+"/"+recallDenominator);
			
			System.out.println("Query "+ fileNum+":{"+"precision: "+precision+", recall:"+recall+"}");
			System.out.println("Query "+ fileNum+"{"+"precision: "+precision+"="+precisionNumerator+"/"
			+precisionDenominator+", recall: "+recall+"="+precisionNumerator+"/"+recallDenominator);
			System.out.println("=================================================");
			precisionDenominator=0;
		}
		outputWriter.close();
		detailWriter.close();
	}
	
//=======================================================================================
	private ArrayList<String> organizeQuery(String input)
	{
		ArrayList<String> result = new ArrayList<String>();
		String[] firstSplit = input.split("\n");
		for(String each:firstSplit)
		{
			String[] secondSplit = each.split(" ");
			result.add(secondSplit[1]);
		}
		return result;
	}
	
//=======================================================================================	
	private int calPreNumerator(ArrayList<String> queryList, ArrayList<String> fileFatch)
	{
		ArrayList<String> orgQue = new ArrayList<String>();
		String fileName = fileFatch.get(0);
		fileName=fileName.replace(".txt", "");
		int fileNum = Integer.parseInt(fileName);
		String query = queryList.get(fileNum-1);
		int result= 0;
		
		orgQue = organizeQuery(query);
		for(int i =1; i < fileFatch.size(); i++)
		{
			String current = fileFatch.get(i);
			current = current.replace(".txt", "");
			current = current.replaceFirst("^0+(?!$)", "");
			for(String each:orgQue)
			{
				if(current.equals(each))
				{
					result+=1;
				}
			}
		}
		return result;
	}
}
