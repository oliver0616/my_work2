package lucenePack;

import java.io.IOException;
import java.nio.file.Path;

import org.apache.lucene.analysis.standard.StandardAnalyzer;
import org.apache.lucene.document.Document;
import org.apache.lucene.index.CorruptIndexException;
import org.apache.lucene.index.DirectoryReader;
import org.apache.lucene.queryparser.classic.ParseException;
import org.apache.lucene.queryparser.classic.QueryParser;
import org.apache.lucene.search.Explanation;
import org.apache.lucene.search.IndexSearcher;
import org.apache.lucene.search.Query;
import org.apache.lucene.search.ScoreDoc;
import org.apache.lucene.search.TopDocs;
import org.apache.lucene.store.Directory;
import org.apache.lucene.store.FSDirectory;
import org.apache.lucene.search.similarities.BM25Similarity;

public class Searcher {
	
   IndexSearcher indexSearcher;
   QueryParser queryParser;
   Query query;
   
   public Searcher(Path indexDirectoryPath) 
      throws IOException {
	  Directory directory = FSDirectory.open(indexDirectoryPath);
      DirectoryReader indexDirectory = DirectoryReader.open(directory);
      
      indexSearcher = new IndexSearcher(indexDirectory);
      //set up boolean similarity
      BM25Similarity bool = new BM25Similarity();
      indexSearcher.setSimilarity(bool);
      
      //queryParser = new QueryParser(LuceneConstants.CONTENTS, new StandardAnalyzer());
      queryParser = new QueryParser(LuceneConstants.OVERVIEW, new StandardAnalyzer());
   }
   
   public TopDocs search(String searchQuery) throws IOException, ParseException {
      query = queryParser.parse(searchQuery);
      int result = indexSearcher.count(query);
      //return indexSearcher.search(query, LuceneConstants.MAX_SEARCH);
      //System.out.println(searchQuery);
      return indexSearcher.search(query, result);
   }

   public Document getDocument(ScoreDoc scoreDoc) 
      throws CorruptIndexException, IOException {
      return indexSearcher.doc(scoreDoc.doc);
   }
   
   public Explanation queryDetail(String searchQuery, ScoreDoc scoreDoc) throws IOException, ParseException
   {
	   query = queryParser.parse(searchQuery);
	   //System.out.println(indexSearcher.explain(query, scoreDoc.doc));
	   return indexSearcher.explain(query, scoreDoc.doc);
   }
   /*public void close() throws IOException {
      indexSearcher.close();
   }*/
}
