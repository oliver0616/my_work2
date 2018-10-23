package lucenePack;

import java.io.File;
import java.io.IOException;
import java.nio.file.Path;

import org.apache.lucene.analysis.standard.StandardAnalyzer;
import org.apache.lucene.document.Document;
import org.apache.lucene.index.CorruptIndexException;
import org.apache.lucene.index.DirectoryReader;
import org.apache.lucene.queryparser.classic.ParseException;
import org.apache.lucene.queryparser.classic.QueryParser;
import org.apache.lucene.search.IndexSearcher;
import org.apache.lucene.search.Query;
import org.apache.lucene.search.ScoreDoc;
import org.apache.lucene.search.TopDocs;
import org.apache.lucene.store.Directory;
import org.apache.lucene.store.FSDirectory;
import org.apache.lucene.util.Version;
import org.apache.lucene.search.similarities.BooleanSimilarity;
import org.apache.lucene.search.similarities.ClassicSimilarity;
import org.apache.lucene.search.similarities.TFIDFSimilarity;

public class Searcher {
	
   IndexSearcher indexSearcher;
   QueryParser queryParser;
   Query query;
   
   public Searcher(Path indexDirectoryPath) 
      throws IOException {
	  Directory directory = FSDirectory.open(indexDirectoryPath);
      DirectoryReader indexDirectory = DirectoryReader.open(directory);
      
      indexSearcher = new IndexSearcher(indexDirectory);
      BooleanSimilarity n = new BooleanSimilarity();
      TFIDFSimilarity  tfidfSIM = new  ClassicSimilarity();
      indexSearcher.setSimilarity(tfidfSIM);
      queryParser = new QueryParser(
         LuceneConstants.CONTENTS,
         new StandardAnalyzer());
   }
   
   public TopDocs search(String searchQuery) 
      throws IOException, ParseException {
      query = queryParser.parse(searchQuery);
      System.out.println(indexSearcher.explain(query, 4));
      return indexSearcher.search(query, LuceneConstants.MAX_SEARCH);
   }

   public Document getDocument(ScoreDoc scoreDoc) 
      throws CorruptIndexException, IOException {
      return indexSearcher.doc(scoreDoc.doc);	
   }

   /*public void close() throws IOException {
      indexSearcher.close();
   }*/
}
