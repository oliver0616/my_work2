package lucenePack;

import java.io.BufferedReader;
import java.io.File;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.IOException;
import java.io.StringReader;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashSet;
import java.util.List;
import java.io.PrintWriter;
import static java.lang.Math.toIntExact;
import java.util.Collections;
import java.util.Comparator;

import org.apache.lucene.queryparser.classic.ParseException;
import org.apache.lucene.analysis.Tokenizer;
import org.apache.lucene.analysis.standard.StandardTokenizer;
import org.apache.lucene.analysis.tokenattributes.CharTermAttribute;

public class LuceneTesterNew {
   static String indexDir = "C:\\Users\\olive\\Documents\\_School Works_\\_Research_\\2018 Summer\\Information Retrieval\\Java\\LuceneModels\\LanguageModel\\Index";
   Path indexPath = Paths.get(indexDir);
   static String dataDir = "C:\\Users\\olive\\Documents\\_School Works_\\_Research_\\2018 Summer\\Information Retrieval\\Java\\LuceneModels\\LanguageModel\\input";
   Path dataPath = Paths.get(dataDir);
   static String outputDir = "C:\\Users\\olive\\Documents\\_School Works_\\_Research_\\2018 Summer\\Information Retrieval\\Java\\LuceneModels\\LanguageModel\\output";
   Path outputPath = Paths.get(outputDir);
   Indexer indexer;
   Reader reader;
   PrintWriter writer;
   static LuceneTesterNew tester;

   public static void main(String[] args) {
      try {
    	
    	//get all files in the data directory
    	TextFileFilter filter = new TextFileFilter();
        File[] files = new File(dataDir.toString()).listFiles();
        tester = new LuceneTesterNew();
        //delete index files
        tester.delete();
        //loop through files index and search
        for (File file : files) 
        {
        	if(!file.isDirectory()
        			&& !file.isHidden()
        			&& file.exists()
        			&& file.canRead()
        			&& filter.accept(file)
        	  )
            {
        		System.out.println("===================================");
            	//create index and search
                tester.createIndex(file);
            	//searching
            	tester.search(file);
            }
        }
      } catch (IOException e) {
         e.printStackTrace();
      } catch (ParseException e) {
         e.printStackTrace();
      }
   }

   private void createIndex(File file) throws IOException {
      indexer = new Indexer(indexPath);
      indexer.deleteThem();
      int numIndexed;
      long startTime = System.currentTimeMillis();	
      numIndexed = indexer.createIndex(file);
      long endTime = System.currentTimeMillis();
      indexer.close();
      System.out.println(numIndexed+" File indexed, time taken: "+(endTime-startTime)+" ms");		
   }

   private void search(File searchFile) throws IOException, ParseException {
	  String outputFileName =outputDir+"\\"+searchFile.getName();
      reader = new Reader(indexPath);
      //read file and tokenize the character
      String line;
      String fileInput="";
      FileReader content = new FileReader(searchFile);
      BufferedReader bufferedReader = new BufferedReader(content);
      while((line = bufferedReader.readLine()) != null) {
          fileInput = fileInput+line;
      }
      content.close();
      bufferedReader.close();
      
      //tokenize the query words
      String searchQuery = tester.tokenization(fileInput);
      //unigram
      String[] unigram = searchQuery.split(" ");
      String[] setUniArray = new HashSet<String>(Arrays.asList(unigram)).toArray(new String[0]);
      List<Tuple> uniTuples = new ArrayList<Tuple>();

      //unigram search and sort
      for(int i=0; i < setUniArray.length; i++)
      {
    	  String searchToken = setUniArray[i];
    	  long tf = reader.findTF(searchToken);
    	  int t = toIntExact(tf);
          uniTuples.add(new Tuple(searchToken, t, i));
      }
      
      //comparator
      Comparator<Tuple> comparator = new Comparator<Tuple>()
      {
          public int compare(Tuple tupleA, Tuple tupleB)
          {
        	  int numA = tupleA.getData();
        	  int numB = tupleB.getData();
        	  if(numA == numB) {return 0;}
        	  else if (numA > numB) {return -1;}
        	  else {return 1;}
          }
      };
      Collections.sort(uniTuples, comparator);
      writeOutput(outputFileName, uniTuples);
      
   }
   
   public void delete() {
	 //delete previous indexes
  	 File folder = new File(indexDir);
  	 File[] listOfFiles = folder.listFiles();
  	 for (File file : listOfFiles) 
  	 {
  		 file.delete();
  	 }
   }
   
   private String tokenization(String searchQuery) throws IOException {
	 //Tokenize the searchQuery and return tokens separate by space
	   Tokenizer standardTok = new StandardTokenizer();
	   standardTok.setReader(new StringReader(searchQuery));
       CharTermAttribute cattr = standardTok.addAttribute(CharTermAttribute.class);
       standardTok.reset();
       String input = "";
       while (standardTok.incrementToken()) {
       	input=input+cattr.toString()+" ";
      }
       standardTok.close();
       return input;
   }
   private void writeOutput(String outputFileName,List<Tuple> output) throws FileNotFoundException {
	   writer = new PrintWriter(outputFileName);
	   //write output file
	   for(int i =0; i < output.size(); i++)
	   {
		   Tuple t = output.get(i);
		   String name = t.getName();
		   int data = t.getData();
		   //System.out.printf("%-5s %-30s %-10s %-10s\n","Term:",name,"Term Frequency:",data);
		   writer.printf("%-5s %-30s %-10s %-10s\n","Term:",name,"Term Frequency:",data);
	   }
	   writer.close();
   }
   
}
