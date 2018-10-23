package lucenePack;

import java.io.IOException;
import java.nio.file.Path;

import org.apache.lucene.index.DirectoryReader;
import org.apache.lucene.index.IndexReader;
import org.apache.lucene.index.Term;
import org.apache.lucene.store.Directory;
import org.apache.lucene.store.FSDirectory;

public class Reader {
	
   IndexReader indexReader;
   
   public Reader(Path indexDirectoryPath) 
      throws IOException {
	  Directory directory = FSDirectory.open(indexDirectoryPath);
      //DirectoryReader indexDirectory = DirectoryReader.open(directory);
      indexReader = DirectoryReader.open(directory);
   }
   
   public long findTF(String inputString) throws IOException {
	   Term termInstance = new Term("contents", inputString);
	   long termFreq = indexReader.totalTermFreq(termInstance);
	   return termFreq;
	   
   }
}
