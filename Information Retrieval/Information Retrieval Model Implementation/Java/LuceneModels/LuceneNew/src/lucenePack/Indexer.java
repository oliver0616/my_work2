package lucenePack;

import java.io.File;
import java.io.FileFilter;
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
import org.apache.lucene.store.RAMDirectory;
import org.apache.lucene.util.Version;
import org.apache.lucene.search.similarities.BooleanSimilarity;
import org.apache.lucene.search.similarities.ClassicSimilarity;
import org.apache.lucene.search.similarities.TFIDFSimilarity;

public class Indexer {

   private IndexWriter writer;

   public Indexer(Path indexDirectoryPath) throws IOException {
      //this directory will contain the indexes
	  //Directory directory = new RAMDirectory();
      Directory indexDirectory = FSDirectory.open(indexDirectoryPath);

      //create the indexer
      Analyzer analyzer = new StandardAnalyzer();
      IndexWriterConfig config = new IndexWriterConfig(analyzer);
      BooleanSimilarity n = new BooleanSimilarity();
      TFIDFSimilarity  tfidfSIM = new  ClassicSimilarity();
      config.setSimilarity(tfidfSIM);
      writer = new IndexWriter(indexDirectory, config);
   }

   public void close() throws CorruptIndexException, IOException {
      writer.close();
   }

   private Document getDocument(File file) throws IOException {
      Document document = new Document();

      FileReader content = new FileReader(file);
      char[] buff = new char[50];
      int c = content.read(buff);
      String a = String.valueOf(buff);
      //System.out.println(a);
      //index file contents
      Field contentField = new Field(LuceneConstants.CONTENTS, a,TextField.TYPE_STORED);
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
}
