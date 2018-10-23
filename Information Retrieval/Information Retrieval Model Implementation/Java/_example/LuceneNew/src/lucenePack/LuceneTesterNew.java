package lucenePack;

import java.io.File;
import java.io.IOException;
import java.nio.file.Path;
import java.nio.file.Paths;

import org.apache.lucene.document.Document;
import org.apache.lucene.queryparser.classic.ParseException;
import org.apache.lucene.search.ScoreDoc;
import org.apache.lucene.search.TopDocs;

public class LuceneTesterNew {
	
   String indexDir = "//Users//chenh15//eclipse-workspace//LuceneNew//Lucene//Index";
   Path indexPath = Paths.get(indexDir);
   String dataDir = "//Users//chenh15//eclipse-workspace//LuceneNew//Lucene//Data";
   Path dataPath = Paths.get(dataDir);
   Indexer indexer;
   Searcher searcher;

   public static void main(String[] args) {
	   LuceneTesterNew tester;
      try {
    	//delete previous indexes 
    	 File folder = new File("//Users//chenh15//eclipse-workspace//LuceneNew//Lucene//Index");
    	 File[] listOfFiles = folder.listFiles();
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
         tester.search("jan");
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
      numIndexed = indexer.createIndex(dataDir, new TextFileFilter());
      long endTime = System.currentTimeMillis();
      indexer.close();
      System.out.println(numIndexed+" File indexed, time taken: "
         +(endTime-startTime)+" ms");		
   }

   private void search(String searchQuery) throws IOException, ParseException {
      searcher = new Searcher(indexPath);
      long startTime = System.currentTimeMillis();
      TopDocs hits = searcher.search(searchQuery);
      long endTime = System.currentTimeMillis();
   
      System.out.println(hits.totalHits +
         " documents found. Time :" + (endTime - startTime));
      for(ScoreDoc scoreDoc : hits.scoreDocs) {
         Document doc = searcher.getDocument(scoreDoc);
            System.out.println("File: "
            + doc.get(LuceneConstants.FILE_PATH));
      }
      //searcher.close();
   }
}
