package analyzerPack;

import java.io.File;
import java.io.IOException;
import java.io.StringReader;
import java.nio.file.Paths;
import java.nio.file.Path;
import java.util.Scanner;

import org.apache.lucene.analysis.Analyzer;
import org.apache.lucene.analysis.TokenStream;
import org.apache.lucene.analysis.standard.StandardAnalyzer;
import org.apache.lucene.analysis.tokenattributes.CharTermAttribute;
import org.apache.lucene.analysis.tokenattributes.OffsetAttribute;


public class Main {
	
	public static void main(String[] args) throws IOException {
		int userChoice;
		Scanner scan = new Scanner(System.in);
		Scanner userScan = new Scanner(System.in);
		String text="";
		
		System.out.println("Enter 1.Keyboard Input, 2.File Input");
		userChoice = scan.nextInt();
		if (userChoice == 1) {
			System.out.print("Input: ");
			//text = "Lucene is simple yet powerful java based search library.";
			text = userScan.nextLine();
		}
		else if(userChoice == 2) {
			Path current =Paths.get(System.getProperty("user.dir"));
			Path inputPath = Paths.get(current.toString(),"input");
			File folder = new File(inputPath.toString());
			File[] listOfFiles = folder.listFiles();
			System.out.println(folder);
			for (File file : listOfFiles) {
				if (file.isFile()) {
					Scanner fileScan = new Scanner(file);
					String temp = fileScan.nextLine();
					text = text+temp;
					fileScan.close();
				}
			}
		}
		
		scan.close();
		userScan.close();
		System.out.println("User Input Sentence is: "+text);
		//standard analyzer
		Analyzer analyzer = new StandardAnalyzer();
		//length analyzer
		Analyzer LengthAnalyzer = new NewAnalyzer();
		TokenStream tokenStream = LengthAnalyzer.tokenStream("FieldName",new StringReader(text));
		OffsetAttribute  offsetAtt = tokenStream.addAttribute(OffsetAttribute.class);
		CharTermAttribute termAtt = tokenStream.addAttribute(CharTermAttribute.class);
		
		PartOfSpeechAttribute posAtt = tokenStream.addAttribute(PartOfSpeechAttribute.class);
		
		tokenStream.reset();
		while(tokenStream.incrementToken()) {
			System.out.println("token: " + termAtt.toString());
			System.out.println("Fake POS:"+posAtt.getPartOfSpeech());
			System.out.println("token details: " + tokenStream.reflectAsString(true));
			
	        System.out.println("token start offset: " + offsetAtt.startOffset());
	        System.out.println("token end offset: " + offsetAtt.endOffset());
		}
		tokenStream.end();
		tokenStream.close();
		analyzer.close();
		LengthAnalyzer.close();
		


		

	}
}
