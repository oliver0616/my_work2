package lucenePack;

import java.io.BufferedReader;
import java.io.File;
import java.io.FileReader;
import java.io.IOException;
import java.nio.file.Path;

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

public class Indexer {

   private IndexWriter writer;

   public Indexer(Path indexDirectoryPath) throws IOException {
      //this directory will contain the indexes
      Directory indexDirectory = FSDirectory.open(indexDirectoryPath);

      //create the indexer
      Analyzer analyzer = new StandardAnalyzer();
      IndexWriterConfig config = new IndexWriterConfig(analyzer);
      writer = new IndexWriter(indexDirectory, config);
   }

   public void close() throws CorruptIndexException, IOException {
      writer.close();
   }

   private Document getDocument(File file) throws IOException {
      Document document = new Document();
      String line;
      String fileInput = "";

      //read the file
      FileReader content = new FileReader(file);
      BufferedReader bufferedReader = new BufferedReader(content);
      while((line = bufferedReader.readLine()) != null) {
          fileInput = fileInput+line;
      }
      content.close();
      bufferedReader.close();
      
      //index file contents
      Field contentField = new Field(LuceneConstants.CONTENTS, fileInput,TextField.TYPE_STORED);
      //index file name
      Field fileNameField = new Field(LuceneConstants.FILE_NAME, file.getName(),TextField.TYPE_STORED);
      //index file path
      Field filePathField = new Field(LuceneConstants.FILE_PATH, file.getCanonicalPath(),TextField.TYPE_STORED);

      document.add(contentField);
      document.add(fileNameField);
      document.add(filePathField);

      return document;
   }   

   private void indexFile(File file) throws IOException {
      System.out.println("Indexing "+file.getCanonicalPath());
      Document document = getDocument(file);
      System.out.println(document.get(LuceneConstants.CONTENTS));
      writer.addDocument(document);
   }

   public int createIndex(File file) 
      throws IOException {
	  indexFile(file);
	  return writer.numDocs();
   }
   public void deleteThem() throws IOException {
	   writer.deleteAll();
   }
}
