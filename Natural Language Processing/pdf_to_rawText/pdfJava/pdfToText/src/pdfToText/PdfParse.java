package pdfToText;
import java.io.File;
import java.io.FileInputStream;
import java.io.IOException;
import java.io.PrintWriter;

import org.apache.tika.exception.TikaException;
import org.apache.tika.metadata.Metadata;
import org.apache.tika.parser.ParseContext;
import org.apache.tika.parser.pdf.PDFParser;
import org.apache.tika.sax.BodyContentHandler;

import org.xml.sax.SAXException;

public class PdfParse {
	
	static int errorCounter=0;
	public static void main(final String[] args) throws IOException, TikaException, SAXException {
		
		File folder = new File("C:\\Users\\olive\\Documents\\_School Works_\\_Research_\\2018 Spring\\pdfJava\\pdfToText\\_pdf_");
		File [] listOfFiles = folder.listFiles();
		String fileName;
		String inputFile;
		String outputFile;
		PrintWriter errorWriter=new PrintWriter("C:\\Users\\olive\\Documents\\_School Works_\\_Research_\\2018 Spring\\pdfJava\\pdfToText\\error.txt");
		
		for(int i=0;i<listOfFiles.length;i++)
		{
			String[] splitString = listOfFiles[i].toString().split("\\\\");
			fileName = splitString[splitString.length-1];
			String[] splitType = fileName.split("\\.");
			inputFile = fileName;
			outputFile = splitType[0]+".txt";
			pdfText(inputFile,outputFile,errorWriter);
		}
		errorWriter.close();
		
	   }
	
	static public void pdfText(String inputFileName,String outputFileName,PrintWriter errorWriter) throws IOException, TikaException, SAXException
	{
		
		inputFileName ="C:\\Users\\olive\\Documents\\_School Works_\\_Research_\\2018 Spring\\pdfJava\\pdfToText\\_pdf_\\"+inputFileName;
		BodyContentHandler handler = new BodyContentHandler(-1);
		Metadata metadata = new Metadata();
		FileInputStream inputstream = new FileInputStream(new File(inputFileName));
	    ParseContext pcontext = new ParseContext();
	    boolean getin = false;
	    
	  //parsing the document using PDF parser
	    PDFParser pdfparser = new PDFParser(); 
	    pdfparser.parse(inputstream, handler, metadata,pcontext);
//===========================================================================================
		//getting metadata of the document
	    System.out.println("Metadata of the PDF:");
	    String[] metadataNames = metadata.names();
	    String fileName=""; 
	    
	    /*for(String name : metadataNames) {
	    	if(name =="pdf:docinfo:title")
	    	{
	    		fileName= metadata.get(name)+".txt";
	    		getin = true;
	    	}
	       //System.out.println(name+ " : " + metadata.get(name));
	       //writer.println(name+ " : " + metadata.get(name));
	    }
	    //System.out.println("==============================================================");
	    if(getin == false)
	    {
	    	errorCounter=errorCounter+1;
    		errorWriter.println(errorCounter+" Could not find the tilte:");
    		errorWriter.println(inputFileName);
    		return;
	    }*/
	    outputFileName = outputFileName.replace(" ", "-");
	    outputFileName = outputFileName.replace("<sup>","");
	    outputFileName = outputFileName.replace("</sup>", "");
	    
	    outputFileName = outputFileName.replace(":","");
	    outputFileName = outputFileName.replace("\"","");
	    outputFileName = outputFileName.replace("/","");
	    outputFileName = outputFileName.replace("\\","");
	    outputFileName = outputFileName.replace("\\*","");
	    outputFileName = outputFileName.replace("?","");
	    outputFileName = outputFileName.replace("|","");
	    outputFileName = outputFileName.replace(">","");
	    outputFileName = outputFileName.replace("<","");
	    
	    
	    System.out.println(outputFileName);
//===========================================================================================		
	    PrintWriter writer = new PrintWriter("C:\\Users\\olive\\Documents\\_School Works_\\_Research_\\2018 Spring\\pdfJava\\pdfToText\\_txt_\\"+outputFileName);
//===========================================================================================	      
	    
	    //getting the content of the document
	    //System.out.println("Contents of the PDF :" + handler.toString());
	    System.out.println("This file has been Finish:"+inputFileName);
	    writer.println(handler.toString());
	      
	    
	    
	    //close the writer
	    writer.close();
	}

}
