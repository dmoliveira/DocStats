# coding: utf-8
from nltk.tokenize.api import StringTokenizer

class Corpus(object):

    def __init__(self, tokenizer=StringTokenizer, ngram=1):
        """
        Create corpus object that will store all documents.
        Also it is responsible for generate a score of similarity
        to a given text with the documents of this corpus.


        Keyword arguments:
        tokenizer -- Tokenizer to break document text
                     (default NLTK StringTokenizer)
        ngram -- Number of tokens that will be analyzed in pairs (default 1)
        """
        self.document_dict = {}
        self.corpus_size = 0

    def consume_documents(self, document_file_path_list=None, documents_path=None):
        """
        Consume all documents and calculate term frequency statistics to use at
        similarity score. If used multiple times the function will update all
        statistics from previous import documents. Documents added multiple times
        will be ignored.


        Keyword arguments:
        document_file_path_list -- List of document file paths. If this parameter is
        informed than document path could be ignored.
        documents_path -- A folder that contains the documents. If this parameter is
        informed than document file path list could be ignored.
        """
        pass

    def consume_document(self, document_file_path):
        """
        Consume document and calculate term frequency statistics to use at similarity score.
        If used multiple times for the same document it will ignore the document.


        Keyword arguments:
        document_file_path -- Document path to be read.
        """
        pass

    def get_text_score(self, text):
        """
        Returns the total text score based on the previous corpus documents.
        To calculate text score it uses TF-IDF formula.

        Keyword arguments:
        text -- Any sentence, text fragment, paragraph or text document tokenized
        in a list format or in raw string.
        """
        return sum(zip(*self.score_text)[1])

    def score_text(self, text):
        """
        Returns individual scores for each token for the text based on the previous statistics
        made using corpus documents. To Calculate text score it uses TF-IDF formula.


        Keyword arguments:
        text -- Any sentence, text fragment, paragraph or text document tokenized
        in a list format or in raw string.
        """
        pass
