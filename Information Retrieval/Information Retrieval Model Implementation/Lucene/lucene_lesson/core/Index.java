package indexing;

import java.io.File;
import java.io.IOException;
import java.io.StringReader;
import java.nio.file.Paths;
import java.nio.file.Path;
import java.util.Scanner;

import org.apache.lucene.analysis.standard.StandardAnalyzer;
import org.apache.lucene.document.Document;
import org.apache.lucene.document.Field;
import org.apache.lucene.document.TextField;
import org.apache.lucene.index.IndexWriter;
import org.apache.lucene.index.IndexWriterConfig;
import org.apache.lucene.analysis.Analyzer;

import org.apache.lucene.store.Directory;
import org.apache.lucene.store.FSDirectory;
import org.apache.lucene.store.RAMDirectory;

public class Main {
	public static void main(String[] arg) throws IOException {
		int userChoice;
		Scanner scan = new Scanner(System.in);
		Scanner userScan = new Scanner(System.in);
		String text="";
		// index object
		Directory index;
		//standard analyzer
		Analyzer analyzer = new StandardAnalyzer();
		
		//Selecting Keyboard Input or File Input
		System.out.println("Enter 1.Keyboard Input, 2.File Input");
		userChoice = scan.nextInt();
		if (userChoice == 1) {
			System.out.print("Input: ");
			//text = "Lucene is simple yet powerful java based search library.";
			text = userScan.nextLine();
			System.out.println("User Input Sentence is: "+text);
			//initialize index using ram to store the data
			index = new RAMDirectory();
			IndexWriterConfig config = new IndexWriterConfig(analyzer);
			//create indexwriter to index data later
			IndexWriter writer = new IndexWriter(index, config);
			//initialize the document that would be added by indexwriter later
			Document document = new Document();
			//Specific out the fields for document
			Field contentField = new Field("COTENT", text,TextField.TYPE_STORED);
			//Add fields into document
			document.add(contentField);
			//Add document into indexwriter
			writer.addDocument(document);
			writer.close();
		}
		else if(userChoice == 2) {
			Path current =Paths.get(System.getProperty("user.dir"));
			Path inputPath = Paths.get(current.toString(),"input");
			Path indexPath = Paths.get(current.toString(),"input","index");
			//initialize index to read the file path
			index = FSDirectory.open(indexPath);
			IndexWriterConfig config = new IndexWriterConfig(analyzer);
			//create indexwriter to index data later
			IndexWriter writer = new IndexWriter(index, config);
			//read each files
			File folder = new File(inputPath.toString());
			File[] listOfFiles = folder.listFiles();
			for (File file : listOfFiles) {
				//initialize the document that would be added by indexwriter later
				Document document = new Document();
				if (file.isFile()) {
					Scanner fileScan = new Scanner(file);
					String temp = fileScan.nextLine();
					text = text+temp;
					fileScan.close();
				}
				//Specific out the fields for document
				Field contentField = new Field("COTENT", text,TextField.TYPE_STORED);
				//index file name
			    Field fileNameField = new Field("FILENAME", file.getName(),TextField.TYPE_STORED);
			    //index file path
			    Field filePathField = new Field("FILEPATH", file.getCanonicalPath(),TextField.TYPE_STORED);
				//Add fields into document
				document.add(contentField);
				document.add(fileNameField);
				document.add(filePathField);
				//Add document into indexwriter
				writer.addDocument(document);
				text="";
			}
			
		}
		userScan.close();
		scan.close();
		
		analyzer.close();
	}
}
