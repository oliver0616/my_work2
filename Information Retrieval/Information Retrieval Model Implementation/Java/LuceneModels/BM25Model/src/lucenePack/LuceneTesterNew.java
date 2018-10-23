package lucenePack;

import java.io.File;
import java.io.IOException;
import java.io.PrintWriter;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.util.Scanner;

import org.apache.lucene.document.Document;
import org.apache.lucene.queryparser.classic.ParseException;
import org.apache.lucene.search.Explanation;
import org.apache.lucene.search.ScoreDoc;
import org.apache.lucene.search.TopDocs;

public class LuceneTesterNew {

	static Path current =Paths.get(System.getProperty("user.dir"));
	static Path indexPath = Paths.get(current.toString(),"Lucene","Index");
	static Path dataPath = Paths.get(current.toString(),"Lucene","Data");
	static Path queryPath = Paths.get(current.toString(),"query");
	static Path outputPath = Paths.get(current.toString(),"output","info");
	static Path detailOutputPath = Paths.get(current.toString(),"output","queryDetail");
	Indexer indexer;
	Searcher searcher;

	public static void main(String[] args) {
		LuceneTesterNew tester;
		try {
			//delete previous indexes 
			File folder = new File(indexPath.toString());
			File[] listOfFiles = folder.listFiles();
			//System.out.println(listOfFiles.length);
			for (File file : listOfFiles) {
				if (file.isFile()) {
					if(file.delete())
    		        {
    		            System.out.println("File deleted successfully");
    		        }
    		        else
    		        {
    		            System.out.println("Failed to delete the file");
    		        } 
    		    }
    		}
    	 
    	 //create index and search
         tester = new LuceneTesterNew();
         tester.createIndex();
         File f = new File(queryPath.toString());
    	 File[] listFiles = f.listFiles();
    	 for (File file : listFiles ) {
    		 if(file.getName().startsWith("."))
    		 {
    			 continue;
    		 }
    		 Scanner scan = new Scanner(file);
    		 String searchQuery="";
    		 while(scan.hasNextLine())
    		 {
    			 String now = scan.nextLine();
    			 if(now != "")
    			 {
    				 searchQuery = searchQuery+now;
    			 }
    		 }
    		 scan.close();
    		 System.out.println("Current Searching Query:"+file.getName());
    		 tester.search(searchQuery,file.getName());
    		 System.out.println("=====================================");
    	 }
         //tester.search("approximate solutions","output.txt");
      } catch (IOException e) {
         e.printStackTrace();
      } catch (ParseException e) {
         e.printStackTrace();
      }
   }

   private void createIndex() throws IOException {
      indexer = new Indexer(indexPath);
      int numIndexed;
      long startTime = System.currentTimeMillis();
      numIndexed = indexer.createIndex(dataPath.toString(), new TextFileFilter());
      long endTime = System.currentTimeMillis();
      indexer.close();
      System.out.println(numIndexed+" File indexed, time taken: " +(endTime-startTime)+" ms");		
   }

   private void search(String searchQuery,String fileName) throws IOException, ParseException {
      searcher = new Searcher(indexPath);
      long startTime = System.currentTimeMillis();
      TopDocs hits = searcher.search(searchQuery);
      long endTime = System.currentTimeMillis();
      System.out.println(hits.totalHits +" documents found. Time :" + (endTime - startTime));
      
      PrintWriter outputFile = new PrintWriter(outputPath.toString()+"//"+fileName);
      PrintWriter detailQueryFile = new PrintWriter(detailOutputPath.toString()+"//"+fileName);
      for(ScoreDoc scoreDoc : hits.scoreDocs) {
    	  Document doc = searcher.getDocument(scoreDoc);
    	  Explanation ex = searcher.queryDetail(searchQuery, scoreDoc);
    	  detailQueryFile.println(ex);
    	  detailQueryFile.println("==============================================================");
          outputFile.println("File: " + doc.get(LuceneConstants.FILE_PATH));
      }
      detailQueryFile.close();
      outputFile.close();
      //searcher.close();
   }
}
