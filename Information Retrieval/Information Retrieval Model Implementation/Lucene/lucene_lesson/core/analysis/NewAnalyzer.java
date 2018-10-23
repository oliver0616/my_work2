package analyzerPack;

import org.apache.lucene.analysis.Analyzer;
import org.apache.lucene.analysis.TokenStream;
import org.apache.lucene.analysis.Tokenizer;

import org.apache.lucene.analysis.core.WhitespaceTokenizer;
import org.apache.lucene.analysis.miscellaneous.LengthFilter;

public class NewAnalyzer extends Analyzer {
	//Tokenizer job is to split the text and return the tokens
	//Token Filter job is to filter the tokens and base on the user's purpose to do the task
	
	//In the following example we use whitespaceTokenizer to split text base on whitespace and lengthFilter
	//To pick out words that has length equal or more than 3
	
	@Override
	   protected TokenStreamComponents createComponents(String fieldName) {
		//split string base on space
		final Tokenizer source = new WhitespaceTokenizer();
	    //filter word that are length of 3 or more
	    TokenStream result = new LengthFilter(source, 3, Integer.MAX_VALUE);
	    result = new PartOfSpeechTaggingFilter(result);
	    return new TokenStreamComponents(source, result);
	   }

	
}
