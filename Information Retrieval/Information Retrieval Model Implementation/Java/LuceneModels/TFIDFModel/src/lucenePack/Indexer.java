package lucenePack;

import java.io.File;
import java.io.FileFilter;
//import java.io.FileReader;
import java.io.IOException;
import java.nio.file.Path;
import java.util.Scanner;

import org.apache.lucene.analysis.Analyzer;
import org.apache.lucene.analysis.standard.StandardAnalyzer;
import org.apache.lucene.document.Document;
import org.apache.lucene.document.Field;
import org.apache.lucene.document.TextField;
import org.apache.lucene.index.CorruptIndexException;
import org.apache.lucene.index.IndexWriter;
import org.apache.lucene.index.IndexWriterConfig;
import org.apache.lucene.store.Directory;
import org.apache.lucene.store.FSDirectory;
import org.apache.lucene.search.similarities.TFIDFSimilarity;
import org.apache.lucene.search.similarities.ClassicSimilarity;

public class Indexer {

   private IndexWriter writer;

   public Indexer(Path indexDirectoryPath) throws IOException {
      //this directory will contain the indexes
      Directory indexDirectory = FSDirectory.open(indexDirectoryPath);

      //create the indexer
      Analyzer analyzer = new StandardAnalyzer();
      IndexWriterConfig config = new IndexWriterConfig(analyzer);
      //set up boolean similarity
      TFIDFSimilarity bool = new ClassicSimilarity(); 
      config.setSimilarity(bool);
      writer = new IndexWriter(indexDirectory, config);
   }

   public void close() throws CorruptIndexException, IOException {
      writer.close();
   }

   private Document getDocument(File file) throws IOException {
      Document document = new Document();
      
      Scanner scan = new Scanner(file);
      String content="";
      while(scan.hasNextLine())
      {
    	  String now = scan.nextLine();
    	  content = content+now+"\n";
      }
      scan.close();
      String[] organize = breakApart(content,file);
      String title, author, bibliography, overview;
      if(organize == null)
      {
    	  title=author=bibliography=overview="";
      }
      else
      {
    	  title=organize[0];
    	  author=organize[1];
    	  bibliography=organize[2];
    	  overview=organize[3];
      }
      
      
      /*FileReader content = new FileReader(file);
      char[] buff = new char[1000];
      content.read(buff);
      String content1 = String.valueOf(buff);
      //System.out.println(content1);*/
      
      //index file contents
      Field contentField = new Field(LuceneConstants.CONTENTS, content,TextField.TYPE_STORED);
      
      Field titleField = new Field(LuceneConstants.TITLE, title, TextField.TYPE_STORED);
      Field authorField = new Field(LuceneConstants.AUTHOR, author, TextField.TYPE_STORED);
      Field bibliographyField = new Field(LuceneConstants.BIBLIOGRAPHY, bibliography, TextField.TYPE_STORED);
      Field overviewField = new Field(LuceneConstants.OVERVIEW, overview, TextField.TYPE_STORED);
      //index file name
      Field fileNameField = new Field(LuceneConstants.FILE_NAME, file.getName(),TextField.TYPE_STORED);
      //index file path
      Field filePathField = new Field(LuceneConstants.FILE_PATH, file.getCanonicalPath(),TextField.TYPE_STORED);

      document.add(titleField);
      document.add(authorField);
      document.add(bibliographyField);
      document.add(overviewField);
      document.add(contentField);
      document.add(fileNameField);
      document.add(filePathField);

      return document;
   }   

   private void indexFile(File file) throws IOException {
      //System.out.println("Indexing "+file.getCanonicalPath());
      Document document = getDocument(file);
      writer.addDocument(document);
   }

   public int createIndex(String dataDirPath, FileFilter filter) 
      throws IOException {
      //get all files in the data directory
      File[] files = new File(dataDirPath).listFiles();

      for (File file : files) {
         if(!file.isDirectory()
            && !file.isHidden()
            && file.exists()
            && file.canRead()
            && filter.accept(file)
         ){
            indexFile(file);
         }
      }
      return writer.numDocs();
   }
   
   private String[] breakApart(String input,File file)
   {
	   String[] result;
	   
	   String[] t = input.split(".A");
	   if(t.length > 2 || t.length < 2)
	   {
		   System.out.print(".T "+t.length+ " ");
		   System.out.println(file.getName());
		   return null;
	   }
	   t[0] = t[0].replace(".T", "");
	   String[] a = t[1].split(".B");
	   if(a.length > 2 || t.length< 2)
	   {
		   System.out.print(".A "+a.length+" ");
		   System.out.println(file.getName());
		   return null;
	   }
	   String[] b = a[1].split(".W");
	   if(b.length > 2 || t.length <2)
	   {
		   System.out.print(".W "+b.length+" ");
		   System.out.println(file.getName());
		   return null;
	   }
	   String w = b[1];
	   //result =(t[0],a[0],b[0],w);
	   result = new String[]{t[0],a[0],b[0],w};
	   return result;
   }
   
}
